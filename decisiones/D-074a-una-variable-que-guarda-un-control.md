---
tipo: decision
id: D-074a
fecha: 2026-11-18
autor: angel
estado: vigente
tema: estandar
reglas: E-02, E-32
---
# D-074a · Una variable que guarda un control termina con el nombre de su tipo
- sobre: 2.1.1, 2.14.3
- Angel decidió: una variable local, un campo o un parámetro que guarda un control de la interfaz termina con el nombre exacto de su tipo: `cancelButton`, `titleLabel`, `menuStackPanel`, `filterTextField`, `friendsTabButton`, `unreadCountBadge`. Si no hace falta más, el nombre es solo el tipo (`label`, `passwordField`).
- excepciones: las figuras de Gum que no son controles (`RectangleRuntime`, `TextRuntime`, `ContainerRuntime`) se nombran por lo que dibujan (`surface`, `background`). Una variable de tipo base que recibe varios controles (`FrameworkElement element`, `ButtonBase button`, `TextBoxBase field`) se queda con su nombre genérico.
- porqué: el sufijo deja ver qué pieza de la pantalla es sin buscar la declaración (la idea de 2.14.3, llevada a variables), y evita que el nombre de un botón se lea como acción ([[D-073a-un-parametro-o-variable-que-guarda|D-073a]]). El estándar solo lo muestra en un ejemplo (`playButton`, §3) y su propio `StackPanel` se llama `menu`; no es regla de la v2.4.
- descartado: sufijo corto por familia (`menuPanel`, `passwordField` para todo campo), porque obliga a mantener una lista de familias y a decidir cada control propio nuevo; sufijo solo para botones.
- dónde vive: solo en el vault; el texto del estándar (`estandar/texto/`) es copia literal del PDF v2.4 y no se edita. José no la ha visto. En el código, aplicada en `Bastion.Client` en la rama `review-parameter-naming`: los botones en el commit `9da39b8` y el resto de los controles (316 variables, campos y parámetros) en `3ecc23a`; PR Arclyne/bastion#30. Las pruebas no tenían variables de controles.
