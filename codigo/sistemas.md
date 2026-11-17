---
tipo: sistemas
verificado: 2026-11-17 (estructura y nombres de Arclyne/bastion@6dfb198; ningún proyecto se leyó entero; dependencias de los .csproj; lo marcado «journal» viene del journal de José del 2026-11-11 sin comprobar)
---
# Sistemas del código

Qué hace cada proyecto y cómo se conectan. Tipos, métodos, operaciones, tablas y paquetes: [[mapa-codigo]]. Números: [[valores]]. Correspondencia con el SAD: [[arquitectura]]. Si esta nota no coincide con el código, gana el código.

Dependencias: `Bastion.Server.Application → Bastion.Domain` · `Bastion.Server.Adapters → Bastion.Domain, Bastion.Server.Application` · `Bastion.Server.Host → Bastion.Contracts, Bastion.Server.Application, Bastion.Server.Adapters` · `Bastion.Client.Networking → Bastion.Contracts` · `Bastion.Client → Bastion.Client.Networking, Bastion.Domain`.

## Bastion.Domain
Entidades y reglas del juego sin dependencias externas: cuentas y bloqueo por intentos, partida y tablero (peones, muros, turnos), emparejamiento, salas, amigos, chat, moderación, sesiones y estadísticas por modo. Las reglas viven en clases `*Policy` (R-07). Las expresiones regulares se crean con `TextPattern.Create` (R-08).

## Bastion.Server.Application
Casos de uso del servidor y sus puertos: servicios (`LoginService`, `MatchSearchService`, `RoomRegistry`, `LobbyChatService`, `PrivateChatService`…) e interfaces `I…Repository` e `I…Service` que implementan los adaptadores. Excepciones de aplicación por cada rechazo.

## Bastion.Server.Adapters
Implementa los puertos: EF Core sobre SQL Server (`Persistence`, configuraciones por entidad, repositorios), seguridad (`PasswordHasher`, `SessionTokenGenerator`), código de sala (`RoomCodeGenerator`) y orden de turnos (`TurnOrderShuffler`). Los errores de la base se traducen en un solo lugar (R-36, R-37).

## Bastion.Server.Host
Arranque del servidor y raíz de composición. Servicios CoreWCF sobre net.tcp que traducen contratos a llamadas de aplicación y fallas tipadas. Configuración en `appsettings.json` (`appsettings.Server.NetTcpPort`).

## Bastion.Contracts
Contratos de servicio y DTO compartidos por cliente y servidor (netstandard2.0). Rutas y puertos en `ServiceEndpoints`.

## Bastion.Client.Networking
Clientes de cada servicio, apertura y cierre de canales (`ChannelSettings`, `ChannelCloser`), sesión y notificaciones del servidor. Traduce contratos a tipos del cliente.

## Bastion.Client
El juego: MonoGame DesktopGL con Gum. Pantallas en `Screens` (inicio de sesión, menú, chat, amigos, partida con escena 3D), controles propios en `Controls`, tema en `Theme`, idiomas en `Localization`. Solo `BastionGame`, `GumScreenHost` y `GumClipboard` tocan los globales de Gum (journal).

## Pruebas
`Bastion.Client.Tests`, `Bastion.Server.Application.Tests` y `Bastion.Domain.Tests`: conteo de clases y pruebas en [[mapa-codigo]] (§ pruebas). No se corrieron.

## Base de datos
Scripts de `database/` (crear base, tablas, datos de prueba y de demostración, amigos, mensajes privados). EF Core se ajusta a ellos, sin migraciones (SAD ADR-005). Modelo: [[modelo-datos]].

## Código transversal
Código que no pertenece a un caso de uso. El verificador lo da por cubierto; un caso de uso se cita en su ficha (`diseno/casos/`).
TRANSVERSAL | arranque, navegación, controles, tema e idiomas del cliente | código: `Bastion.Client`, `Bastion.Client.Controls`, `Bastion.Client.Localization`, `Bastion.Client.Platform`, `Bastion.Client.Screens`, `Bastion.Client.Screens.MainMenu`, `Bastion.Client.Theme`
TRANSVERSAL | conexión, canales, sesión y notificaciones | código: `Bastion.Client.Networking`, `Bastion.Client.Networking.Channels`, `Bastion.Client.Networking.Notifications`, `Bastion.Client.Networking.Sessions`, `Bastion.Contracts`, `Bastion.Contracts.Notifications`, `Bastion.Contracts.Sessions`, `Bastion.Server.Host`, `Bastion.Server.Host.Common`, `Bastion.Server.Host.Sessions`, `Bastion.Server.Application.Sessions`, `Bastion.Server.Application.Security`, `Bastion.Server.Adapters.Security`, `Bastion.Domain.Sessions`
TRANSVERSAL | persistencia y piezas comunes | código: `Bastion.Server.Adapters`, `Bastion.Server.Adapters.Persistence`, `Bastion.Server.Adapters.Persistence.Configurations`, `Bastion.Server.Adapters.Persistence.Conversions`, `Bastion.Server.Adapters.Persistence.Repositories`, `Bastion.Server.Application.Common`, `Bastion.Domain.GameModes`, `Bastion.Domain.Text`
