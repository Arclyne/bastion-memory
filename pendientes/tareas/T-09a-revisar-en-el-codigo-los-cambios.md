---
tipo: tarea
id: T-09a
fecha: 2026-11-17
autor: angel
estado: pendiente
grupo: estandar
---
# T-09a · Revisar en el código los cambios del PR #24
- hecho cuando: Angel revisó en el código cada punto de la lista (marcado `[x]`), lo dudoso quedó como pregunta (`nuevo.py pregunta`) y lo pendiente de probar se probó en el juego o quedó como tarea del grupo `probar`.
- bloqueada por: nada; se revisa después del merge (Angel, 2026-11-17).
- origen: PR #24 de `Arclyne/bastion`, de José (poijn23), rama `review-standard-v2.4-fourth-pass`. Los PRs del #22 al #29 están apilados: cada uno se crea a partir del anterior.
- commits propios: 51, de `05a8e30` a `6772e75`. Para verlos: `git log --oneline 05a8e30..6772e75`. Para ver todo el cambio: `git diff 05a8e30 6772e75`. Los SHA siguen valiendo si se fusiona con merge commit; con squash o rebase cambian, y entonces hay que buscar por el título del commit.
- fuente de esta lista: la descripción del PR y la lectura del diff que hizo Claude el 2026-11-17. Claude no compiló ni corrió las pruebas: las cifras de pruebas son las que reporta José.

## Qué es
Cuarta revisión completa contra el estándar v2.4. Un commit por carpeta; según José, cada uno compila por sí solo.

## Cambios por revisar
### Servidor
- [ ] **Arreglo:** `RankedMatchCreator` rechaza un modo clasificatorio guardado con otro número de asientos. Antes, `Match.SeatEntrants` lanzaba un `ArgumentException` que llegaba al servicio de emparejamiento en segundo plano y detenía el host.
- [ ] `IRoomRegistry.TryOpen` devuelve `bool` y entrega la sala abierta en un parámetro `out` (el #29 vuelve a quitar ese `out`). `FindRoomToJoin` → `ClaimRoomToJoin`; el historial de códigos fallidos se llama `attemptHistory`.
- [ ] Los repositorios de partida y de sala nombran cada operación en una variable `Func` antes de correrla en un contexto nuevo.
- [ ] El límite de amigos cuenta los amigos del otro jugador antes de comparar, y el rechazo de sala inexistente se elige con una cláusula de guarda.
- [ ] `IPrivateRoomService.CreateRoom` documenta el `InvalidOperationException` que deja salir cuando no encuentra un código libre. Los dos servicios en segundo plano heredan su documentación.
- [ ] `MatchmakingQueue` informa el inicio de una búsqueda y si espera una confirmación de presencia.
- [ ] Nombres: `ToRejectionReason`, `ToSearchEndedReason`, `deletedRowCount`, `Pbkdf2IterationCount`, `friendSummary`.
- [ ] Dominio: `Match` y `WaitingRoom` crean sus listas en el constructor; las revisiones de casillas y los tiempos de búsqueda son privados; `BoardLayout.FirstIndex` es público para que el cliente lo use.
### Red
- [ ] `IChatClient.SendMessage` → `SendLobbyChatMessage`. `Disconnect` sale de `INotificationClient`, porque solo se usan `Connect` y `Dispose`.
- [ ] Un keep-alive que encuentra un canal ya cerrado por el cliente lo dice así, en vez de reportar que no llegó al servidor. El callback registra un valor fuera de rango sin afirmar que vino de la notificación.
### Cliente
- [ ] Las únicas implementaciones de `IClipboard`, `IScreenHost` e `INavigator` se llaman `Clipboard`, `ScreenHost` y `Navigator` (E-14, 2.5.2).
- [ ] `ModeratedChatViewModel` guarda el estado de silencio que repetían la conversación del lobby y la privada. `ConversationPartFactory` arma el compositor y el título y detalle del canal global.
- [ ] Reemplazan código repetido: `ViewFactory.SetFixedWidth`, `ButtonSpacing` y `ButtonWidth` de `DialogMetrics` y `ChatComposerViewModel.AddRecentMessage`.
- [ ] **Arreglo:** la pestaña de chat, el chat del lobby y el panel de amigos se suscriben a las notificaciones después de crear sus colecciones. Una notificación que llegara durante la construcción podía encontrar una colección nula.
- [ ] La conversación privada registra cada rechazo de carga y de marcar como leído con su razón. Los logs de solicitudes de amistad hablan de "acción de solicitud", que también cubre cancelar.
- [ ] Los valores que solo lee su clase pasan a privados. Los setters que escribe Gum ignoran un nulo. Los anchos calculados y la distancia de cámara opuesta tienen nombre.
### Pruebas
- [ ] Los helpers de prueba siguen el mismo orden que el código.
- [ ] Los textos de prueba están en inglés, salvo la lista de moderación de `TestChatWordFilter`, que se queda en español porque revisa acentos.
- [ ] Valores repetidos compartidos. Las pruebas comparan listas en vez de conteos. Los view models acompañantes se crean en el contexto de UI en línea. Las pruebas de la cola leen las nuevas consultas de la cola.

## Probar en el juego
José dice que probó: login, chat del lobby y privado, panel de amigos, dos partidas clasificatorias completas con muro y chat de partida, abandono y el diálogo de falla de login con el servidor apagado.
- [ ] Repetir al menos una partida completa después del merge.

## Defectos que José vio y que ya existían antes
- Salir de una partida terminada todavía llama al servidor, que registra un aviso.
- El aviso de "sin coincidencias" del filtro de amigos queda debajo de la lista.
- Los relojes del cliente se quedan en 5:00.
- El menú no avisa que el servidor se cayó hasta la siguiente acción.
- La fila de escribir del chat se mueve cuando aparece el aviso de estado.

## Lo que reporta José
Pasan 655 pruebas (Domain 216, Application 245, Client 194).
