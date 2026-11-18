---
tipo: tarea
id: T-07a
fecha: 2026-11-17
autor: angel
estado: pendiente
grupo: estandar
---
# T-07a · Revisar en el código los cambios del PR #22
- hecho cuando: Angel revisó en el código cada punto de la lista (marcado `[x]`), lo dudoso quedó como pregunta (`nuevo.py pregunta`) y lo pendiente de probar se probó en el juego o quedó como tarea del grupo `probar`.
- bloqueada por: nada; se revisa después del merge (Angel, 2026-11-17).
- origen: PR #22 de `Arclyne/bastion`, de José (poijn23), rama `review-standard-v2.4-sections`. Los PRs del #22 al #29 están apilados: cada uno se crea a partir del anterior.
- commits propios: 59, de `6dfb198` a `e10e98b`. Para verlos: `git log --oneline 6dfb198..e10e98b`. Para ver todo el cambio: `git diff 6dfb198 e10e98b`. Los SHA siguen valiendo si se fusiona con merge commit; con squash o rebase cambian, y entonces hay que buscar por el título del commit.
- fuente de esta lista: la descripción del PR y la lectura del diff que hizo Claude el 2026-11-17. Claude no compiló ni corrió las pruebas: las cifras de pruebas son las que reporta José.

## Qué es
Segunda revisión completa contra el estándar v2.4. Cada clase pasó por el estándar sección por sección (de la 1.3 a la 12.3), con un commit por carpeta. También trae un merge de `main` (#19 a #21) con un conflicto resuelto a mano en `MatchPlayViewModel`.

## Cambios por revisar
### En todo el código
- [ ] Un objeto creado con `new`, con una fábrica o con un `To…` va en su propia variable antes de pasarlo a una llamada; en las vistas, cada hijo se crea antes de `AddChild` o `InsertBehindContent` (ejemplo: `CountBadge`).
- [ ] Los métodos privados siguen el orden de su primer uso, y un manejador de evento va justo debajo del método que lo suscribe (E-56, D-061j).
- [ ] Colecciones con nombre en plural y booleanos como pregunta (`shouldShowToast`, `IsMatchingFilter`, `IsGrooveTaken`).
- [ ] **Dudoso:** constantes que valían 0 o 1 regresan a número directo (`NoWallsLeft`, `NoUnread`, `RowNumberOffset` y los desplazamientos en cero de las vistas y skins) → Q-14a.
- [ ] **Dudoso:** los parámetros que reciben una excepción pasan de `ex` a `cause` (31 parámetros; las variables de `catch` siguen siendo `ex`) → Q-13a.
- [ ] Los clientes revisan la excepción interna de sus fallas.
### Dominio y servidor
- [ ] Una partida de dos jugadores termina en un solo método para meta y abandono: `Match.FinishTwoPlayerMatch`.
- [ ] `IsInside` (de `BoardLayout`) e `IsGrooveOnBoard` (de `WallPolicy`) son públicos y el cliente los usa (`BoardSceneLayout`).
- [ ] `LoginService` registra cada acceso con `RecordAccessLog` y desaparece el helper genérico `Reject`.
- [ ] Salas: un código desconocido lanza `OpenRoomNotFoundException`, que `RoomKeeper.AdmitToOpenRoom` traduce. La revisión de sala ya iniciada se hace fuera del lock del registro, y un error de base llega al host en vez de perderse en un filtro de excepción.
- [ ] **Dudoso:** los servicios del Host validan un argumento nulo con un `if` en vez de `?? throw` (ejemplo: `ChatTranslator.RequireText`) → Q-15a.
- [ ] El servicio de partida lee la hora actual con un solo helper.
### Contratos
- [ ] `IMatchService` documenta cómo se rechaza una jugada o un muro faltante.
### Cliente
- [ ] Después de mandar una jugada o un muro, `MatchPlayViewModel` espera la notificación del servidor antes de dejar mandar otra (`WaitForMoveNotification`, `MoveNotificationWaitSeconds` = 5). Si no llega, deja de esperar y registra un aviso.
- [ ] `WallPlacementViewModel` comparte con `MatchPlayViewModel` la revisión de turno de muro (`IsWallTurn`) y el texto de rechazo del muro.
- [ ] Escena 3D: un solo método convierte un punto de la mesa a coordenadas del tablero (`ToBoardCoordinates`), el cuadro de resaltado se crea una vez y se mueve, y la caja del muro se arma con caras con nombre (`BoxFace`). El plano de la mesa y la media arista del muro se definen en un solo lugar cada uno.
- [ ] `TextStyleCatalog` pasa el tamaño de fuente con nombre (`fontSize: 34`).
### Pruebas
- [ ] Las pruebas que esperan una excepción nombran el tipo completo (`ThrowsArgumentException`, `ThrowsInvalidSessionException`).
- [ ] Los objetos falsos ya no validan nulos (ejemplo: `FakeAccountClient.LogIn`).
- [ ] Cada clase de prueba tiene sus propios datos; solo se comparten valores de los que depende otra pieza.

## Probar en el juego (José dice que no lo probó con este PR)
- [ ] La espera después de mover o poner un muro, incluido que no se pueda confirmar un muro dos veces.
- [ ] La escena 3D: casillas resaltadas, muros y clic sobre la mesa.
- [ ] Unirse a una sala con un código que no existe.

## Lo que reporta José
Compila sin advertencias y pasan 650 pruebas (Domain 212, Application 244, Client 194).
