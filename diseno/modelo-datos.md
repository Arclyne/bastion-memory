---
tipo: referencia
verificado: 2026-11-13 (decisiones.tex de requisitos-bastion@214f749; tablas de database/*.sql en Arclyne/bastion@6dfb198 leídas por script; los scripts no se ejecutaron)
---
# Modelo de datos

No se copia el modelo. Fuentes:
- análisis y diagramas: `requisitos-bastion` (`modelo/`, `er/`, `bd/`, `modelo-datos.tex`, `implementacion/`), con nombres en español;
- lo que existe: `database/01_create_database.sql` a `07_create_private_messages.sql` en el repositorio de código, con nombres en inglés (E-01). Tablas, columnas y procedimientos: sección «base de datos» de [[mapa-codigo]].

## Decisiones de los requisitos que fijan el modelo
REQ D-02 (el invitado es un Usuario), REQ D-03 (seis ranuras de cosméticos; fuera del alcance por D-003a), REQ D-04 (estadísticas por modo, 1:N), REQ D-05 (Sancion con ámbito en lugar de Baneo), REQ D-07 y REQ D-17 (borrado lógico y anonimización), REQ D-09 (catálogos precargados), REQ D-11 (una participación sin terminar por jugador), REQ D-22 (núcleo y fase posterior en dos scripts), REQ D-23 (un solo CodigoVerificacion), REQ D-24 y REQ D-27 (cola, plazas y expulsados en memoria).

## Reglas del equipo
- EF Core se ajusta a los scripts, sin migraciones (SAD ADR-005).
- Entidades de EF: R-01, R-19, R-20, R-31. Consultas: R-32, R-33. Largo de columnas desde una sola definición: E-47.

## Diferencias conocidas
- Los scripts conservan tablas de requisitos deseables (Mute, Block, Appeal, ModerationLog) y procedimientos para ellas (SAD R-09).
- Comentarios de los scripts contra E-67 (Q-03a).
- Sin comprobar: que cada tabla del núcleo de `bd/crear_tablas.sql` de los requisitos tenga su equivalente en `database/`.
