---
tipo: decision
id: D-058j
fecha: 2026-11-11
autor: jose
estado: vigente
tema: estandar
origen: journal R-44
---
# D-058j · R-44 · Una operación de servicio WCF deja su llamada en una variable Func<…> hacia un…
- sobre: R-04, R-14 (L-21)
- Jose decidió: Una operación de servicio WCF deja su llamada en una variable `Func<…>` hacia un método privado `…InRequestScope` (abre el ámbito, pide el servicio, llama y traduce el resultado) y devuelve `Translate…Failures(nameof(…), variable)`, un método privado por servicio que solo convierte excepciones en fallas. Nada de `Run`.
