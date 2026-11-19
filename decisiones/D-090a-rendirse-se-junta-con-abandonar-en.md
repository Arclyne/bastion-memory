---
tipo: decision
id: D-090a
fecha: 2026-11-19
autor: angel
estado: vigente
tema: alcance
---
# D-090a · Rendirse se junta con abandonar en una sola salida
- Angel decidió (2026-11-19): no habrá un «Rendirse» aparte. La única forma de dar por perdida una partida desde el juego es «Salir de la partida», con su confirmación ([[D-089a-abandonar-se-confirma-con-un-mensaje|D-089a]]) y la tablilla «Abandonaste» ([[D-088a-quien-abandona-ve-la-tablilla-de|D-088a]]). La fase 3 del plan de jugabilidad (rendirse) desaparece.
- porqué: con la confirmación que avisa el elo, rendirse y abandonar tenían el mismo efecto para el jugador (pierde la partida y el elo); solo cambiaban el registro (`RESIGNATION` contra `ABANDONMENT`) y el contador de abandonos de moderación.
- Claude eligió (sin aprobar): toda salida voluntaria se guarda como abandono y suma al contador `Abandonments`. El valor `Resignation` de `MatchEndReason` (dominio, contrato y columna `EndReason`) y los textos «Te rendiste» se quedan sin uso por ahora.
- descartado: un menú de partida con «Rendirme» y su confirmación ligera, como pide el caso Rendirse de los requisitos (`requisitos-bastion/casos/CU-17-rendirse.tex`).
- dónde vive: sin código nuevo; se aparta del caso Rendirse de los requisitos, que habría que marcar fuera del alcance en `requisitos-bastion`. La tarjeta f03 del canvas todavía tiene el estado «Rendición». José no lo ha visto.
