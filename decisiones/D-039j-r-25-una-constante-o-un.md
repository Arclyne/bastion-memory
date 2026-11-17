---
tipo: decision
id: D-039j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-25
---
# D-039j · R-25 · Una constante o un método públicos que solo usa su propia clase (ni otro código…
- sobre: Pasada 4
- Jose decidió: Una constante o un método públicos que solo usa su propia clase (ni otro código ni las pruebas; buscar en `src` **y** `tests`) pasan a `private` (`MatchmakingPolicy`, `RoomPolicy.FailedCodeWindowMinutes`, `WaitingRoom.HasMember`). Los límites que forman una pareja de una regla (mínimo y máximo) se quedan públicos juntos.
