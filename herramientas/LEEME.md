# Herramientas

Todas se corren desde cualquier carpeta con `python3 herramientas/<nombre>.py`. Solo usan la biblioteca estándar de Python 3.

## ver.py (leer)
- `ver.py inicio`: estado, huella guardada y huella actual del código, bitácoras recientes, tareas del grupo `ahora` y conteo de preguntas. Es lo primero de cada sesión.
- `ver.py decisiones|preguntas|tareas`: una línea por registro (`id | tema o grupo | estado | título`).
- `ver.py decisiones D-046j`, `ver.py decisiones R-32` (número viejo del journal) o `ver.py preguntas SAD`: con un ID o un texto imprime el registro completo si hay 3 o menos coincidencias; si hay más, la lista.
- `ver.py casos`: una línea por caso de uso (`id | estado | prioridad | nombre`). `ver.py casos CU-12` o `ver.py casos "sin código"`: la ficha completa si hay 3 o menos coincidencias; si hay más, la lista.
- `ver.py reglas`: las 91 reglas en una línea corta. `ver.py reglas E-64`, `ver.py reglas 8.1.1`, `ver.py reglas 2.11` o `ver.py reglas lambda`: el enunciado completo y, debajo, las decisiones que citan esa regla.

## nuevo.py (escribir)
- `nuevo.py decision "Título" --tema estandar` · `nuevo.py pregunta "Título" --grupo hallazgos` · `nuevo.py tarea "Título" --grupo ahora` · `nuevo.py bitacora`
- Pone el ID (siguiente número + letra de la persona), el nombre del archivo y el encabezado. Imprime la ruta creada; después se completa el cuerpo.
- Sabe quién escribe por el archivo `.autor` (una palabra: la clave de `AUTORES.md`) o por `--autor`. Si falta, se detiene y lo dice.
- `--fecha AAAA-MM-DD` si la fecha del sistema no es la de la persona.
- A una decisión que interpreta o se desvía de una regla se le agrega a mano `reglas: E-NN` en el encabezado.

`registros.py` es el módulo común.

## mapa_codigo.py (mapa y valores del código)
Lee el repositorio de código (no lo modifica) y escribe dos notas con la misma huella:
- `codigo/mapa-codigo.md`: solución, proyectos con referencias y paquetes, pruebas por proyecto, contratos de servicio con sus operaciones y fallas, tipos públicos por espacio de nombres con sus métodos, y tablas y procedimientos de `database/*.sql`.
- `codigo/valores.md`: `appsettings*.json` aplanado (`appsettings.Server.NetTcpPort=…`) y cada constante o valor estático inicializado de `src/` como `Clase.Nombre=expresión`, tal como está escrito (sin calcular). Las notas citan estas claves, no los números.

`codigo/sistemas.md` se escribe a mano: qué hace cada proyecto y qué código es transversal.

- La ruta del repositorio se pasa como argumento o se guarda en el archivo `.repo` de la raíz del vault (una línea; no se sincroniza, cada computadora tiene la suya).
- `mapa_codigo.py huella [ruta]`: imprime solo la huella, para compararla con la de la nota.
- `mapa_codigo.py generar [ruta]`: reescribe las dos notas completas.
- No hay parche por líneas (el `parche.py` de la plantilla): el script corre en la misma computadora que el vault y escribe las notas directo, sin pasar el texto por Claude.
- La huella cambia si cambia cualquier `.cs` o `.csproj` de `src/` y `tests/` (`codigo=`) o cualquier `.sql` de `database/` (`sql=`). No depende del commit ni del sistema operativo (ignora los fines de línea). No ve cambios en recursos, configuración ni contenido gráfico.
- Lee el C# con expresiones regulares, no con un compilador: toma el primer tipo de cada archivo (E-55) y los métodos públicos con la sangría normal. Tipos anidados, propiedades y métodos en varias líneas no salen.
- Si dos personas regeneran a la vez, git une las notas línea por línea y quedan revueltas: el verificador lo detecta (más de una línea `huella:`, o huellas distintas entre las dos notas) y se regenera.

## verificar.py
Revisa: notas obligatorias, nombres repetidos, enlaces rotos, marcadores de conflicto, formato e ID únicos de cada registro, registros citados que no existen, reglas E-NN citadas que no existen en `estandar/reglas.md`, identificadores de otros documentos sin su origen (`D-NN` sin `REQ` o `journal`, `ADR-NNN` sin `SAD`, `R-NN` que no es del journal ni lleva `SAD`), una sola huella por nota generada e iguales entre `mapa-codigo` y `valores`, que `codigo/sistemas.md` mencione cada proyecto del mapa, claves de configuración citadas entre comillas invertidas (dueño terminado en Policy, Endpoints o Metrics, o `appsettings`) que existan en `valores`, fichas de casos de uso (encabezado, id igual al nombre del archivo, estado válido; lo que cita su sección «## Código» debe existir en el mapa; avisa de huecos en la numeración, de casos sin código y de tipos que ningún caso ni `sistemas` § Código transversal menciona), rúbricas, bitácoras, `verificado:` en las notas de referencia, tamaño de las notas de arranque y que `archivo/MANIFIESTO.md` liste todo. Termina en `OK (...)` o lista `ERROR` / `AVISO`. Un `AVISO` no hace fallar.

### Rúbricas (cuando exista `estandar/rubricas.md`)
Una línea por criterio: `Entregable | AAAA-MM-DD | criterio | estado`, con estado `cumple`, `falta` o `sin revisar`. El verificador avisa de los `sin revisar` cuya fecha está a 7 días o menos, o ya pasó. La nota no existe todavía (Q-01a).

## Sincronización
- `.gitattributes` une sin conflicto las notas generadas; `.gitignore` deja fuera `.autor`, `.repo` y el espacio de trabajo de Obsidian.
- `.github/workflows/verificar.yml` corre `verificar.py` en cada push.
