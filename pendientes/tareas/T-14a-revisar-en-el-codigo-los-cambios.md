---
tipo: tarea
id: T-14a
fecha: 2026-11-17
autor: angel
estado: pendiente
grupo: estandar
---
# T-14a · Revisar en el código los cambios del PR #29
- hecho cuando: Angel revisó en el código cada punto de la lista (marcado `[x]`), lo dudoso quedó como pregunta (`nuevo.py pregunta`) y lo pendiente de probar se probó en el juego o quedó como tarea del grupo `probar`.
- bloqueada por: nada; se revisa después del merge (Angel, 2026-11-17).
- origen: PR #29 de `Arclyne/bastion`, de José (poijn23), rama `review-no-out-parameters`. Los PRs del #22 al #29 están apilados: cada uno se crea a partir del anterior.
- commits propios: 14, de `ac1da4d` a `2d23ca4`. Para verlos: `git log --oneline ac1da4d..2d23ca4`. Para ver todo el cambio: `git diff ac1da4d 2d23ca4`. Los SHA siguen valiendo si se fusiona con merge commit; con squash o rebase cambian, y entonces hay que buscar por el título del commit.
- fuente de esta lista: la descripción del PR y la lectura del diff que hizo Claude el 2026-11-17. Claude no compiló ni corrió las pruebas: las cifras de pruebas son las que reporta José.

## Qué es
Ningún método propio declara un parámetro `out`: cada método devuelve el resultado, un valor bandera cuando no hay resultado, o actúa sobre el resultado. Las llamadas a `Try…` de .NET (`Dictionary.TryGetValue`, `int.TryParse`, el `TryGetValue` de CoreWCF) conservan su `out`. **Según José, los commits intermedios no compilan.**

## Antes de revisar el código
- [x] Resuelto el 2026-11-18: D-080a reemplaza a D-020j (Angel). **Dudoso: contradice una decisión registrada y el estándar no lo pide.** La D-020j (R-06) pide el patrón `TryGetX(…, out T x)`, y este PR quita justo `TryGetActiveLockEnd`, que salió de esa decisión. Además, E-08 (2.2.3) permite los métodos `Try…`. Si se queda, hace falta una decisión nueva que deje la D-020j como `reemplazada`.
- [ ] **Dudoso: valores bandera.** Un `""` o un `(-1, -1)` olvidado no da advertencia del compilador; un null con anulables sí.

## Cambios por revisar
- [ ] Casillas: `BoardLayout.FindSquare` reemplaza `TryParseSquare` y devuelve la casilla, o `BoardLayout.OffBoardSquare` (-1, -1). `ParseSquare` lanza `FormatException` con esa bandera. `MatchMoveService` y `MatchPlayViewModel` comparan contra ella.
- [ ] Bloqueo de cuenta: `Account.GetLockEnd` reemplaza `TryGetActiveLockEnd` y devuelve el fin del bloqueo, o `now` si no está bloqueada. `IsLockedAt` compara con `now` y `GetRemainingLockMinutes` ya no tiene rama.
- [ ] Códigos de sala: `IRoomRegistry.CreateUnusedCode` devuelve el código, o una cadena vacía si ya está en uso (`RoomKeeper` revisa `code.Length > 0`).
- [ ] Abrir sala: `IRoomRegistry.TryOpen(room)` devuelve solo `bool` (el `out` que agregó el #24 se va). `RoomKeeper` toma la foto de la sala antes de registrarla.
- [ ] Borradores de chat: `ChatComposerViewModel.TakeValidDraft` devuelve el texto recortado, o una cadena vacía después de mostrar el aviso. Los chats de lobby, privado y de partida salen si está vacío.
- [ ] Tablero bajo el cursor: `BoardSceneLayout.FindCoordinates` y `FindGroove` devuelven la celda o ranura, o `OffBoardSquare`. `BoardScene.FindSurfacePoint` devuelve `BoardSceneLayout.OffBoardPoint` si el rayo no toca el tablero. `BastionGame` compara con `OffBoardSquare`.
- [ ] Creador de partida clasificatoria: `RankedMatchCreator.CreateMatch` recibe `IMatchmakingNotifier`, manda él mismo "partida encontrada" o "falló la creación" y no devuelve nada. `NotifyMatchCreationFailed` pasa del despachador al creador.
- [ ] Orden de `using`: arregla 25 archivos del #28 donde `using System;` iba después de `using System.*` (E-57).
### Pruebas
- [ ] Nuevas: `FindCoordinates_FirstCellCenter_ReturnsFirstCell`, `FindCoordinates_OffBoardPoint_ReturnsOffBoardSquare`, `FindGroove_OffBoardPoint_ReturnsOffBoardSquare` y `CreateRoom_CodeOfOpenRoom_UsesNextCode`. `FindSquare_TextOutsideNotation_ReturnsOffBoardSquare` reemplaza la prueba de `TryParseSquare`.
- [ ] `TestRankedMatchCreator` lee los avisos del notificador falso.

## Probar en el juego
José probó: cuenta bloqueada tras tres contraseñas incorrectas, un borrador en blanco y uno real en el chat global, una partida completa (seleccionar peón y hacer clic fuera del tablero, muro, pasar el cursor sobre una ranura ocupada y mensaje en el chat de partida) y salir de la partida terminada.

## Pendientes que José reporta
- NuGet avisa de `System.Security.Cryptography.Pkcs` y `System.Security.Cryptography.Xml` (NU1902/NU1903); el arreglo irá en otra rama.
- Salir de una partida terminada registra un aviso ("A player without an active participation tried to leave the match"); ya pasaba antes.

## Lo que reporta José
Pasan 742 pruebas (Domain 232, Application 277, Client 233).
