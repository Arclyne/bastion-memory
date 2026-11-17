---
tipo: referencia
verificado: 2026-11-13 (carpetas de Bastion.Client en Arclyne/bastion@6dfb198; prototipos solo por lo que dice decisiones.tex; el juego no se abrió)
---
# Interfaz

## Fuentes
- Prototipos: `requisitos-bastion/Prototipos/` (125 pantallas; 57 ilustran una funcionalidad y 68 se descartaron, según `decisiones.tex`). No se abrieron.
- Estilo: 3D low-poly, peones básicos (D-001a). Modelos en Blender (D-002a). Sin skins (D-003a).

## Qué pantallas existen en el código
| Carpeta de `Bastion.Client/Screens` | Qué hay |
|---|---|
| `Login` | inicio de sesión con selector de idioma |
| `MainMenu` | menú, búsqueda de partida clasificatoria y diálogo de presencia |
| `MainMenu/Chat` | chat de lobby y conversaciones privadas |
| `MainMenu/Friends` | amigos, solicitudes, código de amigo |
| `Matches` y `Matches/Scene` | pantalla de enfrentamiento, partida con tablero 3D, muros, chat de partida y abandono |

No hay pantalla de salas, registro, perfil, ranking, historial ni reportes → `python3 herramientas/ver.py casos`.

## Cómo está hecha
- MonoGame DesktopGL con controles de Gum (SAD ADR-003); vistas con modelos de vista. Reglas de Gum: E-41. Propiedades de modelos de vista: E-26 y R-17.
- Solo `BastionGame`, `GumScreenHost` y `GumClipboard` tocan los globales de Gum; las pantallas heredan de `ScreenView` (journal de José, propuesta D1).
- Idiomas es-MX y en-US en `Strings.resx`; nombres de idioma fijos en `LanguageCatalog` (Q-02a sobre E-01).
- Manejadores de eventos se llaman `Handle…`; `On…` es el método que lanza un evento (journal de José).

## Lecciones
- Un cambio de interfaz con Gum se comprueba abriendo el juego: su documentación ya falló una vez (el selector de idioma necesitaba refrescar su lista y la documentación decía que no).
- Defectos anotados sin corregir: T-05a.
