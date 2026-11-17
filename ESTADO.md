---
tipo: estado
verificado: 2026-11-17 (fachadas por nombres de tipos; Arclyne/bastion@6dfb198 leído desde GitHub por estructura; requisitos y SAD por sus listas; no se compiló ni se abrió el juego)
---
# Estado

Bastión está en construcción: servidor y cliente en `Arclyne/bastion` (7 proyectos, 3 de pruebas), con partida clasificatoria de dos jugadores jugable de principio a fin según el journal de José. Entrega por incrementos semanales que el profesor audita.

Esta nota solo cambia cuando cambia lo que existe en el proyecto. Lo que se mueve cada sesión lo arma `python3 herramientas/ver.py inicio`.

## Existe (con código)
- Inicio de sesión con bloqueo por intentos y bitácora de accesos (CU-01), sin segundo factor.
- Emparejamiento clasificatorio con confirmación de presencia (CU-09).
- Partida: mover peón, colocar muro, abandonar; tablero 3D en el cliente (CU-13, CU-14, CU-17).
- Chat de partida, de lobby y privado, con filtro de palabras y sanciones de chat (CU-20, Q-07a).
- Amigos: buscar, solicitar, aceptar, rechazar, eliminar (CU-21, CU-22, CU-24).
- Idiomas es-MX y en-US.
- Estándar v2.4 y 65 decisiones de José sobre cómo aplicarlo.

## Fachada (existe pero no hace lo que aparenta)
- Pista de segundo factor en la pantalla de inicio de sesión (`LoginView`) y `Account.IsTwoFactorEnabled`, sin código de verificación detrás (CU-05).
- El rechazo por expulsión de una sala (`WaitingRoom.HasKicked`) existe, pero nadie puede expulsar (CU-12).
- `MatchStatus.PendingClose`, `MatchEndReason.Resignation` y `AccountType.Guest`: valores sin flujo que los use (CU-18, CU-16, CU-03).
- Datos de clasificación de demostración (`04_insert_leaderboard_demo.sql`) sin operación que los muestre (CU-25).

## A medias
- Salas privadas: servicio y cliente de red, sin pantalla (CU-10, CU-11). Expulsar sin operación (CU-12).
- Cierre de partida: `PendingClose` sin construir (CU-18). Ranking: solo la entidad (CU-25). Reportes: solo sanciones y tablas (CU-27).

## Falta (sin código)
CU-02, CU-03, CU-04, CU-05, CU-06, CU-07, CU-08, CU-15, CU-16, CU-19, CU-23, CU-26. Detalle: `python3 herramientas/ver.py casos`.

## Sin probar o sin saber
- Claude no compiló, no corrió las pruebas ni abrió el juego. Los estados salen de nombres de contratos y carpetas (T-06a).
- Si la revisión del código contra el estándar terminó (Q-08a).
- El mapa del código viene de `main` de GitHub, no de la copia local de nadie (T-03a).
- Rúbricas y fechas de los entregables: no están en el vault (Q-01a).
- La sincronización real entre dos computadoras: el vault aún no es un repositorio (T-01a).

## Contradicciones abiertas entre estándar, requisitos, SAD y código
Q-02a, Q-03a, Q-04a, Q-05a, Q-06a, Q-07a.

## Frases gatillo
| La persona dice | Claude hace |
|---|---|
| "cierra sesión" | protocolo de cierre de `CLAUDE.md` |

## Avisos
- El journal completo de la revisión de José está en `archivo/` (copia del 2026-11-11).
