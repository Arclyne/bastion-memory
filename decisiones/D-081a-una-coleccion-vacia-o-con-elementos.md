---
tipo: decision
id: D-081a
fecha: 2026-11-18
autor: angel
estado: vigente
tema: estandar
reglas: E-38, E-54
---
# D-081a · Una colección vacía o con elementos fijos se crea con expresión de colección
- sobre: 3.4.1, 5.3.1
- Angel decidió (revisión del análisis de SonarQube, 2026-11-18): una colección vacía se crea con `[]` y una con elementos conocidos con `[a, b]`, en lugar de `new List<T>()`, `new Dictionary<K, V>()`, `new HashSet<T>()`, `new ObservableCollection<T>()` o `new List<T> { a }`. El tipo queda donde se declara el campo, la propiedad o el retorno; en una variable local se escribe el tipo explícito (`List<int> ids = [];`), porque `var` con `[]` no compila y la 3.4.1 solo admite `var` cuando el tipo se ve a la derecha.
- porqué: lo pide IDE0028, que la compilación ya revisa (`EnforceCodeStyleInBuild`) y SonarQube importa (80 de sus 144 issues). Ninguna regla del estándar habla de cómo crear una colección vacía o con elementos fijos, y `[]` evita repetir tipos largos como `Dictionary<int, List<FriendSummary>>`. No cambia el comportamiento: con destino `List<T>` el compilador genera lo mismo que `new List<T>()`.
- descartado: desactivar IDE0028 en `.editorconfig` (deja dos formas para lo mismo y quita la sugerencia al código nuevo).
- fuera de esta decisión: materializar una consulta sigue la 5.3.1 con `new List<T>(consulta)`, aunque IDE0028 sugiera `[.. consulta]` (35 casos). Si cambia o no se ve en T-17a.
- dónde vive: PR #33 de `Arclyne/bastion`, rama `review-collection-expressions` sacada de `main`, commit `12654da` (80 cambios en 42 archivos). Compila sin errores y pasan las 743 pruebas. José no lo ha visto.
