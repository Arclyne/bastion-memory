---
tipo: decision
id: D-042j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-28
reglas: E-76
---
# D-042j · R-28 · return x ?? throw new X()
- sobre: R-04, 9.4.2 (L-17)
- Jose decidió: `return x ?? throw new X();` se admite si lo de la izquierda es una variable o una sola llamada: es la llamada y su alternativa en una expresión (9.4.2).
