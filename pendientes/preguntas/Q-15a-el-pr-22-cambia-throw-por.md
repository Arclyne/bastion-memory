---
tipo: pregunta
id: Q-15a
fecha: 2026-11-17
autor: angel
estado: abierta
grupo: estandar
---
# Q-15a · El PR 22 cambia ?? throw por un if en las validaciones del Host
E-76 (9.4.2) obliga a usar `??` cuando una expresión puede ser null y hay un valor alternativo válido. Prohíbe un `if` o un `?:` que solo elige entre la expresión y su alternativa. Si no hay alternativa válida, el null se trata como error (9.3.2).
- D-042j (José, R-28) admite `return x ?? throw new X();` si lo de la izquierda es una variable o una sola llamada.
- El PR #22 de `Arclyne/bastion` (rama `review-standard-v2.4-sections`) cambió `?? throw` por un `if` en las validaciones del Host. Por ejemplo, `ChatTranslator.RequireText`:
  - antes: `return text ?? throw ToFault(new ChatMessageRejectedException(ChatRejection.InvalidMessage));`
  - ahora: `if (text is null) { var missingText = new ChatMessageRejectedException(...); throw ToFault(missingText); } return text;`
  - Probablemente porque su otra regla pide crear cada objeto en su propia variable antes de pasarlo a una llamada.
- **Dos lecturas:** (a) lanzar una excepción no es una "alternativa", así que el `if` está permitido y el cambio es válido; (b) D-042j ya admite el `?? throw`, y la 9.4.2 prohíbe el `if` cuando basta un `??`, así que el cambio va contra el estándar y contra la propia decisión de José.
- Hay que decidir qué forma se usa cuando el lado derecho del `??` crea un objeto, y actualizar o reemplazar D-042j.
- No bloquea: Angel hará merge del #22 y lo revisará después con José (2026-11-17).
