---
tipo: guia-casos
verificado: 2026-11-17 (lista-casos.tex y decisiones.tex de requisitos-bastion@214f749)
---
# Casos de uso: cómo se usan las fichas

Los requisitos no se copian: viven en `Arclyne/requisitos-bastion` (LaTeX; `casos/CU-NN-*.tex`, `casos/deseables/DES-NN-*.tex`, `decisiones.tex`, `priorizacion.tex`, `trazabilidad.tex`). Cada caso del alcance tiene una ficha en `diseno/casos/` con su estado, el código que lo implementa y las decisiones que lo afectan. No hay tabla escrita a mano.

- Ver todos: `python3 herramientas/ver.py casos` · uno: `ver.py casos CU-09` · por estado o texto: `ver.py casos "sin código"`
- Cambia el código de un caso → se edita su ficha en ese momento.

## Formato de una ficha
- Encabezado: `tipo: caso`, `id`, `nombre`, `prioridad` (MoSCoW de `priorizacion.tex`), `categoria`, `estado`, `decisiones`, `verificado`.
- `estado`: `con código` (hay operación de servicio y dominio para el flujo normal), `parcial` (hay piezas pero falta la operación o la pantalla) o `sin código`. Ningún estado dice que el caso cumpla sus reglas de negocio.
- `decisiones`: las REQ D que mencionan el caso en `decisiones.tex` (sacadas por script) y las del vault.
- `## Código`: operaciones (`IServicio.Operación`), tipos o espacios de nombres que existen en [[mapa-codigo]]. El verificador falla si uno no existe o si una ficha `con código` o `parcial` no cita nada.
- `## Nota`: lo que falta o no se comprobó.
- El código que no pertenece a ningún caso se declara en [[sistemas]] (§ Código transversal). El verificador avisa de los tipos que nadie cita.

## Fuera del alcance
- 23 requisitos deseables, DES-01 a DES-23 (REQ D-25): IA rival, espectadores, tienda, cosméticos (D-003a), moderadores, tutorial y otros. No se construyen ni tienen ficha.
- Código sin caso de uso: chat de lobby y conversaciones privadas (Q-07a).

## Diferencias conocidas
- El SAD habla de 28 casos (Q-04a).
- Los casos nombran mensajes propios (`CHAT_SEND_REQUEST`) y tablas en español; el código usa operaciones de servicio y nombres en inglés (E-01) → [[protocolo]], [[modelo-datos]].
