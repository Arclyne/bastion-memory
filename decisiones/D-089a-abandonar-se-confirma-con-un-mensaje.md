---
tipo: decision
id: D-089a
fecha: 2026-11-19
autor: angel
estado: vigente
tema: interfaz
---
# D-089a · Abandonar se confirma con un mensaje, sin escribir una palabra
- Angel decidió (2026-11-19): antes de abandonar sale un diálogo de confirmación con el aviso de que cuenta como derrota, el elo que se perdería (si es clasificatoria) y los botones «Volver a la partida» y «Abandonar». No se pide escribir ninguna palabra: «basta con el mensaje de confirmación».
- porqué: Angel lo prefirió así. Se aparta de la regla RN-02 del caso Abandonar la partida de los requisitos (`requisitos-bastion/casos/CU-18-abandonar-partida.tex`), que pedía escribir una palabra de confirmación; los requisitos no decían cuál.
- Claude eligió (sin aprobar): el elo que se perdería lo calcula el servidor con una consulta que no escribe nada, igual que la vista previa de la rendición (regla RN-02 del caso Rendirse); el foco empieza en «Volver a la partida» y Esc vuelve; si el cálculo tarda, «Abandonar» funciona igual, y si falla, el diálogo no inventa una cifra.
- descartado: escribir «ABANDONAR»; calcular el elo en el cliente.
- dónde vive: tarjetas f04 y f05 de la página «08 · Partida» del canvas (versión 33). Código en la rama `match-closure` de `Arclyne/bastion`, sin commit: `IMatchService.PreviewAbandonment`, `Match.PreviewAbandonment` y `AbandonConfirmDialogView`; probado en el juego el 2026-11-19 (partida 6006: el diálogo avisó −11 y el cierre aplicó −11). Falta corregir la regla RN-02 en `requisitos-bastion`. José no lo ha visto.
