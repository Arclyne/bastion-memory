---
tipo: tarea
id: T-17a
fecha: 2026-11-18
autor: angel
estado: pendiente
grupo: estandar
---
# T-17a · Revisar con José las expresiones de colección y la 5.3.1
- hecho cuando: José vio D-081a y Angel y José decidieron dos cosas, cada una con su decisión registrada:
  1. Agregar D-081a al texto del estándar como regla propia (Angel lo pidió el 2026-11-18): `[]` y `[a, b]` para colecciones vacías o con elementos fijos, con código correcto e incorrecto, cerca de la 2.6.3 o la 3.4, y su línea en `estandar/reglas.md`. Falta que José lo acepte y que decidan la sección y el número E-NN.
  2. Si la 5.3.1 (E-54) admite `[.. consulta]` además de `new List<T>(consulta)` para materializar una consulta en una instrucción aparte. Si se admite, se corrigen los 35 casos que señala IDE0028; si no, se marcan "Accepted" en SonarQube citando E-54 y se revisa si D-026j y D-046j cambian.
- contexto: el análisis de SonarQube del 2026-11-18 marcó 115 IDE0028. 80 ya se corrigieron con D-081a. Los 35 restantes son la última línea de una materialización (`return new List<Participation>(activeParticipations);` en `Match.ListActiveParticipations`, entre otros). Las dos formas dejan la materialización aparte, que es lo que pide la 5.3.1; el texto solo nombra `new List<T>(consulta)`.
- bloqueada por: José no lo ha visto.
