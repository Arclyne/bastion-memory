---
tipo: tarea
id: T-12a
fecha: 2026-11-17
autor: angel
estado: pendiente
grupo: estandar
---
# T-12a · Revisar en el código los cambios del PR #27
- hecho cuando: Angel revisó en el código cada punto de la lista (marcado `[x]`), lo dudoso quedó como pregunta (`nuevo.py pregunta`) y lo pendiente de probar se probó en el juego o quedó como tarea del grupo `probar`.
- bloqueada por: nada; se revisa después del merge (Angel, 2026-11-17).
- origen: PR #27 de `Arclyne/bastion`, de José (poijn23), rama `review-standard-v2.4-seventh-pass`. Los PRs del #22 al #29 están apilados: cada uno se crea a partir del anterior.
- commits propios: 33, de `4019629` a `25ae9f9`. Para verlos: `git log --oneline 4019629..25ae9f9`. Para ver todo el cambio: `git diff 4019629 25ae9f9`. Los SHA siguen valiendo si se fusiona con merge commit; con squash o rebase cambian, y entonces hay que buscar por el título del commit.
- fuente de esta lista: la descripción del PR y la lectura del diff que hizo Claude el 2026-11-17. Claude no compiló ni corrió las pruebas: las cifras de pruebas son las que reporta José.

## Qué es
Séptima revisión completa contra el estándar v2.4. Un commit por carpeta y uno por contrato.

## Cambios por revisar
### Cambios de comportamiento (textos de log)
- [ ] Servidor: los guardias de jugada y de abandono registran "A player without an active participation tried to move in / leave the match.", porque la revisión también da falso en una partida terminada o con un jugador que ya salió.
- [ ] Servidor: el log de jugada rechazada vuelve a decir "The server rejected a pawn move." (el #26 lo había cambiado). Una cuenta sin contraseña conserva su id en el log de accesos.
- [ ] Cliente: el aviso del chat de partida, el de tiempo agotado de la jugada propia y el error del keep-alive cambian de texto.
### Servidor
- [ ] Documentación: 13 líneas `FaultException` en 7 contratos de servicio dicen qué trabajo de base falló, en vez de "could not reach the database". `IMatchAbandonmentService` cubre una partida terminada, `IPrivateRoomService.JoinRoom` documenta la revisión de partida iniciada y `IMatchChatService` coincide con su log.
- [ ] Nombres: `ListActiveParticipantAccountIds`, `draw` en el ciclo de códigos de sala, `requesterIdSelector` y `recipientIdSelector`.
- [ ] Dominio: `Match.BuildBoard` dimensiona su diccionario según las participaciones activas.
### Cliente
- [ ] Tema: el enum de banderas `InteractionFlags` → `InteractionStates`, porque un enum de banderas lleva nombre en plural sin el sufijo Flags.
- [ ] Panel de amigos: el pie con el código de amigo y el menú de acciones comparten `PlaceAtBottomLeft`.
- [ ] Valores con nombre antes de usarse: el título del aviso de cuenta bloqueada, el texto del tiempo de búsqueda, la ruta de la fuente, la ruta de configuración de logs, el identificador de login y la presencia refrescada de la conversación.
### Pruebas
- [ ] 16 teorías nuevas revisan que un ejemplo en inglés y otro en español lleguen sin cambios (servidor: login, abandono, jugadas y muros, salas, búsqueda de jugadores, partida clasificatoria, amigos, sesión y presencia; cliente: chat de partida, notificaciones de chat, abandono y pantalla VS).
- [ ] Los helpers reciben los datos tecleados como parámetro (`AddActiveAccount(nickname)`, `AddSession(nickname)`, `FillRoom(guest)`). Nuevos: `FakeChatClient.LastSentText` y `JoinedMatchSampleFactory.CreateWithRival`.
- [ ] Los inicializadores repetidos de las pruebas de traductor y callback usan un helper por clase. Variable local `expectedAccountIds` y `closedRoom` en vez de `closure`.

## Probar en el juego
José probó el aviso de cuenta bloqueada, el pie y el menú del panel de amigos, la presencia cambiando en una conversación abierta, el reloj de búsqueda, una partida completa con muro y un mensaje en español, salir de la partida terminada y la falla del canal al apagar el servidor.
- [ ] Crear sala: el cliente aún no tiene manejador, así que el ciclo de códigos solo lo cubren las pruebas unitarias.

## Lo que reporta José
Pasan 727 pruebas (Domain 227, Application 276, Client 224).
