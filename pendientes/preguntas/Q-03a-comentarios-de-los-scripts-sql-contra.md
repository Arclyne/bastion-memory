---
tipo: pregunta
id: Q-03a
fecha: 2026-11-13
autor: angel
estado: abierta
grupo: hallazgos
---
# Q-03a · Comentarios de los scripts SQL contra E-67
E-67 admite en un script SQL un único comentario de bloque de encabezado y comentarios de línea junto a una columna solo cuando documentan una regla que el nombre no expresa; pone `GameModeId TINYINT NOT NULL, -- Mode identifier.` como ejemplo incorrecto.
`database/02_create_tables.sql` (commit `6dfb198`) tiene esa misma línea, líneas `-- @entity` y `-- @normalization` antes de cada tabla y un segundo bloque `/*---*/`. Además cita numeración vieja de casos de uso («2 or 4, never 3 (CU-17 RN-02)», y hoy CU-17 es Abandonar la partida).
No hay decisión que lo justifique. Solo se leyó el principio del script.
