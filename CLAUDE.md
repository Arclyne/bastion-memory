# Bastión — memoria compartida del proyecto

Este vault es la fuente de verdad de lo que el equipo sabe y decidió sobre **Bastión** (juego de estrategia por turnos inspirado en Quoridor; C#, MonoGame, CoreWCF sobre TCP, SQL Server). Lo comparten Angel y José, cada uno con su Claude, y se sincroniza por GitHub. Si el vault contradice a la memoria de Claude, gana el vault. Si el vault contradice al código, a los requisitos o al SAD, ganan ellos y se corrige el vault.

## Orden de autoridad
1. **El estándar** (`estandar/`) está por encima de cualquier preferencia de Angel, de José o de Claude (D-006a). Si pide algo que en otros proyectos no se usa, se sigue.
2. Una desviación del estándar solo vale si hay una decisión registrada con `reglas: E-NN` que la justifique. Hoy la mayor es R-39: sin comentarios en el código.
3. Ningún cambio de código se da por terminado sin revisarlo contra las reglas E-NN que le apliquen y sus decisiones (`ver.py reglas`).

## Al empezar (siempre, en este orden)
1. Saber quién es la persona: su clave está en `.autor`; si falta, preguntarle, comprobarla en `AUTORES.md` y crear el archivo.
2. `python3 herramientas/ver.py inicio` (estado, huella del código, bitácoras recientes, tareas urgentes).
3. `python3 herramientas/verificar.py` y arreglar lo que marque. Un `ERROR` de conflicto o de ID repetido significa que alguien más sincronizó: resolverlo antes de trabajar.
4. Si la huella del código cambió: `python3 herramientas/mapa_codigo.py generar`, revisar qué cambió, actualizar `codigo/sistemas.md` y las fichas de los casos afectados, y anotarlo en la bitácora.

## Dónde buscar (no leer todo)
| Necesito | Cómo |
|---|---|
| qué existe, qué falta, qué no se ha probado | `ESTADO.md` |
| una regla del estándar y cómo la aplica el equipo | `python3 herramientas/ver.py reglas [E-NN, sección o texto]` |
| excepciones y ejemplos de una regla | `grep` del número de sección en `estandar/texto/` |
| si algo ya se decidió o descartó | `python3 herramientas/ver.py decisiones [ID, R-NN, tema o texto]` |
| dudas sin resolver | `python3 herramientas/ver.py preguntas [ID, grupo o texto]` |
| trabajo pendiente y elecciones de Claude sin aprobar | `ver.py tareas`, `pendientes/TAREAS.md` |
| estado de un caso de uso, su código y sus decisiones | `python3 herramientas/ver.py casos [CU-NN o texto]` |
| qué hace cada proyecto y el código transversal | `codigo/sistemas.md` |
| SAD contra código | `diseno/arquitectura.md` |
| tablas y de dónde sale el modelo | `diseno/modelo-datos.md` |
| operaciones de servicio y reglas de red | `diseno/protocolo.md` |
| pantallas, estilo, Gum | `diseno/interfaz.md` |
| una clase, método, operación, tabla o paquete | `grep` en `codigo/mapa-codigo.md` (generado) |
| un número (límite, tiempo, puerto) | `grep` en `codigo/valores.md` (generado); en las notas se cita la clave, no el número |
| qué hizo cada quien y cuándo | `bitacora/AAAA-MM-DD-autor.md` |
| identificadores de otros documentos (REQ, SAD, journal) | `decisiones/REGISTRO.md` |

Buscar en todo: `grep -rn "texto" --include=*.md --exclude-dir=archivo .`

## Dos clases de notas
- **Registros** (decisiones, preguntas, tareas, bitácora): un archivo por registro, creado siempre con `python3 herramientas/nuevo.py`. Nunca se inventa un ID ni se crea el archivo a mano.
- **Notas de referencia** (`ESTADO.md`, `estandar/`, `diseno/`, `codigo/sistemas.md`): una por tema o por caso de uso; se editan en su lugar. No se crean notas de referencia nuevas sin que la persona lo pida.

## Al cambiar algo (en el momento, no al final de la sesión)
- Alguien decide algo → `nuevo.py decision`. Si cambia una decisión anterior, la vieja queda `estado: reemplazada por D-…`.
- Una regla del estándar admite dos lecturas, o dos fuentes se contradicen → `nuevo.py pregunta`; no se resuelve por cuenta de Claude. Al resolverse: decisión nueva y se borra la pregunta.
- Queda trabajo pendiente → `nuevo.py tarea`. Al terminarla se borra su archivo.
- Cambia el código → `codigo/sistemas.md` y la ficha del caso de uso en `diseno/casos/`. Cambia lo que existe → `ESTADO.md`.

## Al cerrar (cuando la persona diga "cierra sesión" o se despida)
1. Si cambió el código: `python3 herramientas/mapa_codigo.py generar`.
2. `nuevo.py bitacora` y llenar la nota del día de esta persona (máximo 40 líneas: cambió / probado / sin probar / lecciones / siguiente).
3. `python3 herramientas/verificar.py` hasta que diga `OK`.
4. Recordar a la persona que sincronice el vault. No hacer commit ni push sin que lo pida.

## Reglas del contenido
- Un dato vive en una sola nota; las demás lo citan por ID o enlace. Los números se citan por su clave (`MatchmakingPolicy.PresenceCheckMinutes`), no por su valor. Requisitos, SAD y estándar no se copian ni se resumen: se enlazan y se cita su ID con origen (`REQ D-25`, `SAD ADR-002`).
- Solo cuenta como decidido lo que confirmó una persona, y se anota quién. Lo que eligió Claude se marca **Claude eligió (sin aprobar)**.
- Lo que Claude recuerda de chats viejos no es fuente: se comprueba contra requisitos, SAD o código antes de anotarlo (así entraron al vault skins y tablas que ya no existían).
- Decir lo que no se sabe: si algo no se leyó o no se probó, la nota lo dice. Toda nota de referencia lleva `verificado: AAAA-MM-DD (contra qué)`.
- No editar la bitácora ni los registros de otra persona. Las notas `generado: sí` no se editan a mano.
- No mostrar ni copiar contraseñas, tokens ni cadenas de conexión al leer archivos del proyecto.
- `archivo/` no es fuente de verdad. Notas en español; código e identificadores como diga el estándar (E-01: inglés).

## Reglas de código
- Leer las reglas E-NN que apliquen antes de escribir. Sin rastros de IA en código, commits ni PRs.
- Rutas de error: probarlas contra una falla real antes de darlas por buenas. Interfaz con Gum: abrir el juego.
