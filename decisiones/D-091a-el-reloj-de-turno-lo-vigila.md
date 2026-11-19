---
tipo: decision
id: D-091a
fecha: 2026-11-19
autor: angel
estado: vigente
tema: reglas
---
# D-091a · El reloj de turno lo vigila el servidor cada segundo
- Angel decidió (2026-11-19, al aprobar el plan de relojes y la tarjeta f06 del canvas): quien se queda sin reloj pierde. Con dos jugadores gana el rival y la partida se cierra por tiempo (`TIMEOUT`) con su elo y estadísticas; con cuatro, quien se quedó sin tiempo sale con el peor lugar libre y la partida sigue. Una jugada que llega después de 0:00 se descarta y cierra la partida por tiempo. El cliente cuenta hacia atrás solo el reloj de quien tiene el turno, lo corrige con la cifra que trae cada jugada y pinta en rojo sobre rosado los últimos 30 segundos.
- porqué: el reloj lo lleva el servidor (RN-10 del caso Jugar turno); sin una revisión propia, una partida con un jugador ausente no terminaba nunca.
- Claude eligió (sin aprobar):
  - el primer turno empieza 3 segundos después de crear la partida, cuando termina la cuenta de la pantalla de versus (`MatchClockPolicy.OpeningDelay`); la cuenta de versus usa la misma constante;
  - la partida guarda cuándo empezó el turno (`Match.TurnStartedAt`, script `database/08_add_turn_clock.sql`, corrido en la base local con la cuenta de administrador el 2026-11-19);
  - un servicio de fondo revisa cada segundo las partidas con el reloj agotado; un candado por partida (`MatchGate`) evita que una jugada y el cierre por tiempo se crucen;
  - la fecha de fin es el instante en que se agotó el reloj, no el de la revisión;
  - no hay estado «resultado pendiente» guardado: si el cierre falla, la partida sigue en curso y la revisión del segundo siguiente lo intenta de nuevo;
  - al arrancar, el servidor cierra por tiempo las partidas que quedaron abiertas con el reloj agotado (así se cerraron la 12 de ejemplo y la 6007 de prueba); no hay compensación por el tiempo con el servidor apagado hasta la fase de reconexión.
- descartado: pausar el reloj al abrir la confirmación de abandonar o al perder la conexión (RN-11 del caso Jugar turno lo prohíbe).
- dónde vive: rama `match-closure` sin commit. Canvas página «08 · Partida», tarjeta f06, versión 35. Probado en vivo el 2026-11-19 (partida 6008: pedro_peon agotó su reloj, marta_muros ganó 1022 » 1034). José no lo ha visto.
