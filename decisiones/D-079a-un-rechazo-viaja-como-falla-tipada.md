---
tipo: decision
id: D-079a
fecha: 2026-11-18
autor: angel
estado: vigente
tema: estandar
reglas: E-62, E-75
---
# D-079a · Un rechazo viaja como falla tipada, no como código
- sobre: 7.2.2, 9.4.1
- Angel decidió: una operación de servicio devuelve solo el valor de éxito. Un rechazo no viaja como código dentro de la respuesta: es una falla tipada declarada con `[FaultContract]` (`FaultException<T>`), y el cliente la traduce a su propia excepción o a un estado de la pantalla. Las razones parecidas se agrupan en una sola falla con un enum (`AccountRestrictedFault` con `RestrictionReason` reúne cuenta bloqueada, pendiente, suspendida y vetada). `InvalidCredentialsFault` va aparte porque no debe revelar el estado de la cuenta. Una operación que no tiene nada que devolver es `void`, nunca `bool`.
- porqué: el profesor lo señaló en su revisión del 2026-10-19: `AccessDecision` con `AccessDecisionCode` era "estilo API REST", y el transporte es RPC (WCF), donde el error viaja como falla. También pidió agrupar las razones para no tener muchas fallas. La fecha y los nombres viejos vienen de la memoria de Claude; se comprobó contra `origin/main` (`15b17ce`) el 2026-11-18. Un argumento nulo que llega por la red se responde igual, con falla ([[D-054j-r-40-en-una-operacion-de|D-054j]]). El `bool` de los métodos `Try…` internos lo decide [[D-076a-un-bool-que-solo-avisa-si|D-076a]].
- excepciones: un enum de respuesta que distingue entre éxitos y no entre rechazos se queda (`FriendRequestResult { RequestSent, FriendshipStarted }`; los rechazos van en `FriendshipRejectedFault`). También se queda un valor de éxito con su bandera, como `OwnRoomResult.IsInRoom` (D-075a).
- dónde vive: en `main` ya se cumple. `PlayerSession LogIn(...)` declara `InvalidCredentialsFault` y `AccountRestrictedFault`; `Bastion.Contracts` tiene 52 `[FaultContract]`, ninguna operación devuelve `bool` y no hay enums `*Code`. José no la ha visto.
