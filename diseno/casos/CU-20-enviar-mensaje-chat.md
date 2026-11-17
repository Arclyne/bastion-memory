---
tipo: caso
id: CU-20
nombre: Enviar un mensaje de chat
prioridad: Must
categoria: Obligatorio
estado: con código
decisiones: REQ D-10, REQ D-21, REQ D-25, REQ D-26
verificado: 2026-11-13 (nombres de contratos y carpetas de Arclyne/bastion@6dfb198; el caso no se leyó completo ni se probó, T-06a)
---
# CU-20 · Enviar un mensaje de chat
Fuente: `requisitos-bastion/casos/CU-20-enviar-mensaje-chat.tex` (no se copia).

## Código
- `IChatService.SendMatchChatMessage`
- `Bastion.Contracts.Chat`
- `Bastion.Server.Host.Chat`
- `Bastion.Server.Application.Chat`
- `Bastion.Domain.Chat`
- `Bastion.Client.Networking.Chat`
- `Bastion.Client.Screens.MainMenu.Chat`

## Nota
Canal de partida; el canal de sala no tiene operación; el chat de lobby y el privado no están en el caso (Q-07a).
