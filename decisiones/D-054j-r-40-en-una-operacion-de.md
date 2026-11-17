---
tipo: decision
id: D-054j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-40
reglas: E-75
---
# D-054j · R-40 · En una operación de servicio WCF, el argumento que llega por la red se…
- sobre: 9.4.1 (L-20)
- Jose decidió: En una operación de servicio WCF, el argumento que llega por la red se comprueba al inicio, pero un nulo no lanza `ArgumentNullException`: lanza la falla tipada que corresponde (`InvalidCredentialsFault`, sesión inválida, el rechazo del caso). Así el cliente sabe qué pasó y el canal con sesión no se daña. En los constructores y en las demás clases sigue `ThrowIfNull`.
