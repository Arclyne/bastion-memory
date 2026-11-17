---
tipo: decision
id: D-067j
fecha: 2026-11-11
autor: jose
estado: vigente
tema: estandar
origen: journal R-53
reglas: E-85
---
# D-067j · R-53 · Un catch de Host que traduce un rechazo a falla y la relanza no registra nada,…
- sobre: 11.1.1
- Jose decidió: Un `catch` de `Host` que traduce un rechazo a falla y la relanza no registra nada, ni en Info ni en Warn: se registra donde se maneja al final (el cliente). Una guarda que rechaza antes del `try` (opciones nulas en `RequireSettings`) sí puede registrar en Warn.
