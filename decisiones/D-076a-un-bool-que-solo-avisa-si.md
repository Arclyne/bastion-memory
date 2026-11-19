---
tipo: decision
id: D-076a
fecha: 2026-11-18
autor: angel
estado: vigente
tema: estandar
reglas: E-08, E-45, E-49
---
# D-076a · Un bool que solo avisa si se hizo algo se parte en pregunta y acción
- sobre: 2.2.3, 4.3.2, 4.6.1
- Angel decidió: un método propio `Try…` que devuelve `bool` solo para avisar si pudo actuar, sin una carrera que lo impida, se parte en una pregunta (`Can…`, `Is…`) y una acción `void` que lanza `InvalidOperationException` si se llama sin poder: `IClipboard.TryCopyText` pasa a `CanCopyText` y `CopyText`. Un despacho por tipo no encadena métodos `bool` con `||`: usa una tabla `IReadOnlyDictionary<Type, Action<…>>`, con un método `void` por tipo (`NotificationCallback`, con `AddDispatcher<TNotification>`).
- porqué: el profesor pidió justificar el patrón `Try` (2026-11-18): heredado de C, no aplica a una validación simple y complica la lectura. E-08 exceptúa el patrón Try de .NET, pero `TryCopyText` no lo necesita. Un `switch` de 14 tipos pasa de complejidad 10 (E-49), y partirlo con un `default` que delega lo prohíben E-45 y D-068j.
- Claude eligió (sin aprobar): el nombre `AddDispatcher` y que el falso `FakeClipboard.CopyText` lance si `CanCopyText` es falso, como la clase real.
- descartado: un `switch` por tipo; métodos por grupo encadenados con `default`; renombrar `TryCopyText` a `CanCopyText` sin partirlo (el nombre preguntaría y la llamada copiaría).
- dónde vive: `src/Bastion.Client/Screens/IClipboard.cs`, `src/Bastion.Client/Platform/Clipboard.cs`, `src/Bastion.Client.Networking/Notifications/NotificationCallback.cs`. PR #32 de `Arclyne/bastion`, rama `review-try-out-pattern` sacada de `main`: commits `6d95642` (portapapeles) y `a443fdb` (despacho). José no lo ha visto.
- se mantienen con `Try…` (revisión 2026-11-18, falta que Angel los confirme uno por uno): los que comprueban y actúan en un solo paso bajo `lock` o `Interlocked` (`TryStartCooldown`, `MatchmakingQueue.TryRemove`, `RoomRegistry.TryOpen`, `TryStopKeepAlive`) y `TrySubmitTurn`, cuyo éxito solo se sabe después de llamar al servidor.
