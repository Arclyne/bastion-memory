---
tipo: referencia
verificado: 2026-11-13 (SAD v0.2 de bastion_game_sad@b33913f, recorrido por secciones y tablas, no leído completo; proyectos de Arclyne/bastion@6dfb198)
---
# Arquitectura

El SAD no se copia: vive en `Arclyne/bastion_game_sad` (`main.tex`, `main.pdf`, v0.2 del 2026-10-12). Aquí va cómo se corresponde con el código y dónde ya no coincide.

## Decisiones del SAD (índice; el texto está en el SAD)
| ID | Decisión | Estado en el SAD |
|---|---|---|
| SAD ADR-001 | capas cliente-servidor con el servidor como única autoridad | aceptado |
| SAD ADR-002 | CoreWCF dúplex sobre net.tcp con llamadas asíncronas | aceptado |
| SAD ADR-003 | cliente con MonoGame DesktopGL | aceptado |
| SAD ADR-004 | `SecurityMode.None` | sustituido por SAD ADR-007 |
| SAD ADR-005 | EF Core y SQL Server 2022, con el esquema en scripts SQL, sin migraciones | aceptado |
| SAD ADR-006 | el cliente traduce los resultados codificados del servidor; idioma por omisión en-US (sustituye el es-MX de REQ D-21) | aceptado |
| SAD ADR-007 | canal net.tcp cifrado con TLS; el cliente reconoce al servidor por la huella de su certificado | aceptado |

Restricciones del curso (CON-NN), escenarios de calidad (QAS-NN) y requisitos significativos (ASR-NN): solo en el SAD.

## Componentes del SAD y proyectos del código
| SAD | Nombre en el SAD | Proyecto en el código |
|---|---|---|
| C-01 | Bastion.Client | `Bastion.Client` (MonoGame y Gum) más `Bastion.Client.Networking`, que el SAD no nombra |
| C-02 | Bastion.Contracts | `Bastion.Contracts` (netstandard2.0) |
| C-03 | Bastion.Server.Host | `Bastion.Server.Host` |
| C-04 | Bastion.Server.Services | `Bastion.Server.Application` |
| C-05 | Bastion.Domain | `Bastion.Domain` |
| C-06 | Bastion.Server.Data | `Bastion.Server.Adapters` |
| C-07 | base de datos | scripts de `database/` → [[modelo-datos]] |
| C-08 | pasarela de correo y segundo factor (planeado) | no existe |

La correspondencia de C-04 y C-06 la dedujo Claude por responsabilidad; nadie la confirmó (Q-05a).

Qué hace cada proyecto y sus dependencias: [[sistemas]].

## Dónde no coinciden el SAD y el código
- Nombres de módulos y `ILeaderboardService` «ya construido» (Q-05a).
- Presentación del tablero abierta en SAD R-02; decidida en D-001a (Q-06a).
- 28 casos de uso contra 27 (Q-04a).
- SAD R-09 dice que el esquema conserva tablas de requisitos deseables; siguen en `database/` (Mute, Block, Appeal, ModerationLog).

## Reglas del equipo sobre la arquitectura
Están en decisiones con `tema: estandar`: inyección y raíz de composición (R-30, R-34, R-46, R-49, R-55), errores de la base (R-36, R-37, R-38), servicios WCF (R-40, R-44, R-45, R-50, R-53), sufijos `Repository` y `Store` (R-35).
