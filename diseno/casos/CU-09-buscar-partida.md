---
tipo: caso
id: CU-09
nombre: Elegir modo y buscar partida clasificatoria
prioridad: Must
categoria: Jugabilidad
estado: con código
decisiones: REQ D-01, REQ D-24, REQ D-29
verificado: 2026-11-13 (nombres de contratos y carpetas de Arclyne/bastion@6dfb198; el caso no se leyó completo ni se probó, T-06a)
---
# CU-09 · Elegir modo y buscar partida clasificatoria
Fuente: `requisitos-bastion/casos/CU-09-buscar-partida.tex` (no se copia).

## Código
- `IMatchmakingService.StartSearch`
- `IMatchmakingService.CancelSearch`
- `IMatchmakingService.ConfirmPresence`
- `Bastion.Contracts.Matchmaking`
- `Bastion.Server.Host.Matchmaking`
- `Bastion.Server.Application.Matchmaking`
- `Bastion.Domain.Matchmaking`
- `Bastion.Server.Adapters.Matchmaking`
- `Bastion.Client.Networking.Matchmaking`
- `MatchSearchPanel`
- `MatchSearchViewModel`
- `MatchSearchStage`
- `PresenceDialogView`

## Nota
Solo el modo clásico de dos jugadores (según el journal); elegir modo sin comprobar.
