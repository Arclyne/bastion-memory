---
tipo: decision
id: D-077a
fecha: 2026-11-18
autor: angel
estado: vigente
tema: estandar
reglas: E-06, E-11, E-13
---
# D-077a · Nombres del juego, sin vocabulario web
- sobre: 2.2.1, 2.4.1, 2.5.1
- Angel decidió: un tipo o método se nombra por lo que es o hace en el juego, no por la técnica que lo lleva. No se usan `Request`, `Response`, `Reply`, `Dto` ni `Payload` como parte del nombre, ni nombres abstractos que no dicen qué guardan (`LoginRequest` pasó a `PlayerCredentials` y `ClientDevice`; `LoginResponse`, a `LoginOutcome`). Los métodos propios no terminan en `Async`.
- porqué: el profesor lo señaló en su revisión del 2026-10-19: `Request`/`Response` y `async` son vocabulario web y filtran cómo viaja el dato en vez de decir qué es. La fecha y los renombres vienen de la memoria de Claude; se comprobó contra `origin/main` (`15b17ce`) el 2026-11-18.
- excepciones: `Request` se queda cuando es un objeto del juego (`FriendRequest`, la solicitud de amistad; `PresenceRequest`, la confirmación de presencia de CU-09) o un adjetivo (`RequestedRoomSettings`). `Async` se queda en lo que impone .NET (`ExecuteAsync`, `StartAsync`, `StopAsync` de `BackgroundService` e `IHostedService`), como permite E-06.
- dónde vive: en el código ya se cumple en `main`. No hay tipos `*Response`, `*Reply` ni `*Dto`, y los únicos `*Async` son las tres sobrescrituras de .NET. José no la ha visto.
