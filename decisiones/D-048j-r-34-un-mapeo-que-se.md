---
tipo: decision
id: D-048j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-34
reglas: E-46, E-81
---
# D-048j · R-34 · Un mapeo que se repite de una entidad a un tipo de Application es una fábrica…
- sobre: 4.4.1, 10.1.1
- Jose decidió: Un mapeo que se repite de una entidad a un tipo de `Application` es una fábrica estática en ese tipo (`PlayerIdentity.FromAccount`), que es la capa más interna que conoce los dos. No se inyecta ni va en un ensamblado propio mientras sea una función pura; se inyectaría si llegara a necesitar un servicio externo (10.1.1).
