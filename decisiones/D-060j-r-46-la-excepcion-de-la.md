---
tipo: decision
id: D-060j
fecha: 2026-11-11
autor: jose
estado: vigente
tema: estandar
origen: journal R-46
reglas: E-83
---
# D-060j · R-46 · La excepción de la 10.3.1 también vale para un singleton que necesita un…
- sobre: 10.3.1 (L-08)
- Jose decidió: La excepción de la 10.3.1 también vale para un singleton que necesita un servicio `Scoped` en cada operación (`FriendPresenceReporter`): recibe `IServiceScopeFactory` y abre un ámbito por operación, como el patrón de Microsoft para consumir un servicio con ámbito desde un singleton. Fuera de WCF el envoltorio no traduce: registra y sigue (`LogPresenceFailures`), con un `…InOwnScope` por operación.
