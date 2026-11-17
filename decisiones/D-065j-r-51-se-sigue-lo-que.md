---
tipo: decision
id: D-065j
fecha: 2026-11-11
autor: jose
estado: vigente
tema: estandar
origen: journal R-51
reglas: E-38
---
# D-065j · R-51 · Se sigue lo que pidan IDE0007 e IDE0008, porque la 3.4.1 dice que su definición…
- sobre: 3.4.1 (L-01)
- Jose decidió: Se sigue lo que pidan IDE0007 e IDE0008, porque la 3.4.1 dice que su definición coincide con la de esos analizadores. En una llamada calificada cuyo método nombra el tipo que devuelve (`MatchmakingTranslator.ToMatchFoundNotification(…)` → `MatchFoundNotification`) va `var`. En una llamada sin calificar dentro de la misma clase (`ToPrivateChatMessage(…)`) el analizador pide el tipo explícito (comprobado en `PrivateChatTranslator`, 2026-11-11).
