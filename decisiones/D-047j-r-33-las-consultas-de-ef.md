---
tipo: decision
id: D-047j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-33
reglas: E-51, E-52
---
# D-047j · R-33 · Las consultas de EF se parten en pasos simples
- sobre: 5.1.1, 5.1.2 (L-19)
- Jose decidió: Las consultas de EF se parten en pasos simples: un `.Where` por condición `&&`; los dos sentidos de una pareja con `Concat` o con dos búsquedas unidas con `??`; `GroupBy(clave, elemento)` en lugar de una lambda anidada; el selector de `SetProperty` en un campo `Expression<…>`; y las proyecciones anidadas se arman en memoria con un método usado como grupo de método.
