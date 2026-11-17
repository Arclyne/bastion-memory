---
tipo: decision
id: D-052j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-38
reglas: E-71
---
# D-052j · R-38 · Se traduce un error de la base a una excepción de Application solo donde un…
- sobre: 9.2.1
- Jose decidió: Se traduce un error de la base a una excepción de `Application` solo donde un componente de adentro reacciona a ella (`MatchRepositoryException`, `RoomRepositoryException`). La unidad de trabajo no traduce: sus fallas suben hasta `Host`, que es el borde y atrapa `DbException`/`DbUpdateException`. `DatabaseFailureTranslator` queda aparte para cuando haga falta en otro lugar.
