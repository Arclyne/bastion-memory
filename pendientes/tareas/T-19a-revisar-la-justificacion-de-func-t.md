---
tipo: tarea
id: T-19a
fecha: 2026-11-19
autor: angel
estado: pendiente
grupo: estandar
---
# T-19a · Revisar la justificación de Func<T> en las pruebas de constructores
- hecho cuando: Angel (y José, si cambia algo) revisó por qué una prueba que comprueba que un constructor lanza usa `Func<T>` en vez de `Action` (D-085a), y quedó confirmado o cambiado; si se confirma, decidir si va al estándar en la sección 12.
- la justificación que se dio (Claude, 2026-11-19, sin revisar contra documentación):
  - El equipo guarda la acción en una variable con nombre antes de `Assert.Throws` (121 pruebas, ninguna en línea), por E-90 y D-013j.
  - `Action` es código que no devuelve nada; `Func<T>` es código que devuelve un `T`. Construir un objeto devuelve algo, así que con `Action` el objeto se descarta y CA1806 avisa.
  - Con la lambda en línea, `Assert.Throws<T>(() => new X(…))`, el compilador elige la sobrecarga de xUnit que recibe un `Func`; por dentro es lo mismo que `Func<T>` con nombre.
  - Descartado: `Action x = () => _ = new X(…);` (se lee como crear algo para tirarlo).
- por revisar: que xUnit v3 tenga la sobrecarga `Assert.Throws<T>(Func<object?>)` y la elija así (se comprobó solo que compila y pasa); si conviene escribir la regla para todas las pruebas de excepciones.
- bloqueada por: nada.
