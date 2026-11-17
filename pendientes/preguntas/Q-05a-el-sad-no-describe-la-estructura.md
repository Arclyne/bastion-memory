---
tipo: pregunta
id: Q-05a
fecha: 2026-11-13
autor: angel
estado: abierta
grupo: hallazgos
---
# Q-05a · El SAD no describe la estructura actual del código
El SAD v0.2 (2026-10-12) nombra los módulos `Bastion.Server.Services` (C-04) y `Bastion.Server.Data` (C-06) y da por construido `ILeaderboardService`. El código (commit `6dfb198`) tiene `Bastion.Server.Application`, `Bastion.Server.Adapters` y `Bastion.Client.Networking`, y no tiene ningún tipo de clasificación. El riesgo SAD R-06 dice que el repositorio remoto será GitLab o Bitbucket y es GitHub.
Hay que decidir quién actualiza el SAD y cuándo. Detalle en [[arquitectura]].
