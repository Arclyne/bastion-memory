---
tipo: estandar-texto
seccion: 8
verificado: 2026-11-13 (copia literal de pdftotext del PDF v2.4; ver [[estandar-v2.4]])
---
# 8. Comentarios Internos

```text
8.     Comentarios Internos
    Los comentarios forman parte del programa y se redactan siempre en inglés. Esta sección
regula los comentarios de línea (//) y de bloque (/* ... */) del código C#. Los comentarios de
documentación (///) se rigen por la Sección 7. Los archivos de configuración (.editorconfig,
.csproj, .props) y los scripts SQL siguen las reglas de esta sección con las precisiones de las
reglas 8.1.2 y 8.2.2.

8.1.     Intención e Idioma
8.1.1.    Regla: explicar el porqué en inglés
    Regla: El código debe ser autoexplicativo por su nombrado. Un comentario se admite
únicamente cuando explica una razón de negocio, una restricción técnica o una decisión que el
código no puede expresar por sí mismo. Todo comentario se escribe en inglés y nunca repite lo
que hace la instrucción.
    Descripción: Martin sostiene que la mayoría de los comentarios compensan código poco
claro; el comentario valioso explica una intención que el código no puede comunicar por sí solo
(Martin, 2008).
    Código correcto:
if (rollValue == MaximumFaceValue)
{
    // The official rules grant an extra turn after the maximum roll.
    GrantExtraTurn();
}

     Código incorrecto:
if (rollValue == MaximumFaceValue)
{
    // If the roll equals the maximum value, grant an extra turn.
    GrantExtraTurn();
}


8.1.2.    Regla: referencias a reglas y requisitos
    Regla: Un comentario puede expresar su porqué citando el número de una regla de este
estándar o el identificador de un requisito del proyecto (caso de uso, regla de negocio o decisión
de diseño). La cita debe existir en la versión vigente del documento citado; cuando cambia la
numeración del estándar o del requisito, el comentario se actualiza en el mismo cambio.



                                               48
   Ejemplo correcto: En .editorconfig, el comentario “# 3.3.1 Allman braces” antece-
de las opciones que aplican esa regla, y “– Seats in the match: 2 or 4, never 3 (CU-17
RN-02).” explica una restricción de una columna SQL.
   Ejemplo incorrecto: “# 3.4.1 At most 120 characters per line” cita una regla que ya
no existe en la versión vigente del estándar.

8.2.     Comentarios de Línea y de Bloque
8.2.1.    Regla: preferir comentarios de línea breves
    Regla: Se usa un comentario de línea con // para una explicación breve y excepcional. Se
evita el comentario de bloque /* ... */; si la explicación requiere varias líneas, se mejora el
diseño o se traslada la explicación al documento técnico correspondiente. Ningún comentario
conserva código deshabilitado (Microsoft, 2025e). El comentario de documentación /// no es un
comentario de bloque y se rige por la Sección 7.
    Código correcto:
// Saves from version 1.x store the board without the wall count.
int wallCount = saveData.WallCount ?? DefaultWallCount;

   Código incorrecto:
/* Read the wall count from the save data.
   If it is missing, use the default value.
   Then assign it to the local variable. */
int wallCount = saveData.WallCount ?? DefaultWallCount;
// int wallCount = LegacyReader.ReadWalls(saveData);


8.2.2.    Regla: comentarios en scripts SQL
    Regla: Un script SQL admite un único comentario de bloque como encabezado, que describe
el propósito del script. Un comentario de línea – junto a una columna se admite solo cuando
documenta una regla que el nombre no expresa: un rango de valores, el origen del dato o el
requisito que la exige. Prohibido el comentario que repite el nombre de la columna.
    Código correcto:
PlayerCount TINYINT NOT NULL, -- 2 or 4, never 3 (CU-17 RN-02).
WallsPerPlayer TINYINT NOT NULL,

   Código incorrecto:
GameModeId TINYINT NOT NULL, -- Mode identifier.
WallsPerPlayer TINYINT NOT NULL, -- Walls per player.


8.3.     Comentarios Especiales
8.3.1.    Regla: TODO y FIXME solo en ramas de trabajo
    Regla: TODO identifica trabajo planificado y FIXME un defecto conocido que requiere correc-
ción. Ambos se admiten únicamente en una rama de trabajo, se escriben en inglés, incluyen el
identificador de una tarea y describen una acción concreta. Una solicitud de cambios enviada a
revisión, y el código integrado a la rama principal, no contiene ningún TODO ni FIXME: antes de
solicitar la revisión, el trabajo pendiente se completa o se registra como una tarea independiente
en el sistema de seguimiento del equipo, y el comentario se retira del código.
    Código correcto (en una rama de trabajo, antes de solicitar la revisión):



                                               49
// TODO(GAME-142): Replace the temporary save adapter.
private readonly ISaveAdapter _saveAdapter = new MemorySaveAdapter();

      Código incorrecto:
// TODO: Fix this later.
private readonly ISaveAdapter _saveAdapter = new MemorySaveAdapter();

   Ejemplo incorrecto: La solicitud de cambios enviada a revisión conserva “TODO(GAME-
142): Replace the temporary save adapter.” en lugar de resolverlo o registrarlo como tarea.
```
