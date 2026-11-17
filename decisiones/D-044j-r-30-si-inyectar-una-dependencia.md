---
tipo: decision
id: D-044j
fecha: 2026-11-10
autor: jose
estado: vigente
tema: estandar
origen: journal R-30
reglas: E-07, E-81
---
# D-044j · R-30 · Si inyectar una dependencia lleva un constructor a más de tres parámetros, las…
- sobre: 2.2.2 con 10.1.1
- Jose decidió: Si inyectar una dependencia lleva un constructor a más de tres parámetros, las dependencias que van juntas se agrupan en un record (como `PrivateChatChannel`), que la raíz de composición registra para que el contenedor lo arme por su constructor.
