---
tipo: decision
id: D-066j
fecha: 2026-11-11
autor: jose
estado: vigente
tema: estandar
origen: journal R-52
reglas: E-85, E-73
---
# D-066j · R-52 · Un proceso registra en Fatal la excepción que lo termina con un manejador de…
- sobre: 11.1.1, 9.3.1
- Jose decidió: Un proceso registra en Fatal la excepción que lo termina con un manejador de `AppDomain.CurrentDomain.UnhandledException` puesto justo después de configurar log4net. Solo registra, no atrapa ni sigue (`Program.LogUnhandledException`). El mensaje de arranque se registra después de `app.Start()`. También aplica al `Program` del cliente (decidido en 386–387, 2026-11-11).
