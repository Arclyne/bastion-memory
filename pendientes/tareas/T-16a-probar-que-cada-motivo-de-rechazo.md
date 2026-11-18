---
tipo: tarea
id: T-16a
fecha: 2026-11-18
autor: angel
estado: pendiente
grupo: probar
---
# T-16a · Probar que cada motivo de rechazo de sala tiene su renglón
- hecho cuando: hay una prueba en `Bastion.Client.Tests` que recorre cada valor de `RoomRejectionReason` y comprueba que `RoomContractTranslator.ToRejection` lo traduce sin lanzar, al estilo de `TestChatContractTranslator.ToRejection_KnownReason_MapsRejection`; y se decidió qué hacer con `RoomTranslator.ToReason` del servidor.
- bloqueada por: nada. La escribe Angel, no Claude (Angel, 2026-11-18).
- origen: revisión de las tablas de D-068j (2026-11-18). Si se agrega un motivo al enum y se olvida su renglón, solo se nota en tiempo de ejecución con `ArgumentOutOfRangeException`.
- falta saber: `RoomTranslator` vive en `Bastion.Server.Host`, que no tiene proyecto de pruebas; no se ha decidido si se crea uno o se deja sin cubrir.
