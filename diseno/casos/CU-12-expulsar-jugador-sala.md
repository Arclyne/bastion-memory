---
tipo: caso
id: CU-12
nombre: Expulsar a un jugador de la sala
prioridad: Must
categoria: Obligatorio
estado: parcial
decisiones: REQ D-27
verificado: 2026-11-13 (nombres de contratos y carpetas de Arclyne/bastion@6dfb198; el caso no se leyó completo ni se probó, T-06a)
---
# CU-12 · Expulsar a un jugador de la sala
Fuente: `requisitos-bastion/casos/CU-12-expulsar-jugador-sala.tex` (no se copia).

## Código
- `WaitingRoom`
- `RoomRegistry`

## Nota
La sala rechaza a un expulsado (`HasKicked`), pero no hay operación para expulsar.
