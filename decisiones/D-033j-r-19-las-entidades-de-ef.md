---
tipo: decision
id: D-033j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-19
reglas: E-20
---
# D-033j · R-19 · Las entidades de EF son class aunque sean inmutables (catálogos como GameMode)
- sobre: 2.8.1 (L-12)
- Jose decidió: Las entidades de EF son `class` aunque sean inmutables (catálogos como `GameMode`): EF las identifica por su clave (R-01), y la igualdad por valor de un `record` no aplica a una fila. La regla de `record` para valores inmutables vale para lo que no es entidad de EF.
