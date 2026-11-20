---
tipo: decision
id: D-085a
fecha: 2026-11-19
autor: angel
estado: vigente
tema: estandar
reglas: E-90, E-91
---
# D-085a · Los avisos CA1822, CA1806 y CA1834 que quedaban se corrigen
- Angel decidió (revisión de los 24 issues que dejó SonarQube, 2026-11-19):
  - CA1822: un método privado que no usa datos de la instancia se declara `static`. Se marcaron los `Translate…Failures` de los ocho servicios de `Bastion.Server.Host`, con sus sobrecargas `void` para que no las señale el siguiente análisis, y `ReportMarkReadFailure` y `CreateActionRow` en el cliente (13 métodos). No choca con D-058j, que no dice si el método es estático.
  - CA1806: una prueba que comprueba que un constructor lanza guarda la acción en `Func<T>`, no en `Action` (`Func<FriendRequest> requestSelf = () => new FriendRequest(…);`). Afectó a `TestFriendRequest` y `TestFriendship`. Justificación pendiente de revisar → T-19a.
  - CA1834: `UpperSnakeCaseEnumConverter.Separator` es `char`; el código se vuelve nombre con `string.Concat(code.Split(Separator))` en dos pasos.
- porqué: los tres son correcciones pequeñas sin cambio de comportamiento. El convertidor no tiene pruebas: se comprobó con un programa temporal que llevó los 57 valores de todos los enums del dominio a texto y de regreso con el código viejo y con el nuevo; los resultados fueron idénticos. Compila sin errores y pasan las 763 pruebas.
- fuera de esta decisión: los 11 CA1859 (devolver un tipo más concreto por rendimiento) no se cambian: respetan el contrato de Gum (`VisualTemplate` espera `GraphicalUiElement`), D-068j (`IReadOnlyDictionary`) o la intención de la prueba. Falta decidir si se marcan «Accepted» en SonarQube o se desactiva CA1859 en `.editorconfig`.
- ampliada (2026-11-19): el PR de salas privadas trajo dos métodos nuevos con el mismo aviso (`SendRoomRequest` y `DescribeHostWait` en `PrivateRoomViewModel`), porque CA1822 venía como sugerencia y `dotnet build` no lo mostraba. Angel aprobó subir `dotnet_diagnostic.CA1822.severity = warning` en `.editorconfig` y marcar los dos `static`. Se comprobó que el build avisa al quitar un `static`. Rama `static-private-room-helpers`.
- dónde vive: PR #37 de `Arclyne/bastion`, rama `review-remaining-analyzer-issues` sacada de `main`: commits `f3145f3` (CA1822), `7067279` (CA1806) y `f4f81e9` (CA1834). José no lo ha visto.
