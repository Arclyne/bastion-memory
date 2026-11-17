---
tipo: decision
id: D-050j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-36
reglas: E-46
---
# D-050j · R-36 · Los errores de EF (DbUpdateException, DbException) se traducen en un solo…
- sobre: 4.4.1
- Jose decidió: Los errores de EF (`DbUpdateException`, `DbException`) se traducen en un solo lugar, `DatabaseFailureTranslator<TFailure>`, que recibe cómo crear la excepción de quien lo usa. Los repositorios que abren un contexto por operación usan `NewContextRunner<TFailure>`, que a su vez usa el traductor. `UnitOfWork` puede usar el traductor (211).
