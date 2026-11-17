---
tipo: decision
id: D-034j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-20
reglas: E-26
---
# D-034j · R-20 · Una navegación de EF que expone un campo de respaldo (Participations =>…
- sobre: 2.11.4 (L-04)
- Jose decidió: Una navegación de EF que expone un campo de respaldo (`Participations => _participations`, con `UsePropertyAccessMode.Field`) puede usar `=>`: se anota como excepción de EF. No cubre los valores calculados (R-17). Los `DbSet` de `BastionDbContext` se preguntan en su revisión.
