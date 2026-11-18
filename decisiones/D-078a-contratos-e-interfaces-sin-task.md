---
tipo: decision
id: D-078a
fecha: 2026-11-18
autor: angel
estado: vigente
tema: estandar
reglas: E-80
---
# D-078a · Contratos e interfaces sin Task
- sobre: 9.7.1
- Angel decidió: un contrato de servicio y una interfaz propia (puertos de Application, clientes de Client.Networking, repositorios) no exponen `Task` ni `Task<T>`. Devuelven el tipo simple o `void`. La concurrencia (`Task.Run`, un hilo aparte) vive solo dentro de la implementación o del que llama: el cliente envuelve la llamada bloqueante, por ejemplo `await Task.Run(() => _accounts.LogIn(credentials))` en `LoginViewModel`.
- porqué: el profesor lo señaló en su revisión del 2026-10-19: un contrato no dice con qué técnica se ejecuta, y `Task` filtra esa técnica hacia quien solo debe saber qué pide. Va con [[D-077a-nombres-del-juego-sin-vocabulario-web|D-077a]] (sin sufijo `Async`). La fecha viene de la memoria de Claude; se comprobó contra `origin/main` (`15b17ce`) el 2026-11-18.
- excepciones: los métodos que impone .NET (`BackgroundService.ExecuteAsync`, `IHostedService.StartAsync` y `StopAsync`) y los métodos de la interfaz gráfica que esperan esa llamada (`async Task` en los view models, con E-80).
- dónde vive: en `main` ya se cumple. Ni `Bastion.Contracts` ni las interfaces `I*.cs` de `src` mencionan `Task`. José no la ha visto.
