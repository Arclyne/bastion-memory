---
tipo: decision
id: D-051j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-37
reglas: E-71
---
# D-051j · R-37 · El contexto de EF usa NonRetryingExecutionStrategy
- sobre: 9.2.1
- Jose decidió: El contexto de EF usa `NonRetryingExecutionStrategy`. La estrategia por defecto de SQL Server envuelve los errores transitorios en `InvalidOperationException`, que escapa de la traducción. Si algún día se activan reintentos, hay que traducir también `RetryLimitExceededException`.
