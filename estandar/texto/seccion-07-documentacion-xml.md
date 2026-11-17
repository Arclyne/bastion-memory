---
tipo: estandar-texto
seccion: 7
verificado: 2026-11-13 (copia literal de pdftotext del PDF v2.4; ver [[estandar-v2.4]])
---
# 7. Documentación XML

```text
7.     Documentación XML
   Los comentarios de documentación XML se escriben íntegramente en inglés y son obligatorios
únicamente en los servicios. Un servicio es toda interfaz pública cuyo nombre termina en Service,

                                                 46
junto con la clase que la implementa, en cualquier proyecto de la solución. Un contrato de red (por
ejemplo, una interfaz marcada con [ServiceContract]) es un servicio. Ningún otro tipo agrega
documentación XML. El código generado por una herramienta, como Strings.Designer.cs,
queda fuera de esta sección. Para respetar la política de ejemplos sin comentarios, esta sección
ilustra las reglas mediante descripciones textuales fuera de los bloques de código.

7.1.     A Nivel de Tipo
7.1.1.    Regla: etiqueta summary en la interfaz del servicio
    Regla: La interfaz pública de un servicio lleva una etiqueta <summary> en inglés que describe
su responsabilidad. Prohibido agregar documentación XML a tipos que no son servicios: dominio,
infraestructura, interfaz gráfica o pruebas (Microsoft, 2026c).
    Ejemplo correcto: ISaveGameService incluye un summary en inglés que indica: “Saves and
restores game sessions.”
    Ejemplo incorrecto: ISaveGameService carece de summary, o lo redacta en español. También
es incorrecto documentar la entidad Player o la vista BoardView.

7.1.2.    Regla: inheritdoc en la implementación
    Regla: La clase que implementa la interfaz de un servicio no repite la documentación:
coloca <inheritdoc/> sobre la clase y sobre cada miembro que implementa la interfaz. Así la
documentación vive en un solo lugar y quien programa contra la interfaz la ve sin abrir la clase
(Microsoft, 2026c).
    Ejemplo correcto: SaveGameService lleva <inheritdoc/> sobre la clase y sobre Save; el
texto se hereda de ISaveGameService.
    Ejemplo incorrecto: SaveGameService copia el summary de la interfaz, o redacta uno
distinto, o no lleva documentación.

7.2.     A Nivel de Miembro
7.2.1.    Regla: orden de las etiquetas param, returns y exception
    Regla: Cada miembro de la interfaz de un servicio se documenta en inglés con las etiquetas
en este orden: <summary>, una etiqueta <param> por cada parámetro, <returns> si devuelve un
valor y <exception> por cada excepción documentada. Las propiedades llevan <summary>; los
constructores no se documentan, porque no forman parte de la interfaz (Microsoft, 2026c).
    Ejemplo correcto: CalculateFinalScore documenta primero su propósito; después describe
baseScore y tile; luego el valor devuelto; y finalmente ArgumentOutOfRangeException. Todo
el contenido está en inglés.
    Ejemplo incorrecto: El método coloca returns antes de param, omite parámetros o combina
descripciones en español con identificadores en inglés.

7.2.2.    Regla: qué excepciones se documentan
    Regla: Se documenta con <exception> toda excepción que el método deja salir hacia
quien lo llama, incluidos los fallos de red que el servicio envía al cliente (por ejemplo,
FaultException<TDetail>). No se documentan las excepciones que el propio método captura y
maneja.
    Ejemplo correcto: IAccountService.LogIn documenta FaultException<InvalidCredentialsFault>
y FaultException<AccountRestrictedFault>.
    Ejemplo incorrecto: IAccountService.LogIn documenta DbUpdateException, que el ser-
vicio captura y nunca llega al cliente.



                                                47
7.3.     Verificación
7.3.1.    Regla: el compilador exige la documentación de los servicios
    Regla: Todo proyecto que contiene un servicio activa GenerateDocumentationFile en su
.csproj. En esos proyectos, el aviso CS1591 (miembro público sin documentación) se suprime en
los tipos que no son servicios y se trata como error en los servicios, de modo que la compilación
falla si falta un summary (Microsoft, 2026c).
    Ejemplo correcto: Bastion.Server.Application.csproj declara <GenerateDocumentationFile>true</G
y la compilación falla si ILoginService pierde su documentación.
    Ejemplo incorrecto: Directory.Build.props declara GenerateDocumentationFile en
false para toda la solución, por lo que la falta de documentación solo se detecta en revisión.
```
