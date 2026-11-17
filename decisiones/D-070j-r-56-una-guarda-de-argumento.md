---
tipo: decision
id: D-070j
fecha: 2026-11-11
autor: jose
estado: vigente
tema: estandar
origen: journal R-56
reglas: E-46
---
# D-070j · R-56 · Una guarda de argumento de red que se repite igual en varios servicios WCF es…
- sobre: 4.4.1
- Jose decidió: Una guarda de argumento de red que se repite igual en varios servicios WCF es un método público estático del traductor que crea su falla: `SessionTranslator.RequireSessionToken` y `ChatTranslator.RequireText`. Las guardas propias de un servicio (`RequireFriendCode`) siguen privadas. `GetUtcNow` se queda en cada clase y el ámbito sigue la R-44.
