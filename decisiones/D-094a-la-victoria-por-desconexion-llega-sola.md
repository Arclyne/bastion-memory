---
tipo: decision
id: D-094a
fecha: 2026-11-19
autor: angel
estado: vigente
tema: interfaz
---
# D-094a · La victoria por desconexión llega sola y la reconexión no tiene botones
- Angel decidió (2026-11-19, al aprobar el rediseño de las tarjetas f07 a f10 de la página «08 · Partida», versión 38):
  - no hay «Reclamar victoria»: el aviso del rival muestra una cuenta regresiva de 60 s y, si no vuelve, la partida se cierra sola como abandono del que se fue (con cuatro jugadores, sale con el peor lugar libre y la partida sigue);
  - la propia caída se muestra con un ícono de conexión perdida al centro y el tablero apagado; los reintentos son solo automáticos, sin botón ni mensaje de error;
  - al iniciar sesión con una partida en curso el juego vuelve solo a ella: no hay diálogo «Tienes una partida en curso», ni «Más tarde», ni franja ámbar para este caso.
- porqué: si el rival ya no puede volver, no tiene sentido que haya que reclamar; reintentar y volver son lo único sensato, así que no hay nada que preguntar (Angel). La barra roja tampoco le gustó.
- Claude eligió (sin aprobar): la partida termina a la hora en que se cumplieron los 60 s, no a la de la revisión. El ícono es una imagen PNG en `Content/Icons`, porque el cliente no tenía íconos dibujados.
- Si todos los jugadores activos están fuera, decide el reloj de turno: lo confirmó Angel en [[D-095a-si-todos-pierden-la-conexion-decide|D-095a]].
- descartado: el botón «Reclamar victoria», la barra roja con «Reintentar ahora», el error tras 3 intentos y el diálogo con «Más tarde» de la versión 37.
- dónde vive: canvas https://claude.ai/artifact/JMdfC1XAcc8CrT2UE7M5AR, versión 38. Se aparta del caso Abandonar la partida (FA-06, reclamar la victoria) y del FA-01 del caso Reconectar a una partida en curso («Más tarde»); habría que corregirlos en `requisitos-bastion`. Probado en vivo el 2026-11-19 (partidas 6012 y 6013): vuelta directa al iniciar sesión, victoria automática a los 60 s (pedro_peon 982 » 998), ícono central y reconexión automática tras reiniciar el servidor sin que nadie ganara por desconexión. José no lo ha visto.
