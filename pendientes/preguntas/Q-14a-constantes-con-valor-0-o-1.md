---
tipo: pregunta
id: Q-14a
fecha: 2026-11-17
autor: angel
estado: abierta
grupo: estandar
---
# Q-14a · Constantes con valor 0 o 1 que el PR 22 cambió por literales
E-22 (2.10.1) prohíbe literales con significado en el dominio. Su aclaración permite el 0 y el 1 como valores neutros (un contador que empieza en cero, un incremento, el primer índice), pero *"si el 0 o el 1 tiene significado en el dominio, lleva nombre"*.
- El PR #22 de `Arclyne/bastion` (rama `review-standard-v2.4-sections`) quitó constantes que valían 0 o 1 y dejó el número directo, porque, según José, el nombre solo repetía lo que recibe el valor:
  - `Participation.NoWallsLeft`: `ownRemainingWalls > Participation.NoWallsLeft` pasó a `ownRemainingWalls > 0` en `IsWallTurn()`;
  - `BoardLayout.RowNumberOffset`: `boardSize - RowNumberOffset` pasó a `boardSize - 1` en `GetLastIndex`;
  - `NoUnread` en `ChatTabViewModel` y `LobbyChatViewModel`, y los desplazamientos en cero de las vistas y las skins.
- **Duda:** "le quedan muros" puede leerse como significado del dominio (una regla del juego), y entonces `NoWallsLeft` debería seguir existiendo. `_unreadCount = 0` sí parece un contador neutro.
- **Inconsistencia:** `ChatTabViewModel` quitó `NoUnread = 0` y conservó `OneUnread = 1` y `FirstPosition = 0`.
- Hay que decidir el criterio para el 0 y el 1 con significado de juego y registrarlo como decisión con `reglas: E-22`.
- No bloquea: Angel hará merge del #22 y lo revisará después con José (2026-11-17).
