---
tipo: decision
id: D-041j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-27
reglas: E-59, E-60, E-61, E-62, E-63
---
# D-041j · R-27 · Cada interfaz I…Service se documenta (summary, param, returns, exception) al…
- sobre: 7.1–7.3
- Jose decidió: Cada interfaz `I…Service` se documenta (summary, param, returns, exception) al revisar su archivo, y su implementación lleva `<inheritdoc/>`. `GenerateDocumentationFile` y CS1591 como error en `I*Service.cs` (apagado en lo demás) se activan al **terminar cada capa** que tenga servicios: Application, Contracts y Client.
