---
tipo: decision
id: D-059j
fecha: 2026-11-11
autor: jose
estado: vigente
tema: estandar
origen: journal R-45
reglas: E-46
---
# D-059j · R-45 · Una operación void pasa por la R-44 con una segunda sobrecarga…
- sobre: 4.4.1, R-44
- Jose decidió: Una operación `void` pasa por la R-44 con una segunda sobrecarga `Translate…Failures(string, Action)` que la convierte en `Func<bool>` con un privado `CompleteOperation` (llama y devuelve `true`). Los `catch` quedan una sola vez, en la sobrecarga con `Func<TResult>`. Vale para los servicios que tienen operaciones `void` y operaciones con resultado. Un servicio con solo operaciones `void` tiene un único `Translate…Failures(…, Action)` con los `catch`, sin la sobrecarga `Func` ni `CompleteOperation` (precisado en `MatchService`, 2026-11-11).
