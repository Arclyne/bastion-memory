---
tipo: decision
id: D-061j
fecha: 2026-11-11
autor: jose
estado: vigente
tema: estandar
origen: journal R-47
reglas: E-56
---
# D-061j · R-47 · Los métodos privados van en el orden de los públicos que los usan (decidido en…
- sobre: 6.2
- Jose decidió: Los métodos privados van en el orden de los públicos que los usan (decidido en `RoomRepository` y en `FriendshipTranslator`). Los privados que se llaman en cadena van juntos y de arriba abajo, cada uno debajo del que lo llama, aunque un público anterior use un eslabón de en medio; un privado suelto que usan casi todos (`GetUtcNow`) va al final (precisado en `NotificationChannelRegistry`, 2026-11-11).
