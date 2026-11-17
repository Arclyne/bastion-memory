---
tipo: decision
id: D-064j
fecha: 2026-11-11
autor: jose
estado: vigente
tema: estandar
origen: journal R-50
reglas: E-46, E-85
---
# D-064j · R-50 · Una operación IsOneWay no traduce
- sobre: R-44, 4.4.1, 11.1.1
- Jose decidió: Una operación `IsOneWay` no traduce: su falla no llega al cliente, y si se escapa, CoreWCF no la registra (comprobado en `oneway-experiment`). Guarda su `…InRequestScope` en una variable `Action<string>` y llama `Log…OneWayFailures(nameof(…), sessionToken, operación)`. Ese envoltorio tiene la guarda del token nulo (Warn) y los `catch` de tipos conocidos, que registran sin relanzar. Aplica a `RoomService.LeaveRoom`.
