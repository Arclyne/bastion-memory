---
tipo: guia-registros
verificado: 2026-11-13
---
# Tareas

Cada tarea es un archivo en `pendientes/tareas/`. No hay lista escrita a mano: se consulta con el visor.

- Ver todas: `python3 herramientas/ver.py tareas` · una: `ver.py tareas T-01a` · por texto o grupo: `ver.py tareas probar`
- Crear: `python3 herramientas/nuevo.py tarea "Título corto" --grupo ahora` (grupos: `ahora`, `probar`, `construir`, `estandar`). Luego completar el cuerpo.
- Terminar: borrar el archivo y anotarlo en la bitácora. Quien la deja a medias cambia `estado:` y explica en el cuerpo.
- `responsable:` en el encabezado dice quién la hace; sin ese campo es de cualquiera.
- Un caso de uso sin construir no es una tarea: su estado vive en su ficha (`ver.py casos`).

## Elecciones de Claude sin aprobar
Valen hasta que Angel o José las cambien; si las aprueban, pasan a una decisión.
- El alias `R-NN` y la forma `journal D-0N` (D-007a).
- Los estados y el código que cita cada ficha de caso de uso (T-06a).
- Qué espacios de nombres cuentan como transversales en [[sistemas]].
- Qué tipos de [[valores]] cuentan como fachada en `ESTADO.md`.
- Las lecciones convertidas en reglas de trabajo de `CLAUDE.md`.

## Fases
El curso pide incrementos semanales auditables en 14 semanas. Sin las rúbricas no se sabe qué pide cada incremento ni en qué semana va el equipo (Q-01a).
| Fase | Objetivo | Estado |
|---|---|---|
| Análisis y diseño | contexto, requisitos, SAD, modelo de datos | hecho: requisitos, SAD v0.2 y scripts de la base |
| Construcción | casos de uso del alcance | 9 con código, 6 parciales, 12 sin código (`ver.py casos`) |
| Estándar | código revisado contra la v2.4 | revisado hasta el archivo 404 de 493 al 2026-11-11 (Q-08a) |
| Pruebas y entrega | casos probados, rúbricas cumplidas | sin empezar; rúbricas sin cargar (Q-01a) |
