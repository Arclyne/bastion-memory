---
tipo: decision
id: D-056j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-42
reglas: E-54
---
# D-056j · R-42 · Un arreglo de contrato se arma con ContractArray.ConvertAll(origen,…
- sobre: 5.3.1, R-14
- Jose decidió: Un arreglo de contrato se arma con `ContractArray.ConvertAll(origen, convertidor)` (en `Host/Common`), en una variable antes del `return`, no con `Select(…).ToArray()`.
