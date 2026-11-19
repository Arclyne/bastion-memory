---
tipo: decision
id: D-020j
fecha: 2026-11-10
autor: jose
estado: reemplazada por D-080a
tema: estandar
origen: journal R-06
reglas: E-46
---
# D-020j · R-06 · Cuando dos métodos necesitan la misma condición sobre un valor que puede…
- sobre: 4.4.1 y CS8629
- Jose decidió: Cuando dos métodos necesitan la misma condición sobre un valor que puede faltar, se usa el patrón Try: un privado `TryGetX(…, out T x)` que devuelve `bool` y entrega el valor; los demás lo llaman (con `out _` si solo importa el `bool`). Sin atributos de nulabilidad ni `.Value`.
