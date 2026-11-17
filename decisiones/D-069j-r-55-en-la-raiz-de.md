---
tipo: decision
id: D-069j
fecha: 2026-11-11
autor: jose
estado: vigente
tema: estandar
origen: journal R-55
reglas: E-47
---
# D-069j · R-55 · En la raíz de composición del servidor cada método de registro registra solo…
- sobre: Pasada 3, 4.4.2
- Jose decidió: En la raíz de composición del servidor cada método de registro registra solo los tipos de su capa (`AddBastionAdapters`, `AddBastionApplication`, `AddBastionHost`). La lista de servicios WCF para CoreWCF (`AddBastionServices`) va en `ServiceRegistration`, junto a sus `AddTransient`, y `Program` compone. Una clase que no se llama como un registro (`ServerCertificate`) no registra servicios. Se pregunta si aplica a la raíz de composición del cliente al revisarla.
