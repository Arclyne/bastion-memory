---
tipo: decision
id: D-068j
fecha: 2026-11-11
autor: jose
estado: vigente
tema: estandar
origen: journal R-54
reglas: E-45, E-49
---
# D-068j · R-54 · Una traducción de enum a enum con más casos de los que caben en complejidad 10…
- sobre: 4.3.2, 4.6.1
- Jose decidió: Una traducción de enum a enum con más casos de los que caben en complejidad 10 va en una tabla `private static readonly IReadOnlyDictionary<TOrigen, TDestino> _xByY` con `TryGetValue`, y lanza `ArgumentOutOfRangeException` si falta el valor. No se parte el `switch` con un `default` que delega. Aplica a `RoomContractTranslator` del cliente.
