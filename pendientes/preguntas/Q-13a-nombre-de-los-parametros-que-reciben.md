---
tipo: pregunta
id: Q-13a
fecha: 2026-11-17
autor: angel
estado: abierta
grupo: estandar
---
# Q-13a · Nombre de los parámetros que reciben una excepción: ex o cause
E-69 (9.1.1) dice que toda variable de excepción que se usa **en el bloque catch** se llama `ex`. No dice cómo se llama un parámetro de método que recibe una excepción.
- **Lectura de José:** un parámetro no es un `catch`, así que puede llamarse `cause`. La aplicó en el PR #22 de `Arclyne/bastion` (rama `review-standard-v2.4-sections`), con 31 parámetros renombrados de `ex` a `cause` (por ejemplo, `ChannelCloser.LogAndAbort` y los `ToClientException` de Client.Networking). Las variables de `catch` siguen siendo `ex`. Su razonamiento solo está en el journal archivado (`archivo/journal-revision-v2.4.md`).
- **Lectura de Angel:** también se llama `ex`. El código correcto de la sección 11 del estándar (`estandar/texto/seccion-11-bitacoras.md`, ejemplo de niveles) declara `public void AbortSession(GameSession session, Exception ex)`, un parámetro que recibe la excepción para registrarla. Además, E-69 busca que el nombre sea predecible en todo el equipo, y con `cause` la misma excepción cambia de nombre al pasar del `catch` al método.
- No hay decisión registrada que justifique `cause` (`CLAUDE.md`: una desviación necesita decisión con `reglas: E-NN`).
- No bloquea: Angel hará merge del #22 y lo revisará después con José (2026-11-17). Si gana `ex`, se regresan esos parámetros en un PR aparte.
