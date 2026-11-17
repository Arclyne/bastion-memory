---
tipo: decision
id: D-019j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-05
---
# D-019j · R-05 · Un return puede devolver directamente una condición corta (comparación, &&, is…
- sobre: R-04, condiciones
- Jose decidió: Un `return` puede devolver directamente una condición corta (comparación, `&&`, `is not null`): se lee como una pregunta. Ejemplo: `return PasswordHash is not null && PasswordSalt is not null;`.
