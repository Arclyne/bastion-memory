#!/usr/bin/env python3
import datetime
import pathlib
import re
import sys

import registros

VAULT_ROOT = registros.VAULT_ROOT
IGNORED_DIRECTORIES = {"archivo", ".obsidian", ".git", ".trash", ".github"}
REQUIRED_NOTES = [
    "CLAUDE.md",
    "ESTADO.md",
    "AUTORES.md",
    "estandar/reglas.md",
    "decisiones/REGISTRO.md",
    "diseno/CASOS.md",
    "diseno/arquitectura.md",
    "diseno/modelo-datos.md",
    "diseno/protocolo.md",
    "diseno/interfaz.md",
    "codigo/mapa-codigo.md",
    "codigo/valores.md",
    "codigo/sistemas.md",
    "pendientes/PREGUNTAS.md",
    "pendientes/TAREAS.md",
    "herramientas/LEEME.md",
    "archivo/MANIFIESTO.md",
]
RULES_NOTE = "estandar/reglas.md"
RUBRICS_NOTE = "estandar/rubricas.md"
CASE_DIRECTORY = "diseno/casos/"
MAP_NOTE = "codigo/mapa-codigo.md"
VALUES_NOTE = "codigo/valores.md"
SYSTEMS_NOTE = "codigo/sistemas.md"
GENERATED_NOTES = (MAP_NOTE, VALUES_NOTE)
STANDARD_TEXT_DIRECTORY = "estandar/texto/"
LINE_BUDGETS = {"CLAUDE.md": 80, "ESTADO.md": 60}
SESSION_NOTE_LINE_BUDGET = 40
RECORD_LINE_BUDGET = 30
NOTES_WITHOUT_VERIFICATION_STAMP = {"CLAUDE.md", "herramientas/LEEME.md", *GENERATED_NOTES}
SESSION_DIRECTORY = "bitacora"
SESSION_AUTHORS_WITHOUT_PERSON = {"resumen"}
REQUIRED_RECORD_FIELDS = ("tipo", "id", "fecha", "autor", "estado")
USE_CASE_STATES = {"con código", "parcial", "sin código"}
RUBRIC_PENDING_STATE = "sin revisar"
RUBRIC_WARNING_DAYS = 7
UNCOVERED_NAMESPACE_LIMIT = 10

WIKILINK = re.compile(r"\[\[([^\]|#]+)")
FENCED_BLOCK = re.compile(r"```.*?```", re.DOTALL)
RECORD_REFERENCES = {
    "decision": re.compile(r"\bD-\d{3}[a-z]?\b"),
    "pregunta": re.compile(r"(?<!SAD )\bQ-\d{2,3}[a-z]?\b"),
    "tarea": re.compile(r"\bT-\d{2,3}[a-z]?\b"),
}
RULE_LINE = re.compile(r"^(E-\d{2,3}) \| §([\d.]+) \| ", re.MULTILINE)
RULE_REFERENCE = re.compile(r"\bE-\d{2,3}\b")
JOURNAL_RULE_REFERENCE = re.compile(r"(?<!SAD )\bR-\d{2}\b")
BARE_EXTERNAL_DECISION = re.compile(r"(?<!REQ )(?<!journal )\bD-\d{2}\b(?![\da-z])")
BARE_ARCHITECTURE_DECISION = re.compile(r"(?<!SAD )\bADR-\d{3}\b")
FINGERPRINT_LINE = re.compile(r"^huella: (.+)$", re.MULTILINE)
GENERATED_DATE = re.compile(r"generado=(\d{4}-\d{2}-\d{2})")
SESSION_NOTE_NAME = re.compile(r"^(\d{4}-\d{2}-\d{2})-([a-z0-9]+)$")
CONFLICT_MARKER = re.compile(r"^(<<<<<<<|>>>>>>>) ", re.MULTILINE)
CASE_ID = re.compile(r"^CU-(\d{2})$")
CODE_SECTION = "## Código"
CASE_FIELDS = ("tipo", "id", "nombre", "estado", "verificado")
CROSS_CUTTING_LINE = re.compile(r"^TRANSVERSAL \| (.+)$", re.MULTILINE)
CODE_TOKEN = re.compile(r"`([^`]+)`")
CONFIGURATION_OWNER_SUFFIXES = ("Policy", "Endpoints", "Metrics")
SETTINGS_OWNER = "appsettings"
CODE_KEY_REFERENCE = re.compile(r"`((?:appsettings|[A-Z]\w*)(?:\.[A-Z]\w*)+)`")
VALUE_LINE = re.compile(r"^((?:appsettings|[A-Z]\w*)(?:\.\w+)+)=", re.MULTILINE)
RUBRIC_LINE = re.compile(r"^([^|#\n]+) \| (\d{4}-\d{2}-\d{2}) \| ([^|]+) \| ([^|\n]+)$", re.MULTILINE)


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, message):
        self.errors.append(message)

    def warn(self, message):
        self.warnings.append(message)


def relative(path):
    return path.relative_to(VAULT_ROOT).as_posix()


def collect_notes():
    notes = {}
    for path in sorted(VAULT_ROOT.rglob("*.md")):
        if IGNORED_DIRECTORIES.intersection(path.relative_to(VAULT_ROOT).parts):
            continue
        notes[relative(path)] = path.read_text(encoding="utf-8")
    return notes


def prose(text):
    return FENCED_BLOCK.sub("", text)


def frontmatter_value(text, key):
    return registros.split_frontmatter(text)[0].get(key)


def section_lines(text, heading):
    lines = text.splitlines()
    if heading not in lines:
        return []
    collected = []
    for line in lines[lines.index(heading) + 1:]:
        if line.startswith("# "):
            break
        collected.append(line)
    return collected


def is_session_note(name):
    return name.startswith(SESSION_DIRECTORY + "/")


def is_standard_text(name):
    return name.startswith(STANDARD_TEXT_DIRECTORY)


def check_required_notes(report):
    for name in REQUIRED_NOTES:
        if not (VAULT_ROOT / name).is_file():
            report.error(f"falta la nota {name}")


def check_merge_leftovers(notes, report):
    for name, text in notes.items():
        if CONFLICT_MARKER.search(prose(text)):
            report.error(f"{name}: tiene marcadores de conflicto de git sin resolver")


def check_unique_names(notes, report):
    seen = {}
    for name in notes:
        stem = pathlib.PurePosixPath(name).stem.lower()
        if stem in seen:
            report.error(f"dos notas con el mismo nombre: {seen[stem]} y {name}")
        seen[stem] = name
    return set(seen)


def check_wikilinks(notes, stems, report):
    for name, text in notes.items():
        for target in WIKILINK.findall(prose(text)):
            if pathlib.PurePosixPath(target.strip()).name.lower() not in stems:
                report.error(f"{name}: enlace roto [[{target}]]")


def check_records(report):
    people = set(registros.author_letters())
    identifiers = {}
    origins = set()
    for kind in registros.KINDS.values():
        identifiers[kind.name] = set()
        directory = VAULT_ROOT / kind.directory
        for path in sorted(directory.glob("*.md")):
            if path.stem.isupper():
                continue
            if not path.name.startswith(kind.prefix + "-"):
                report.error(f"{relative(path)}: en esta carpeta solo van registros {kind.prefix}-…; crearlos con nuevo.py")
        for record in registros.load_records(kind):
            name = relative(record.path)
            missing = [field for field in (*REQUIRED_RECORD_FIELDS, kind.group_field) if not record.fields.get(field)]
            if missing:
                report.error(f"{name}: faltan campos en el encabezado: {', '.join(missing)}")
                continue
            identifier = record.identifier
            if not registros.RECORD_ID.match(identifier) or not identifier.startswith(kind.prefix + "-"):
                report.error(f"{name}: id inválido '{identifier}'")
            if not record.path.name.startswith(identifier + "-"):
                report.error(f"{name}: el nombre del archivo no empieza con su id {identifier}")
            if not record.title:
                report.error(f"{name}: falta el título '# {identifier} · …'")
            if identifier in identifiers[kind.name]:
                report.error(f"{name}: id repetido {identifier}; renombrar el registro más nuevo con nuevo.py")
            identifiers[kind.name].add(identifier)
            if record.fields["autor"] not in people:
                report.error(f"{name}: autor '{record.fields['autor']}' no está en AUTORES.md")
            if record.text.count("\n") + 1 > RECORD_LINE_BUDGET:
                report.warn(f"{name}: pasa de {RECORD_LINE_BUDGET} líneas; un registro debe ser corto")
            if record.origin:
                origins.add(record.origin.split(" ")[-1])
    return identifiers, origins


def check_record_references(notes, identifiers, report):
    for name, text in notes.items():
        if is_standard_text(name):
            continue
        for kind_name, pattern in RECORD_REFERENCES.items():
            if kind_name != "decision" and is_session_note(name):
                continue
            for reference in sorted(set(pattern.findall(prose(text))) - identifiers[kind_name]):
                report.error(f"{name}: cita {reference}, que no existe (o ya se cerró)")


def check_rule_references(notes, report):
    rules_text = notes.get(RULES_NOTE, "")
    rule_identifiers = [identifier for identifier, _ in RULE_LINE.findall(rules_text)]
    repeated = sorted({identifier for identifier in rule_identifiers if rule_identifiers.count(identifier) > 1})
    if repeated:
        report.error(f"{RULES_NOTE}: reglas repetidas: {', '.join(repeated)}")
    known = set(rule_identifiers)
    for name, text in notes.items():
        if name == RULES_NOTE or is_standard_text(name):
            continue
        for reference in sorted(set(RULE_REFERENCE.findall(prose(text))) - known):
            report.error(f"{name}: cita la regla {reference}, que no existe en {RULES_NOTE}")
    return len(known)


def check_external_identifiers(notes, origins, report):
    for name, text in notes.items():
        if is_standard_text(name):
            continue
        body = prose(text)
        for reference in sorted(set(JOURNAL_RULE_REFERENCE.findall(body)) - origins):
            report.error(f"{name}: cita {reference} sin origen; si es del SAD se escribe 'SAD {reference}', si es del journal no existe")
        for reference in sorted(set(BARE_EXTERNAL_DECISION.findall(body))):
            report.error(f"{name}: cita {reference} sin origen; escribir 'REQ {reference}' o 'journal {reference}' (los del vault son D-NNN con letra)")
        for reference in sorted(set(BARE_ARCHITECTURE_DECISION.findall(body))):
            report.error(f"{name}: cita {reference} sin origen; escribir 'SAD {reference}'")


def parse_code_map(notes):
    code_map = notes.get(MAP_NOTE, "")
    types_by_namespace = {}
    namespace = ""
    for line in section_lines(code_map, "# tipos"):
        if line.startswith("## "):
            namespace = line[3:].strip()
            types_by_namespace[namespace] = set()
        elif line and namespace:
            types_by_namespace[namespace].add(line.split(" ", 1)[0].lstrip("~"))
    operations = set()
    contract = ""
    for line in section_lines(code_map, "# contratos"):
        if line.startswith("## "):
            contract = line[3:].strip()
        elif line and contract:
            operations.add(f"{contract}.{line.split('(', 1)[0]}")
    return types_by_namespace, operations


def covered_types(token, types_by_namespace, operations):
    if token in types_by_namespace:
        return {(token, type_name) for type_name in types_by_namespace[token]}
    owner = token.split(".", 1)[0] if token in operations else token
    return {(namespace, owner) for namespace, type_names in types_by_namespace.items() if owner in type_names}


def check_fingerprints(notes, report):
    fingerprints = {}
    for name in GENERATED_NOTES:
        matches = FINGERPRINT_LINE.findall(notes.get(name, ""))
        if len(matches) != 1:
            report.error(f"{name}: debe tener exactamente una línea 'huella:' (tiene {len(matches)}); regenerar con mapa_codigo.py")
        else:
            fingerprints[name] = matches[0].strip()
    if len(set(fingerprints.values())) > 1:
        report.error(f"{MAP_NOTE} y {VALUES_NOTE} tienen huellas distintas: regenerar las dos con mapa_codigo.py")


def project_names(notes):
    return [line.split(" | ", 1)[0] for line in section_lines(notes.get(MAP_NOTE, ""), "# proyectos") if line]


def check_systems_cover_projects(notes, report):
    systems = notes.get(SYSTEMS_NOTE, "")
    projects = project_names(notes)
    for project in projects:
        if not re.search(r"(?<![\w.])" + re.escape(project) + r"(?![\w.])", systems):
            report.error(f"{SYSTEMS_NOTE} no menciona el proyecto {project}")
    return len(projects)


def member_names(notes):
    members = {}
    for line in section_lines(notes.get(MAP_NOTE, ""), "# tipos"):
        if not line or line.startswith("## "):
            continue
        type_name, _, rest = line.partition(" ")
        listed = rest.split(" | ", 1)[1] if " | " in rest else ""
        members.setdefault(type_name.lstrip("~"), set()).update(listed.split(","))
    return members


def check_config_keys(notes, report):
    known_keys = set(VALUE_LINE.findall(notes.get(VALUES_NOTE, "")))
    owners = {key.split(".", 1)[0] for key in known_keys}
    owners = {owner for owner in owners if owner == SETTINGS_OWNER or owner.endswith(CONFIGURATION_OWNER_SUFFIXES)}
    members = member_names(notes)
    for name, text in notes.items():
        if name in GENERATED_NOTES or is_session_note(name) or is_standard_text(name):
            continue
        for key in sorted(set(CODE_KEY_REFERENCE.findall(prose(text)))):
            owner, _, member = key.partition(".")
            if owner not in owners or member in members.get(owner, set()) or key in known_keys:
                continue
            report.error(f"{name}: cita {key}, que no existe en {VALUES_NOTE}")


def case_sheets(notes):
    return {name: text for name, text in notes.items() if name.startswith(CASE_DIRECTORY)}


def cited_in_code_section(text):
    lines = registros.split_frontmatter(text)[1].splitlines()
    if CODE_SECTION not in lines:
        return []
    tokens = []
    for line in lines[lines.index(CODE_SECTION) + 1:]:
        if line.startswith("## "):
            break
        tokens.extend(CODE_TOKEN.findall(line))
    return tokens


def check_case_sheet(name, text, case_numbers, report):
    fields = registros.split_frontmatter(text)[0]
    missing = [field for field in CASE_FIELDS if not fields.get(field)]
    if missing:
        report.error(f"{name}: faltan campos en el encabezado: {', '.join(missing)}")
        return None
    identifier, state = fields["id"], fields["estado"]
    match = CASE_ID.match(identifier)
    if not match or not pathlib.PurePosixPath(name).name.startswith(identifier + "-"):
        report.error(f"{name}: id '{identifier}' inválido o distinto del nombre del archivo")
        return None
    if match.group(1) in case_numbers:
        report.error(f"{name}: caso de uso repetido {identifier}")
    case_numbers.append(match.group(1))
    if state not in USE_CASE_STATES:
        report.error(f"{name}: estado '{state}' inválido ({', '.join(sorted(USE_CASE_STATES))})")
        return None
    return identifier, state


def check_cited_code(source, tokens, types_by_namespace, operations, report):
    covered = set()
    for token in tokens:
        found = covered_types(token, types_by_namespace, operations)
        if not found:
            report.error(f"{source} cita `{token}`, que no existe en {MAP_NOTE}")
        covered |= found
    return covered


def check_traceability(notes, report):
    types_by_namespace, operations = parse_code_map(notes)
    all_types = {(namespace, type_name) for namespace, type_names in types_by_namespace.items() for type_name in type_names}
    covered = set()
    without_code = []
    case_numbers = []
    for name, text in sorted(case_sheets(notes).items()):
        checked = check_case_sheet(name, text, case_numbers, report)
        if checked is None:
            continue
        identifier, state = checked
        tokens = cited_in_code_section(text)
        if state == "sin código":
            without_code.append(identifier)
        elif not tokens:
            report.error(f"{name}: dice '{state}' pero su sección '{CODE_SECTION}' no cita ninguna clase, espacio de nombres u operación")
        covered |= check_cited_code(f"{name}:", tokens, types_by_namespace, operations, report)
    gaps = sorted({f"{number:02d}" for number in range(1, len(case_numbers) + 1)} - set(case_numbers))
    if gaps:
        report.warn("faltan fichas de casos de uso: " + ", ".join("CU-" + gap for gap in gaps))
    for rest in CROSS_CUTTING_LINE.findall(notes.get(SYSTEMS_NOTE, "")):
        covered |= check_cited_code(f"{SYSTEMS_NOTE}: TRANSVERSAL", CODE_TOKEN.findall(rest), types_by_namespace, operations, report)
    if without_code:
        report.warn(f"casos de uso sin código ({len(without_code)}): {', '.join(sorted(without_code))}")
    uncovered = sorted(all_types - covered)
    if uncovered:
        namespaces = sorted({namespace for namespace, _ in uncovered})
        shown = ", ".join(namespaces[:UNCOVERED_NAMESPACE_LIMIT])
        extra = f" y {len(namespaces) - UNCOVERED_NAMESPACE_LIMIT} más" if len(namespaces) > UNCOVERED_NAMESPACE_LIMIT else ""
        report.warn(f"{len(uncovered)} tipos del código que ningún caso de uso menciona, en: {shown}{extra}")
    return len(case_numbers), len(all_types)


def check_rubrics(notes, report):
    rubrics = notes.get(RUBRICS_NOTE)
    if rubrics is None:
        return
    today = datetime.date.today()
    for deliverable, due_text, criterion, state in RUBRIC_LINE.findall(rubrics):
        if state.strip() != RUBRIC_PENDING_STATE:
            continue
        days_left = (datetime.date.fromisoformat(due_text) - today).days
        if days_left <= RUBRIC_WARNING_DAYS:
            report.warn(f"{RUBRICS_NOTE}: '{criterion.strip()}' de {deliverable.strip()} está sin revisar y vence el {due_text}")


def check_session_notes(notes, report):
    people = set(registros.author_letters()) | SESSION_AUTHORS_WITHOUT_PERSON
    latest_date = ""
    for name, text in notes.items():
        if not is_session_note(name):
            continue
        match = SESSION_NOTE_NAME.match(pathlib.PurePosixPath(name).stem)
        if not match:
            report.error(f"{name}: el nombre debe ser AAAA-MM-DD-autor.md; crearla con nuevo.py bitacora")
            continue
        if match.group(2) not in people:
            report.error(f"{name}: autor '{match.group(2)}' no está en AUTORES.md")
        latest_date = max(latest_date, match.group(1))
        if text.count("\n") + 1 > SESSION_NOTE_LINE_BUDGET:
            report.warn(f"{name} pasa de {SESSION_NOTE_LINE_BUDGET} líneas: resumir")
    if not latest_date:
        report.error("no hay notas en bitacora/")
        return
    generated = GENERATED_DATE.search(notes.get(MAP_NOTE, ""))
    if generated and generated.group(1) < latest_date:
        report.warn(f"{MAP_NOTE} se generó el {generated.group(1)} y hay bitácora del {latest_date}; regenerar si cambió el código")


def check_stamps_and_budgets(notes, record_paths, report):
    for name, text in notes.items():
        line_count = text.count("\n") + 1
        if name in LINE_BUDGETS and line_count > LINE_BUDGETS[name]:
            report.warn(f"{name} tiene {line_count} líneas (máximo {LINE_BUDGETS[name]}): resumir")
        if is_session_note(name) or name in record_paths or name in NOTES_WITHOUT_VERIFICATION_STAMP:
            continue
        if not frontmatter_value(text, "verificado"):
            report.error(f"{name}: falta 'verificado:' en el encabezado")


def check_archive_manifest(report):
    archive = VAULT_ROOT / "archivo"
    manifest_path = archive / "MANIFIESTO.md"
    manifest = manifest_path.read_text(encoding="utf-8") if manifest_path.is_file() else ""
    for path in sorted(archive.rglob("*")):
        if path.is_file() and path.name != "MANIFIESTO.md" and path.name not in manifest:
            report.error(f"archivo/MANIFIESTO.md no lista {relative(path)}")
    for listed in re.findall(r"^\| `([^`]+)` \|", manifest, re.MULTILINE):
        if not (archive / listed).is_file():
            report.error(f"archivo/MANIFIESTO.md lista {listed}, que no existe")


def main():
    report = Report()
    notes = collect_notes()
    check_required_notes(report)
    check_merge_leftovers(notes, report)
    stems = check_unique_names(notes, report)
    check_wikilinks(notes, stems, report)
    identifiers, origins = check_records(report)
    check_record_references(notes, identifiers, report)
    rule_count = check_rule_references(notes, report)
    check_external_identifiers(notes, origins, report)
    check_fingerprints(notes, report)
    project_count = check_systems_cover_projects(notes, report)
    check_config_keys(notes, report)
    use_case_count, type_count = check_traceability(notes, report)
    check_rubrics(notes, report)
    check_session_notes(notes, report)
    record_paths = {relative(record.path) for kind in registros.KINDS.values() for record in registros.load_records(kind)}
    check_stamps_and_budgets(notes, record_paths, report)
    check_archive_manifest(report)
    for message in report.errors:
        print("ERROR " + message)
    for message in report.warnings:
        print("AVISO " + message)
    summary = (
        f"{len(notes)} notas, {len(identifiers['decision'])} decisiones, {len(identifiers['pregunta'])} preguntas, "
        f"{len(identifiers['tarea'])} tareas, {rule_count} reglas, {use_case_count} casos de uso, {project_count} proyectos y {type_count} tipos del código"
    )
    if report.errors:
        print(f"FALLA: {len(report.errors)} errores ({summary})")
        sys.exit(1)
    print(f"OK ({summary})")


if __name__ == "__main__":
    main()
