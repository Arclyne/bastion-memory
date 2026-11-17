---
tipo: tarea
id: T-04a
fecha: 2026-11-13
autor: angel
estado: pendiente
grupo: estandar
---
# T-04a · Actualizar la numeración que cita .editorconfig
- hecho cuando: los comentarios de `.editorconfig` citan las reglas de la v2.4. Hoy dice «3.4.1 At most 120 characters per line», y en la v2.4 la 3.4.1 es `var` (E-38) y la 3.5.1 dice que no hay largo máximo (E-39). Comprobado en el commit `6dfb198`.
- abierto: `max_line_length = 120` sigue activo; decidir si se quita.
