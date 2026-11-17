---
tipo: decision
id: D-026j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-12
reglas: E-54
---
# D-026j · R-12 · Una cadena LINQ que termina en un solo valor (Any, Count, First, Sum…) se…
- sobre: R-04 y 5.3.1, LINQ
- Jose decidió: Una cadena LINQ que termina en un solo valor (`Any`, `Count`, `First`, `Sum`…) se guarda, un operador por línea, en una variable con nombre, y el `return` devuelve esa variable. Las lambdas de una línea se quedan en la cadena. Las cadenas que devuelven una secuencia siguen la 5.3.1 (`IEnumerable<T>` y `new List<T>(…)` aparte).
