---
tipo: tarea
id: T-08a
fecha: 2026-11-17
autor: angel
estado: pendiente
grupo: estandar
---
# T-08a · Revisar en el código los cambios del PR #23
- hecho cuando: Angel revisó en el código cada punto de la lista (marcado `[x]`), lo dudoso quedó como pregunta (`nuevo.py pregunta`) y lo pendiente de probar se probó en el juego o quedó como tarea del grupo `probar`.
- bloqueada por: nada; se revisa después del merge (Angel, 2026-11-17).
- origen: PR #23 de `Arclyne/bastion`, de José (poijn23), rama `review-standard-v2.4-third-pass`. Los PRs del #22 al #29 están apilados: cada uno se crea a partir del anterior.
- commits propios: 67, de `e10e98b` a `05a8e30`. Para verlos: `git log --oneline e10e98b..05a8e30`. Para ver todo el cambio: `git diff e10e98b 05a8e30`. Los SHA siguen valiendo si se fusiona con merge commit; con squash o rebase cambian, y entonces hay que buscar por el título del commit.
- fuente de esta lista: la descripción del PR y la lectura del diff que hizo Claude el 2026-11-17. Claude no compiló ni corrió las pruebas: las cifras de pruebas son las que reporta José.

## Qué es
Tercera revisión completa contra el estándar v2.4, clase por clase y sección por sección. Un commit por carpeta; según José, cada commit compila la solución por sí solo.

## Cambios por revisar
### En todo el código
- [ ] Una instrucción larga ya no se corta después del `=`: la asignación queda en su línea y los argumentos van uno por línea. Los inicializadores de colección, las cadenas interpoladas y las llamadas sin argumentos sí se siguen cortando después del `=`.
- [ ] Los eventos se lanzan desde un método privado `On…`.
- [ ] Una tarea que se arranca sin esperarla pasa por `RunSafely`, que registra como aviso un `ObjectDisposedException` si la pantalla ya se cerró.
- [ ] Los accesores de una propiedad cuentan como primer uso de un método privado al ordenar la clase.
- [ ] Un campo no se inicializa en su declaración si el constructor asigna los demás.
### Dominio y servidor
- [ ] `SessionTicket`, `LoggedInPlayer` y `GeneratedToken` (guardan tokens, contraseñas y hashes) pasan de record a clase sellada.
- [ ] `Message.GetPartnerId` rechaza un mensaje de chat de partida, y `MessageParticipants` se renombra a `MessageRoute`.
- [ ] El tablero gana `IsStepOpen` y `CopyWithWall`; `Match` gana `IsFinished`.
- [ ] Los repositorios corren los procedimientos de borrado con un solo `DeleteProcedure`, y una sala terminada revisa primero su partida.
- [ ] El reportador de presencia de amigos registra una falla de base en vez de dejar escapar la excepción.
- [ ] `RoomService` rechaza un modo de juego desconocido como configuración inválida.
- [ ] El registro de notificaciones rechaza un mensaje privado sin destinatario.
### Contratos y red
- [ ] **Cambio de nombres:** `ServiceEndpoints` → `EndpointCatalog` y `ChannelSettings` → `ChannelConfiguration`.
- [ ] La búsqueda de jugadores y la lista de conversaciones declaran que sus arreglos pueden llegar nulos.
- [ ] El callback de notificaciones registra como aviso una notificación con un valor desconocido en vez de dejar escapar la excepción. Los datos de partida encontrada pasan a `Matchmaking`.
### Cliente
- [ ] Conjuntos con nombre en singular: `LocalServiceSet`, `ChatClientSet`, `SocialClientSet`, `JoinedMatchViewModelSet`. `ConversationParts` → `ConversationPartFactory`.
- [ ] `ViewFactory`, `TextStyle`, `ShapeFactory` y `PanelMetrics` concentran piezas que varias vistas repetían: el bloque de falla de carga con su botón de reintentar, etiquetas, contenedores y botones con visibilidad o texto enlazados, la etiqueta de ancho fijo, el avatar, la superficie elevada y el espaciado de filas.
- [ ] **Comportamiento:** los tres chats validan y recortan el borrador en un solo lugar y ahora mandan el texto recortado.
- [ ] Las horas del chat usan la zona horaria del `TimeProvider`.
- [ ] Las filas de mensaje toman el ancho de su lista, así que la fila del chat de partida cabe en su lista más angosta.
- [ ] `JoinedMatch` responde si una notificación le pertenece, su tamaño de tablero y el turno propio. `NoticeBox` ignora valores que no cambiaron. El índice de idioma se busca antes de cambiar la cultura. `BastionGame` libera su `GraphicsDeviceManager`.
- [ ] Las filas de amigos exponen como propiedades de solo lectura los valores que asigna su constructor. El botón genérico Cancelar tiene su propia clave de texto, `FriendsCancel` (cambia `Strings.resx` y `Strings.es-MX.resx`).
### Pruebas
- [ ] Cada prueba corre el método que prueba (también las de constructor) y comparte su preparación repetida con un helper, un campo estático o el constructor de la clase.
- [ ] Una prueba revisa un solo comportamiento, compara contra un valor esperado preparado antes y revisa la razón de un rechazo cuando hay varias.
- [ ] Los objetos falsos de Application inicializan sus colecciones en un constructor.
- [ ] Las pruebas de enfriamiento pasan a `TestChatCooldown`, `VerifyIdentity` tiene su propia prueba y la prueba del panel de amigos se mueve junto a su clase.

## Probar en el juego (José dice que no lo probó con este PR)
- [ ] El ancho de la fila del chat de partida.
- [ ] El espaciado de la falla de carga de la lista de canales (bajó de 12 a 10 píxeles).
- [ ] El panel de amigos, el chat y los avisos.
- [ ] Los cambios de repositorios contra SQL Server.

## Lo que reporta José
Compila sin advertencias y pasan 654 pruebas (Domain 216, Application 244, Client 194).
