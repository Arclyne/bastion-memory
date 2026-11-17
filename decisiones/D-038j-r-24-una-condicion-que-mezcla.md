---
tipo: decision
id: D-038j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-24
---
# D-038j · R-24 · Una condición que mezcla && y || (con paréntesis) no es corta
- sobre: R-05 (L-15)
- Jose decidió: Una condición que mezcla `&&` y `||` (con paréntesis) no es corta: se separa en guardas, una pregunta por `if`, y el último `return` devuelve la comparación que queda. Las condiciones solo con `&&` siguen la R-05.
