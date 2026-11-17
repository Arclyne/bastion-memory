---
tipo: decision
id: D-072j
fecha: 2026-11-11
autor: jose
estado: vigente
tema: estandar
origen: journal R-58
reglas: E-47, E-22
---
# D-072j · R-58 · Bastión solo usa puertos registrados de IANA (RFC 6335), del 1024 al 49151
- sobre: 4.4.2, 2.10.1
- Jose decidió: Bastión solo usa puertos registrados de IANA (RFC 6335), del 1024 al 49151. Se rechazan los del sistema (0–1023) y los dinámicos (49152–65535), que el sistema operativo usa como efímeros. La regla vive una sola vez en `ServiceEndpoints.IsRegisteredPort`, con `FirstRegisteredPort` y `LastRegisteredPort`. El cliente vuelve al puerto por defecto, y el servidor no arranca (decidido en `Channels` de `Client.Networking`).
