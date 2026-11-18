---
tipo: decision
id: D-075a
fecha: 2026-11-18
autor: angel
estado: vigente
tema: estandar
reglas: E-75, E-76
---
# D-075a · Ningún método devuelve null
- sobre: 9.4.1, 9.4.2, 9.3.2
- Angel decidió: ningún método ni operación de servicio devuelve `null` ni declara un tipo de retorno anulable. Cuando lo buscado puede faltar se devuelve un `Lookup<T>` (`Lookup.Found`, `Lookup.Missing`, `Lookup.FromNullable`) o un valor bandera: un `None` del enum (`WallRejection.None`), un índice -1 o un texto vacío con su `Has…` (`WinnerNickname` y `HasWinner`, como `NoticeText` y `HasNotice`). Un valor anulable dentro de un método se revisa en seguida con `??` o `is null` y nunca sale como resultado.
- porqué: el profesor lo señaló en la revisión, con `FindBlockedPlayer` (`WallPolicy`), que devolvía `WallRejection?` y `null` cuando nadie quedaba encerrado. Resuelve lo dudoso de T-13a: el estándar no lo pide (el ejemplo correcto de E-75 es `Player? FindPlayer(...)`), pero lo pide quien evalúa.
- no aplica a: propiedades con datos opcionales, que son columnas que aceptan nulos (`Account.LockedUntil`, `Match.EndedAt`, `ChatMuteStatus.EndsAt`), los campos de los DTO de contrato ni `WallRejection.BlockedTurnOrder`, que solo tiene valor cuando el muro deja a alguien sin camino.
- Claude eligió (sin aprobar): los traductores del cliente (`FriendContractTranslator.ToFoundPlayers`, `ConversationContractTranslator.ToPreviews`) siguen recibiendo `[]?` y usan `?? Array.Empty`, porque lo que llega por la red puede venir sin el arreglo.
- dónde vive: el PR #28 de José quitó todos los `return null`. El 2026-11-18 Angel quitó los dos retornos anulables que quedaban en contratos (`IFriendshipService.SearchPlayers` y `IConversationService.ListConversations`, de `[]?` a `[]`) y el `null` de `MatchPlayViewModel.WinnerNickname`, y agregó la prueba `SelectSquare_MatchAlreadyOver_NamesNoWinner`. Está en la rama `review-no-nullable-returns`, sacada de `main`, con los commits `84161c5` (contratos) y `da47397` (ganador). En `review-tests` pasaron 743 pruebas. José no la ha visto.
