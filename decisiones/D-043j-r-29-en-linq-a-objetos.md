---
tipo: decision
id: D-043j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-29
reglas: E-38
---
# D-043j · R-29 · En LINQ a objetos, un diccionario o un conjunto que se arma desde una lista se…
- sobre: 3.4.1 (L-01)
- Jose decidió: En LINQ a objetos, un diccionario o un conjunto que se arma desde una lista se crea con `var x = new Dictionary<K, V>(fuente.Count);` (o `new HashSet<T>(…)`) y se llena con un `foreach`, en lugar de `ToDictionary`/`ToHashSet`. Así el `var` cumple la 3.4.1 (caso `new`) y el compilador no avisa (IDE0007). Las consultas de EF sobre `IQueryable` se ven en su revisión.
