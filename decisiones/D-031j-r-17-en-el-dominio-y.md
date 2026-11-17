---
tipo: decision
id: D-031j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-17
reglas: E-26
---
# D-031j · R-17 · En el dominio y el servidor, un valor calculado a partir de otros miembros es…
- sobre: 2.11.4
- Jose decidió: En el dominio y el servidor, un valor calculado a partir de otros miembros es un método `GetX()` (`FriendRequest.GetExpirationTime()`), no una propiedad con `=>` ni con bloque `get`. Las propiedades calculadas de los modelos de vista (Gum enlaza propiedades) y los `DbSet` se preguntan en su capa.
