---
tipo: referencia
verificado: 2026-11-13 (contratos de Bastion.Contracts en Arclyne/bastion@6dfb198 leídos por script; SAD ADR-002 y SAD ADR-007 por su ficha; no se abrió ninguna conexión)
---
# Protocolo cliente-servidor

No hay mensajes TCP propios. El curso pide TCP sin WebSockets y el equipo lo cumple con CoreWCF dúplex sobre net.tcp (SAD ADR-002), cifrado con TLS (SAD ADR-007). Los «mensajes» son las operaciones de los contratos de servicio; la lista con parámetros, retorno y fallas está en la sección «contratos» de [[mapa-codigo]].

## Cómo funciona (según los contratos)
- `IAccountService.LogIn` devuelve la sesión con su token. Casi todas las demás operaciones reciben `sessionToken` como primer parámetro.
- `ISessionService.Subscribe` abre el canal de notificaciones; el servidor avisa al cliente por `INotificationCallback.ReceiveNotification`. Los tipos de aviso están en `Bastion.Contracts.Notifications`.
- Un rechazo llega como falla tipada (`FaultException<TDetail>`); las de cada operación aparecen tras `!` en el mapa.
- Las operaciones marcadas `oneway` no devuelven nada ni fallas al cliente.

## Reglas del equipo
- Puertos: solo registrados de IANA, de `ServiceEndpoints.FirstRegisteredPort` a `ServiceEndpoints.LastRegisteredPort`; por omisión `ServiceEndpoints.DefaultPort` y en el servidor `appsettings.Server.NetTcpPort` (R-58).
- Forma de una operación de servicio y de sus fallas: R-40, R-43, R-44, R-45, R-50, R-53, R-56. Arreglos de contrato: R-42. `MessageId` se queda en los contratos (R-57).
- Cerrar un canal WCF: E-80.
- El cliente valida el certificado con la huella SHA-256 que lee de la variable de entorno `BASTION_SERVER_THUMBPRINT` (journal de José; sin comprobar).

## Diferencias conocidas
- Los casos de uso nombran mensajes como `CHAT_SEND_REQUEST`; en el código son operaciones (`IChatService.SendMatchChatMessage`). No hay tabla de equivalencias.
- Operaciones sin caso de uso: lobby y chat privado (Q-07a).
