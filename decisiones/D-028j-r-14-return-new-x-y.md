---
tipo: decision
id: D-028j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-14
---
# D-028j · R-14 · return new X(…) y return new X { … } cuentan como una sola llamada si cada…
- sobre: R-04, creación
- Jose decidió: `return new X(…)` y `return new X { … }` cuentan como una sola llamada si cada argumento o asignación es una variable, una constante, una propiedad o un literal. Si alguno lleva una llamada (incluido otro `new`), una operación o un cast, va antes en una variable.
