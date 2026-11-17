---
tipo: decision
id: D-035j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-21
---
# D-035j · R-21 · Un return con un solo operador LINQ y una lambda de una línea (FirstOrDefault(x…
- sobre: R-04, R-12 (L-13)
- Jose decidió: Un `return` con **un solo** operador LINQ y una lambda de una línea (`FirstOrDefault(x => …)`, `Count(x => …)`) cuenta como una sola llamada, como en el ejemplo correcto de la 2.11.4. La R-12 aplica a cadenas de dos o más operadores.
