---
tipo: tarea
id: T-15a
fecha: 2026-11-18
autor: angel
estado: pendiente
grupo: estandar
---
# T-15a · Buscar condiciones que juntan varias preguntas en un if
- hecho cuando: se revisó todo `src/` y `tests/` en busca de un `if` que junta con `||` o `&&` preguntas distintas (nulo, búsqueda con `TryGetValue`/`TryParse`, tipo con `is`, rango) sin que se lea qué comprueba; cada caso quedó partido en pasos o métodos con nombre, o anotado por qué se queda; y Angel aprobó la lista antes de editar.
- bloqueada por: nada.
- origen: Angel, 2026-11-18, al revisar `CallerAddress.GetCurrent`. Tenía `properties is null || !TryGetValue(…) || value is not …` en una sola condición. Quedó partido en `GetCurrent` (¿hay llamada en curso?) y `ReadRemoteAddress` (lee la dirección con `hasRemoteEndpoint` y un cast), porque el código debe documentarse solo (E-64).
- candidatos ya vistos: `BoardLayout.FindSquare` (columna, `isRowNumber` y fila en un `if`), `ServerAddress.GetPort`, `MatchPlayViewModel.ReceivePawnMove` y `ReceiveWallPlacement` (el 2026-11-18 la búsqueda ya tiene nombre, `isKnownMover` e `isKnownPlacer`, pero sigue junta con `== OffBoardSquare` en un solo `if` y un solo aviso), `MatchViewModel:103` (`!HasLeft && TryGetValue`).
- cuidado: D-019j y D-038j ya dicen cuándo una condición es corta; no partir una que esas decisiones dejan pasar sin preguntarle a Angel.
