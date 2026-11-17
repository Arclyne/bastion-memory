---
tipo: caso
id: CU-10
nombre: Crear una sala privada
prioridad: Must
categoria: Obligatorio
estado: parcial
decisiones: REQ D-01, REQ D-24, REQ D-29
verificado: 2026-11-13 (nombres de contratos y carpetas de Arclyne/bastion@6dfb198; el caso no se leyó completo ni se probó, T-06a)
---
# CU-10 · Crear una sala privada
Fuente: `requisitos-bastion/casos/CU-10-crear-sala-privada.tex` (no se copia).

## Código
- `IRoomService.CreateRoom`
- `IRoomService.ChangeOptions`
- `IRoomService.StartMatch`
- `Bastion.Contracts.Rooms`
- `Bastion.Server.Host.Rooms`
- `Bastion.Server.Application.Rooms`
- `Bastion.Domain.Rooms`
- `Bastion.Server.Adapters.Rooms`
- `Bastion.Client.Networking.Rooms`

## Nota
Servicio y cliente de red; `Bastion.Client` no tiene pantalla de salas.
