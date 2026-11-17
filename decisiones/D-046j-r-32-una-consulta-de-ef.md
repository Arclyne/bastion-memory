---
tipo: decision
id: D-046j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-32
reglas: E-54
---
# D-046j · R-32 · Una consulta de EF sigue la forma de la 5.3.1
- sobre: R-04, 5.3.1 (L-18)
- Jose decidió: Una consulta de EF sigue la forma de la 5.3.1: va en un `IQueryable<T>` con nombre en plural y se materializa con `new List<T>(consulta)` (o `new Dictionary<K, V>(consulta)` sobre `KeyValuePair<K, V>`). Las de valor único devuelven `consulta.FirstOrDefault()` (o `Any()`), o lo guardan en una variable si lo usan después. Un método privado que arma una consulta la guarda en una variable y la devuelve, o devuelve una sola llamada (`a.Concat(b)`).
