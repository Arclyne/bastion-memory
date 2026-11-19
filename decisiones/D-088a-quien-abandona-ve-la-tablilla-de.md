---
tipo: decision
id: D-088a
fecha: 2026-11-19
autor: angel
estado: vigente
tema: interfaz
---
# D-088a · Quien abandona ve la tablilla de fin con el elo que perdió
- Angel decidió (2026-11-19, después de la prueba real de la fase 1): al abandonar, el jugador ya no vuelve al menú sin saber qué pasó. Ve la misma tablilla de fin que el ganador, con «Derrota», «Abandonaste la partida.», su renglón marcado «Abandonó», el elo que perdió en rojo y los botones «Volver al menú» y «Buscar otra». En cuatro jugadores ve su lugar y cuántos siguen jugando. La confirmación previa (el elo que perdería y la palabra que hay que escribir, regla RN-02 del caso Abandonar la partida de los requisitos) sigue en la fase del abandono.
- porqué: en la prueba real el que abandonaba perdía elo sin enterarse.
- Claude eligió (sin aprobar): el aviso de fin llega también al jugador que provocó el fin (`MatchCloser.ListRecipientAccountIds`); quienes ya habían abandonado antes en cuatro jugadores siguen sin recibirlo. El cliente ya no regresa al menú al aceptar el abandono; espera el aviso. Si el servidor responde que la partida ya había terminado, vuelve al menú como antes.
- descartado: la franja roja del menú de la tarjeta m05 para el abandono; una consulta aparte que devuelva el resultado al abandonar.
- dónde vive: tarjeta f03 (estado «Abandonaste») y notas de f01 y f03 en la página «08 · Partida» del canvas, versión 30; rama `match-closure` de `Arclyne/bastion`, sin commit. Reemplaza en parte [[D-086a-el-fin-de-partida-sigue-la|D-086a]] y [[D-087a-cierre-de-partida-elo-con-k|D-087a]]. José no lo ha visto.
