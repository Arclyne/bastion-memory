---
tipo: caso
id: CU-01
nombre: Iniciar sesión
prioridad: Must
categoria: Obligatorio
estado: con código
decisiones: REQ D-01, REQ D-25
verificado: 2026-11-13 (nombres de contratos y carpetas de Arclyne/bastion@6dfb198; el caso no se leyó completo ni se probó, T-06a)
---
# CU-01 · Iniciar sesión
Fuente: `requisitos-bastion/casos/CU-01-iniciar-sesion.tex` (no se copia).

## Código
- `IAccountService.LogIn`
- `Bastion.Contracts.Accounts`
- `Bastion.Server.Host.Accounts`
- `Bastion.Server.Application.Accounts`
- `Bastion.Domain.Accounts`
- `Bastion.Client.Networking.Accounts`
- `Bastion.Client.Screens.Login`
- `Bastion.Domain.Auditing`
- `Bastion.Server.Application.Auditing`

## Nota
El flujo no pide segundo factor: no hay código de verificación en el servicio.
