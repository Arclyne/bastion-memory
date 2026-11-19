---
tipo: decision
id: D-095a
fecha: 2026-11-19
autor: angel
estado: vigente
tema: reglas
---
# D-095a · Si todos pierden la conexión decide el reloj de turno
- Angel decidió (2026-11-19, «de momento está bien»): nadie gana por desconexión mientras todos los jugadores activos estén fuera. La victoria automática de los 60 s ([[D-094a-la-victoria-por-desconexion-llega-sola|D-094a]]) solo saca a un desconectado si queda al menos otro jugador activo conectado.
  - Si ninguno vuelve, el reloj del jugador en turno sigue corriendo y, al agotarse, pierde por tiempo; el otro gana aunque también esté fuera.
  - Si vuelve uno, el otro pasa a la regla de los 60 s contados desde su propia desconexión: si ya lleva más, sale en la revisión siguiente y gana el que volvió; si lleva menos, al que volvió le sale la cuenta regresiva de lo que falta.
  - Con cuatro jugadores es igual entre los activos. Una caída del servidor cuenta como que se cayeron todos: los 60 s empiezan a contar desde el arranque ([[D-093a-la-reconexion-se-arma-con-la|D-093a]]).
- porqué: así nadie pierde por una caída que le pasó también al rival o al servidor, y la partida no se queda abierta para siempre, porque el reloj de turno siempre la termina.
- descartado (por ahora): que la partida termine sin ganador y sin cambio de elo cuando todos se van y ninguno vuelve. Angel lo deja abierto para revisarlo después.
- dónde vive: rama `match-closure`, sin commit. `Match.HasAbsentPlayerToTakeOut` y la consulta `FindMatchIdsWithAbsentPlayer` del repositorio de partidas. Probado en vivo el 2026-11-19 (partida 6013, reinicio del servidor con los dos fuera: nadie ganó por desconexión). No está en los requisitos ni en el canvas. José no lo ha visto.
