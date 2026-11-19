---
tipo: decision
id: D-084a
fecha: 2026-11-18
autor: angel
estado: vigente
tema: estandar
reglas: E-38, E-54, E-92
---
# D-084a · Una consulta se materializa con [.. consulta] y el estándar lo dice
- sobre: 3.4.1, 3.4.2, 5.3.1
- Angel y José decidieron (Angel lo confirmó el 2026-11-18 después de hablarlo con José): la 5.3.1 (E-54) materializa una consulta en una instrucción aparte con la expresión de colección `[.. consulta]`, no con `new List<T>(consulta)`. Un diccionario sigue con `new Dictionary<TKey, TValue>(consulta)`, porque la expresión de colección no admite diccionarios con elementos. Lo de D-081a (`[]` y `[a, b]`) pasa al estándar como regla nueva, E-92 en la 3.4.2. En una variable local se escribe el tipo explícito (`List<Sanction> sanctionsInEffect = [.. currentSanctions];`), porque `var` con una expresión de colección no compila.
- porqué: es la sintaxis actual de C# 12 y la que sugiere IDE0028. Angel dudó si `..` se entiende; lo aceptó porque es el operador de propagación que usan otros lenguajes (`...` en JavaScript, `*` en Python). La separación entre armar la consulta y materializarla, que es lo que pide la 5.3.1, no cambia.
- cambios en el vault: la 5.3.1 y sus tres ejemplos de la sección 5, la 3.4.2 nueva y su línea en el índice (`estandar/texto/`), E-54 y E-92 en `estandar/reglas.md`, y [[estandar-v2.4]]. El PDF y el LaTeX siguen con el texto viejo → T-18a.
- código: 61 materializaciones pasan a `[.. consulta]`: 35 que señalaba IDE0028 (las aplicó `dotnet format style --diagnostics IDE0028`) y 26 con `var` que IDE0028 no ve. `new List<BoardPawn>(Players.Count)` en `MatchViewModel` se queda: es la capacidad inicial, no una copia. `dotnet format` también ordenó los `using` de `LanguageService`, `FriendRequestRepository` y `RoomService`, que no cumplían la E-57.
- reemplaza en parte: la forma `new List<T>(…)` de D-026j y D-046j (de José); lo demás de esas decisiones sigue. José debe marcarlas (T-18a).
- dónde vive: PR #36 de `Arclyne/bastion`, rama `review-collection-spread` sacada de `main`: commits `af68cfc` (orden de los `using`) y `22dcf2d` (las 61 materializaciones). Compila sin errores y pasan las 763 pruebas.
