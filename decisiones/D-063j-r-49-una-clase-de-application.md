---
tipo: decision
id: D-063j
fecha: 2026-11-11
autor: jose
estado: vigente
tema: estandar
origen: journal R-49
reglas: E-81
---
# D-063j · R-49 · Una clase de Application que hace E/S por sus colaboradores o usa estado…
- sobre: 10.1.1
- Jose decidió: Una clase de `Application` que hace E/S por sus colaboradores o usa estado compartido se recibe por una interfaz, aunque sea interna (`IMatchmakingDispatcher`). También vale en `Host` (decidido en `Sessions`): `INotificationChannelRegistry` (el evento `PlayerDisconnected` y `RegisterChannel`) e `IFriendPresenceReporter`, junto a su clase; el registro concreto se queda en el contenedor solo para resolver los puertos.
