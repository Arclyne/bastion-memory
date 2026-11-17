#!/usr/bin/env python3
import re
import sys

import registros

FULL_TEXT_MATCH_LIMIT = 3
RECENT_SESSION_NOTES = 3
START_TASK_GROUP = "ahora"
RULES_NOTE = registros.VAULT_ROOT / "estandar" / "reglas.md"
MAP_NOTE = registros.VAULT_ROOT / "codigo" / "mapa-codigo.md"
CASE_DIRECTORY = registros.VAULT_ROOT / "diseno" / "casos"
RULE_LINE = re.compile(r"^(E-\d{2,3}) \| §([\d.]+) \| (.+)$")
FINGERPRINT_LINE = re.compile(r"^huella: .+$", re.MULTILINE)


def without_frontmatter(text):
    return registros.split_frontmatter(text)[1].strip()


def matching_records(records, search_term):
    wanted = search_term.lower()
    exact = [record for record in records if record.identifier.lower() == wanted]
    by_origin = [record for record in records if record.origin.lower().split(" ")[-1] == wanted]
    return exact or by_origin or [record for record in records if wanted in record.text.lower()]


def show_records(kind, search_term):
    records = registros.load_records(kind)
    if not search_term:
        print("\n".join(record.summary_line for record in records))
        return
    matches = matching_records(records, search_term)
    if len(matches) <= FULL_TEXT_MATCH_LIMIT:
        print("\n\n".join(record.text.strip() for record in matches) or "sin resultados")
    else:
        print("\n".join(record.summary_line for record in matches))


def load_rules():
    rules = []
    for line in RULES_NOTE.read_text(encoding="utf-8").splitlines():
        match = RULE_LINE.match(line)
        if match:
            rules.append((match.group(1), match.group(2), line))
    return rules


def decisions_citing(rule_identifier):
    pattern = re.compile(r"\b" + re.escape(rule_identifier) + r"\b")
    decisions = registros.load_records(registros.KINDS["decision"])
    return [decision for decision in decisions if pattern.search(decision.text)]


def show_rules(search_term):
    rules = load_rules()
    if not search_term:
        print("\n".join(line.split(" | ", 3)[0] + " | " + " | ".join(line.split(" | ", 3)[1:3]) for _, _, line in rules))
        return
    wanted = search_term.lower().lstrip("§")
    matches = [rule for rule in rules if rule[0].lower() == wanted or rule[1] == wanted]
    matches = matches or [rule for rule in rules if rule[1].startswith(wanted + ".") or wanted in rule[2].lower()]
    if not matches:
        print("sin resultados")
        return
    for identifier, _, line in matches:
        print(line)
        for decision in decisions_citing(identifier):
            print("  → " + decision.summary_line)


def load_cases():
    cases = []
    for path in sorted(CASE_DIRECTORY.glob("CU-*.md")):
        text = path.read_text(encoding="utf-8")
        fields = registros.split_frontmatter(text)[0]
        line = f"{fields.get('id', '')} | {fields.get('estado', '')} | {fields.get('prioridad', '')} | {fields.get('nombre', '')}"
        cases.append((fields.get("id", ""), line, text))
    return cases


def show_cases(search_term):
    cases = load_cases()
    if not search_term:
        print("\n".join(line for _, line, _ in cases))
        return
    wanted = search_term.lower()
    matches = [case for case in cases if case[0].lower() == wanted]
    matches = matches or [case for case in cases if wanted in case[2].lower()]
    if not matches:
        print("sin resultados")
    elif len(matches) <= FULL_TEXT_MATCH_LIMIT:
        print("\n\n".join(text.strip() for _, _, text in matches))
    else:
        print("\n".join(line for _, line, _ in matches))


def stored_fingerprint():
    if not MAP_NOTE.is_file():
        return ""
    match = FINGERPRINT_LINE.search(MAP_NOTE.read_text(encoding="utf-8"))
    return match.group(0) if match else ""


def current_fingerprint():
    import mapa_codigo

    if not mapa_codigo.LOCAL_REPOSITORY_FILE.is_file():
        return "sin archivo .repo: no se puede comparar con el código (herramientas/LEEME.md)"
    try:
        repository = mapa_codigo.resolve_repository([])
    except SystemExit as failure:
        return str(failure)
    current = mapa_codigo.fingerprint_line(repository)
    verdict = "coincide con el vault" if current == stored_fingerprint() else "CAMBIÓ: regenerar codigo/mapa-codigo.md y revisar qué cambió"
    return f"{current}\n{verdict}"


def show_start():
    root = registros.VAULT_ROOT
    print(without_frontmatter((root / "ESTADO.md").read_text(encoding="utf-8")))
    print("\n## Huella del código guardada en el vault\n" + (stored_fingerprint() or "sin huella"))
    print("\n## Huella del código ahora\n" + current_fingerprint())
    print("\n## Bitácoras recientes")
    for path in sorted((root / "bitacora").glob("*.md"))[-RECENT_SESSION_NOTES:]:
        print(without_frontmatter(path.read_text(encoding="utf-8")) + "\n")
    tasks = registros.load_records(registros.KINDS["tarea"])
    print("## Tareas del grupo 'ahora'")
    print("\n".join(task.summary_line for task in tasks if task.group == START_TASK_GROUP) or "ninguna")
    questions = registros.load_records(registros.KINDS["pregunta"])
    by_group = {}
    for question in questions:
        by_group[question.group] = by_group.get(question.group, 0) + 1
    counts = ", ".join(f"{group}: {count}" for group, count in sorted(by_group.items()))
    print(f"\n## Preguntas abiertas: {len(questions)} ({counts})")


def main():
    commands = ("inicio", "reglas", "casos", *registros.KINDS_BY_PLURAL)
    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        sys.exit(
            "uso: ver.py inicio | ver.py decisiones|preguntas|tareas [ID o texto] | "
            "ver.py reglas [E-NN, sección o texto] | ver.py casos [CU-NN, estado o texto]"
        )
    search_term = " ".join(sys.argv[2:])
    if sys.argv[1] == "inicio":
        show_start()
    elif sys.argv[1] == "reglas":
        show_rules(search_term)
    elif sys.argv[1] == "casos":
        show_cases(search_term)
    else:
        show_records(registros.KINDS_BY_PLURAL[sys.argv[1]], search_term)


if __name__ == "__main__":
    main()
