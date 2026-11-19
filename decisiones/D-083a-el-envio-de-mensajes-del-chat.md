---
tipo: decision
id: D-083a
fecha: 2026-11-18
autor: angel
estado: vigente
tema: estandar
reglas: E-42, E-52, E-53, E-75
---
# D-083a · El envío de mensajes del chat del lobby y del privado vive en la base moderada
- Angel decidió (revisión del código duplicado de SonarQube, 2026-11-18): el único bloque duplicado del proyecto (28 líneas, 0.2 %), el `try`/`catch` de `SendMessage` en `LobbyChatViewModel` y `PrivateConversationViewModel`, sube a `ModeratedChatViewModel.DeliverMessage(row, send, confirmSent)`. Cada clase arma su `Func<DateTime>` de envío y su confirmación: el lobby pasa `row.Confirm`; el privado confirma la fila y lanza `MessageSent` en `ConfirmSent`. `ShowRejection` pasa a la base como `protected virtual` (fila fallida y silencio) y el privado la extiende para `NotFriends`. Antes de mover el código se escribieron 20 pruebas del envío (`TestLobbyChatViewModel`, `TestPrivateConversationViewModel`) y pasaron con el código viejo y con el nuevo.
- porqué: las dos clases ya heredaban de `ModeratedChatViewModel` y el bloque solo cambiaba el texto de la bitácora. Ninguna prueba cubría esas clases, así que las pruebas van primero.
- Claude eligió (sin aprobar): la base registra con su propio `ILog` (`typeof(ModeratedChatViewModel)`, como el resto del código) y un texto común ("chat message"), así que la bitácora ya no distingue lobby de privado por la categoría ni por el texto. Los fakes `FakeChatClient` y `FakeConversationClient` ahora envían de verdad (`LobbyChatSendFailure`, `SendFailure`, `ConfirmedSentAt`); listar y marcar como leída siguen sin soporte.
- fuera de esta decisión: `MatchChatViewModel` tiene casi el mismo bloque con un `catch` más (`ChatChannelForbiddenException`) y hereda de `ChatComposerViewModel`, no de la base moderada; SonarQube no lo marca. El trío `ServerUnreachableException`/`ConnectionLostException`/`ServerErrorException` se repite 18 veces en el cliente porque no tiene clase base común.
- dónde vive: PR #35 de `Arclyne/bastion`, rama `review-chat-send-in-base` sacada de `main`: commits `e5e4665` (pruebas) y `abc0ecb` (el cambio). Compila sin errores y pasan las 763 pruebas. José no lo ha visto.
