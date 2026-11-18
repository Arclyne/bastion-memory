---
tipo: tarea
id: T-11a
fecha: 2026-11-17
autor: angel
estado: pendiente
grupo: estandar
---
# T-11a · Revisar en el código los cambios del PR #26
- hecho cuando: Angel revisó en el código cada punto de la lista (marcado `[x]`), lo dudoso quedó como pregunta (`nuevo.py pregunta`) y lo pendiente de probar se probó en el juego o quedó como tarea del grupo `probar`.
- bloqueada por: nada; se revisa después del merge (Angel, 2026-11-17).
- origen: PR #26 de `Arclyne/bastion`, de José (poijn23), rama `review-standard-v2.4-sixth-pass`. Los PRs del #22 al #29 están apilados: cada uno se crea a partir del anterior.
- commits propios: 41, de `94c6256` a `4019629`. Para verlos: `git log --oneline 94c6256..4019629`. Para ver todo el cambio: `git diff 94c6256 4019629`. Los SHA siguen valiendo si se fusiona con merge commit; con squash o rebase cambian, y entonces hay que buscar por el título del commit.
- fuente de esta lista: la descripción del PR y la lectura del diff que hizo Claude el 2026-11-17. Claude no compiló ni corrió las pruebas: las cifras de pruebas son las que reporta José.

## Qué es
Sexta revisión completa contra el estándar v2.4. Un commit por carpeta.

## Cambios por revisar
### Cambios de comportamiento
- [ ] **Botones de píldora:** el botón de salir del login usa la altura compartida (44 en vez de 42), y el radio es la mitad de esa altura (22 en vez de 21).
- [ ] **Logs del cliente:** los avisos por una falla de partida dicen solo lo que respondió el servidor. `NotYourTurnException` nombra las dos causas y el número de la siguiente jugada.
- [ ] **Logs del servidor:** el guardia del chat de partida, el creador de partidas clasificatorias (cuando no hay modo activo con el código clasificatorio) y el reportador de presencia (falla de comando de base, como los demás).
- [ ] **Ojo:** este PR cambia una palabra del log de jugada rechazada y el #27 la regresa ("The server rejected a pawn move.").
### Servidor
- [ ] `Match` da nombre a sus dos revisiones repetidas: `IsTwoPlayerMatch()` y `Participation.HasEnded()`.
- [ ] `MatchSearch` quita los `Equals` y `GetHashCode` que nadie usaba.
- [ ] `BoardLayout.FirstIndex` se mueve junto a las demás constantes públicas.
- [ ] Documentación: `IRoomService.CreateRoom` e `IPrivateRoomService.CreateRoom` documentan la falla de código de sala del #25; `ILoginService.LogIn` cubre una cuenta sin contraseña.
- [ ] Nombres: `completeOperation` en los siete envoltorios `Call(Action)`, `chosenMove`, `MaximumCodeDraws`, `recipientAccountId`, `_readAtSelector`.
- [ ] La huella del dispositivo se calcula en una variable con nombre antes de crear el dispositivo.
### Cliente
- [ ] `DialogCard` arma los botones de los cuatro diálogos con `CreateDialogButton` y `CreateWideButton`.
- [ ] `ViewFactory.CreateCenteredLines` reemplaza cuatro copias de un bloque centrado de dos líneas; `ConversationPartFactory.CreateLoadFailure` reemplaza tres copias de la falla de carga del chat.
- [ ] El umbral del contador del chat es el máximo menos un margen con nombre. El radio del marcador de pestaña es la mitad de su altura.
- [ ] `ChatTimeText.IsYesterday`. El estado del compositor tiene setter privado. El filtro de amigos se nombra antes de usarlo. Los helpers siguen a su primer uso.
### Pruebas
- [ ] Ejemplos en inglés y español para datos tecleados en el traductor de amigos, el chat de partida, las notificaciones de chat, los mensajes privados, la política de chat y el login. La prueba de login revisa que el identificador llegue sin cambios al servidor.
- [ ] Nueva prueba: una búsqueda de código de sala agotada lanza `RoomCodeUnavailableException`.
- [ ] Las pruebas de tope llenan hasta el límite con un helper. Se renombran cinco pruebas y dos miembros de objetos falsos.
- [ ] `FakeLanguageService` ya no lanza un evento que nadie escucha.

## Probar en el juego
José probó login, panel de amigos, diálogo de eliminar amigo (cancelado), contador del chat en 192/200, una partida completa con muro, un abandono y, con el servidor apagado, la búsqueda y el diálogo de falla de login.
- [ ] Revisar a simple vista el botón de salir del login (cambió de tamaño).

## Lo que reporta José
Pasan 695 pruebas (Domain 227, Application 252, Client 216).
