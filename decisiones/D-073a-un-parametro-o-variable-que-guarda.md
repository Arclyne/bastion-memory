---
tipo: decision
id: D-073a
fecha: 2026-11-18
autor: angel
estado: vigente
tema: estandar
reglas: E-02, E-06, E-11
---
# D-073a · Un parámetro o variable que guarda un dato no se nombra como verbo
- sobre: 2.1.1, 2.2.1, 2.4.1
- Angel decidió: un parámetro, una variable local o un parámetro de lambda que guarda un dato no se llama con una palabra que se lea como acción (`move`, `search`, `look`, `fill`). Se nombra con un sustantivo que dice qué dato es: `ChosenPawnMove` → `chosenMove`, `PawnMove` → `pawnMove`, `Move` (jugada guardada) → `playedMove`, `MatchSearch` → `matchSearch`, `ButtonLook` → `buttonLook`, `Color` de relleno → `fillColor`, `AddFriendViewModel` → `addFriendViewModel`. Un parámetro delegado también va con sustantivo: `snapRule`, `converter`, `matchStarter`, `roomChange`, `presenceReport`, `failureFactory`, `viewModelFactory`.
- porqué: E-02 pide nombres descriptivos; un verbo no dice qué dato llega.
- Angel aprobó al pedir el commit: aplicar el mismo nombre a los campos que guardan ese parámetro (`_buttonLook`, `_failureFactory`, `_addFriendViewModel`) y a los locales del mismo tipo.
- Angel decidió también: `play` pasa a `matchPlayViewModel` y la propiedad `Play` a `MatchPlay`, porque "play" solo se lee como "reproducir". `ChatMute` pasa a `ChatMuteStatus` (con `muteStatus`, `MuteStatus`, `FindMuteStatus`, `ShowMuteStatus`, `DescribeMuteStatus`), porque el valor es el estado del silencio y puede decir "no silenciado"; sigue la convención `…Status` de lo que dice cómo está algo. `TrySendToServer(sendToServer)` pasa a `TrySubmitTurn(turnSubmission)`: el nombre dice qué hace en el juego, no hacia dónde viaja, y evita vocabulario web (`Request`).
- Angel decidió también: la clase `Move` se queda así. Cumple E-11 (sustantivo singular, el término de juego de mesa para una jugada), es la entidad de la tabla `dbo.Move`, y el criterio de esta decisión aplica a parámetros y variables, no a tipos.
- Angel decidió también: un botón local lleva el sufijo `Button` (`cancelButton`, `sendButton`, `placeWallButton`); la regla general para todos los controles quedó en [[D-074a-una-variable-que-guarda-un-control|D-074a]]. Además, `PawnMovedEventArgs move` pasa a `pawnMove`. Los delegados locales (`Action movePawn = () => …`, `Func<RoomState> createRoom = …`, `Action send` en las pruebas) quedan exentos: guardan código que se ejecuta enseguida y se nombran con verbo, como un método (E-06). Los parámetros delegado sí van con sustantivo de rol.
- descartado: renombrar los ~230 delegados locales con un sustantivo (`sendAttempt`, `lobbyChatMessageCall`); `mutedChat` (el valor no es un chat); `serverRequest` (vocabulario web); renombrar la clase `Move` a `PlayedMove` (obligaba a cambiar la tabla, los scripts SQL y `Match.Moves`).
- dónde vive: rama `review-parameter-naming` de `Arclyne/bastion`, commits `9da39b8` y `3ecc23a`, PR Arclyne/bastion#30 (2026-11-18).
