---
tipo: decision
id: D-086a
fecha: 2026-11-19
autor: angel
estado: vigente
tema: interfaz
---
# D-086a · El fin de partida sigue la página 08 del canvas de alta fidelidad
- Angel decidió (2026-11-19, al aprobar el diseño): la pantalla de fin de partida (`GUI_MatchEnd`, pasos 13 a 15 del caso Finalizar la partida de los requisitos) se construye como la dibujan las tarjetas f01, f02 y f03 de la página «08 · Partida» del canvas «Bastión · Prototipos de alta fidelidad». Es una tablilla de 500 px sobre el tablero, que queda visible detrás. Lleva el tipo de partida, el resultado, la forma de término, los jugadores, el elo de entrada → final (solo en clasificatoria), un resumen, «Volver al menú» y «Buscar otra».
  - «Añadir al rival» no es un botón: el renglón del rival abre su menú de jugador (tarjeta p08).
  - Quien abandona vuelve al menú con la franja roja de m05; no ve la tablilla.
  - Hay estados para privada (sin elo, aviso azul), cuatro jugadores (el lugar se ve al terminar la participación), invitado (sin «Buscar otra») y resultado pendiente (aviso ámbar).
- porqué: los prototipos que cuentan son los del canvas, no los bocetos de `requisitos-bastion/Prototipos` (Angel, 2026-11-19). El canvas no tenía pantalla de fin y se dibujó antes de programarla.
- Claude eligió (sin aprobar): las cifras de elo de las tarjetas usan Elo con K = 32 (1 842 contra 1 886: +18, −14, +2); la fórmula sigue sin decidirse. El fondo de f01 es el tablero de la lección t03, porque la pantalla de partida no está dibujada.
- descartado: los bocetos 2g y 2h de `requisitos-bastion/Prototipos`; «Reportar» en la tablilla (el caso de reportar no está construido); revancha (ningún caso de uso la pide).
- dónde vive: canvas https://claude.ai/artifact/JMdfC1XAcc8CrT2UE7M5AR, versión 27, página «08 · Partida». Faltan las versiones en-US, 1920, ventana mínima y 1280 que tienen las otras páginas. José no lo ha visto.
- reemplazada en parte (2026-11-19): quien abandona ya no vuelve al menú sin aviso; también recibe el aviso de fin y ve la tablilla ([[D-088a-quien-abandona-ve-la-tablilla-de|D-088a]]).
