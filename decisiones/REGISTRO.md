---
tipo: guia-registros
verificado: 2026-11-13
---
# Registro de decisiones

Cada decisión es un archivo en esta carpeta (`D-NNNx-titulo.md`). No hay índice escrito a mano: se consulta con el visor.

- Ver todas (una línea cada una): `python3 herramientas/ver.py decisiones`
- Una: `ver.py decisiones D-046j` · por número viejo del journal: `ver.py decisiones R-39` · por tema o texto: `ver.py decisiones estandar`
- Las que tocan una regla: `ver.py reglas E-67`
- Crear: `python3 herramientas/nuevo.py decision "Título corto" --tema estandar`. Luego completar el cuerpo y borrar las líneas que no apliquen.

## Formato del cuerpo
- `<Persona> decidió:` lo que confirmó una persona del equipo, con su nombre.
- `Claude eligió (sin aprobar):` detalle que nadie ha aprobado; se puede cambiar sin nueva decisión.
- `porqué:`, `descartado:`, `dónde vive:`, `abierto:` solo si aportan.
- Encabezado opcional: `reglas: E-NN, E-NN` (reglas del estándar que interpreta o de las que se desvía) y `origen:` (número que tenía en otro documento).

## Reglas
- `estado:` es `vigente`, `reemplazada por D-NNNx` o `retirada`. Una decisión no se borra ni se reescribe: si cambia, se crea otra y la vieja se marca reemplazada.
- El ID lo pone `nuevo.py`: siguiente número más la letra de quien escribe (`a` Angel, `j` José). Así dos personas nunca crean el mismo ID.
- Una desviación del estándar solo vale si su decisión lleva `reglas:` con la regla de la que se desvía (D-006a).
- Temas en uso: `estandar`, `revision`, `alcance`, `interfaz`, `vault`.

## Identificadores de otros documentos (D-007a)
| Se escribe | Qué es | Dónde está |
|---|---|---|
| `REQ D-NN` | decisión de diseño de los requisitos (REQ D-01 a REQ D-29) | `requisitos-bastion/decisiones.tex` |
| `CU-NN`, `DES-NN`, `RN-NN` | caso de uso, requisito deseable, regla de negocio | `requisitos-bastion/casos/` |
| `SAD ADR-NNN`, `SAD R-NN`, `SAD Q-NN` | decisión, riesgo y pregunta de arquitectura | `bastion_game_sad/main.tex` |
| `R-NN` (sin prefijo) | número viejo de una decisión de reglas del journal de José; hoy es una decisión del vault (`origen: journal R-NN`) | `decisiones/` |
| `journal D-0N` | decisión de método del journal de José (`origen: journal D-0N`) | `decisiones/` |
| `L-NN` | lectura abierta del journal de José; las que siguen abiertas son preguntas con `origen: journal L-NN` | `pendientes/preguntas/`, `archivo/` |

Las decisiones migradas del journal conservan el texto de José sin cambios; solo se añadió «journal» delante de sus `D-0N`.
