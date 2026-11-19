---
tipo: decision
id: D-093a
fecha: 2026-11-19
autor: angel
estado: vigente
tema: reglas
---
# D-093a · La reconexión se arma con la conexión de la partida en el servidor
- Angel decidió (2026-11-19, al aprobar el plan de la fase de reconexión): cuando se cae el canal de avisos de un jugador con partida en curso, el servidor lo marca desconectado (`Participation.IsConnected`, `DisconnectedAt`) y avisa a los rivales; a los 60 s (`MatchConnectionPolicy.ClaimDelay`) un rival puede reclamar, y el reclamo se guarda como abandono del desconectado. Volver a la partida devuelve el estado completo y avisa a los rivales. Al arrancar, el servidor ya no cierra por tiempo las partidas abiertas: marca a todos desconectados desde el arranque y empieza el turno en ese momento (RN-05 del caso Reconectar a una partida en curso). Esto reemplaza la parte de [[D-091a-el-reloj-de-turno-lo-vigila|D-091a]] que cerraba al arrancar.
- porqué: el caso Reconectar a una partida en curso es obligatorio y la base ya tenía las columnas de conexión sin código que las usara.
- Claude eligió (sin aprobar):
  - el tiempo que llevaba el jugador en turno antes de una caída del servidor se le perdona, porque el servidor no guarda a qué hora se cayó;
  - el contrato de inicio de sesión no cambia: la partida en curso se pregunta con `IMatchService.FindOngoingMatch`, que no reconecta; `RejoinMatch` sí reconecta; `ClaimVictory` rechaza con `VictoryClaimRejectedFault`;
  - otro dispositivo: cuando una cuenta se suscribe de nuevo, el canal anterior recibe `MatchTakenOverNotification`; el cliente lo ignora mientras se reconecta y durante 10 s después, para no confundir su propia reconexión;
  - el cliente reintenta a los 2, 5, 10, 20 y 30 s y muestra el error tras 3 intentos fallidos (en la prueba real, con 1, 2 y 4 s el error salía antes de que el servidor volviera);
  - la barra roja, la franja de aviso y el aviso del rival van apilados arriba al centro;
  - si el cliente se cerró y la partida terminó mientras estaba fuera, al volver a entrar no ve el resultado (no hay partida en curso que encontrar); la tablilla solo sale si se reconecta desde la partida.
- descartado: guardar una «última señal de vida» del servidor para descontar solo el tiempo de juego antes de la caída.
- dónde vive: rama `match-closure`, sin commit. Probado en vivo el 2026-11-19: caída de un cliente y aviso al rival, volver desde el diálogo y desde la franja ámbar, reclamo a los 60 s (partida 6009, pedro_peon 925 » 946), reinicio del servidor con partida abierta sin descontar el tiempo caído (partidas 6010 y 6011) y reconexión automática de los dos clientes. José no lo ha visto.
- reemplazada en parte (2026-11-19): el reclamo deja de ser una operación del jugador; el servidor cierra solo a los 60 s ([[D-094a-la-victoria-por-desconexion-llega-sola|D-094a]]).
