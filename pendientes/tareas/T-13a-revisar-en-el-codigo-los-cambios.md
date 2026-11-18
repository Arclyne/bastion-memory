---
tipo: tarea
id: T-13a
fecha: 2026-11-17
autor: angel
estado: pendiente
grupo: estandar
---
# T-13a · Revisar en el código los cambios del PR #28
- hecho cuando: Angel revisó en el código cada punto de la lista (marcado `[x]`), lo dudoso quedó como pregunta (`nuevo.py pregunta`) y lo pendiente de probar se probó en el juego o quedó como tarea del grupo `probar`.
- bloqueada por: nada; se revisa después del merge (Angel, 2026-11-17).
- origen: PR #28 de `Arclyne/bastion`, de José (poijn23), rama `review-no-null-returns`. Los PRs del #22 al #29 están apilados: cada uno se crea a partir del anterior.
- commits propios: 28, de `25ae9f9` a `ac1da4d`. Para verlos: `git log --oneline 25ae9f9..ac1da4d`. Para ver todo el cambio: `git diff 25ae9f9 ac1da4d`. Los SHA siguen valiendo si se fusiona con merge commit; con squash o rebase cambian, y entonces hay que buscar por el título del commit.
- fuente de esta lista: la descripción del PR y la lectura del diff que hizo Claude el 2026-11-17. Claude no compiló ni corrió las pruebas: las cifras de pruebas son las que reporta José.

## Qué es
Ningún método devuelve `null`: ahora devuelve un valor bandera o un `Lookup<T>` que se revisa solo. Un commit por carpeta. **Según José, los commits intermedios no compilan**; solo compila el último.

## Antes de revisar el código
- [x] **Dudoso: el estándar no lo pide.** Resuelto: el cambio se queda porque lo pidió el profesor ([[D-075a-ningun-metodo-devuelve-null|D-075a]], 2026-11-18).

## Cambios por revisar
### El resultado de búsqueda
- [ ] Nuevo `Bastion.Domain.Common.Lookup<T>`: `IsFound`; `GetValue()`, que lanza `InvalidOperationException` con lo que se buscó (por ejemplo, "No Match was found. MatchId=42"); y las fábricas `Lookup.Found`, `Lookup.Missing<T>(key)` y `Lookup.FromNullable`.
- [ ] Lo usan los nueve puertos de repositorio y sus implementaciones, la búsqueda por código de amigo, la solicitud de amistad pendiente, el registro y el guardián de salas (`FindRoomOf`, `Leave`), `FindOwnRoom`, el inicio de búsqueda en la cola y el catálogo de idiomas del cliente.
### Banderas en vez de null
- [ ] Muros: `WallRejectionReason.None` (`WallRejection.None`) significa que el muro cabe.
- [ ] Posiciones: `Match` y la pestaña de chat buscan participaciones y filas por índice, con -1 cuando no hay.
- [ ] Presencia: `PartnerPresence { NotFriend, Connected, Disconnected }` reemplaza la presencia nula de alguien que no es amigo.
- [ ] Texto vacío: la solicitud de búsqueda devuelve una clave de falla vacía cuando se mandó, y el almacén de idioma devuelve un nombre de cultura vacío cuando no hay idioma guardado.
### Cambios de comportamiento
- [ ] **Idioma guardado:** una falla de lectura ya no se trata como "no hay idioma guardado". El almacén deja pasar la excepción de IO y `LanguageService` la registra como aviso y usa el idioma del sistema.
- [ ] **Cambio en el contrato WCF:** `FindOwnRoom` responde `OwnRoomResult { bool IsInRoom; RoomState? Room }` en vez de un `RoomState` nulo. En el cliente, `OwnRoom` se revisa solo, y el traductor lanza `ServerErrorException` si la respuesta dice "en una sala" pero no trae sala. Nota de Claude: `Room` sigue siendo anulable, así que el null viaja igual y el flag puede contradecirlo.
- [ ] **Login:** una cuenta desconocida y una cuenta sin contraseña se rechazan con dos guardias separadas. El log de accesos es igual que antes.
### Pruebas
- [ ] Nuevas: `TestLookup`, `TestOwnRoom`, `TestRoomContractTranslator` y tres de `TestLanguageService` (idioma guardado, faltante e ilegible).
- [ ] Los repositorios falsos devuelven lookups; las pruebas que esperaban null revisan `IsFound` o `WallRejection.None`.

## Probar en el juego
José probó: login con cuenta desconocida, iniciar y cancelar búsqueda, buscar amigo por un código existente y por uno inexistente, conversación privada con presencia, partida completa con muro y ranura ocupada, salir de la partida terminada y cerrar un cliente (que guarda la última vez visto).
- [ ] Repetir con el cliente y el servidor nuevos, porque cambió el contrato.

## Lo que reporta José
Pasan 738 pruebas (Domain 232, Application 276, Client 230).
