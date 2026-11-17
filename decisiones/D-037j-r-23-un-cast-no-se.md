---
tipo: decision
id: D-037j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-23
---
# D-037j · R-23 · Un cast no se combina en la misma línea con una llamada o una operación, en…
- sobre: R-04 (L-14)
- Jose decidió: Un cast no se combina en la misma línea con una llamada o una operación, en ningún lugar (asignaciones y argumentos incluidos): `TimeSpan clockTime = …; double clockMilliseconds = clockTime.TotalMilliseconds; RemainingClockMilliseconds = (int)clockMilliseconds;`. Las demás asignaciones de varios pasos se dejan; la R-04 completa sigue siendo para los `return`.
