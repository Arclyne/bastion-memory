---
tipo: decision
id: D-080a
fecha: 2026-11-18
autor: angel
estado: vigente
tema: estandar
reglas: E-05, E-75, E-76
---
# D-080a · Cómo se lee un diccionario o un texto que puede no tener el dato
- sobre: 2.1.4, 9.4.1, 9.4.2
- Angel decidió (revisión del patrón `Try`, 2026-11-18):
  - Diccionario con valor de tipo referencia: `T? x = d.GetValueOrDefault(k);` y en seguida `if (x is null)` que lanza, sale, salta o crea el valor; con valor alternativo, `x ?? alternativa` (`?? Array.Empty<…>()`) o `Lookup.FromNullable`. No se usa `?? throw`: un `throw` dentro de una expresión se lee como ternaria.
  - Diccionario con valor de tipo valor (`DateTime`, `byte`, `Color`, enum): se queda `TryGetValue`, con el resultado en un `bool` con nombre (`hasSentMessage`, `isKnownMover`) antes del `if`, porque `default(T)` se confunde con un dato real.
  - Se quedan con su `out`: `int.TryParse` sobre texto que puede venir mal (`BoardLayout.FindSquare`, `ServerAddress.GetPort`), `MessageProperties.TryGetValue` de CoreWCF (`CallerAddress`, que solo es `IDictionary` y cuyo indexador lanza) y las tablas de D-068j.
  - Dentro de un ciclo con cuerpo corto se usa el `if` en positivo, no `continue` (`MatchViewModel.RebuildPawns`).
- porqué: el profesor pidió justificar el patrón `Try`/`out` (2026-11-18). Las Framework Design Guidelines piden evitar `out` y aceptan el patrón Try-Parse; CA1854 prefiere `TryGetValue` a `ContainsKey` + indexador. Con un tipo referencia, guardar el `bool` de `TryGetValue` aparte hace perder al compilador el seguimiento de nulos (CS8604 en `RebuildPawns`); `is null` sí lo conserva.
- descartado: `ContainsKey` + indexador (dos búsquedas); el indexador con `catch`; `Values.OfType<…>()` en `CallerAddress`; `?? throw`; `== null` o `!x` (la 9.4.1 exige `is null`).
- dónde vive: PR #32 de `Arclyne/bastion`, rama `review-try-out-pattern` sacada de `main`: commits `238f34d` (`CallerAddress`), `02c2ff7` (tipos valor), `b961e18` (`RebuildPawns`) y `9d85da6` (tipos referencia). José no lo ha visto.
- reemplaza a: D-020j (patrón `TryGetX(…, out T)` privado), que el PR #29 ya había quitado del código. Ningún método propio declara `out`; cuando dos métodos necesitan la misma condición sobre un valor que puede faltar, se usa `Lookup<T>` o una bandera (D-075a). Angel lo confirmó el 2026-11-18; José no lo ha visto.
