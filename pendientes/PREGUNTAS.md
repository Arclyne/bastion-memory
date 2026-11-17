---
tipo: guia-registros
verificado: 2026-11-13
---
# Preguntas abiertas

Cada pregunta es un archivo en `pendientes/preguntas/`. Solo existe mientras está abierta.

- Ver todas: `python3 herramientas/ver.py preguntas` · una: `ver.py preguntas Q-03a` · por texto o grupo: `ver.py preguntas hallazgos`
- Crear: `python3 herramientas/nuevo.py pregunta "Título corto" --grupo estandar`. En el cuerpo: qué hay que decidir, qué se sabe y qué bloquea.
- Grupos en uso: `hallazgos` (contradicción entre estándar, requisitos, SAD y código que alguien debe resolver), `estandar` (una regla admite dos lecturas), `proyecto`.
- Resolver: crear la decisión que la responde y borrar el archivo de la pregunta. El verificador avisa de toda nota que la siga citando.
- Una regla del estándar ambigua nunca se resuelve por cuenta de Claude: se abre una pregunta del grupo `estandar`.
