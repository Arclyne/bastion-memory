#!/usr/bin/env python3
import datetime
import hashlib
import pathlib
import re
import subprocess
import sys

import registros

MAP_NOTE = registros.VAULT_ROOT / "codigo" / "mapa-codigo.md"
VALUES_NOTE = registros.VAULT_ROOT / "codigo" / "valores.md"
SETTINGS_PREFIX = "appsettings"
LOCAL_REPOSITORY_FILE = registros.VAULT_ROOT / ".repo"
SOURCE_DIRECTORIES = ("src", "tests")
DATABASE_DIRECTORY = "database"
BUILD_DIRECTORIES = {"bin", "obj", ".git", ".vs", ".idea"}
GENERATED_SUFFIXES = (".Designer.cs", ".g.cs", ".AssemblyInfo.cs")
MEMBER_LIMIT = 14
TYPE_KIND_LETTERS = {"class": "C", "interface": "I", "record": "R", "struct": "S", "enum": "E"}

NAMESPACE = re.compile(r"^namespace\s+([\w.]+)", re.MULTILINE)
TYPE_DECLARATION = re.compile(
    r"^(public|internal)\s+((?:(?:static|sealed|abstract|partial|readonly)\s+)*)(class|interface|record|struct|enum)\s+(\w+)",
    re.MULTILINE,
)
PUBLIC_METHOD = re.compile(
    r"^    public\s+(?:(?:static|override|virtual|async|abstract|new|sealed)\s+)*[\w<>\[\],.? ]+?\s+(\w+)(?:<[^>(]*>)?\(",
    re.MULTILINE,
)
INTERFACE_METHOD = re.compile(r"^    [\w<>\[\],.? ]+?\s+(\w+)(?:<[^>(]*>)?\(", re.MULTILINE)
ENUM_VALUE = re.compile(r"^    (\w+)\s*(?:=\s*[^,]+)?,?\s*$", re.MULTILINE)
SERVICE_CONTRACT = re.compile(r"\[ServiceContract")
OPERATION = re.compile(
    r"\[OperationContract(?P<options>[^\]]*)\]\s*(?P<faults>(?:\[FaultContract\(typeof\(\w+\)\)\]\s*)*)"
    r"(?P<returns>[\w<>\[\]?.]+)\s+(?P<name>\w+)\((?P<parameters>[^)]*)\);"
)
FAULT = re.compile(r"typeof\((\w+)\)")
TEST_METHOD = re.compile(r"^\s*\[(?:Fact|Theory)\b", re.MULTILINE)
PROJECT_REFERENCE = re.compile(r'<ProjectReference Include="[^"]*?([\w.]+)\.csproj"')
PACKAGE_REFERENCE = re.compile(r'<PackageReference Include="([^"]+)"')
TARGET_FRAMEWORK = re.compile(r"<TargetFrameworks?>([^<]+)<")
CREATE_TABLE = re.compile(r"CREATE TABLE (?:dbo\.)?(\w+)\s*\((.*?)^\);", re.MULTILINE | re.DOTALL)
COLUMN = re.compile(r"^\s+(\w+)\s+[A-Z]+", re.MULTILINE)
CREATE_PROCEDURE = re.compile(r"CREATE (?:OR ALTER )?PROCEDURE (?:dbo\.)?(\w+)")
PUBLIC_CONSTANT = re.compile(r"^    (?:(?:public|internal|private|protected) )?const [\w<>?.]+ (\w+) = (.+);$", re.MULTILINE)
PUBLIC_STATIC_VALUE = re.compile(r"^    (?:public|internal|private) static (?:readonly )?[\w<>?.]+ (\w+)(?: \{ get; \})? = (.+);$", re.MULTILINE)
LOGGER_FACTORY = "LogManager."
NON_COLUMN_WORDS = {"CONSTRAINT", "PRIMARY", "FOREIGN", "UNIQUE", "CHECK", "INDEX", "AND", "OR", "REFERENCES", "ON"}


def resolve_repository(arguments):
    if arguments:
        candidate = pathlib.Path(arguments[0]).expanduser()
    elif LOCAL_REPOSITORY_FILE.is_file():
        candidate = pathlib.Path(LOCAL_REPOSITORY_FILE.read_text(encoding="utf-8").strip()).expanduser()
    else:
        raise SystemExit(
            "FALLA: no sé dónde está el repositorio de código. Pasa la ruta como argumento "
            "o guárdala en el archivo .repo de la raíz del vault (no se sincroniza)."
        )
    if not (candidate / SOURCE_DIRECTORIES[0]).is_dir():
        raise SystemExit(f"FALLA: {candidate} no tiene la carpeta {SOURCE_DIRECTORIES[0]}/; no parece el repositorio de Bastión.")
    return candidate


def normalized_text(path):
    return path.read_text(encoding="utf-8-sig", errors="replace").replace("\r\n", "\n")


def is_build_output(path, repository):
    return bool(BUILD_DIRECTORIES.intersection(path.relative_to(repository).parts))


def collect_files(repository, directories, pattern):
    files = []
    for directory in directories:
        root = repository / directory
        if root.is_dir():
            files.extend(path for path in root.rglob(pattern) if not is_build_output(path, repository))
    return sorted(files, key=lambda path: path.relative_to(repository).as_posix())


def digest(repository, files):
    hasher = hashlib.sha1()
    for path in files:
        hasher.update(path.relative_to(repository).as_posix().encode("utf-8"))
        hasher.update(normalized_text(path).encode("utf-8"))
    return hasher.hexdigest()[:8]


def git_value(repository, *arguments):
    try:
        completed = subprocess.run(["git", "-C", str(repository), *arguments], capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return "desconocido"
    return completed.stdout.strip() or "desconocido"


def fingerprint_line(repository):
    code_files = collect_files(repository, SOURCE_DIRECTORIES, "*.cs")
    project_files = collect_files(repository, SOURCE_DIRECTORIES, "*.csproj")
    database_files = collect_files(repository, (DATABASE_DIRECTORY,), "*.sql")
    line_count = sum(normalized_text(path).count("\n") for path in code_files)
    return (
        f"huella: archivos={len(code_files)} lineas={line_count} codigo={digest(repository, code_files + project_files)} "
        f"sql={digest(repository, database_files)}"
    )


def shorten(names):
    unique = sorted(set(names))
    if len(unique) <= MEMBER_LIMIT:
        return ",".join(unique)
    return ",".join(unique[:MEMBER_LIMIT]) + f",+{len(unique) - MEMBER_LIMIT}"


def describe_type(text):
    declaration = TYPE_DECLARATION.search(text)
    if not declaration:
        return None
    visibility, _, kind, name = declaration.groups()
    body = text[declaration.end():]
    if kind == "enum":
        members = [value for value in ENUM_VALUE.findall(body)]
        member_text = ",".join(members)
    elif kind == "interface":
        member_text = shorten(INTERFACE_METHOD.findall(body))
    else:
        member_text = shorten(method for method in PUBLIC_METHOD.findall(body) if method != name)
    marker = "~" if visibility == "internal" else ""
    line_count = text.count("\n")
    description = f"{marker}{name} {TYPE_KIND_LETTERS[kind]}{line_count}"
    return description + (f" | {member_text}" if member_text else "")


def type_sections(repository):
    by_namespace = {}
    for path in collect_files(repository, ("src",), "*.cs"):
        if path.name.endswith(GENERATED_SUFFIXES):
            continue
        text = normalized_text(path)
        namespace = NAMESPACE.search(text)
        description = describe_type(text)
        if namespace and description:
            by_namespace.setdefault(namespace.group(1), []).append(description)
    lines = []
    for namespace in sorted(by_namespace):
        lines.append(f"## {namespace}")
        lines.extend(sorted(by_namespace[namespace], key=lambda description: description.lstrip("~")))
    return lines


def contract_lines(repository):
    lines = []
    for path in collect_files(repository, ("src",), "*.cs"):
        text = normalized_text(path)
        if not SERVICE_CONTRACT.search(text):
            continue
        declaration = TYPE_DECLARATION.search(text)
        lines.append(f"## {declaration.group(4)}")
        for operation in OPERATION.finditer(text):
            parameters = ",".join(parameter.split()[-1] for parameter in operation.group("parameters").split(",") if parameter.strip())
            faults = ",".join(FAULT.findall(operation.group("faults")))
            one_way = " oneway" if "IsOneWay" in operation.group("options") else ""
            fault_text = f" !{faults}" if faults else ""
            lines.append(f"{operation.group('name')}({parameters}) -> {operation.group('returns')}{one_way}{fault_text}")
    return lines


def project_lines(repository):
    lines = []
    for path in collect_files(repository, SOURCE_DIRECTORIES, "*.csproj"):
        text = normalized_text(path)
        framework = TARGET_FRAMEWORK.search(text)
        references = ",".join(sorted(PROJECT_REFERENCE.findall(text))) or "-"
        packages = ",".join(sorted(PACKAGE_REFERENCE.findall(text))) or "-"
        target = framework.group(1) if framework else "heredado"
        lines.append(f"{path.stem} | {target} | ref:{references} | paq:{packages}")
    return lines


def test_lines(repository):
    lines = []
    root = repository / "tests"
    if not root.is_dir():
        return lines
    for project in sorted(path for path in root.iterdir() if path.is_dir()):
        files = [path for path in project.rglob("Test*.cs") if not is_build_output(path, repository)]
        test_count = sum(len(TEST_METHOD.findall(normalized_text(path))) for path in files)
        lines.append(f"{project.name} | clases={len(files)} pruebas={test_count}")
    return lines


def database_lines(repository):
    table_lines = []
    procedure_names = []
    for path in collect_files(repository, (DATABASE_DIRECTORY,), "*.sql"):
        text = normalized_text(path)
        for table_name, body in CREATE_TABLE.findall(text):
            columns = [column for column in COLUMN.findall(body) if column.upper() not in NON_COLUMN_WORDS]
            table_lines.append(f"{table_name} | {path.name} | {','.join(columns)}")
        procedure_names.extend(f"{name} | {path.name}" for name in CREATE_PROCEDURE.findall(text))
    scripts = [path.name for path in collect_files(repository, (DATABASE_DIRECTORY,), "*.sql")]
    return scripts, sorted(table_lines), sorted(procedure_names)


def flatten_settings(prefix, value, lines):
    if isinstance(value, dict):
        for key in value:
            flatten_settings(f"{prefix}.{key}", value[key], lines)
    else:
        lines.append(f"{prefix}={value}")


def settings_lines(repository):
    import json

    lines = []
    for path in collect_files(repository, ("src",), "appsettings*.json"):
        settings = json.loads(normalized_text(path))
        flatten_settings(path.stem, settings, lines)
    return lines


def constant_lines(repository):
    entries = {}
    for path in collect_files(repository, ("src",), "*.cs"):
        if path.name.endswith(GENERATED_SUFFIXES):
            continue
        text = normalized_text(path)
        declaration = TYPE_DECLARATION.search(text)
        if not declaration or declaration.group(3) == "enum":
            continue
        owner = declaration.group(4)
        for pattern in (PUBLIC_CONSTANT, PUBLIC_STATIC_VALUE):
            for name, expression in pattern.findall(text):
                if expression.startswith(LOGGER_FACTORY):
                    continue
                entries.setdefault(owner, []).append(f"{owner}.{name}={expression.strip()}")
    lines = []
    for owner in sorted(entries):
        lines.extend(entries[owner])
    return lines


def heading_lines(repository):
    return [
        "# huella",
        f"repo={repository.name} commit={git_value(repository, 'rev-parse', '--short', 'HEAD')} "
        f"rama={git_value(repository, 'rev-parse', '--abbrev-ref', 'HEAD')} generado={datetime.date.today().isoformat()}",
        fingerprint_line(repository),
    ]


def build_values(repository):
    lines = [
        "---",
        "tipo: valores",
        "generado: sí (herramientas/mapa_codigo.py; no editar a mano; ver herramientas/LEEME.md)",
        "---",
        "# Valores del código",
        "",
        "Constantes (de cualquier visibilidad) y propiedades o campos estáticos con valor inicial de `src/` (`Clase.Nombre=expresión`, tal como está en el código) "
        "y configuración de `appsettings*.json` aplanada (`appsettings.Sección.Clave=valor`). "
        "Las notas citan la clave, nunca el número. Para cambiar un valor se edita el código y se regenera esta nota.",
        "",
        *heading_lines(repository),
        "# configuracion",
        *settings_lines(repository),
        "# constantes",
        *constant_lines(repository),
    ]
    return "\n".join(lines) + "\n"


def build_map(repository):
    scripts, tables, procedures = database_lines(repository)
    solution_files = sorted(path.name for path in repository.glob("*.sln*"))
    lines = [
        "---",
        "tipo: mapa-codigo",
        "generado: sí (herramientas/mapa_codigo.py; no editar a mano; ver herramientas/LEEME.md)",
        "---",
        "# Mapa del código",
        "",
        "Formato. proyectos: `Proyecto | framework | ref:proyectos | paq:paquetes`. tipos: `Nombre TipoLíneas | miembros públicos` "
        "(C clase, R record, I interfaz, E enum, S struct; `~` interno; `+N` = N más sin listar). "
        "contratos: `Operación(parámetros) -> retorno [oneway] !fallas`. tablas: `Tabla | script | columnas`. "
        "Qué hace cada proyecto: [[sistemas]]. Valores: [[valores]]. Qué caso de uso usa cada cosa: `python3 herramientas/ver.py casos`.",
        "",
        *heading_lines(repository),
        "# solucion",
        ",".join(solution_files) or "sin archivo de solución",
        "# proyectos",
        *project_lines(repository),
        "# pruebas",
        *test_lines(repository),
        "# contratos",
        *contract_lines(repository),
        "# tipos",
        *type_sections(repository),
        "# base de datos",
        "scripts: " + ",".join(scripts),
        "## tablas",
        *tables,
        "## procedimientos",
        *procedures,
    ]
    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("generar", "huella"):
        sys.exit("uso: mapa_codigo.py generar|huella [ruta del repositorio de código]")
    repository = resolve_repository(sys.argv[2:])
    if sys.argv[1] == "huella":
        print(fingerprint_line(repository))
        return
    MAP_NOTE.parent.mkdir(exist_ok=True)
    MAP_NOTE.write_text(build_map(repository), encoding="utf-8")
    VALUES_NOTE.write_text(build_values(repository), encoding="utf-8")
    print(MAP_NOTE.relative_to(registros.VAULT_ROOT).as_posix())
    print(VALUES_NOTE.relative_to(registros.VAULT_ROOT).as_posix())


if __name__ == "__main__":
    main()
