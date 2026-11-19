---
tipo: decision
id: D-087a
fecha: 2026-11-19
autor: angel
estado: vigente
tema: interfaz
---
# D-087a · Cierre de partida: elo con K 32, dos avisos de fin y estadísticas escribibles
- Angel decidió (2026-11-19, al aprobar la fase 1 del plan de jugabilidad):
  - El elo es el Elo clásico con K = 32 (`EloPolicy.KFactor`), redondeado al entero más cercano y sin piso. Solo se aplica en partidas clasificatorias de dos jugadores, porque la cola de clasificatoria solo usa el modo clásico (`MatchmakingPolicy.RankedGameModeCode`).
  - Dos avisos de fin: `ParticipationEndedNotification` (un jugador sale del tablero por meta o abandono y la partida sigue) y `MatchEndedNotification` (la partida terminó). `MatchAbandonedNotification` desaparece y `PawnMovedNotification` pierde `IsMatchOver`. Los avisos van a todos los participantes que no abandonaron.
  - `PendingClose` y el estado «resultado pendiente» pasan a la fase del reloj: hoy todo cierre lo provoca un jugador y una falla de escritura no aplica nada.
  - El renglón del rival en la tablilla de fin no abre nada hasta que exista el perfil de otro jugador; enviar una solicitud de amistad pide el código de amigo, no el nickname.
  - `ModeStatistic` deja de ser de solo lectura: el cierre la actualiza (jugadas, ganadas, perdidas, abandonos, elo, fecha) y la crea con `ModeStatistic.DefaultEloRating` si falta. Reemplaza en parte [[D-082a-las-entidades-de-catalogo-de-solo|D-082a]].
- porqué: el caso Finalizar la partida de los requisitos pide elo y estadísticas en una sola transacción, y los requisitos, el SAD y `GameMode` no fijan la fórmula del elo.
- Claude eligió (sin aprobar): el record que agrupa las dependencias de `MatchMoveService` se llama `MatchMoveFollowUp` (R-30); los jugadores se identifican en los avisos de fin por su `TurnOrder`, no por nickname; en cuatro jugadores solo el 1.er lugar cuenta como `Won`.
- descartado: calcular el elo en el cliente; un solo aviso con banderas `IsMatchOver` en cada jugada; construir `PendingClose` en esta fase.
- dónde vive: rama `match-closure` de `Arclyne/bastion`, sin commit al 2026-11-19. José no lo ha visto.
- reemplazada en parte (2026-11-19): quien abandona ya no vuelve al menú sin aviso; también recibe el aviso de fin y ve la tablilla ([[D-088a-quien-abandona-ve-la-tablilla-de|D-088a]]).
