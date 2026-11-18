---
tipo: tarea
id: T-10a
fecha: 2026-11-17
autor: angel
estado: pendiente
grupo: estandar
---
# T-10a · Revisar en el código los cambios del PR #25
- hecho cuando: Angel revisó en el código cada punto de la lista (marcado `[x]`), lo dudoso quedó como pregunta (`nuevo.py pregunta`) y lo pendiente de probar se probó en el juego o quedó como tarea del grupo `probar`.
- bloqueada por: nada; se revisa después del merge (Angel, 2026-11-17).
- origen: PR #25 de `Arclyne/bastion`, de José (poijn23), rama `review-standard-v2.4-fifth-pass`. Los PRs del #22 al #29 están apilados: cada uno se crea a partir del anterior.
- commits propios: 47, de `6772e75` a `94c6256`. Para verlos: `git log --oneline 6772e75..94c6256`. Para ver todo el cambio: `git diff 6772e75 94c6256`. Los SHA siguen valiendo si se fusiona con merge commit; con squash o rebase cambian, y entonces hay que buscar por el título del commit.
- fuente de esta lista: la descripción del PR y la lectura del diff que hizo Claude el 2026-11-17. Claude no compiló ni corrió las pruebas: las cifras de pruebas son las que reporta José.

## Qué es
Quinta revisión completa contra el estándar v2.4. Un commit por carpeta.

## Cambios por revisar
### Cambios de comportamiento
- [ ] **Nicknames:** aceptan `ÁÉÍÓÚÜÑáéíóúüñ`, como espera CU-02 RN-01. Solo se permite el alfabeto latino, así que una letra cirílica que se parece sigue rechazada.
- [ ] **Códigos de sala:** el registro saca un código por intento (`TryCreateUnusedCode`, que el #29 cambia a `CreateUnusedCode`), y los 10 intentos de `RoomKeeper` cubren las salas abiertas y las guardadas.
- [ ] **Códigos de sala:** cuando fallan todos los intentos, `RoomCodeUnavailableException` se registra como error y regresa como falla del servidor. Antes, un `InvalidOperationException` llegaba a CoreWCF sin traducir y nunca se registraba.
- [ ] **Arreglo de notificaciones:** si un cliente cierra su canal justo antes de una notificación, el host ya no se detiene. El registro de canales atrapa el `ObjectDisposedException`, lo registra como aviso y da de baja el canal.
- [ ] **Logs del cliente:** un canal de notificaciones con falla y un keep-alive que no llega al servidor se registran como error.
### Servidor
- [ ] Textos de log: un `DbException` atrapado registra "A database command failed" en vez de afirmar que no se pudo llegar a la base. La partida clasificatoria registra que "no se pudo crear".
- [ ] `LoginService.RejectPassword` devuelve la excepción y quien lo llama la lanza. Ya no usa `[DoesNotReturn]`.
- [ ] Dos revisiones que calculaban dentro de un `if` ahora son métodos pregunta: `Account.HasResetPeriodPassed` y `ChatCooldown.IsCoolingDown`.
- [ ] Nombres: cada variable de operación del Host se llama como su método público; también `chosenMove` y `counterpartAccountIdSelector`.
### Red
- [ ] Cada `Call`/`CallForRoom` de los siete clientes recibe su operación en una variable con nombre.
- [ ] El traductor de conversaciones comparte una sola conversión `ToContact` y llama `lastChatMessage` al último mensaje.
- [ ] `PawnMovedEventArgs` quita `FromSquare`, que el cliente nunca leía. El contrato lo sigue mandando.
### Cliente
- [ ] `UiThread.Run` y `TrySendToServer` también reciben su operación en una variable con nombre.
- [ ] Posiciones y tamaños calculados pasan a constantes: `FriendsPanelY`, `WallControlsOffsetY`, `AbandonStatusOffsetY`, `ClipWidthReduction`, `HaloGrowth`, `PasswordInputWidth`, `WallCenterHeight`, `InverseDisplayGamma`. El radio del chip del menú, el desplazamiento de ajustes y el ancho del botón de partida privada se calculan desde su origen.
- [ ] Piezas compartidas: `ViewFactory.CreateBoundButton`, `SectionSpacing` y `PlayerRowHeight` de `PanelMetrics` (reemplazan cinco copias locales). El diálogo de eliminar amigo arma sus botones con un helper, y la colocación de muros comparte cómo muestra el muro bajo el cursor.
- [ ] Los avisos de `RunSafely` culpan a la conexión cerrada en vez de a una pantalla cerrada. Los avisos del tablero nombran a quien movió o colocó.
- [ ] `MainMenuViewModel.Nickname` es de solo lectura.
### Pruebas
- [ ] Textos de chat, nicknames y correos se prueban con un ejemplo en inglés y uno en español.
- [ ] Nueva `TestStrings`: revisa que cada texto tenga traducción al español con los caracteres intactos y los mismos marcadores.
- [ ] Las pruebas que desbordan un chat lo llenan en la preparación y publican un mensaje en la acción.
- [ ] Las pruebas de sala y de turno tienen sus propios datos. Siete pruebas se renombran por lo que revisan. Las dos muestras del modo clásico comparten un inicializador.

## Probar en el juego
José probó login, panel de amigos, los tres chats con texto en español, una partida completa con dos muros y una ranura ocupada, un abandono y la búsqueda cancelada o cortada por servidor caído.
- [ ] Un nickname con acentos o ñ (José no lo menciona entre lo que probó).
- [ ] Los cambios de códigos de sala: José no los probó porque el botón de crear sala no tiene manejador.

## Lo que reporta José
Pasan 681 pruebas (Domain 224, Application 251, Client 206). Romper un marcador y un acento en `Strings.es-MX.resx` hace fallar las dos revisiones de `TestStrings`.
