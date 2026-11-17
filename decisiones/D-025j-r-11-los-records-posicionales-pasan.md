---
tipo: decision
id: D-025j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-11
reglas: E-75
---
# D-025j · R-11 · Los records posicionales pasan a un constructor explícito con…
- sobre: 9.4.1 (L-02)
- Jose decidió: Los records posicionales pasan a un **constructor explícito** con `ArgumentNullException.ThrowIfNull` para cada parámetro de referencia no anulable, y propiedades `{ get; }`. Solo los records que se copian con `with` llevan `{ get; init; }`. Cada record se cambia al revisar su archivo.
