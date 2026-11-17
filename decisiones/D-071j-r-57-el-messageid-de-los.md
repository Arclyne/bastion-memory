---
tipo: decision
id: D-071j
fecha: 2026-11-11
autor: jose
estado: vigente
tema: estandar
origen: journal R-57
---
# D-071j · R-57 · El MessageId de los contratos se queda aunque el cliente no lo lea
- sobre: Pasada 4
- Jose decidió: El `MessageId` de los contratos se queda aunque el cliente no lo lea: es la identidad del mensaje en la red (`ChatMessageReceipt`, `LobbyChatMessage`, las tres notificaciones de mensaje y `PrivateChatMessage`). No se vuelve a preguntar en `Notifications` ni en `PrivateChat` (decidido en `Chat` de `Contracts`).
