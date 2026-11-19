---
tipo: decision
id: D-082a
fecha: 2026-11-18
autor: angel
estado: vigente
tema: estandar
---
# D-082a · Las entidades de catálogo de solo lectura conservan su constructor privado
- Angel decidió (revisión del análisis de SonarQube, 2026-11-18): `BannedWord` y `ModeStatistic` se quedan con su único constructor `private` y sin otro modo de crearlas. Los dos issues S3453 ("This class can't be instantiated; make its constructor 'public'") se marcan como **False positive** en SonarQube, con un comentario que lo explica. No se cambia el código.
- porqué: son tablas de catálogo de solo lectura. Sus filas las cargan los scripts SQL de `database/` (por ejemplo `04_insert_leaderboard_demo.sql`) y el código solo las consulta: `BannedWordRepository` para `ChatModerator` y `MatchRepository.FindEloRatingsByAccountId` para el emparejamiento. El constructor privado impide crear una palabra prohibida o un elo desde el código. EF Core sí puede materializarlas, porque usa el constructor privado por reflexión, y S3453 no lo sabe.
- descartado: constructor `public` (permite crear entidades vacías); `protected` (sugiere herencia que no existe); `[SuppressMessage]` en el código (el proyecto no usa ese patrón y la justificación funciona como comentario, R-39).
- dónde vive: en SonarQube local (proyecto `Bastion`), estado de los dos issues. Si una entidad de catálogo llega a crearse desde el código (por ejemplo, actualizar el elo al terminar una partida), deja de ser de solo lectura y esta decisión no le aplica. José no lo ha visto.
- reemplazada en parte (2026-11-19): `ModeStatistic` dejó de ser de solo lectura; el cierre de partida la crea y la escribe ([[D-087a-cierre-de-partida-elo-con-k|D-087a]]). Sigue vigente para `BannedWord`. El issue S3453 de `ModeStatistic` deja de aplicar.
