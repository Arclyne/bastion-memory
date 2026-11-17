# Journal de la revisión con el Estándar v2.4

Bitácora viva de la revisión archivo por archivo del repositorio `bastion/` contra el **Estándar de Codificación
v2.4**. Guarda los hallazgos, el contexto y las decisiones del usuario para que la revisión siga igual en cualquier
sesión. **Antes de revisar un archivo, leer este journal completo.**

- Estándar: `Tecnologia/estandar v2.4/Estandar v2.4.pdf` (rama `estandar-v2.4`, PR #21 del repositorio del estándar).
  Texto completo en `estandar-v2.4.txt` y una línea por regla en `reglas-v2.4.md`, ambos en esta carpeta.
- Código: rama de trabajo `review-standard-v2.4` en `bastion/`, creada desde `main` `8b4d4ee` (ya con el PR #14,
  sin comentarios `//`).
- Inicio: 2026-11-10.

## Estado de la entrega (2026-11-10)

- **Push y PR por petición del usuario:** la rama `review-standard-v2.4` (30 commits, `8b4d4ee..12b9ebe`) está en GitHub y
  el **PR #15** (https://github.com/Arclyne/bastion/pull/15) quedó abierto contra `main`. El cuerpo está en inglés, con
  secciones Summary, Domain, Application, Adapters, Database, Build configuration, Not changed yet y Verification,
  sin atribución ni mención de IA. Autor de los commits y del PR: la cuenta del usuario (`poijn23`).
- **Cómo se abrió:** esta máquina no tiene `gh` y la sesión no tiene conector de GitHub. Con autorización expresa del
  usuario, se usó el token de Git Credential Manager (`git credential fill`) solo en el encabezado de la llamada a
  `api.github.com`; no se imprimió ni se guardó.
- El repositorio no tiene CI (`.github/workflows`); GitHub marcó el PR como `mergeable: clean`.
- La revisión **sigue**: faltan los almacenes y repositorios de Adapters, Host, Contracts, Client.Networking, Client y
  las pruebas. Los cambios nuevos irán en commits sobre la misma rama (el PR se actualiza solo) o en otro PR, según
  decida el usuario.

## Decisiones de método

| Id | Fecha | Decisión |
| --- | --- | --- |
| D-01 | 2026-11-10 | Se revisa archivo por archivo, nunca el proyecto entero de una vez. |
| D-02 | 2026-11-10 | Orden por capas, de adentro hacia afuera: Domain → Server.Application → Server.Adapters → Server.Host → Contracts → Client.Networking → Client; al final las pruebas de cada proyecto. |
| D-03 | 2026-11-10 | Los hallazgos se registran aquí; las decisiones las toma el usuario; al aprobarlas se corrige ese archivo en la rama de trabajo, con compilación y pruebas. Nada se sube sin que el usuario lo pida. |
| D-04 | 2026-11-10 | Una pausa al terminar cada archivo, con todas sus dudas juntas. No se supone nada: toda duda va al usuario. |
| D-05 | 2026-11-10 | El journal vive en `context/revision-v2.4/`, fuera del repositorio. |
| D-07 | 2026-11-10 | Un commit local por archivo revisado, con su identidad y sin rastro de IA, en `review-standard-v2.4`. **El push se hace solo al final de toda la revisión.** Las decisiones de los archivos anteriores (tabla «Decisiones de reglas») se aplican sin volver a preguntar en los siguientes. |
| D-06 | 2026-11-10 | **La prioridad es la facilidad de lectura.** Un `return` se lee de un vistazo: si la expresión hace más de un paso (restar, convertir, redondear), cada paso va en una variable con nombre antes del `return`. Se evita repetir código, pero sin repartir lo que describe una misma cosa en varios lugares (por ejemplo, los valores iniciales de una clase no se dividen entre declaraciones y constructores). Toda propuesta se juzga primero por cómo se lee. |

## Cómo se revisa cada archivo

Cuatro pasadas, siempre en este orden:

1. **Reglas del estándar**, en etapas; cada etapa es una sección completa del estándar y se comprueba regla por
   regla (91 reglas en total):
   - §1 Idioma: 1.3.1.
   - §2 Nombrado: 2.1 variables, 2.2 métodos, 2.3 constantes, 2.4 clases, 2.5 interfaces, 2.6 campos privados,
     2.7 descartes, 2.8 class/struct/record, 2.9 identidad, 2.10 literales, 2.11 propiedades, 2.12 eventos,
     2.13 genéricos, 2.14 sufijos, 2.15 enumeraciones (33 reglas).
   - §3 Estilo: 3.1 indentación, 3.2 espaciado, 3.3 llaves Allman, 3.4 `var`, 3.5 división de líneas,
     3.6 atributos, 3.7 controles de Gum (7 reglas).
   - §4 Complejidad: anidamiento, guardas, llaves, `switch`/`default`, DRY, `?:`, complejidad ciclomática, patrón
     `is` (9 reglas).
   - §5 Funcional: lambdas de una línea, contextos prohibidos de lambda, grupo de método, LINQ a objetos (4 reglas).
   - §6 Estructura de archivos: un tipo por archivo, orden de miembros, `using`, espacio de nombres (4 reglas).
   - §7 Documentación XML (5 reglas). §8 Comentarios (5 reglas). §9 Excepciones (12 reglas).
     §10 Inyección (4 reglas). §11 Bitácoras (3 reglas). §12 Pruebas (4 reglas).
   - Una sección que no aplica al archivo se anota como «no aplica» con el porqué.
2. **Repetición**: datos o lógica repetidos dentro del archivo o con archivos ya revisados. Si conviene moverlos a
   una clase reutilizable, se anota en «Candidatos a reutilizar» y se pregunta.
3. **Nombres ambiguos para alguien ajeno a la aplicación**: tipo, miembros, parámetros y variables. Un nombre es
   ambiguo si al leerlo sin el contexto de la clase no se sabe qué es o qué hace, o si se confunde con otro.
4. **Necesidad**: cada miembro debe usarse en algún lugar de la solución. Lo que no se usa se reporta con la
   búsqueda que lo comprueba.

## Lecturas abiertas del estándar

Interpretaciones que el estándar no fija y que se preguntan al usuario la primera vez que aparecen en un archivo.
La respuesta pasa a la tabla de decisiones de reglas.

| Id | Regla | Duda |
| --- | --- | --- |
| L-01 | 3.4.1 | IDE0007 toma `ToList()`/`ToX()` como tipo evidente y pide `var`; la letra de la 3.4.1 pide el tipo explícito. |
| L-02 | 2.2.2, 9.4.1 | ¿El constructor primario de un record posicional cuenta para el límite de tres parámetros y para `ThrowIfNull`? |
| L-03 | 2.9.1 | ¿Toda entidad debe redefinir `Equals` con su clave de negocio? |
| L-04 | 2.11.4 | ¿Una navegación de EF Core con `=>` entra en la excepción de framework? |
| L-05 | 1.3.1 | Recursos y mallas de los modelos 3D en español (vienen de `requisitos-bastion/modelos-3d`). |
| L-06 | 12.2.1 | ¿Una prueba puede nombrarse por el evento que dispara un manejador privado? |
| L-07 | 12.3.2 | Ayudantes de prueba que esconden un `Assert`. |
| L-08 | 10.3.1 | `GetRequiredService` en un singleton que no crea CoreWCF. |
| L-09 | Pasada 4 | ¿Un miembro que solo usan las pruebas cuenta como usado? |
| L-17 | R-04, 9.4.2 | ¿`return llamada() ?? throw new X();` cuenta como «una sola llamada» con su alternativa, o va `if (x is null) throw …; return x;`? |
| L-16 | 2.11.4 | ¿Una propiedad que solo expone un campo como solo lectura (`Members => _members`) fuera de EF va con bloque `get`, como método o se queda con `=>`? |
| L-15 | R-05 | ¿Una condición que mezcla `&&` y `||` con paréntesis sigue siendo «corta» para devolverla en el `return`? |
| L-14 | R-04 | ¿La R-04 (un paso por línea: casts, aritmética y llamadas en variables) vale también para las asignaciones, o solo para los `return`? |
| L-13 | R-04, R-12 | ¿Un `return` con una sola llamada LINQ y una lambda de una línea (`FirstOrDefault(x => …)`) cuenta como «una sola llamada», o va en una variable como las cadenas? |
| L-12 | 2.8.1, R-01 | ¿Una entidad de EF inmutable (catálogo de solo lectura) se declara `record`, como pide la 2.8.1 para los valores inmutables, aunque un record redefina `Equals`? |
| L-11 | 9.4.1, R-11 | ¿Un record posicional sin parámetros de referencia (nada que comprobar) también pasa a constructor explícito? |
| L-10 | 2.6.3 | La regla dice «campo»: ¿también obliga a inicializar en su declaración las propiedades autoimplementadas cuyo valor no depende del constructor? |

## Decisiones de reglas

| Id | Fecha | Regla | Decisión |
| --- | --- | --- | --- |
| R-01 | 2026-11-10 | 2.9.1 (L-03) | Las entidades que persiste EF Core **no** redefinen `Equals`: EF ya las identifica por su clave. Se anota como interpretación de la 2.9.1. |
| R-02 | 2026-11-10 | 2.1.2 | Un `byte[]` que representa un solo valor binario (hash, sal) **no** es una colección: va en singular. |
| R-04 | 2026-11-10 | D-06, todos los `return` | Un `return` devuelve una variable, un literal o una sola llamada con argumentos simples. Los casts, la aritmética y las llamadas anidadas van antes, en variables con nombre, un paso por línea. |
| R-05 | 2026-11-10 | R-04, condiciones | Un `return` puede devolver directamente una condición corta (comparación, `&&`, `is not null`): se lee como una pregunta. Ejemplo: `return PasswordHash is not null && PasswordSalt is not null;`. |
| R-06 | 2026-11-10 | 4.4.1 y CS8629 | Cuando dos métodos necesitan la misma condición sobre un valor que puede faltar, se usa el patrón Try: un privado `TryGetX(…, out T x)` que devuelve `bool` y entrega el valor; los demás lo llaman (con `out _` si solo importa el `bool`). Sin atributos de nulabilidad ni `.Value`. |
| R-07 | 2026-11-10 | 2.4.1 | Las clases `*Rules` del dominio pasan a singular con el sufijo `Policy`, como `LockoutPolicy`: `AccountPolicy`, `ChatPolicy`, `FriendCodePolicy`, `FriendshipPolicy`, `MatchmakingPolicy`, `RoomPolicy`. Cada una se renombra al revisar su archivo. |
| R-08 | 2026-11-10 | 4.4.2 | Las expresiones regulares del dominio se crean con una clase compartida (`TextPattern.Create`) que fija `CultureInvariant` y el tiempo límite en un solo lugar. |
| R-09 | 2026-11-10 | 2.2.2 (L-02) | El constructor primario de un record posicional **cuenta** para el límite de 3 parámetros. Un record con más campos se agrupa en otro record o pasa a propiedades `init` con inicializador de objeto. |
| R-10 | 2026-11-10 | Vocabulario | El inicio de sesión se nombra **Login/LogIn** en todo el proyecto. Los nombres con «SignIn» se renombran: los de `Account`, `AccountPolicy` y `LockoutPolicy` en un commit aparte (2026-11-10); `SignedInPlayer`, `SignedInSession` y `ToSignedInSession` al revisar sus archivos. |
| R-11 | 2026-11-10 | 9.4.1 (L-02) | Los records posicionales pasan a un **constructor explícito** con `ArgumentNullException.ThrowIfNull` para cada parámetro de referencia no anulable, y propiedades `{ get; }`. Solo los records que se copian con `with` llevan `{ get; init; }`. Cada record se cambia al revisar su archivo. |
| R-12 | 2026-11-10 | R-04 y 5.3.1, LINQ | Una cadena LINQ que termina en un solo valor (`Any`, `Count`, `First`, `Sum`…) se guarda, un operador por línea, en una variable con nombre, y el `return` devuelve esa variable. Las lambdas de una línea se quedan en la cadena. Las cadenas que devuelven una secuencia siguen la 5.3.1 (`IEnumerable<T>` y `new List<T>(…)` aparte). |
| R-13 | 2026-11-10 | 2.2.1 | La convención `To<Tipo>`/`From<Tipo>` es solo para convertir a **otro tipo**. Un método que transforma un valor sin cambiar su tipo (de `string` a `string`) empieza con un verbo, como `NormalizeWords`. |
| R-14 | 2026-11-10 | R-04, creación | `return new X(…)` y `return new X { … }` cuentan como una sola llamada si cada argumento o asignación es una variable, una constante, una propiedad o un literal. Si alguno lleva una llamada (incluido otro `new`), una operación o un cast, va antes en una variable. |
| R-15 | 2026-11-10 | Pasada 4 (L-09) | `Message.MarkRead`: un miembro que solo usan las pruebas se queda cuando expresa una regla del dominio que producción aplica por otra vía (SQL) y el doble de pruebas la necesita. Las demás apariciones de la L-09 se siguen preguntando. |
| R-16 | 2026-11-10 | R-11 (L-11) | Un record posicional **sin** parámetros de referencia (solo tipos por valor y enumeraciones) se queda posicional: la 9.4.1 no tiene nada que comprobar. La R-11 aplica solo cuando hay al menos un parámetro de referencia no anulable. |
| R-17 | 2026-11-10 | 2.11.4 | En el dominio y el servidor, un valor calculado a partir de otros miembros es un método `GetX()` (`FriendRequest.GetExpirationTime()`), no una propiedad con `=>` ni con bloque `get`. Las propiedades calculadas de los modelos de vista (Gum enlaza propiedades) y los `DbSet` se preguntan en su capa. |
| R-18 | 2026-11-10 | 4.4.1 | La guarda «el mismo jugador en los dos lados» se queda en cada entidad (`FriendRequest`, `Friendship`, `Message`) con su propio texto de dominio; no se comparte ni se cambia por `ThrowIfEqual`. |
| R-19 | 2026-11-10 | 2.8.1 (L-12) | Las entidades de EF son `class` aunque sean inmutables (catálogos como `GameMode`): EF las identifica por su clave (R-01), y la igualdad por valor de un `record` no aplica a una fila. La regla de `record` para valores inmutables vale para lo que no es entidad de EF. |
| R-20 | 2026-11-10 | 2.11.4 (L-04) | Una navegación de EF que expone un campo de respaldo (`Participations => _participations`, con `UsePropertyAccessMode.Field`) puede usar `=>`: se anota como excepción de EF. No cubre los valores calculados (R-17). Los `DbSet` de `BastionDbContext` se preguntan en su revisión. |
| R-21 | 2026-11-10 | R-04, R-12 (L-13) | Un `return` con **un solo** operador LINQ y una lambda de una línea (`FirstOrDefault(x => …)`, `Count(x => …)`) cuenta como una sola llamada, como en el ejemplo correcto de la 2.11.4. La R-12 aplica a cadenas de dos o más operadores. |
| R-22 | 2026-11-10 | Pasada 3 | Un método que hace una acción no devuelve un `bool` que no dice su nombre (`Abandon` devolvía «terminó la partida»). Pasa a `void` y quien llama pregunta por el estado. |
| R-23 | 2026-11-10 | R-04 (L-14) | Un cast no se combina en la misma línea con una llamada o una operación, en ningún lugar (asignaciones y argumentos incluidos): `TimeSpan clockTime = …; double clockMilliseconds = clockTime.TotalMilliseconds; RemainingClockMilliseconds = (int)clockMilliseconds;`. Las demás asignaciones de varios pasos se dejan; la R-04 completa sigue siendo para los `return`. |
| R-24 | 2026-11-10 | R-05 (L-15) | Una condición que mezcla `&&` y `||` (con paréntesis) no es corta: se separa en guardas, una pregunta por `if`, y el último `return` devuelve la comparación que queda. Las condiciones solo con `&&` siguen la R-05. |
| R-25 | 2026-11-10 | Pasada 4 | Una constante o un método públicos que solo usa su propia clase (ni otro código ni las pruebas; buscar en `src` **y** `tests`) pasan a `private` (`MatchmakingPolicy`, `RoomPolicy.FailedCodeWindowMinutes`, `WaitingRoom.HasMember`). Los límites que forman una pareja de una regla (mínimo y máximo) se quedan públicos juntos. |
| R-26 | 2026-11-10 | 2.11.4 (L-16) | Una propiedad que solo expone un campo como solo lectura (`Members => _members`) puede usar `=>`, dentro y fuera de EF (amplía la R-20). Los valores calculados siguen la R-17. |
| R-27 | 2026-11-10 | 7.1–7.3 | Cada interfaz `I…Service` se documenta (summary, param, returns, exception) al revisar su archivo, y su implementación lleva `<inheritdoc/>`. `GenerateDocumentationFile` y CS1591 como error en `I*Service.cs` (apagado en lo demás) se activan al **terminar cada capa** que tenga servicios: Application, Contracts y Client. |
| R-28 | 2026-11-10 | R-04, 9.4.2 (L-17) | `return x ?? throw new X();` se admite si lo de la izquierda es una variable o una sola llamada: es la llamada y su alternativa en una expresión (9.4.2). |
| R-29 | 2026-11-10 | 3.4.1 (L-01) | En LINQ a objetos, un diccionario o un conjunto que se arma desde una lista se crea con `var x = new Dictionary<K, V>(fuente.Count);` (o `new HashSet<T>(…)`) y se llena con un `foreach`, en lugar de `ToDictionary`/`ToHashSet`. Así el `var` cumple la 3.4.1 (caso `new`) y el compilador no avisa (IDE0007). Las consultas de EF sobre `IQueryable` se ven en su revisión. |
| R-30 | 2026-11-10 | 2.2.2 con 10.1.1 | Si inyectar una dependencia lleva un constructor a más de tres parámetros, las dependencias que van juntas se agrupan en un record (como `PrivateChatChannel`), que la raíz de composición registra para que el contenedor lo arme por su constructor. |
| R-31 | 2026-11-10 | 2.11.4 | Los `DbSet<T> X => Set<T>();` del `DbContext` se quedan con `=>`, como patrón de EF con nulos activados (amplía la R-20). |
| R-32 | 2026-11-10 | R-04, 5.3.1 (L-18) | Una consulta de EF sigue la forma de la 5.3.1: va en un `IQueryable<T>` con nombre en plural y se materializa con `new List<T>(consulta)` (o `new Dictionary<K, V>(consulta)` sobre `KeyValuePair<K, V>`). Las de valor único devuelven `consulta.FirstOrDefault()` (o `Any()`), o lo guardan en una variable si lo usan después. Un método privado que arma una consulta la guarda en una variable y la devuelve, o devuelve una sola llamada (`a.Concat(b)`). |
| R-33 | 2026-11-10 | 5.1.1, 5.1.2 (L-19) | Las consultas de EF se parten en pasos simples: un `.Where` por condición `&&`; los dos sentidos de una pareja con `Concat` o con dos búsquedas unidas con `??`; `GroupBy(clave, elemento)` en lugar de una lambda anidada; el selector de `SetProperty` en un campo `Expression<…>`; y las proyecciones anidadas se arman en memoria con un método usado como grupo de método. |
| R-34 | 2026-11-10 | 4.4.1, 10.1.1 | Un mapeo que se repite de una entidad a un tipo de `Application` es una fábrica estática en ese tipo (`PlayerIdentity.FromAccount`), que es la capa más interna que conoce los dos. No se inyecta ni va en un ensamblado propio mientras sea una función pura; se inyectaría si llegara a necesitar un servicio externo (10.1.1). |
| R-36 | 2026-11-10 | 4.4.1 | Los errores de EF (`DbUpdateException`, `DbException`) se traducen en un solo lugar, `DatabaseFailureTranslator<TFailure>`, que recibe cómo crear la excepción de quien lo usa. Los repositorios que abren un contexto por operación usan `NewContextRunner<TFailure>`, que a su vez usa el traductor. `UnitOfWork` puede usar el traductor (211). |
| R-37 | 2026-11-10 | 9.2.1 | El contexto de EF usa `NonRetryingExecutionStrategy`. La estrategia por defecto de SQL Server envuelve los errores transitorios en `InvalidOperationException`, que escapa de la traducción. Si algún día se activan reintentos, hay que traducir también `RetryLimitExceededException`. |
| R-38 | 2026-11-10 | 9.2.1 | Se traduce un error de la base a una excepción de `Application` solo donde un componente de adentro reacciona a ella (`MatchRepositoryException`, `RoomRepositoryException`). La unidad de trabajo no traduce: sus fallas suben hasta `Host`, que es el borde y atrapa `DbException`/`DbUpdateException`. `DatabaseFailureTranslator` queda aparte para cuando haga falta en otro lugar. |
| R-39 | 2026-11-10 | 8.1.1 | **Sin comentarios en el código**, ni siquiera los `//` de "por qué" que admite la 8.1.1. El porqué se lee en los nombres: un método extraído que diga la garantía, una variable explicativa o un nombre que revele la intención. La documentación XML de las interfaces de servicio (§7) se queda. |
| R-40 | 2026-11-10 | 9.4.1 (L-20) | En una operación de servicio WCF, el argumento que llega por la red se comprueba al inicio, pero un nulo no lanza `ArgumentNullException`: lanza la falla tipada que corresponde (`InvalidCredentialsFault`, sesión inválida, el rechazo del caso). Así el cliente sabe qué pasó y el canal con sesión no se daña. En los constructores y en las demás clases sigue `ThrowIfNull`. |
| R-41 | 2026-11-10 | R-10, textos | La R-10 también vale para los textos del programa: bitácora, mensajes de excepción y razones de falla dicen "login"/"log in", no "sign-in". Los textos de la interfaz (`Strings.resx`) siguen con "Sign in". También vale para la documentación XML: "logged-in player", no "signed-in" (decidido en `Matches` de `Contracts`, 2026-11-11; `IMatchmakingService` e `ISessionService` se cambian al revisar su carpeta). |
| R-42 | 2026-11-10 | 5.3.1, R-14 | Un arreglo de contrato se arma con `ContractArray.ConvertAll(origen, convertidor)` (en `Host/Common`), en una variable antes del `return`, no con `Select(…).ToArray()`. |
| R-43 | 2026-11-10 | 4.4.1, R-14 | Una falla tipada se crea con `FaultExceptionFactory.Create(detalle, rechazo)`, que usa el mensaje del rechazo como razón. El detalle va antes en una variable. |
| R-44 | 2026-11-11 | R-04, R-14 (L-21) | Una operación de servicio WCF deja su llamada en una variable `Func<…>` hacia un método privado `…InRequestScope` (abre el ámbito, pide el servicio, llama y traduce el resultado) y devuelve `Translate…Failures(nameof(…), variable)`, un método privado por servicio que solo convierte excepciones en fallas. Nada de `Run`. |
| R-45 | 2026-11-11 | 4.4.1, R-44 | Una operación `void` pasa por la R-44 con una segunda sobrecarga `Translate…Failures(string, Action)` que la convierte en `Func<bool>` con un privado `CompleteOperation` (llama y devuelve `true`). Los `catch` quedan una sola vez, en la sobrecarga con `Func<TResult>`. Vale para los servicios que tienen operaciones `void` y operaciones con resultado. Un servicio con solo operaciones `void` tiene un único `Translate…Failures(…, Action)` con los `catch`, sin la sobrecarga `Func` ni `CompleteOperation` (precisado en `MatchService`, 2026-11-11). |
| R-46 | 2026-11-11 | 10.3.1 (L-08) | La excepción de la 10.3.1 también vale para un singleton que necesita un servicio `Scoped` en cada operación (`FriendPresenceReporter`): recibe `IServiceScopeFactory` y abre un ámbito por operación, como el patrón de Microsoft para consumir un servicio con ámbito desde un singleton. Fuera de WCF el envoltorio no traduce: registra y sigue (`LogPresenceFailures`), con un `…InOwnScope` por operación. |
| R-47 | 2026-11-11 | 6.2 | Los métodos privados van en el orden de los públicos que los usan (decidido en `RoomRepository` y en `FriendshipTranslator`). Los privados que se llaman en cadena van juntos y de arriba abajo, cada uno debajo del que lo llama, aunque un público anterior use un eslabón de en medio; un privado suelto que usan casi todos (`GetUtcNow`) va al final (precisado en `NotificationChannelRegistry`, 2026-11-11). |
| R-48 | 2026-11-11 | Pasada 3 | Un traductor no sobrecarga `ToNotification`: cada método dice qué notificación arma (`ToMatchFoundNotification`, `ToSearchEndedNotification`). Aplica a `PrivateChatTranslator.ToNotification` al revisarlo. |
| R-49 | 2026-11-11 | 10.1.1 | Una clase de `Application` que hace E/S por sus colaboradores o usa estado compartido se recibe por una interfaz, aunque sea interna (`IMatchmakingDispatcher`). También vale en `Host` (decidido en `Sessions`): `INotificationChannelRegistry` (el evento `PlayerDisconnected` y `RegisterChannel`) e `IFriendPresenceReporter`, junto a su clase; el registro concreto se queda en el contenedor solo para resolver los puertos. |
| R-56 | 2026-11-11 | 4.4.1 | Una guarda de argumento de red que se repite igual en varios servicios WCF es un método público estático del traductor que crea su falla: `SessionTranslator.RequireSessionToken` y `ChatTranslator.RequireText`. Las guardas propias de un servicio (`RequireFriendCode`) siguen privadas. `GetUtcNow` se queda en cada clase y el ámbito sigue la R-44. |
| R-50 | 2026-11-11 | R-44, 4.4.1, 11.1.1 | Una operación `IsOneWay` no traduce: su falla no llega al cliente, y si se escapa, CoreWCF no la registra (comprobado en `oneway-experiment`). Guarda su `…InRequestScope` en una variable `Action<string>` y llama `Log…OneWayFailures(nameof(…), sessionToken, operación)`. Ese envoltorio tiene la guarda del token nulo (Warn) y los `catch` de tipos conocidos, que registran sin relanzar. Aplica a `RoomService.LeaveRoom`. |
| R-52 | 2026-11-11 | 11.1.1, 9.3.1 | Un proceso registra en Fatal la excepción que lo termina con un manejador de `AppDomain.CurrentDomain.UnhandledException` puesto justo después de configurar log4net. Solo registra, no atrapa ni sigue (`Program.LogUnhandledException`). El mensaje de arranque se registra después de `app.Start()`. También aplica al `Program` del cliente (decidido en 386–387, 2026-11-11). |
| R-53 | 2026-11-11 | 11.1.1 | Un `catch` de `Host` que traduce un rechazo a falla y la relanza no registra nada, ni en Info ni en Warn: se registra donde se maneja al final (el cliente). Una guarda que rechaza antes del `try` (opciones nulas en `RequireSettings`) sí puede registrar en Warn. |
| R-54 | 2026-11-11 | 4.3.2, 4.6.1 | Una traducción de enum a enum con más casos de los que caben en complejidad 10 va en una tabla `private static readonly IReadOnlyDictionary<TOrigen, TDestino> _xByY` con `TryGetValue`, y lanza `ArgumentOutOfRangeException` si falta el valor. No se parte el `switch` con un `default` que delega. Aplica a `RoomContractTranslator` del cliente. |
| R-55 | 2026-11-11 | Pasada 3, 4.4.2 | En la raíz de composición del servidor cada método de registro registra solo los tipos de su capa (`AddBastionAdapters`, `AddBastionApplication`, `AddBastionHost`). La lista de servicios WCF para CoreWCF (`AddBastionServices`) va en `ServiceRegistration`, junto a sus `AddTransient`, y `Program` compone. Una clase que no se llama como un registro (`ServerCertificate`) no registra servicios. Se pregunta si aplica a la raíz de composición del cliente al revisarla. |
| R-57 | 2026-11-11 | Pasada 4 | El `MessageId` de los contratos se queda aunque el cliente no lo lea: es la identidad del mensaje en la red (`ChatMessageReceipt`, `LobbyChatMessage`, las tres notificaciones de mensaje y `PrivateChatMessage`). No se vuelve a preguntar en `Notifications` ni en `PrivateChat` (decidido en `Chat` de `Contracts`). |
| R-58 | 2026-11-11 | 4.4.2, 2.10.1 | Bastión solo usa puertos registrados de IANA (RFC 6335), del 1024 al 49151. Se rechazan los del sistema (0–1023) y los dinámicos (49152–65535), que el sistema operativo usa como efímeros. La regla vive una sola vez en `ServiceEndpoints.IsRegisteredPort`, con `FirstRegisteredPort` y `LastRegisteredPort`. El cliente vuelve al puerto por defecto, y el servidor no arranca (decidido en `Channels` de `Client.Networking`). |
| R-51 | 2026-11-11 | 3.4.1 (L-01) | Se sigue lo que pidan IDE0007 e IDE0008, porque la 3.4.1 dice que su definición coincide con la de esos analizadores. En una llamada calificada cuyo método nombra el tipo que devuelve (`MatchmakingTranslator.ToMatchFoundNotification(…)` → `MatchFoundNotification`) va `var`. En una llamada sin calificar dentro de la misma clase (`ToPrivateChatMessage(…)`) el analizador pide el tipo explícito (comprobado en `PrivateChatTranslator`, 2026-11-11). |
| R-35 | 2026-11-10 | 2.14.2 | El sufijo `Store` es solo para los datos locales del cliente (`LanguagePreferenceStore`). Lo que guarda en la base desde el servidor se llama `Repository`, también si abre su propio contexto por operación (`MatchRepository`, `RoomRepository`). |
| R-03 | 2026-11-10 | 2.6.3 (L-10) | La 2.6.3 aplica a campos. Las propiedades autoimplementadas se inicializan en los constructores, para no repartir los valores iniciales entre declaraciones y constructores (D-06). Si dos constructores comparten valores por omisión, el público encadena `: this()` al que los fija. |

## Candidatos a reutilizar

Datos o lógica vistos en archivos revisados, para comparar con los siguientes.

| Qué | Dónde aparece | Estado |
| --- | --- | --- |
| Tiempo límite y creación de `Regex` | `AccountRules`, `FriendCodeRules` | Decidido (R-08): `TextPattern.Create`; `FriendCodeRules` se cambia al revisarlo |
| Jugadores por partida clasificatoria (4.4.2) | `MatchmakingRules.PlayersPerMatch = 2`; `GameMode(CLASSIC).PlayerCount = 2` en el catálogo | Decidido: se queda (archivos 116–134) |
| Alfabeto de los códigos | `FriendCodeRules.Alphabet` (sin L) y `RoomRules.CodeAlphabet` (con L) | Se pregunta al revisar `RoomRules.cs` |
| Buscar jugador por código de amigo | `FriendRequestService.FindPlayerByCode`, `PrivateChatService` (normalizar → validar → `FindPlayerIdentityByFriendCode`) | Decidido: `FriendCodeLookup.FindPlayer` (archivos 85–108) |
| Verificar la sesión y buscar la identidad | `FriendListService`, `FriendRequestService`, `PrivateChatService` | Decidido: `ISessionVerifier.VerifyIdentity`; falta adoptarlo en `PrivateChatService` |
| Largo máximo del mensaje (4.4.2) | `ChatRules.MaximumMessageLength = 200`; `MessageConfiguration.TextLength = 500`; `Message.Text NVARCHAR(500)` | Decidido: `ChatPolicy` en EF y `NVARCHAR(200)` en el script (commit `12b9ebe`); la base local sigue en 500 hasta que el usuario decida |

## Registro de archivos

| # | Archivo | Estado | Hallazgos | Commit |
| --- | --- | --- | --- | --- |
| 399–404 | `src/Bastion.Client/Screens/*.cs` (+ los 4 de D1) | Cerrado (rama `review-standard-v2.4-host`), commit `12338cd` | 9.4.1 ×5, R-23 ×4, 2.10.1, 4.2.1, pasada 3 (`UiThread.Run` se queda) | `12338cd` |
| 393–398 | `src/Bastion.Client/Localization/*` (`SupportedLanguages` → `LanguageCatalog`) | Cerrado (rama `review-standard-v2.4-host`), commit `e3f891a` | R-27, R-11, R-04, R-23, R-47, 2.11.4 ×2, 2.4.1, 2.1.2, 2 nombres | `e3f891a` |
| 388–392 | `src/Bastion.Client/Controls/*` (+ D1: `ScreenView`, `Platform`, `ScreenNavigator`, 4 pantallas, portapapeles, `ILanguageService`) | Cerrado (rama `review-standard-v2.4-host`), commit `eb9d572` | 3.3.1 ×2, R-23 ×2, 2.10.1, 10.1.1 (D1 + L1), 4.4.1, probado en el juego | `eb9d572` |
| 386–387 | `src/Bastion.Client/BastionGame.cs`, `Program.cs` | Cerrado (rama `review-standard-v2.4-host`), commit `32cbc25` | 6.3, D-06, R-47, R-52, pasada 3 | `32cbc25` |
| 384–385 | `src/Bastion.Client.Networking/ServerConnection.cs`, `Sessions/InvalidSessionException.cs` | Cerrado (rama `review-standard-v2.4-host`), commit `031592a` | D-06 | `031592a` |
| 374–383 | `src/Bastion.Client.Networking/Rooms/*` | Cerrado (rama `review-standard-v2.4-host`), commit `84e8f0d` | R-54, R-48, R-14, 5.3.1, R-04 ×2, R-45, R-47, R-09 | `84e8f0d` |
| 367–373 | `src/Bastion.Client.Networking/PrivateChat/*` (+ piezas compartidas en `Chat` y `Friends`) | Cerrado (rama `review-standard-v2.4-host`), commit `4bfb855` | R-11 ×4, R-14, 5.3.1 ×2, 5.1.1, R-47, 4.4.1 ×2 | `4bfb855` |
| 350–366 | `src/Bastion.Client.Networking/Notifications/*` (+ `SessionChannelFactory`, `ServerConnection`, `INotificationCallback`) | Cerrado (rama `review-standard-v2.4-host`), commit `fb4c3ec` | R-48 ×8, R-14, 5.3.1, R-47, R-23 ×2, 10.1.1, 9.4.1 (R-50), pasada 2 | `fb4c3ec` |
| 345–349 | `src/Bastion.Client.Networking/Matchmaking/*` | Cerrado (rama `review-standard-v2.4-host`), commit `19ac951` | R-14, R-47 | `19ac951` |
| 342–344 | `src/Bastion.Client.Networking/Matches/*` | Cerrado sin cambios | — | — |
| 328–341 | `src/Bastion.Client.Networking/Friends/*` | Cerrado (rama `review-standard-v2.4-host`), commit `bae09c1` | R-11 ×6, R-14, 5.3.1 ×3, R-47, 5.1.1, 4.4.1 | `bae09c1` |
| 318–327 | `src/Bastion.Client.Networking/Chat/*` | Cerrado (rama `review-standard-v2.4-host`), commit `542c757` | R-11 ×3, R-14 ×4, 5.3.1, R-47 | `542c757` |
| 311–317 | `src/Bastion.Client.Networking/Channels/*` (+ `ServiceEndpoints` y `Program` del servidor) | Cerrado (rama `review-standard-v2.4-host`), commit `5382eac` | R-14, R-04 ×3, R-28, R-58 (puertos registrados), 2.14.3 | `5382eac` |
| 301–310 | `src/Bastion.Client.Networking/Accounts/*` (+ canales inyectados en los 7 clientes) | Cerrado (rama `review-standard-v2.4-host`), commits `e83e6d3` y `c54aba2` | R-10, R-41, R-14, 6.4, pasada 2, 10.1.1 | `e83e6d3`, `c54aba2` |
| 298–300 | `src/Bastion.Contracts/ServiceEndpoints.cs`, `Sessions/*` (+ `GenerateDocumentationFile`) | Cerrado (rama `review-standard-v2.4-host`), commits `6d689a1` y `ab0c785` | 9.4.1, R-04, R-41, R-27 | `6d689a1`, `ab0c785` |
| 291–297 | `src/Bastion.Contracts/Rooms/*` (+ 2 traductores) | Cerrado (rama `review-standard-v2.4-host`), commit `ab66fbb` | 7.2, 7.2.2, pasada 3 (`InvalidOptions`) | `ab66fbb` |
| 287–290 | `src/Bastion.Contracts/PrivateChat/*` | Cerrado (rama `review-standard-v2.4-host`), commit `9e3f09c` | 7.1.1 (R-27) | `9e3f09c` |
| 270–286 | `src/Bastion.Contracts/Notifications/*` (+ `<inheritdoc/>` en `NotificationCallback`) | Cerrado (rama `review-standard-v2.4-host`), commit `ac2a8b4` | 7.1.1, 7.1.2 | `ac2a8b4` |
| 267–269 | `src/Bastion.Contracts/Matchmaking/*` | Cerrado (rama `review-standard-v2.4-host`), commit `3878797` | R-41, 7.2.2, 7.2 | `3878797` |
| 265–266 | `src/Bastion.Contracts/Matches/*` | Cerrado (rama `review-standard-v2.4-host`), commit `40e3763` | 7.2, 7.2.2, R-41 | `40e3763` |
| 254–264 | `src/Bastion.Contracts/Friends/*` (+ el renombre en 8 archivos más) | Cerrado (rama `review-standard-v2.4-host`), commit `43e62a0` | 7.1.1 (R-27), 2.1.2 | `43e62a0` |
| 247–253 | `src/Bastion.Contracts/Chat/*` (+ el renombre en 8 archivos más) | Cerrado (rama `review-standard-v2.4-host`), commit `1326770` | Pasada 4 (`MessageId`, R-57), pasada 3 (`ConnectedPlayerCount`) | `1326770` |
| 240–246 | `src/Bastion.Contracts/Accounts/*` (+ `Host/Accounts/AccountService`) | Cerrado (rama `review-standard-v2.4-host`), commit `2a59451` | 7.1.1 (R-27), 9.4.1, R-44 | `2a59451` |
| 236–239 | `src/Bastion.Server.Host/Sessions/*` (+ 2 interfaces, guardas compartidas en 6 servicios) | Cerrado (rama `review-standard-v2.4-host`), commit `ebb0e3b` | R-44, R-45, R-43, R-23, 10.1.1 (R-49), 4.4.1 ×2 (R-56), R-47, 4 nombres | `ebb0e3b` |
| 234–235 | `src/Bastion.Server.Host/ServerCertificate.cs`, `ServiceRegistration.cs` (y `Program.cs`) | Cerrado (rama `review-standard-v2.4-host`), commit `08f2766` | R-14, 11.3.1, 9.4.2, 4.4.2 (R-55), 4.4.1, 5.2.1, 2 nombres | `08f2766` |
| 231–233 | `src/Bastion.Server.Host/Rooms/*` (`RoomBackgroundService` → `RoomCleanupService`) | Cerrado, commit `e8d9d4c` | R-43, R-42, R-14 ×5, R-23, R-47, R-44, R-45, R-50, R-28, 4.2.1, R-53, R-54, 3 nombres | `e8d9d4c` |
| 230 | `src/Bastion.Server.Host/Program.cs` | Cerrado, commit `edd69af` | 11.1.1 (R-52), 11.3.1, 9.4.1, 2.10.1 | `edd69af` |
| 228–229 | `src/Bastion.Server.Host/PrivateChat/*` | Cerrado, commit `c5c0a5e` | 7.1.2, R-44, R-45, R-04, R-28, R-42 ×2, R-14 ×2, R-48, 3.4.1, R-51 (corregida), 3 nombres, 1 texto | `c5c0a5e` |
| 225–227 | `src/Bastion.Server.Host/Matchmaking/*` (+ `Application/Matchmaking/IMatchmakingDispatcher` nuevo) | Cerrado, commit `8a231a1` | R-42, R-43, R-14, R-47, R-44, R-45, R-48, R-49, R-50, R-51, 2 nombres | `8a231a1` |
| 223–224 | `src/Bastion.Server.Host/Matches/*` | Cerrado, commit `e03286a` | R-43, R-44, R-45 (precisada), 11.3.1 (contexto de la bitácora), 1 texto, 1 nombre | `e03286a` |
| 220–222 | `src/Bastion.Server.Host/Friends/*` | Cerrado, commit `0f43b0f` | 7.1.2, R-42 ×4, R-43, R-14 ×3, R-44, R-45, R-46, R-47, 1 repetición, 6 nombres | `0f43b0f` |
| 218–219 | `src/Bastion.Server.Host/Chat/*` (+ `Common/ContractArray`, `Common/FaultExceptionFactory`) | Cerrado, commit `83ee729` | R-42, R-43, R-44, 1 nombre | `83ee729` |
| 215–217 | `src/Bastion.Server.Host/Accounts/*`, `Common/CallerAddress.cs` | Cerrado, commit `81757eb` | 6.3 ×2, 7.1.2, R-14, R-40, R-41 | `81757eb` |
| 183–200 | `src/Bastion.Server.Adapters/` registro, contexto, configuraciones, convertidor (+ `EnumColumnMapping` nuevo) | Cerrado, commit `12b9ebe` | 9.4.1 ×8, R-25, 4.4.2 ×2, 1 repetición (×14) | `12b9ebe` |
| — | Cierre de Application: `GenerateDocumentationFile` y CS1591 en `I*Service.cs` (R-27) | Commit `7171c56` | 7.3.1 | `7171c56` |
| 175–182 | `src/Bastion.Server.Application/Security/*`, `Sessions/*` | Cerrado, commit `d4b645e` (175 y 178) | 2.8.1 ×2 | `d4b645e` |
| 149–174 | `src/Bastion.Server.Application/Rooms/*` | Cerrado, commit `1fd9813` | 9.4.1 ×5, R-09, 5.3.1 ×5, R-04 ×4, R-14, R-17, R-23, R-11 ×2, 2 repeticiones, 1 memoria | `1fd9813` |
| 137–148 | `src/Bastion.Server.Application/PrivateChat/*` (+ `PrivateChatChannel` nuevo) | Cerrado, commit `85ffd48` | 10.1.1 con 2.2.2, 5.1.1, 5.3.1, R-14, R-04, R-11 ×6, R-27, 1 nombre, L-01 | `85ffd48` |
| 135–136 | `src/Bastion.Server.Application/Moderation/*` | Cerrado sin cambios | 0 | — |
| 116–134 | `src/Bastion.Server.Application/Matchmaking/*` | Cerrado, commit `fa4b91d` | 5.3.1 ×2, R-14, R-11 ×4, 1 repetición con el catálogo (se queda) | `fa4b91d` |
| 109–115 | `src/Bastion.Server.Application/Matches/*` | Cerrado, commit `8e57acb` | 7.2.2, 5.3.1, R-11 | `8e57acb` |
| 85–108 | `src/Bastion.Server.Application/Friends/*` | Cerrado, commit `d486e69` | 5.3.1 ×5, 5.1.1, R-04, R-11 ×8, R-27 ×3, 4 repeticiones, 2 nombres, 1 lectura, 1 espacio de nombres | — |
| 82–84 | `src/Bastion.Server.Application/Common/*` | Cerrado sin cambios | 0 | — |
| 61–81 | `src/Bastion.Server.Application/Chat/*` | Cerrado, commit `2bb2c4f` | 10.1.1, 5.3.1 ×3, R-14 ×4, R-11 ×4, R-27, 3 nombres, 1 repetición | — |
| 60 | `src/Bastion.Server.Application/Auditing/IAccessLogRepository.cs` | Cerrado sin cambios | 0 | — |
| 53–59 | `src/Bastion.Server.Application/Accounts/*` | Cerrado, commit `31547fb` (54 y 57 sin cambios) | 7.1.1/7.2, 7.1.2, 7.3.1, 2.8.1, R-14, R-10 ×3, 1 nombre, 2 repeticiones | — |
| 48–52 | `Sessions/*`, `Statistics/ModeStatistic.cs`, `Text/TextPattern.cs` | Cerrado, commit `cd96587` (48 y 50; el resto sin cambios) | R-11, 2.8.1 | `cd96587` |
| 39–47 | `src/Bastion.Domain/Rooms/*` (45 sin cambios) | Cerrado, commit `28d73c2` | 5.2.1, R-04, R-07, R-11 ×3, R-17 ×2, 2.4.1, 1 repetición, 3 nombres, 2 accesos | `28d73c2` |
| 38 | `src/Bastion.Domain/Moderation/SanctionScope.cs` | Cerrado sin cambios | 0 (valores de la base) | — |
| 37 | `src/Bastion.Domain/Moderation/Sanction.cs` | Cerrado, commit `3288d60` | 1 incumplimiento (2.11.4), 1 lectura (L-15), 1 nombre, 2 miembros solo de pruebas | — |
| 36 | `src/Bastion.Domain/Moderation/BannedWordScope.cs` | Cerrado sin cambios | 0 (valores de la base) | — |
| 35 | `src/Bastion.Domain/Moderation/BannedWord.cs` | Cerrado sin cambios | 0 | — |
| 34 | `src/Bastion.Domain/Matchmaking/SearchStatus.cs` | Cerrado sin cambios | 0 | — |
| 33 | `src/Bastion.Domain/Matchmaking/MatchmakingRules.cs` (ahora `MatchmakingPolicy.cs`) | Cerrado, commit `a3463d8` | 1 incumplimiento (2.4.1), 1 acceso de más | `a3463d8` |
| 32 | `src/Bastion.Domain/Matchmaking/MatchSearch.cs` | Cerrado, commit `a3463d8` | 1 incumplimiento (R-04 ×3), 2 nombres | `a3463d8` |
| 31 | `src/Bastion.Domain/Matches/PawnSymbol.cs` | Cerrado sin cambios | 0 | — |
| 30 | `src/Bastion.Domain/Matches/ParticipationResult.cs` | Cerrado sin cambios | 0 (valores de la base) | — |
| 29 | `src/Bastion.Domain/Matches/Participation.cs` | Cerrado, commit `78c7011` | 1 incumplimiento (R-04), 1 lectura (L-14 → R-23) | `78c7011` |
| 28 | `src/Bastion.Domain/Matches/MatchType.cs` | Cerrado sin cambios | 0 | — |
| 27 | `src/Bastion.Domain/Matches/MatchStatus.cs` | Cerrado sin cambios | 1 valor sin uso (se queda, CU-18 RN-11) | — |
| 26 | `src/Bastion.Domain/Matches/MatchFormat.cs` | Cerrado, commit `78c7011` | R-11 | `78c7011` |
| 25 | `src/Bastion.Domain/Matches/MatchEntrant.cs` | Cerrado sin cambios | 0 (R-16) | — |
| 24 | `src/Bastion.Domain/Matches/MatchEndReason.cs` | Cerrado sin cambios | 0 (valores de la base) | — |
| 23 | `src/Bastion.Domain/Matches/Match.cs` | Cerrado, commits `6227c25` y `78c7011` (R-23) | 2 incumplimientos (9.4.1, 5.3.1), 2 lecturas (L-04, L-13), 1 repetición, 2 nombres | — |
| 22 | `src/Bastion.Domain/Matches/BoardLayout.cs` | Cerrado, commit `dd8ffb3` | 1 incumplimiento (R-04), 1 nombre | `dd8ffb3` |
| 21 | `src/Bastion.Domain/Matches/BoardCoordinates.cs` | Cerrado sin cambios | 0 (R-16) | — |
| 20 | `src/Bastion.Domain/GameModes/GameModeCode.cs` | Cerrado sin cambios | 0 | — |
| 19 | `src/Bastion.Domain/GameModes/GameMode.cs` | Cerrado sin cambios | 1 lectura (L-12 → R-19), 1 nombre (se queda) | — |
| 18 | `src/Bastion.Domain/Friends/FriendshipRules.cs` (ahora `FriendshipPolicy.cs`) | Cerrado, commit `7b5fb83` | 1 incumplimiento (2.4.1) | `7b5fb83` |
| 17 | `src/Bastion.Domain/Friends/Friendship.cs` | Cerrado, commit `5e23ebe` | 2 nombres, 1 método solo de pruebas (quitado) | `5e23ebe` |
| 16 | `src/Bastion.Domain/Friends/FriendRequest.cs` | Cerrado, commit `22f7502` | 1 incumplimiento (2.11.4 → R-17), 1 repetición entre entidades (R-18) | `22f7502` |
| 15 | `src/Bastion.Domain/Friends/FriendCodeRules.cs` (ahora `FriendCodePolicy.cs`) | Cerrado, commit `b97c92c` | 3 incumplimientos (2.4.1, R-08, R-04), 2 nombres | `b97c92c` |
| 14 | `src/Bastion.Domain/Chat/MessageParticipants.cs` | Cerrado sin cambios | 1 lectura (L-11 → R-16) | — |
| 13 | `src/Bastion.Domain/Chat/MessageChannel.cs` | Cerrado sin cambios | 0 (valores de la base) | — |
| 12 | `src/Bastion.Domain/Chat/Message.cs` | Cerrado, commit `7a17d55` | 1 incumplimiento (R-04), 1 lectura (R-14), 1 nombre, 1 miembro solo de pruebas (R-15) | `7a17d55` |
| 11 | `src/Bastion.Domain/Chat/MatchChatSubmission.cs` | Cerrado, commit `a7cb6dd` | R-11 | `a7cb6dd` |
| 10 | `src/Bastion.Domain/Chat/ChatWordFilter.cs` | Cerrado, commit `014dc0c` | 2 incumplimientos (2.2.3, R-04), 1 lectura (2.2.1), 1 repetición, 4 nombres | — |
| 9 | `src/Bastion.Domain/Chat/ChatRules.cs` (ahora `ChatPolicy.cs`) | Cerrado, commit `47be2f3` | 2 incumplimientos (2.4.1, R-04), 3 nombres, 1 constante de más | `47be2f3` |
| 8 | `src/Bastion.Domain/Auditing/AccessLogResult.cs` | Cerrado sin cambios | 0 (vocabulario resuelto con R-10) | — |
| 7 | `src/Bastion.Domain/Auditing/AccessLog.cs` | Cerrado sin cambios | 0 | — |
| 6 | `src/Bastion.Domain/Auditing/AccessAttempt.cs` | Cerrado, commit `36d0280` | 1 lectura (L-02 → R-11) | `36d0280` |
| — | Vocabulario «Login» en los archivos 1, 2 y 5 | Commit `c406863` | R-10 | `c406863` |
| 5 | `src/Bastion.Domain/Accounts/LockoutPolicy.cs` | Cerrado, commit `a48853e` | 1 incumplimiento (R-04), 3 nombres | `a48853e` |
| 4 | `src/Bastion.Domain/Accounts/AccountType.cs` | Cerrado sin cambios | 0 | — |
| 3 | `src/Bastion.Domain/Accounts/AccountStatus.cs` | Cerrado sin cambios | 0 | — |
| 2 | `src/Bastion.Domain/Accounts/AccountRules.cs` (ahora `AccountPolicy.cs`) | Cerrado, commit `2a09e60` | 2 incumplimientos (2.4.1, 4.4.2), 1 lectura (R-05), 1 repetición, 4 nombres, 3 métodos solo usados por pruebas | — |
| 1 | `src/Bastion.Domain/Accounts/Account.cs` | Cerrado, commit `38a940d` | 1 incumplimiento (2.6.3), 3 lecturas (2.9.1, 2.1.2, 2.6.3), 2 repeticiones, 3 nombres, 5 miembros sin uso en producción | — |

## Bitácora por archivo

### 1. `src/Bastion.Domain/Accounts/Account.cs` (2026-11-10)

Entidad de la cuenta; la persiste EF Core (`AccountConfiguration`) y la usan `LoginService`, `FriendPresenceService`
y los repositorios.

**Pasada 1, reglas por sección**
- §1 Idioma: cumple.
- §2 Nombrado: cumple en 2.1–2.8 y 2.10–2.15. Dudas: **2.9.1** (L-03, no redefine `Equals`) y **2.1.2** (¿`byte[]
  PasswordHash`/`PasswordSalt` cuentan como colección y van en plural?).
- §3 Estilo: cumple (no usa `var`, Allman, espaciado). 3.7 no aplica.
- §4 Complejidad: cumple (guardas en `Activate` y `GetRemainingLockMinutes`, patrón `is`).
- §5 Funcional: no aplica (sin lambdas ni LINQ).
- §6 Estructura: cumple (un tipo, orden constante → constructores → propiedades → métodos, `using`, espacio de
  nombres = carpeta).
- §7 y §8: cumple (no es servicio; sin documentación ni comentarios).
- §9 Excepciones: cumple (`InvalidOperationException` en inglés, `ThrowIfNull` en el constructor y en
  `ChangePassword`).
- §10 Inyección: cumple (recibe `now`, no lee el reloj). §11 y §12: no aplican.

**Pasada 2, repetición**
- R-1: la condición del bloqueo (`LockedUntil is DateTime lockedUntil && lockedUntil > now`) está en `IsLockedAt` y,
  negada, en `GetRemainingLockMinutes`.
- R-2: los dos constructores repiten `PreferredLanguage = DefaultLanguage` y `FriendCode = string.Empty`.
- `"en"` solo está aquí en C#; también es el `DEFAULT ('en')` de `Account.PreferredLanguage` en
  `02_create_tables.sql:104` (otra capa, no se repite en código).

**Pasada 3, nombres**
- N-1: `ChangePassword(byte[] hash, byte[] salt)` no recibe una contraseña sino su hash → `SetPasswordHash(passwordHash,
  passwordSalt)`.
- N-2: `FailedAttempts`, `LastFailedAttemptAt` no dicen de qué → `FailedSignInCount`, `LastFailedSignInAt` (con
  `HasColumnName` para no tocar la base).
- N-3: `DefaultLanguage` → `DefaultPreferredLanguage`.
- Se quedan por decisión anterior (`05-pendientes.md`): `Activate`.

**Pasada 4, necesidad** (búsqueda con `git grep` en `src/` y `tests/`)
- `CanSignIn()`: solo lo usan las pruebas; el login decide por `AccountStatus` en `LoginService.AdmitByAccountStatus`.
- `ChangePassword`, `Activate()` y el constructor público: solo los usan las pruebas (CU-02 y CU-04 no están en el
  servidor todavía).
- `IsTwoFactorEnabled`: nadie la lee; EF la mapea por convención.
- `DefaultLanguage` es `public` pero solo se usa dentro de la clase.

**Hallazgo nuevo al preparar las propuestas:** la **2.6.3** pide inicializar en su declaración todo valor que no
depende de un parámetro del constructor. En `Account` eso son `AccountType = Registered`, `AccountStatus = Pending`,
`PreferredLanguage = DefaultLanguage` y `FriendCode = string.Empty`, hoy asignados en los constructores. La regla dice
«campo»; si aplica también a propiedades autoimplementadas es la lectura L-10.

**Decisiones tomadas:** R-01 (2.9.1) y R-02 (2.1.2).

**Propuestas presentadas el 2026-11-10** (el usuario pidió contexto, propuesta, pros y contras antes de decidir):
- A1 quitar `CanSignIn` y sus 2 pruebas · A2 quitar `ChangePassword` · A3 quitar `Activate` · A4 quitar el constructor
  público · A5 quitar `IsTwoFactorEnabled` · A6 `DefaultLanguage` a `private`.
- B1 unificar la condición del bloqueo · B2 inicializar en la declaración (2.6.3) · B3 `ChangePassword` →
  `SetPasswordHash` · B4 `FailedAttempts`/`LastFailedAttemptAt` → `FailedSignInCount`/`LastFailedSignInAt` ·
  B5 `DefaultLanguage` → `DefaultPreferredLanguage`.
- Recomendación dada: aplicar A1, A6, B1, B2, B4 y B5; mantener A2–A5 (las pruebas los necesitan y CU-02, CU-04 y
  CU-05 los usarán); B3 solo si se mantiene A2.

**Respuesta del usuario (2026-11-10):** el `return` de B1 queda difícil de leer, y B2 reparte la inicialización
entre declaraciones y constructores. De ahí sale la decisión D-06. Propuestas revisadas:
- **B1′**: `GetRemainingLockMinutes` usa `IsLockedAt` como guarda y separa el cálculo en
  `TimeSpan remainingLock = LockedUntil.Value - now;` antes de `return (int)Math.Ceiling(remainingLock.TotalMinutes);`.
- **B2′**: toda la inicialización sigue en los constructores; para no repetirla, el constructor público encadena
  `: this()` y el privado fija los valores comunes (`Nickname = string.Empty`, `PreferredLanguage`, `FriendCode`).
  Con eso la L-10 se respondería así: la 2.6.3 aplica a campos, no a propiedades autoimplementadas.

**Respuesta del usuario sobre B1′:** `return (int)Math.Ceiling(remainingLock.TotalMinutes);` sigue difícil de leer
porque mezcla un cast y una llamada. Propuesta **B1″**, un paso por línea:

```csharp
TimeSpan remainingLock = LockedUntil.Value - now;
double roundedUpMinutes = Math.Ceiling(remainingLock.TotalMinutes);
int remainingMinutes = (int)roundedUpMinutes;
return remainingMinutes;
```

Criterio propuesto para todos los `return` (pendiente de confirmar, ampliaría la D-06): el `return` devuelve una
variable, un literal o una sola llamada con argumentos simples; los casts, la aritmética y las llamadas anidadas
van antes, en variables con nombre, un paso por línea.

**Observación del usuario sobre B2′:** el constructor privado no reescribe el `Nickname`. Aclaración: con `: this()`
el privado corre primero (`Nickname = string.Empty`) y después el cuerpo del público asigna el parámetro, así que el
valor final es correcto. Pero `Nickname` se asigna dos veces y quien lee tiene que saber ese orden, lo que va contra
la D-06. Opciones:
- **B2′** (encadenar con `: this()`): sin repetir `PreferredLanguage` ni `FriendCode`; el orden queda oculto y
  `Nickname` se asigna dos veces.
- **B2-0** (dejar los constructores como están): cada uno se lee completo sin saltar al otro; se repiten dos
  asignaciones de valores por omisión.
- Recomendación: B2-0, porque prima la lectura (D-06).

**Decisión del usuario:** B2′, encadenar con `: this()` (queda como R-03).

**Decisiones finales del archivo (2026-11-10):**
- Se aplican: A1 (quitar `CanSignIn` y sus 2 pruebas), A6 (`DefaultLanguage` privada), B1″ (un paso por línea),
  B2′ (`: this()`), B4 (`FailedSignInCount`/`LastFailedSignInAt` con `HasColumnName`) y B5
  (`DefaultPreferredLanguage`).
- Se quedan: `ChangePassword`, `Activate`, el constructor público (los usan las pruebas y los usarán CU-02 y CU-04) e
  `IsTwoFactorEnabled` (la usará CU-05). B3 no se aplica. La L-09 queda abierta: se decide caso por caso.
- El criterio del `return` queda como R-04.

**Al compilar (2026-11-10):** B1″ da el aviso CS8629 en `LockedUntil.Value`, porque el compilador no sabe que la
guarda `IsLockedAt(now)` ya descartó el nulo. El usuario pidió pros, contras y alternativas. Opciones:
1. `[MemberNotNullWhen(true, nameof(LockedUntil))]` sobre `IsLockedAt` (probado, sin aviso).
2. Volver a la guarda con `is` en `GetRemainingLockMinutes` (la condición queda dos veces).
3. Un privado `TryGetActiveLockEnd(now, out DateTime lockEnd)` y los dos públicos lo usan.
4. Un privado `GetRemainingLock(now)` que devuelve `TimeSpan.Zero` si no hay bloqueo: `IsLockedAt` compara con cero
   y `GetRemainingLockMinutes` ya no necesita guarda (probado, sin aviso y con el mismo resultado en tres casos).
5. `LockedUntil.GetValueOrDefault()`: no se recomienda, porque sugiere un valor alternativo que nunca ocurre (9.4.2).
- Recomendación: la 4. Queda pendiente si la R-04 admite una comparación en el `return` (`return remainingLock >
  TimeSpan.Zero;`) o si va a una variable `bool`; lo mismo afecta a `HasPassword` e `IsLockedAt`.
- Mientras se decide, el archivo queda con B1″ y el aviso; no hay commit.
- **Decisión del usuario:** opción 3, el patrón Try (queda como R-06). Antes de elegir pidió que se le explicara el
  patrón y cómo funciona `out`. `HasPassword` se queda igual por la R-05.

**Estado final del archivo (2026-11-10):** cambios aplicados en `review-standard-v2.4`. Además de `Account.cs`, tocan
`AccountConfiguration.cs` (dos `HasColumnName`), `TestAccount.cs` (se quitan las 2 pruebas de `CanSignIn` y
`FailedAttempts` pasa a `FailedSignInCount`) y `TestLoginService.cs` (`FailedSignInCount` y el nombre de una prueba).
Todo compila sin avisos de código (el Host, en otra carpeta, porque el servidor del usuario sigue abierto) y pasan
518 pruebas (162 + 220 + 136). Con un programa aparte se comprobó contra la base local, en solo lectura, que
`FailedSignInCount` y `LastFailedSignInAt` siguen leyendo las columnas `FailedAttempts` y `LastFailedAttemptAt`.
Commit `38a940d` (2026-11-10), sin push (D-07).

### 2. `src/Bastion.Domain/Accounts/AccountRules.cs` (2026-11-10)

Clase estática con las longitudes del apodo y del correo, y la validación de su formato con expresiones regulares.

**Pasada 1, reglas por sección**
- §1: cumple. §3: cumple (argumentos de `new Regex(` uno por línea, 3.5.1). §5: no aplica. §6: cumple. §7, §8: cumple.
  §9: cumple (los parámetros son `string?`, no piden `ThrowIfNull`). §10–§12: no aplican.
- §2 **2.4.1**: `AccountRules` está en plural y no es una clase que solo agrupe valores del mismo tipo (mezcla `int`,
  `TimeSpan`, `Regex` y métodos). Lo mismo pasa con `ChatRules`, `FriendCodeRules`, `FriendshipRules`,
  `MatchmakingRules` y `RoomRules`. Ya existe un precedente en singular: `LockoutPolicy`.
- §4 **4.4.2**: `MatchTimeoutMilliseconds = 250` y `_matchTimeout` están iguales en `Friends/FriendCodeRules.cs:15-17`.
- R-05: `IsEmail` devuelve una condición de tres partes con una llamada
  (`text is not null && text.Length <= MaximumEmailLength && _emailPattern.IsMatch(text)`). Hay que decidir si eso
  sigue siendo «corta».

**Pasada 2, repetición**
- El tiempo límite de las expresiones regulares y la forma de crearlas (`new Regex(patrón, CultureInvariant,
  _matchTimeout)`) se repiten en `FriendCodeRules`. Candidato a una clase compartida del dominio.

**Pasada 3, nombres**
- `MatchTimeoutMilliseconds`/`_matchTimeout`: en Bastión «match» es la partida → `RegexTimeoutMilliseconds`/
  `_regexTimeout`.
- `IsNickname(text)`, `IsEmail(text)`, `IsIdentifier(text)` → `IsValidNickname(nickname)`, `IsValidEmail(email)`,
  `IsValidSignInIdentifier(identifier)`; `MaximumIdentifierLength` → `MaximumSignInIdentifierLength`.
- Lectura (D-06): `$"^[A-Za-z0-9_]{{{MinimumNicknameLength},{MaximumNicknameLength}}}$"` es difícil de leer por las
  llaves triples; se puede comprobar la longitud aparte y dejar el patrón en `^[A-Za-z0-9_]+$`.

**Pasada 4, necesidad**
- `IsNickname`, `IsEmail` e `IsIdentifier` solo los usan las pruebas (`TestAccountRules`).
- CU-01, paso 3 y FA-04, pide que el cliente valide que el identificador tenga formato de apodo o de correo;
  `LoginViewModel` solo comprueba que no esté vacío. `IsIdentifier` es la pieza para eso, y `Bastion.Client` ya
  referencia `Bastion.Domain`. CU-02 RN-01 (apodo de 3 a 30) usará `IsNickname`.
- Las constantes sí se usan: `MinimumNicknameLength` (búsqueda de amigos), `MaximumNicknameLength`,
  `MaximumEmailLength` y `MaximumIdentifierLength` (configuraciones de EF).

**Decisiones tomadas:** R-07 (`AccountRules` → `AccountPolicy`), R-08 (`TextPattern.Create`), y se mantienen
`IsNickname`/`IsEmail`/`IsIdentifier`, con CU-01 FA-04 anotado para revisar `LoginViewModel`.

**Propuestas de nombres y lectura presentadas** (el usuario pidió razón, pros, contras y propuesta de cada una):
N1 `MatchTimeout` → queda resuelto dentro de `TextPattern` · N2 `IsValidNickname`/`IsValidEmail`/
`IsValidSignInIdentifier` y `MaximumSignInIdentifierLength` · N3 la longitud del apodo fuera del patrón ·
N4 `IsEmail` con guarda · ubicación de `TextPattern` en `Bastion.Domain/Text`.

**Decisión del usuario:** «Todas» (N2, N3, N4 y `TextPattern` en `Bastion.Domain/Text`).

**Estado final (2026-11-10):** `AccountRules.cs` → `AccountPolicy.cs` con `IsValidNickname`, `IsValidEmail`,
`IsValidSignInIdentifier` y `MaximumSignInIdentifierLength`; nuevo `src/Bastion.Domain/Text/TextPattern.cs`;
`TestAccountRules.cs` → `TestAccountPolicy.cs` (clase y pruebas renombradas, sin tocar sus datos, que se revisan con
las pruebas); llamadas actualizadas en `AccessLogConfiguration`, `AccountConfiguration` y `FriendRequestService`.
Nota de CU-01 FA-04 agregada a `05-pendientes.md`. Compila sin avisos de código y pasan 518 pruebas. Commit
`2a09e60`, sin push.

### 3. `src/Bastion.Domain/Accounts/AccountStatus.cs` (2026-11-10)

Enumeración de los estados de una cuenta.
- Pasada 1: cumple. §2.15.1 sustantivo singular sin sufijo ni prefijos en los valores; §6 un tipo y su espacio de
  nombres. Las demás secciones no aplican a una enumeración sin lógica.
- Pasada 2: los valores se repiten solo en el `CHECK` de la base (`CK_Account_AccountStatus`), que es otra capa.
- Pasada 3: nombres claros.
- Pasada 4: los cinco valores se usan en `src` (`LoginService.AdmitByAccountStatus` y otros).
- **Cerrado sin cambios.**

### 4. `src/Bastion.Domain/Accounts/AccountType.cs` (2026-11-10)

Enumeración del tipo de cuenta: registrada o invitado.
- Pasada 1: cumple, igual que `AccountStatus`.
- Pasada 2: sin repetición en C#. Pasada 3: nombres claros.
- Pasada 4: `Guest` no se nombra en el código, pero la base tiene una cuenta `GUEST` (`Invitado_4821`). EF la lee con
  el conversor de la enumeración, así que quitar el valor rompería la lectura de esa fila. CU-03 (jugar como invitado)
  también lo usará.
- **Cerrado sin cambios.**

### 5. `src/Bastion.Domain/Accounts/LockoutPolicy.cs` (2026-11-10)

Bloqueo escalonado por intentos fallidos. Coincide con CU-01 RN-03: 3 intentos → 5 min, 6 → 30 min, desde 9 → 60 min,
y el contador se restablece a las 24 h.
- Pasada 1: §2, §3, §6 y §9 cumplen. §4.5.1 admite el `?:`, pero **R-04** no: el último `return` es un condicional
  con una llamada. Se aplica la R-04 (D-07): `if (consecutiveFailures == FirstThreshold)` con su `return` y al final
  `return TimeSpan.Zero;`, igual que las dos ramas anteriores.
- Pasada 2: sin repetición.
- Pasada 3 (se pregunta): `CounterResetPeriod` no dice de qué contador → `FailedSignInCountResetPeriod`, que coincide con
  `Account.FailedSignInCount`; `FirstThreshold`/`SecondThreshold`/`ThirdThreshold` → `FirstLockThreshold`/…;
  `consecutiveFailures` → `failedSignInCount`.
- Pasada 4: `CounterResetPeriod` y `GetLockDuration` los usa `Account`; las constantes son privadas.

**Decisión del usuario:** los tres renombres. Se aplicaron con la R-04; también cambian `Account.cs` (usa
`FailedSignInCountResetPeriod`) y `TestLockoutPolicy.cs` (nombre de la prueba). La constante privada
`CounterResetHours` se dejó igual porque no se preguntó. Compila y pasan las pruebas de dominio y aplicación
(162 + 220). Commit `a48853e`, sin push.

### 6. `src/Bastion.Domain/Auditing/AccessAttempt.cs` (2026-11-10)

Record posicional con el identificador escrito, la conexión y la hora de un intento de inicio de sesión. Lo usan
`LoginService`, `AccountService` y `LoginTranslator`.
- Pasada 1: §2.8.1 (valor inmutable como `record`), §2.2.2 (3 parámetros), §3, §6 cumplen. **Lectura L-02**: sus
  parámetros de referencia (`EnteredIdentifier`, `Connection`) no se comprueban con `ThrowIfNull`; ¿la 9.4.1 aplica al
  constructor primario de un record posicional? ¿Y cuenta para el límite de 3 de la 2.2.2?
- Pasada 2: sin repetición. Pasada 4: se usa.
- Pasada 3: ver la decisión de vocabulario «Login/SignIn» (abajo).

### 7. `src/Bastion.Domain/Auditing/AccessLog.cs` (2026-11-10)

Entidad de la bitácora de accesos; la crea `LoginService` y EF la inserta.
- Pasada 1: cumple (R-01 sin `Equals`; R-03 cada constructor asigna sus valores, sin valores comunes que encadenar;
  `ThrowIfNull(attempt)`).
- Pasada 2: sin repetición. Pasada 3: nombres claros.
- Pasada 4: ninguna clase lee sus propiedades, pero son las columnas que la bitácora guarda: se quedan.

### 8. `src/Bastion.Domain/Auditing/AccessLogResult.cs` (2026-11-10)

Enumeración del resultado de un intento de acceso.
- Pasada 1: cumple. Pasada 2: los valores se repiten solo en el `CHECK` de la base, que además admite otros para
  casos futuros. Pasada 4: los seis valores los usa `LoginService`.
- Pasada 3: `LoginSucceeded` usa «Login», y en archivos ya revisados se usa «SignIn» (`RecordFailedSignIn`,
  `FailedSignInCount`, `IsValidSignInIdentifier`). Es el mismo concepto con dos palabras.

**Decisión de vocabulario abierta:** en `src` hay unos 35 nombres con «Login/LogIn» (`LoginService`, `LoginViewModel`,
`LoginCredentials`, `IAccountService.LogIn`, claves de recursos) y unos 13 con «SignIn/SignedIn» (`Account`,
`AccountPolicy`, `LockoutPolicy`, `SignedInPlayer`, `SignedInSession`).

**Decisiones tomadas:** R-09 (los records cuentan para la 2.2.2) y R-10 («Login» en todo). El renombre de los
nombres «SignIn» de los archivos 1, 2 y 5 (con `LoginService`, `AccessLogConfiguration`, `AccountConfiguration` y sus
pruebas) va en el commit `c406863`; compila y pasan 162 + 220 pruebas. `AccessLog.cs` y `AccessLogResult.cs` quedan
cerrados sin cambios (`LoginSucceeded` ya usa «Login»).

**L-02, regla 9.4.1 en records posicionales:** el usuario pidió razonamiento, pros, contras y alternativas. Hay 67
records posicionales en `src` (Domain 10, Server.Application 29, Client 10, Client.Networking 18); `with` se usa en 3
lugares (`MatchFormat`, `RoomSettings` y un evento de `PrivateConversationViewModel`); no se usa la deconstrucción.
Opciones presentadas:
- A. Constructor explícito con `ThrowIfNull` (deja de ser posicional). Única que cumple la letra. Recomendada.
- B. Exentos: se quedan en una línea.
- C. `?? throw` en las propiedades del record posicional (no usa `ThrowIfNull`, se lee peor).
- D. Por capa: A en Domain y Server.Application, B en Client y Client.Networking.

**Decisión del usuario (L-02):** opción A, constructor explícito → **R-11**. `AccessAttempt` pasa a un constructor con
`ThrowIfNull(enteredIdentifier)` y `ThrowIfNull(connection)` y propiedades `{ get; }`; no se usa con `with`. Los dos
lugares que lo crean (`LoginTranslator` y `TestLoginService`) ya pasan los argumentos en orden y no cambian. Compila el
servidor (en carpeta aparte, el servidor del usuario sigue abierto) y pasan 162 + 220 pruebas. Commit `36d0280`, sin push.

### 9. `src/Bastion.Domain/Chat/ChatRules.cs` (2026-11-10)

Reglas del chat (CU-20 RN-03 largo, RN-04 ritmo): `MaximumMessageLength = 200`, `CooldownSeconds = 3`,
`HistoryCapacity = 200`, `RecentMessageCount = 50` e `IsValidMessage`. Lo usan el cliente (tres modelos de vista y
`ChatRejectionText`) y el servidor (`ChatModerator`, `ChatCooldown`, `LobbyChatRoom`, `LobbyChatService`,
`PrivateChatService`).
- Pasada 1: §1, §3, §5–§12 cumplen o no aplican (sin lambdas, sin comentarios, `text` es `string?` y no pide
  `ThrowIfNull`). §2.4.1: nombre en plural → **R-07**, pasa a `ChatPolicy` (y `TestChatRules` → `TestChatPolicy`, 12.1.1).
  **R-04**: `return !string.IsNullOrWhiteSpace(text) && text.Trim().Length <= MaximumMessageLength;` encadena una
  llamada (`Trim().Length`) dentro de la condición → guarda `if (string.IsNullOrWhiteSpace(text)) { return false; }`,
  `string trimmedText = text.Trim();` y `return trimmedText.Length <= MaximumMessageLength;` (R-05).
- Pasada 2: `IsValidMessage` es la única validación del largo y la usan cliente y servidor (CU-20 RN-06): bien.
  Fuera del archivo: `MessageConfiguration.TextLength = 500` y `Message.Text NVARCHAR(500)` no usan los 200 del dominio
  (4.4.2). Se pregunta al revisar `MessageConfiguration.cs`.
- Pasada 3 (se pregunta): `CooldownSeconds` no dice de qué (el CU-20 RN-12 tiene otro de 10 s para los emotes);
  `RecentMessageCount` se lee como una cuenta, y es un límite (cuántos mensajes recientes manda el servidor y conserva
  la pantalla); `IsValidMessage` solo mira el largo, no el filtro de palabras, pero coincide con
  `ChatRejection.InvalidMessage`.
- Pasada 4 (se pregunta): `HistoryCapacity` solo lo usa `LobbyChatRoom`: guarda 200 líneas, pero en producción solo
  se leen las últimas 50 (`LobbyChatService` llama `ListRecent(RecentMessageCount)`; la única llamada con
  `HistoryCapacity` es la prueba `Post_AboveCapacity_DropsOldestLine`). 150 líneas se guardan y nunca se sirven.

**Decisiones del usuario:** quitar `HistoryCapacity` (el lobby guarda solo `MaximumRecentMessages`);
`RecentMessageCount` → `MaximumRecentMessages`; `CooldownSeconds` → `MessageCooldownSeconds`; `IsValidMessage` se queda
(coincide con `ChatRejection.InvalidMessage` y el CU-20 RN-03). Se aplicaron con la R-07 y la R-04: `ChatPolicy.cs`,
`TestChatPolicy.cs`, los nueve archivos de cliente y servidor que la usan, y la prueba
`MatchChatMessageReceived_OverMaximumRecentMessages_DropsOldestMessage` (llevaba el nombre viejo). Compila el servidor
(carpeta aparte) y pasan 162 + 220 + 136 pruebas. Commit `47be2f3`, sin push.

Para los siguientes archivos: `ILobbyChatRoom.ListRecent(int count)` y `LobbyChatRoom` ya solo guardan lo que se pide;
al revisarlos, ver si el parámetro `count` sigue haciendo falta.

### 10. `src/Bastion.Domain/Chat/ChatWordFilter.cs` (2026-11-10)

Filtro de palabras prohibidas (CU-20 RN-01). Pasa el texto y cada término a minúsculas sin acentos, con un solo
espacio entre palabras y un espacio a cada lado, para que `Contains(" term ")` encuentre solo palabras completas. Lo
usa `ChatModerator`.
- Pasada 1: §1, §3 (Allman, `var builder` evidente, `&&` al inicio de la continuación), §4.1–4.6, §6, §9
  (`ThrowIfNull` de los dos parámetros) cumplen; §7, §8, §10–§12 no aplican.
  - **2.2.3 (incumplimiento):** `ContainsBannedTerm` devuelve `bool` y es una pregunta; `Contains` no está en la lista
    (Is, Are, Has, Can, Should) ni es un miembro de la plataforma o de una interfaz → `HasBannedTerm`.
  - **R-04 (incumplimiento):** el `return` es una cadena LINQ de tres operadores con dos lambdas. La 5.3.1 la admite
    (termina en `Any`, un operador por línea), pero la R-04 pide devolver una variable. Es el primer `return` con
    LINQ: se pregunta cómo resolverlo para todo el proyecto.
  - **Lectura de la 2.2.1:** `ToComparableWords` usa la convención `To<Tipo>`, pero el estándar la admite para
    convertir «en otro tipo», y aquí va de `string` a `string`.
- Pasada 2: «agregar un separador si el último carácter no lo es» se repite en `ToComparableWords` (al final) y en
  `AppendComparable` (dentro de un `else if` que mezcla dos condiciones).
- Pasada 3: `ToComparableWords`, `AppendComparable`, `comparableText` y `decomposed` no dicen qué le pasa al texto.
- Pasada 4: los tres métodos y la constante se usan.

**Decisiones del usuario:** la cadena LINQ va en una variable `bool` y el `return` la devuelve (**R-12**, para todo el
proyecto); `ContainsBannedTerm` → `HasBannedTerm` (y `containsBannedTerm` → `hasBannedTerm`, 2.1.4); se crea
`AppendSeparator(builder)` y el `else if` queda con una sola condición; nombres de la familia «Normalize»:
`NormalizeWords`, `AppendNormalizedCharacter`, `normalizedText`, `decomposedText` (**R-13** para la 2.2.1). Cambian
también `ChatModerator` (la llamada) y `TestChatWordFilter` (nombres de las pruebas y la variable). Compila el
servidor (carpeta aparte) y pasan 162 + 220 pruebas. Commit `014dc0c`, sin push.

### 11. `src/Bastion.Domain/Chat/MatchChatSubmission.cs` (2026-11-10)

Lo que un jugador manda al chat de una partida: el número de partida y el texto. Lo crean `ChatService` (Host) y
`MatchChatRelay`, y lo reciben `IMatchChatService.SendMessage` y `Message.CreateForMatch`.
- Pasada 1: record posicional con un `string` sin comprobar → **R-11**: constructor con `ThrowIfNull(text)` y
  propiedades `{ get; }`; no se copia con `with`. El resto cumple; 2.2.2 con dos parámetros.
- Pasada 2: sin repetición. Pasada 3: nombre claro (lo que se envía al chat de partida).
- Pasada 4: necesario. Sin él, `SendMessage` y `CreateForMatch` tendrían cuatro parámetros (2.2.2).

Cerrado sin preguntas (solo la R-11). Los llamadores ya pasan los argumentos en orden. Compila el servidor (carpeta
aparte) y pasan 162 + 220 pruebas. Commit `a7cb6dd`, sin push.

### 12. `src/Bastion.Domain/Chat/Message.cs` (2026-11-10)

Entidad de EF de un mensaje guardado: privado (canal `Friends`, con constructor público) o de partida (canal `Match`,
con `CreateForMatch`).
- Pasada 1: §1, §3, §6 y §9 cumplen (`ThrowIfNull` de `participants`, `text` y `submission`; `ArgumentException` con
  `nameof`). R-01: sin `Equals`. R-03: los dos constructores no comparten valores (el privado solo pone
  `Text = string.Empty` para EF), así que no se encadenan.
  - **R-04 (incumplimiento):** `GetPartnerId` devuelve `IsSentBy(accountId) ? RecipientId.GetValueOrDefault() : AuthorId`,
    un condicional con dos llamadas → `if (IsSentBy(accountId)) { return RecipientId.GetValueOrDefault(); }` y
    `return AuthorId;`, como en `LockoutPolicy`.
  - **Lectura de la R-04:** `CreateForMatch` devuelve `new Message { … }` con cinco asignaciones simples. Hay 121
    `return new` en `src`: se pregunta si una creación cuenta como «una sola llamada».
- Pasada 2: sin repetición (`GetPartnerId` reutiliza `IsSentBy`).
- Pasada 3: `new Message(participants, …)` crea un mensaje privado, pero la llamada no lo dice, mientras que el de
  partida usa `CreateForMatch`. `SameAccountMessage` sigue la convención del proyecto para textos de excepción
  (`FriendRequest`, `Friendship`, `DefaultMessage`). `GetPartnerId` usa el vocabulario de `PrivateChatService`.
- Pasada 4: `MarkRead` solo lo usan `FakeMessageRepository` y `TestMessage`. En producción,
  `MessageRepository.MarkRead` marca con `ExecuteUpdate` y el filtro `ReadAt == null`, que es la misma regla.
  Es un caso de la L-09.

**Decisiones del usuario:** `Message.CreatePrivate(participants, text, sentAt)` en lugar del constructor público, que
pasa a ser solo el privado de EF; `return new X { … }` con valores simples se admite (**R-14**), y `CreateForMatch`
se queda; `MarkRead` se mantiene (**R-15**). Se aplicó también la R-04 en `GetPartnerId`. Cambian
`PrivateChatService` (la llamada), `TestPrivateChatService` (el ayudante `StoreMessage`) y `TestMessage`: dos pruebas
pasan a `CreatePrivate_DifferentPlayers_UsesFriendsChannel` y `CreatePrivate_SameAuthorAndRecipient_Throws`, y el
ayudante `CreateMessage` guarda primero los participantes en una variable (R-14). Compila el servidor (carpeta aparte)
y pasan 162 + 220 + 136 pruebas. Commit `7a17d55`, sin push.

### 13. `src/Bastion.Domain/Chat/MessageChannel.cs` (2026-11-10)

Enumeración del canal de un mensaje: `Match`, `Spectators`, `Room`, `Global`, `Friends`.
- Pasada 1: 2.15.1 (singular, no es `[Flags]`) y el resto cumplen.
- Pasada 2: los valores se repiten en el `CHECK` `CK_Message_Channel` de la base, que es su origen.
- Pasada 3: nombres claros.
- Pasada 4: el código solo usa `Friends` y `Match`, pero la base de prueba tiene filas `GLOBAL` (2), `ROOM` (3) y
  `SPECTATORS` (1), y EF las lee con `UpperSnakeCaseEnumConverter`. Se quedan, como `AccountType.Guest`.

**Cerrado sin cambios.**

### 14. `src/Bastion.Domain/Chat/MessageParticipants.cs` (2026-11-10)

Autor y destinatario de un mensaje privado: `record MessageParticipants(int AuthorId, int RecipientId)`. Lo usan
`Message.CreatePrivate` y `IMessageRepository.MarkRead`.
- Pasada 1: record posicional **sin parámetros de referencia**: la 9.4.1 no tiene nada que comprobar. Lectura **L-11**:
  ¿la R-11 lo convierte igual a constructor explícito?
- Pasada 2: sin repetición. Pasada 3: nombre claro.
  Fuera del archivo: en `IMessageRepository.MarkRead` y `MessageRepository.MarkRead` el parámetro se llama
  `readMessages`, que parece una colección de mensajes (2.1.2) y es la pareja autor-destinatario. Se pregunta al
  revisar esos archivos.
- Pasada 4: necesario. Sin él, `CreatePrivate` y `MarkRead` tendrían cuatro y tres datos sueltos (2.2.2).

**Decisión del usuario (L-11):** se queda posicional → **R-16**. **Cerrado sin cambios.** Con esto termina la carpeta
`Chat` del dominio; sigue `Friends`.

### 15. `src/Bastion.Domain/Friends/FriendCodeRules.cs` (2026-11-10)

Código de amigo (CU-21 RN-05): seis caracteres de un alfabeto sin los que se confunden (sin I, L, O, 0, 1). Valida
(`IsValidFriendCode`), quita guiones y espacios y pasa a mayúsculas (`NormalizeFriendCode`), y agrega un guion después
del segundo carácter para mostrarlo (`FormatFriendCode`, «QU-7K2P»). Lo usan `FriendRequestService`,
`FriendListService`, `PrivateChatService`, `AccountConfiguration` (largo de la columna) y el cliente
(`FriendsPanelViewModel`).
- Pasada 1: §1, §3, §4.1–4.3, §6 y §9 cumplen.
  - **2.4.1:** plural → **R-07**: `FriendCodePolicy` (y `TestFriendCodeRules` → `TestFriendCodePolicy`).
  - **R-08:** crea su `Regex` con su propio tiempo límite → `TextPattern.Create`; se van `MatchTimeoutMilliseconds` y
    `_matchTimeout`.
  - **R-04:** `return code.Insert(GroupLength, Separator.ToString());` lleva una llamada anidada → la cadena del
    separador va antes en una variable.
  - R-05: `return text is not null && _friendCodePattern.IsMatch(text);` es una condición corta: se queda.
- Pasada 2: el alfabeto se repite en `database/05_create_friends.sql` (generación y `CHECK`), que es la definición
  de la base, como los `CHECK` de las enumeraciones. `RoomRules.CodeAlphabet` es otro alfabeto que **sí** incluye la L:
  se pregunta al revisar `RoomRules`.
  Fuera del archivo: normalizar, validar y buscar por código se repite en `FriendRequestService.FindPlayerByCode` y en
  `PrivateChatService` (y algo parecido en `FriendListService`). Se pregunta en la capa de aplicación.
- Pasada 3 (se pregunta): los métodos repiten «FriendCode» en una clase que ya se llama así (`Length` no lo repite);
  `GroupLength = 2` hace pensar en grupos de dos («QU-7K-2P»), pero solo se agrega un guion, después del segundo carácter.
- Pasada 4: los tres métodos y `Length` se usan en producción.

**Decisiones del usuario:** `IsValid`, `Normalize` y `Format` (sin repetir «FriendCode»); `GroupLength` →
`SeparatorPosition`. Se aplicaron con la R-07, la R-08 y la R-04. Cambian `FriendRequestService`,
`FriendListService`, `PrivateChatService`, `AccountConfiguration`, `FriendsPanelViewModel` y
`TestFriendCodePolicy` (nombres de las pruebas). Compila el servidor (carpeta aparte) y pasan 162 + 220 + 136 pruebas.
Commit `b97c92c`, sin push.

### 16. `src/Bastion.Domain/Friends/FriendRequest.cs` (2026-11-10)

Entidad de EF de una solicitud de amistad pendiente (CU-21, CU-22). La clave es (`RequesterId`, `RecipientId`) y caduca
a los `FriendshipRules.RequestLifetimeDays` días.
- Pasada 1: §1, §3, §4, §6 y §9 cumplen (solo parámetros por valor). R-01: sin `Equals`; R-03: el constructor privado
  de EF está vacío.
  - **2.11.4 (incumplimiento):** `public DateTime ExpiresAt => RequestedAt.AddDays(...)` es un valor calculado con
    cuerpo de expresión fuera de un catálogo de diccionario; la regla pide un método. Es el primero del dominio: en
    `src` hay 80 propiedades con `=>`, casi todas en modelos de vista del cliente (que Gum enlaza por nombre de
    propiedad) y 13 `DbSet` en `BastionDbContext` (L-04). Esos se verán en su capa.
- Pasada 2: la comprobación «el mismo jugador en los dos lados» (`if (a == b) throw new ArgumentException(…)`) se
  repite en `FriendRequest`, `Friendship` y `Message.CreatePrivate`, cada una con su texto.
  Fuera del archivo: la fórmula de caducidad se repite en la proyección de EF de `FriendRequestRepository` (línea 85,
  `request.RequestedAt.AddDays(FriendshipRules.RequestLifetimeDays)`), porque EF no traduce un método propio a SQL; y
  `FriendRequestService` filtra los `FriendRequestSummary` con `ExpiresAt > now` (líneas 97 y 100). Se ven al revisar
  esos archivos.
- Pasada 3: nombres claros. Pasada 4: todo se usa en producción.

**Decisiones del usuario:** `ExpiresAt` pasa al método `GetExpirationTime()` (**R-17**); la guarda «el mismo jugador»
se queda en cada entidad con su texto (**R-18**). Se va `builder.Ignore(request => request.ExpiresAt)` de
`FriendRequestConfiguration` (EF no mapea métodos); cambian `FriendRequestService` (línea 87) y
`FakeFriendRequestRepository`. Los `ExpiresAt` de `FriendshipTranslator` y del cliente son de `FriendRequestSummary` y
`PendingFriendRequest`, no de la entidad, y no cambian. Compila el servidor (carpeta aparte) y pasan 162 + 220 pruebas.
Commit `22f7502`, sin push.

### 17. `src/Bastion.Domain/Friends/Friendship.cs` (2026-11-10)

Entidad de EF de una amistad. Guarda la pareja ordenada (`AccountAId` el menor y `AccountBId` el mayor, por el `CHECK
CK_Friendship_Order` de la base) y la fecha. La crea `FriendRequestService` al aceptar una solicitud.
- Pasada 1: cumple (R-01, R-03, R-18; `Math.Min`/`Math.Max` en asignaciones, no en un `return`).
- Pasada 2: sin repetición. `GetFriendAccountId` se parece a `Message.GetPartnerId`, pero aquel lanza una excepción con
  un tercero y este no.
- Pasada 3 (se pregunta): `AccountAId`/`AccountBId` no dicen que el primero es el menor (lo dicen el `CHECK` y los
  comentarios del SQL; las pruebas ya usan `SmallerAccountId`/`LargerAccountId`). `StrangerMessage` puede leerse como
  un mensaje de chat de un desconocido.
- Pasada 4 (se pregunta): `GetFriendAccountId` (y con él `StrangerMessage`) solo lo usan 3 pruebas de `TestFriendship`.
  Producción obtiene los amigos en SQL (`FriendshipRepository.ListFriendAccountIds`) y el fake usa `AccountAId`/
  `AccountBId`. La R-15 no aplica porque ningún doble lo necesita.

**Decisiones del usuario:** quitar `GetFriendAccountId`, `StrangerMessage` y sus 3 pruebas; `AccountAId`/`AccountBId`
→ `SmallerAccountId`/`LargerAccountId`, con `HasColumnName("AccountAId"/"AccountBId")` en `FriendshipConfiguration`
(constantes `SmallerAccountIdColumn`/`LargerAccountIdColumn`). Cambian `FriendshipRepository` (consulta LINQ),
`FakeFriendshipRepository` y `TestFriendship` (dos pruebas pasan a `Constructor_LargerIdFirst_SetsSmallerAccountId` y
`…SetsLargerAccountId`). Una lectura sobre la base local confirmó el mapeo (`SmallerAccountId → AccountAId`) y que
`FriendRequest` mapea solo `RequesterId`, `RecipientId` y `RequestedAt`. Compila el servidor (carpeta aparte) y pasan
159 + 220 pruebas (3 menos de dominio). Commit `5e23ebe`, sin push.
Para `FriendshipRepository`: `Remove` repite el orden `Math.Min`/`Math.Max` del constructor, y sus variables locales
siguen siendo `accountAId`/`accountBId` (parámetros del procedimiento `usp_Friendship_Delete`). Se ven al revisarlo.

### 18. `src/Bastion.Domain/Friends/FriendshipRules.cs` (2026-11-10)

Dos constantes: `MaximumFriends = 100` (CU-21 RN-02) y `RequestLifetimeDays = 30` (CU-21 RN-08, CU-22 RN-05).
- Pasada 1: 2.4.1 en plural → **R-07**: `FriendshipPolicy`. El resto cumple.
- Pasada 2: los 30 días se repiten en la proyección de `FriendRequestRepository` usando la constante, sin literal.
- Pasada 3: nombres claros (dentro de `FriendshipPolicy`, «Request» es la solicitud de amistad).
- Pasada 4: las dos se usan en producción.

Cerrado sin preguntas (solo la R-07). Cambian `FriendRequest`, `FriendRequestRepository`, `FriendRequestService` y dos
archivos de pruebas. Compila el servidor (carpeta aparte) y pasan 159 + 220 + 136 pruebas. Commit `7b5fb83`, sin push.
Con esto termina la carpeta `Friends` del dominio; sigue `GameModes`.

### 19. `src/Bastion.Domain/GameModes/GameMode.cs` (2026-11-10)

Fila del catálogo `GameMode` (CLASSIC 9×9 con 2 jugadores y 10 muros; FOUR_PLAYERS 9×9 con 4 y 5; QUICK 7×7 con 2 y 6).
Solo la crea EF al leer la base; las pruebas la arman con inicializador de objeto (`RoomSamples`, `TestMatch`,
`FakeMatchStore`). Seis propiedades `{ get; init; }`.
- Pasada 1: §1, §3, §6 cumplen; §9 no aplica (sin métodos ni constructores). 2.11.1 cumple: los valores no cambian
  y usan `init`. R-01: sin `Equals`.
  - **Lectura L-12 (2.8.1):** «valores inmutables […] se declaran record». `GameMode` es inmutable, pero es una
    entidad de EF, y un record redefine `Equals` por valor, lo que choca con la R-01.
- Pasada 2: sin repetición; los valores viven en la base, y el dominio no los copia en constantes.
- Pasada 3: `WallsPerPlayer` es el número de muros del modo, que una sala privada puede cambiar
  (`RoomSettings.WallsPerPlayer`, y `MatchFormat` lo toma como valor inicial). Se pregunta si el nombre lo deja claro.
- Pasada 4: las seis propiedades se usan en producción.

**Decisiones del usuario:** sigue como `class` (**R-19**); `WallsPerPlayer` se queda. **Cerrado sin cambios.**

### 20. `src/Bastion.Domain/GameModes/GameModeCode.cs` (2026-11-10)

Enumeración de la clave del modo: `Classic`, `FourPlayers`, `Quick`. EF la guarda como `CLASSIC`, `FOUR_PLAYERS` y
`QUICK` (`UpperSnakeCaseEnumConverter`), que son también las claves de los diccionarios de recursos (D-21).
- Pasada 1: 2.15.1 (singular, sin `[Flags]`) y el resto cumplen. Pasada 2: los valores coinciden con las filas del
  catálogo y con la traducción de contratos (`RoomTranslator`), sin literales. Pasada 3: nombres claros.
  Pasada 4: los tres se usan (`RoomTranslator`, `MatchmakingRules.RankedGameModeCode`).

**Cerrado sin cambios.**

### 21. `src/Bastion.Domain/Matches/BoardCoordinates.cs` (2026-11-10)

`record BoardCoordinates(int ColumnIndex, int RowIndex)`: casilla del tablero en índices desde cero. La usan
`BoardLayout`, el cliente (`BoardPawn`, `BoardSceneLayout`, `MatchViewModel`) y sus pruebas.
- Pasada 1: valor inmutable como `record` (2.8.1); solo enteros → **R-16**, se queda posicional. Pasadas 2 a 4: sin
  repetición, nombres claros (dicen que son índices), se usa en producción.

**Cerrado sin cambios.**

### 22. `src/Bastion.Domain/Matches/BoardLayout.cs` (2026-11-10)

Casilla de salida de cada jugador según el tamaño del tablero y su turno (CU-13): `GetStartingCoordinates` (índices)
y `GetStartingSquare` (nombre de la casilla, como «e1», que guarda `Participation.CurrentSquare`).
- Pasada 1: §1, §3 (3.5.1: argumentos del `throw` uno por línea), §4.3.2 (`default` con
  `ArgumentOutOfRangeException` porque el turno llega como argumento), §6 cumplen; `return new BoardCoordinates(…)`
  con valores simples (R-14).
  - El mensaje literal del `throw` **no** incumple la 2.10.1: los ejemplos correctos del propio estándar (4.3.2 y
    1.3.1) escriben el mensaje literal en el `throw`. Pasa igual en unos 12 `default` de Client.Networking y Client.
  - **R-04 (incumplimiento):** `return string.Create(…, $"{column}{coordinates.RowIndex + FirstRow}")` suma dentro del
    `return`, y `char column = (char)(FirstColumn + coordinates.ColumnIndex);` suma y convierte en la misma línea →
    un paso por línea: `int columnCode = …; char column = (char)columnCode; int rowNumber = …;` y el `return` con
    variables.
- Pasada 2: el cliente (`BoardSceneLayout`) tiene su propia letra de columna `FirstColumnName = 'A'` para los nombres
  de las mallas 3D. Es otro dato (el nombre de una malla, en mayúscula), no la notación de la casilla.
- Pasada 3 (se pregunta): `int lastIndex = boardSize - FirstRow;` resta el número de la primera fila (1) para obtener
  el último índice, que solo es correcto porque las filas empiezan en 1. Quien lo lee tiene que deducirlo.
- Pasada 4: los dos métodos se usan en producción (`Participation`, cliente).

**Decisión del usuario:** `FirstRow` → `RowNumberOffset`. Se aplicó con la R-04 (cuatro líneas, un paso cada una).
Compila el servidor (carpeta aparte) y pasan 159 + 220 + 136 pruebas. Commit `dd8ffb3`, sin push.

### 23. `src/Bastion.Domain/Matches/Match.cs` (2026-11-10)

Entidad de EF de una partida (CU-09, CU-10, CU-17): la empiezan `StartRanked` y `StartPrivate`, que sientan a los
jugadores en orden de turno, y `Abandon` resuelve el abandono (con dos jugadores termina la partida; con cuatro, el
que se va pierde, pasa el turno y, si queda uno, ese gana). La usan `RankedMatchCreator`, `PrivateMatchCreator`,
`MatchAbandonmentService`, `MatchStore` y el cliente (las constantes de turno).
- Pasada 1: §1, §3, §4.1–4.6 (el `?:` de `Finish` elige entre dos valores sin efectos), §6, §10 cumplen. Los mensajes
  literales de los `throw` se admiten (los ejemplos del estándar los escriben igual).
  - **9.4.1 (incumplimiento):** `StartRanked` y `StartPrivate` son públicos y no comprueban `entrantsInTurnOrder`; la
    comprobación está en el privado `SeatEntrants` → `ThrowIfNull` al inicio de los dos públicos, y se quita del
    privado.
  - **5.3.1 (incumplimiento):** `ListActiveParticipations` encadena `ToList()` al final de la consulta → la consulta
    va en un `IEnumerable<Participation>` con nombre y se materializa con `new List<Participation>(…)`.
  - **L-04 (2.11.4):** `public IReadOnlyCollection<Participation> Participations => _participations;` es la navegación
    de EF (configurada con `UsePropertyAccessMode.Field`). La 2.11.4 no tiene excepción para frameworks.
  - **Lectura L-13 (R-04/R-12):** `return _participations.FirstOrDefault(participation => …);` es una sola llamada
    LINQ con una lambda. La R-12 habla de cadenas; el propio estándar devuelve `_players.Count(player => player.IsActive)`
    en su ejemplo correcto de la 2.11.4.
- Pasada 2 (se pregunta): `StartRanked` y `StartPrivate` son iguales salvo el `MatchType` (guardas, `new Match` y
  `SeatEntrants`). Un `Start(MatchType, …)` privado tendría cuatro parámetros (2.2.2).
- Pasada 3 (se pregunta): `bool Abandon(…)` no dice qué significa `true` (que la partida terminó;
  `MatchAbandonmentService` lo guarda como `isMatchOver`). `LastPlayerCount = 1` se lee como «cuántos jugadores hubo al
  final», y en `if (activeParticipations.Count > LastPlayerCount)` significa «queda más de uno».
- Pasada 4: todos los miembros públicos se usan en producción.

**Decisiones del usuario:** `Participations => _participations` se queda como excepción de EF (**R-20**);
`FindParticipation` se queda (**R-21**: un operador LINQ con una lambda de una línea es una llamada); `Abandon` pasa a
`void` y `MatchAbandonmentService` pregunta `match.Status == MatchStatus.Finished`; las dos fábricas se quedan;
`LastPlayerCount` → `LastStandingPlayerCount`. Se aplicaron también la 9.4.1 (`ThrowIfNull(entrantsInTurnOrder)` en
las dos fábricas, fuera de `SeatEntrants`) y la 5.3.1 (`ListActiveParticipations`). La prueba
`Abandon_FourPlayersFirstLeaves_KeepsMatchGoing` comprueba ahora `MatchStatus.InProgress`. Compila el servidor
(carpeta aparte) y pasan 159 + 220 + 136 pruebas. Commit `6227c25`, sin push.

### 24 a 31. Los tipos pequeños de `Matches` (2026-11-10)

- **24. `MatchEndReason.cs`** (`Goal`, `Timeout`, `Resignation`, `Draw`, `Abandonment`): cumple. El código solo usa
  `Abandonment`, pero los cinco están en el `CHECK` `CK_Match_EndReason` y tienen filas en la base de prueba, que EF
  lee. Se quedan (como `MessageChannel`). **Cerrado sin cambios.**
- **25. `MatchEntrant.cs`** (`record MatchEntrant(int AccountId, short? EloRating)`): solo tipos por valor → R-16,
  posicional. `EloRating` es nulo en las partidas privadas. **Cerrado sin cambios.** Para `PrivateMatchCreator`: la
  línea 44 encadena `.ToList()` (5.3.1).
- **26. `MatchFormat.cs`** (`record MatchFormat(GameMode GameMode, byte ClockMinutes)` con `WallsPerPlayer` que toma el
  del modo): **R-11**, porque `GameMode` es una referencia sin comprobar → constructor con `ThrowIfNull(gameMode)`,
  que también pone `WallsPerPlayer` (R-03). `GameMode` y `ClockMinutes` quedan `{ get; }`, y `WallsPerPlayer`
  `{ get; init; }` porque se cambia con inicializador (`PrivateMatchCreator`) y con `with` (`TestMatch`).
- **27. `MatchStatus.cs`** (`InProgress`, `PendingClose`, `Finished`): `PendingClose` no lo usa el código ni tiene
  filas. Está en el `CHECK` `CK_Match_Status` y lo pide el CU-18 RN-11 (una partida que no se puede cerrar queda
  pendiente de cierre y se reintenta), que todavía no está hecho. Se pregunta.
- **28. `MatchType.cs`** (`Ranked`, `Private`): cumple y se usan los dos. **Cerrado sin cambios.**
- **29. `Participation.cs`**: entidad de EF de un jugador en una partida; la crea `Match` (constructor `internal`).
  - Pasada 1: cumple §2 (`_pawnSymbolsInTurnOrder` en plural), §6, §9 (la 9.4.1 no aplica a `internal`;
    `GetPawnSymbol` comprueba el rango con `ThrowIfLessThan`/`ThrowIfGreaterThan`). **R-04:**
    `return _pawnSymbolsInTurnOrder[turnOrder - Match.FirstTurnOrder];` resta dentro del `return` → `int symbolIndex`.
  - **Lectura L-14:** en el constructor, `RemainingClockMilliseconds = (int)TimeSpan.FromMinutes(format.ClockMinutes).TotalMilliseconds;`
    junta una llamada, una propiedad y un cast, que es lo que la R-04 separa, pero no es un `return`.
  - Pasadas 2 a 4: sin repetición; nombres claros; las propiedades que nadie lee son columnas que EF guarda.
- **30. `ParticipationResult.cs`** (`Won`, `Lost`, `Draw`): `Draw` no lo usa el código, pero está en el `CHECK` y en las
  filas de prueba. **Cerrado sin cambios.**
- **31. `PawnSymbol.cs`** (`Blue`, `Red`, `Green`, `Yellow`): cumple; los cuatro se usan. **Cerrado sin cambios.**

**Decisiones del usuario:** `PendingClose` se queda (CU-18 RN-11, pendiente de implementar); la R-04 vale en cualquier
línea donde un cast se junte con una llamada o una operación (**R-23**). Se aplicaron la R-11 en `MatchFormat`, la R-04
en `GetPawnSymbol` y la R-23 en `Participation` (reloj) y en `Match` (`placement` y `turnOrderNumber`, archivo ya
cerrado). `var clockTime = TimeSpan.FromMinutes(…)` usa `var` porque el tipo está a la vista (3.4.1, IDE0007).
Compila el servidor (carpeta aparte) sin advertencias y pasan 159 + 220 + 136 pruebas. Commit `78c7011`, sin push.
Con esto termina la carpeta `Matches`; sigue `Matchmaking`.

### 32. `src/Bastion.Domain/Matchmaking/MatchSearch.cs` (2026-11-10)

Búsqueda de un jugador en la cola clasificatoria, en memoria (no es entidad de EF). Lleva la confirmación de presencia
(a los 15 min sale «¿sigues ahí?» con 60 s para responder, `05-pendientes.md`). La usan `MatchmakingQueue` y
`MatchSearchService`.
- Pasada 1: §1, §3, §6 cumplen; §9 (`ThrowIfNull(nickname)`); 2.8.1 `class` porque cambia; **2.9.1 cumple**: redefine
  `Equals`/`GetHashCode` por `AccountId`, su clave de negocio (la R-01 no aplica, no es de EF). 2.11.1: lo que no cambia
  es `{ get; }`, y lo demás `private set`.
  - **R-04 (incumplimiento, tres `return`):** `ShouldStartPresenceCheck` y `HasPresenceExpired` restan fechas dentro de la
    condición del `return`, y `StartPresenceCheck` devuelve `now + PresenceResponseWindow` → la resta o la suma va
    antes en una variable; en `HasPresenceExpired`, guarda `if (PresenceRequestedAt is not DateTime requestedAt)` (4.7.1).
- Pasada 2: sin repetición.
- Pasada 3 (se pregunta): `IsAvailable()` no dice para qué está disponible (es `Status == Searching`: se puede emparejar
  y no espera respuesta de presencia). `StartPresenceCheck` devuelve la hora límite de la respuesta, y el nombre no lo
  dice (como la R-22, pero no es un `bool`).
- Pasada 4: todos los miembros se usan (`MatchmakingQueue`).

### 33. `src/Bastion.Domain/Matchmaking/MatchmakingRules.cs` (2026-11-10)

Reglas de la cola: `PlayersPerMatch = 2`, los minutos y segundos de la presencia, el modo (`Classic`) y el reloj
(5 min) de la partida clasificatoria, y dos `TimeSpan`.
- Pasada 1: 2.4.1 en plural → **R-07**: `MatchmakingPolicy`. **2.3.2 cumple**: los `TimeSpan` públicos son
  `public static TimeSpan X { get; } = …`, que es lo que pide la regla (`LockoutPolicy` ya lo hace igual).
- Pasada 2: `PlayersPerMatch = 2` es el `PlayerCount` del modo `CLASSIC` en el catálogo; si cambiaran por separado,
  `Match.SeatEntrants` rechazaría la partida. Lo usa solo `MatchmakingQueue`: se pregunta al revisarlo (4.4.2).
- Pasada 3: nombres claros.
- Pasada 4 (se pregunta): `PresenceCheckMinutes` y `PresenceResponseSeconds` son públicas y solo las usa esta clase
  para armar los `TimeSpan`; afuera se usan los `TimeSpan`. En `LockoutPolicy`, la constante de horas es privada.

### 34. `src/Bastion.Domain/Matchmaking/SearchStatus.cs` (2026-11-10)

`Searching`, `AwaitingPresence`: cumple (2.15.1) y se usan los dos. **Cerrado sin cambios.**

**Decisiones del usuario (32 y 33):** `IsAvailable` → `IsSearching`; `StartPresenceCheck` sigue devolviendo la hora límite
(al revisar `MatchmakingQueue`, el resultado va en `DateTime presenceDeadline = …`); `PresenceCheckMinutes` y
`PresenceResponseSeconds` pasan a `private`. Se aplicaron con la R-04 (las tres variables `timeSinceConfirmation`,
`waitingTime` y `presenceDeadline`) y la R-07 (`MatchmakingPolicy`). Cambian `MatchmakingQueue`, `RankedMatchCreator` y
tres archivos de pruebas. Compila el servidor (carpeta aparte) y pasan 159 + 220 + 136 pruebas. Un solo commit para los
dos archivos, porque `MatchSearch` usa la clase renombrada: `a3463d8`, sin push. Termina `Matchmaking`; sigue
`Moderation`.

### 35 a 38. `Moderation` (2026-11-10)

- **35. `BannedWord.cs`**: catálogo de EF de solo lectura (`BannedWordId`, `Term`, `Scope`), con un único constructor
  privado. Cumple (R-19 `class`; 2.11.1 sin `set` público). La columna `Language` de la base no se mapea porque el
  filtro todavía no distingue idiomas (CU-20 RN-01). Los tres miembros se usan (`BannedWordRepository`). **Cerrado sin
  cambios.**
- **36. `BannedWordScope.cs`** (`Nickname`, `Chat`, `Both`): `Nickname` no lo usa el código (el filtro de nicknames del
  CU-02 no está hecho), pero está en el `CHECK` y en filas de la base. **Cerrado sin cambios.**
- **37. `Sanction.cs`**: entidad de EF de una sanción; producción solo la lee (`SanctionRepository.ListChatSanctions`)
  para saber si un jugador está silenciado (`ChatModerator`, `ChatMute`).
  - Pasada 1: §1, §3, §6 cumplen; §9 sin referencias. **2.11.4 → R-17:** `public bool IsPermanent => EndedAt is null;`
    es un valor calculado → método `IsPermanent()` (2.2.3).
  - **Lectura L-15 (R-05):** `return RevokedAt is null && (IsPermanent || EndedAt > now);` mezcla `&&` y `||` con
    paréntesis; la R-05 admite condiciones cortas.
  - Pasada 2: sin repetición.
  - Pasada 3 (se pregunta): `EndedAt` está en pasado, pero es la fecha en que **termina** la sanción, aunque sea
    futura; `ChatMute` la llama `EndsAt`. La columna de la base es `EndedAt`.
  - Pasada 4 (se pregunta): `Revoke` solo lo usa una prueba (`TestSanction`). El constructor público solo lo usan las
    pruebas y los dobles: la sanción que arma no se podría guardar, porque le faltan columnas `NOT NULL`
    (`ModeratorId`, `SanctionType`, `Reason`). Producción nunca crea sanciones.
- **38. `SanctionScope.cs`** (`Account`, `Chat`): `Account` solo lo usan las pruebas, pero está en el `CHECK` y en filas
  de la base. **Cerrado sin cambios.**

**Decisiones del usuario (37):** `IsInEffectAt` con guardas, una pregunta por `if` (**R-24**); `EndedAt` → `EndsAt` con
`HasColumnName("EndedAt")` (constante `EndsAtColumn`); se quita `Revoke` y su prueba, y el constructor se queda (R-15:
es la única forma de que pruebas y dobles armen una sanción). Se aplicó la R-17 (`IsPermanent()`). Cambian
`SanctionConfiguration`, `ChatMute` y `TestSanction`. Una lectura de la base local confirmó `EndsAt → EndedAt`, y que
las sanciones 1 y 4, revocadas, no están en vigor. Compila el servidor (carpeta aparte) y pasan 158 + 220 pruebas (una
menos de dominio). Commit `3288d60`, sin push. Termina `Moderation`; sigue `Rooms`.

### 39 a 47. `Rooms` (2026-11-10)

- **39. `FailedCodeAttempts.cs`**: intentos fallidos de código de sala de un jugador (5 en 5 min); lo usa
  `RoomRegistry`.
  - **2.4.1 (incumplimiento):** el nombre está en plural (se pregunta el nuevo).
  - **R-17:** `public bool HasAttempts => _attemptTimes.Count > 0;` → método `HasAttempts()`.
  - **R-04:** `return _attemptTimes.Peek() + RoomRules.FailedCodeWindow - now;` → un paso por línea.
  - Pasada 2 (se pregunta): `_attemptTimes.Peek() + FailedCodeWindow` (cuándo caduca el intento más viejo) se repite en
    `GetRetryDelay` y en la condición del `while` de `ForgetOldAttempts`.
- **40. `RoomRules.cs`**: código de sala (6 caracteres), muros 1–20, relojes 3/5/10 (CU-09, `CK_Room_Settings`) e
  intentos fallidos.
  - **2.4.1 → R-07:** `RoomPolicy`, y su prueba `TestRoomPolicy`.
  - **5.2.1 (incumplimiento):** `code.All(character => CodeAlphabet.Contains(character))` solo reenvía el argumento →
    `code.All(CodeAlphabet.Contains)`.
  - Pasada 4: `FailedCodeWindowMinutes` es pública y solo la usa la clase para armar el `TimeSpan` → `private`, como en
    `MatchmakingPolicy` (D-07). `MinimumWallsPerPlayer` solo la usa la clase; `MaximumWallsPerPlayer`, la clase y una
    prueba (se pregunta).
  - Pasada 2 (se pregunta, candidato anotado): `CodeAlphabet` (con L) y `FriendCodePolicy.Alphabet` (sin L) son
    distintos, y cada uno coincide con su base: `CK_Room_Code` (`[A-HJ-NP-Z2-9]`) y `05_create_friends.sql`. Además,
    las salas validan con `All`/`Contains` y los códigos de amigo con un `Regex`.
- **41. `RoomIdentity.cs`** (`record (int RoomId, string Code)`) y **43. `RoomOpening.cs`** (`record (string Code, int
  HostId, DateTime OpenedAt)`): **R-11**, constructor con `ThrowIfNull(code)`.
- **42. `RoomMember.cs`**: miembro de una sala en espera (`class`, cambia de asiento y de «listo»). Cumple. Pasada 3 (se
  pregunta): `MarkReady(bool isReady)` se lee raro con `false` (`member.MarkReady(false)`), y `WaitingRoom` llama la
  misma acción `SetReady`.
- **44. `RoomSettings.cs`** (`record (GameMode, byte WallsPerPlayer, byte ClockMinutes)` con `IsValid()`): **R-11**,
  `ThrowIfNull(gameMode)`. `TestRoom` lo copia con `with { WallsPerPlayer = … }` → `WallsPerPlayer { get; init; }`.
  `IsValid` devuelve tres condiciones con `&&` (R-05).
- **45. `RoomStatus.cs`** (`Open`, `InMatch`, `Closed`): cumple; los tres se usan y están en `CK_Room_Status`.
  **Cerrado sin cambios.**
- **46. `Room.cs`**: entidad de EF de la sala (`Open`, `ChangeSettings`, `Close`, `StartMatch`, `FinishMatch`). Cumple
  §1–§9 (9.4.1, R-14, mensajes literales admitidos). Pasada 3 (se pregunta): `HostId` (y `RoomOpening.HostId`) frente a
  `WaitingRoom.HostAccountId` para lo mismo; la columna es `HostId`.
- **47. `WaitingRoom.cs`**: sala en espera en memoria (no es de EF).
  - **R-17:** `public int SeatCount => Settings.GameMode.PlayerCount;` es un valor calculado → método. Fuera del
    dominio, `RoomSnapshot` tiene la misma propiedad (se ve en su revisión).
  - **Lectura L-16 (2.11.4):** `public IReadOnlyList<RoomMember> Members => _members;` expone un campo con `=>`, y no es
    de EF (la R-20 no lo cubre).
  - Pasada 4 (se pregunta): `_kickedAccountIds` nunca recibe un valor (no hay método para expulsar; el CU-12 «Expulsar»
    es Must y no está hecho), así que `HasKicked` siempre da `false`, y la rama `RoomRejection.Kicked` de
    `RoomRegistry` nunca se cumple. `HasMember` es público y solo lo usa la clase (`Admit`).
  - Fuera del archivo: `RoomKeeper` (línea 69) repite la cuenta de `CanSeatAllMembers`.

**Decisiones del usuario (39 a 47):** `FailedCodeAttemptHistory`; `GetOldestAttemptExpiry()` privado (con la R-04
aplicada también a su `return`, que la vista previa traía con una suma); alfabetos separados; los límites de muros se
quedan públicos y `HasMember` pasa a `private`; `HostId` → `HostAccountId` en `Room` y `RoomOpening`
(`HasColumnName("HostId")`); `MarkReady` → `SetReady`; `Members => _members` se queda (**R-26**); `_kickedAccountIds` se
queda y el CU-12 se anota en `05-pendientes.md` (junto con el CU-18 RN-11 de `PendingClose`). Se aplicaron también la
R-07 (`RoomPolicy`), la R-11 (tres records), la R-17 (`HasAttempts()` y el privado `GetSeatCount()`, que solo usa la
clase), la 5.2.1 y la R-25 (`FailedCodeWindowMinutes` privada). Una lectura de la base local confirmó
`HostAccountId → HostId`. Compila el servidor (carpeta aparte) y pasan 158 + 220 + 136 pruebas. Commit `28d73c2`, sin
push. Termina `Rooms`; siguen `Sessions`, `Statistics` y `Text`.

### 48 a 52. `Sessions`, `Statistics` y `Text` (2026-11-10)

- **48. `ClientConnection.cs`** (`record (string IpAddress, string DeviceFingerprint, string ClientVersion)` y
  `MaximumIpAddressLength = 45`): **R-11**, constructor con tres `ThrowIfNull`. La constante la usan
  `SessionConfiguration` y `AccessLogConfiguration` (4.4.2); los largos de huella y versión solo los usa
  `SessionConfiguration` y viven ahí. Nombres claros.
- **49. `Session.cs`**: entidad de EF de una sesión de 24 h. Cumple (R-03, R-05 en `IsActiveAt`, R-02 en `TokenHash`).
  `MaximumLifetimeHours` la usan dos pruebas, así que no es un caso de la R-25 y se queda pública (el cambio se intentó
  y se deshizo al no compilar las pruebas). Pasada 4: `LastUsedAt` y `EndedAt` son columnas que EF lee
  (`IsActiveAt` usa `EndedAt`), pero ningún código las actualiza: la base dice que `LastUsedAt` se actualiza cada minuto
  y que `EndedAt` marca el cierre explícito. El cierre de sesión y el latido no están hechos. **Cerrado sin cambios.**
- **50. `SessionTicket.cs`**: `sealed class` inmutable (hash del token y hora de emisión), no es de EF →
  **2.8.1 (incumplimiento):** pasa a `sealed record` con el mismo constructor.
- **51. `ModeStatistic.cs`**: entidad de EF de solo lectura (Elo por modo); `DefaultEloRating` la usan los dos
  creadores de partidas. **Cerrado sin cambios.**
- **52. `Text/TextPattern.cs`**: creada en esta revisión (R-08). Cumple; el `var regex = …; return regex;` se admite
  (la R-14 también permitiría devolver el `new` directamente). **Cerrado sin cambios.**

Compila el servidor (carpeta aparte) y pasan 158 + 220 + 136 pruebas. Commit `cd96587`, sin push.
**Con esto termina la capa `Bastion.Domain`** (52 archivos). Sigue `Bastion.Server.Application` (130 archivos), en el
orden de sus carpetas: `Accounts`, `Auditing`, `Chat`, `Common`, `Friends`, `Matches`, `Matchmaking`, `Moderation`,
`PrivateChat`, `Rooms`, `Security`, `Sessions`. Pendientes anotados para esa capa (tabla «Candidatos a reutilizar» y
bitácoras): búsqueda por código de amigo repetida, `PlayersPerMatch` frente al catálogo, `presenceDeadline` en
`MatchmakingQueue`, `.ToList()` encadenados (5.3.1) en `PrivateMatchCreator`, `RoomKeeper` frente a
`CanSeatAllMembers`, `RoomSnapshot.SeatCount` con `=>`, `ListRecent(count)` del lobby, `readMessages` en `MarkRead`,
y `SignedInPlayer`/`SignedInSession`/`ToSignedInSession` (R-10).

## Capa `Bastion.Server.Application`

### 53 a 59. `Accounts` (2026-11-10)

- **53. `AccountRestrictedException.cs`**: 9.6.1 cumple (sealed, mensaje en inglés en el constructor, datos de solo
  lectura, un solo constructor porque lleva datos). **R-10:** el mensaje dice «cannot sign in» → «cannot log in».
  Pasada 2 (se pregunta): `LoginService` pasa `0` minutos tres veces (`Pending`, `Suspended`, `Banned`), un literal
  que significa «sin bloqueo».
- **54. `AccountRestriction.cs`** (`Locked`, `Pending`, `Suspended`, `Banned`): cumple y se usan todos. **Cerrado sin
  cambios.**
- **55. `IAccountRepository.cs`**: puerto de las cuentas; no es un servicio, así que no lleva documentación XML (7.1.1).
  Los seis métodos se usan. Pasada 3 (se pregunta): `FindByIdentifier(identifier)` junto a `FindById(accountId)`;
  «identifier» puede leerse como el Id, y es el apodo o el correo (`AccountPolicy.IsValidLoginIdentifier`). Nota:
  `PlayerIdentity` vive en `Friends`, pero la usan cuentas y chat (se ve en `Friends`).
- **56. `ILoginService.cs`**: es un servicio (`I…Service`) **sin documentación XML** → **7.1.1, 7.2.1 y 7.2.2
  (incumplimiento):** `<summary>` de la interfaz y de `LogIn`, `<param>` de `attempt` y `password`, `<returns>` y
  `<exception>` de `ArgumentNullException`, `InvalidCredentialsException` y `AccountRestrictedException`, como en
  `IMatchSearchService`. Los fallos al guardar salen como excepciones de EF (`UnitOfWork.SaveChanges` no las
  traduce, a diferencia de `MatchStoreException`), y la capa de aplicación no puede nombrarlas: se ve en `UnitOfWork`.
  **R-10:** devuelve `SignedInPlayer` → `LoggedInPlayer`.
  - **7.3.1 (incumplimiento de la solución):** `Directory.Build.props` pone `GenerateDocumentationFile` en `false` para
    todo, que es el ejemplo incorrecto de la regla. Se pregunta cuándo activarlo.
- **57. `InvalidCredentialsException.cs`**: sin datos → los tres constructores estándar (9.6.1, CA1032). **Cerrado sin
  cambios.**
- **58. `LoginService.cs`**: CU-01. Cumple §1–§6, §9 (guardas, `default` con `InvalidOperationException` porque el
  estado viene del objeto), §10 (inyección por constructor) y §11 (Info si entra, Warn si no; mensaje con
  `Clave=valor`).
  - **7.1.2 (incumplimiento):** falta `<inheritdoc/>` en la clase y en `LogIn`.
  - **R-14:** `return new AccountRestrictedException(AccountRestriction.Locked, account.GetRemainingLockMinutes(now));`
    lleva una llamada en un argumento → la cuenta de minutos va antes en una variable.
  - **R-10:** el mensaje de bitácora «Sign-in attempt processed» → «Login attempt processed».
  - Pasada 2 (se pregunta): en `AdmitByAccountStatus`, los casos `Pending`, `Suspended` y `Banned` repiten
    `throw Reject(new AccessLog(…), new AccountRestrictedException(…, 0));`.
- **59. `SignedInPlayer.cs`**: **R-10** → `LoggedInPlayer`. Es una clase inmutable que no es de EF → **2.8.1:**
  `sealed record` con el mismo constructor (R-11).

**Decisiones del usuario (53 a 59):** la 7.3.1 se activa **al terminar la capa**: cada servicio se documenta al revisar su
archivo, y al cerrar Application se pone `GenerateDocumentationFile` en su `.csproj`, con CS1591 como error en
`I*Service.cs` y apagado en lo demás (**R-27**). `FindByIdentifier` → `FindByLoginIdentifier` (parámetro
`loginIdentifier`). `AccountRestrictedException` gana un constructor sin minutos que encadena `: this(restriction,
NoLockMinutes)`. El `switch` de `AdmitByAccountStatus` se queda. Se aplicaron la documentación de `ILoginService` (7.1.1,
7.2.1, 7.2.2), `<inheritdoc/>` en `LoginService` (7.1.2), la R-10 (`LoggedInPlayer` y los mensajes «log in»), la 2.8.1 y la
R-14. Cambian `AccountRepository`, `AccountService`, `LoginTranslator`, `FakeAccountRepository` y `TestLoginService`.
Compila el servidor (carpeta aparte) y pasan 158 + 220 pruebas. Commit `31547fb`, sin push.

### 60. `Auditing/IAccessLogRepository.cs` (2026-11-10)

Puerto con `Add(AccessLog)`. Cumple; lo usa `LoginService`. **Cerrado sin cambios.**

### 61 a 81. `Chat` (2026-11-10)

Chat del lobby (en memoria, CU-20 sin canal propio todavía) y chat de partida (se guarda). En orden alfabético:
- **61. `ChatChannelForbiddenException`**: sin datos → tres constructores estándar (9.6.1). **Sin cambios.**
- **62. `ChatCooldown`**: espera de 3 s por jugador. Cumple §4 (2 niveles). Pasada 3 (se pregunta): la misma acción se llama
  `TryClaimTurn` (aquí, en `ILobbyChatRoom` y en `IPrivateChatRoom`) y `TryStartCooldown` (`IMatchChatRelay`); en un juego
  por turnos, «turn» se confunde con el turno de la partida (`_lastTurnByAccountId`, `lastTurn`).
- **63. `ChatHistoryEntry`**, **64. `ChatLine`**, **76. `LobbyChatHistory`** y **81. `PostedChatLine`**: records
  posicionales con referencias → **R-11**.
- **65. `ChatMessageRejectedException`**: dos constructores con datos (9.6.1). **Sin cambios.**
- **66. `ChatModerator`**: valida el largo, el silencio y las palabras prohibidas (CU-20 RN-01, RN-03, RN-05). **5.3.1:**
  `FindMute` encadena `.ToList()` (y su `var` no tenía tipo evidente, L-01) → secuencia con nombre y `new List<Sanction>(…)`.
- **67. `ChatMute`**: record solo de valores (R-16). **R-14:** `return new ChatMute(true, sanctions.Max(…));` lleva una
  llamada en un argumento → variable antes.
- **68. `ChatRejection`**, **69. `IChatBroadcaster`**, **73. `IMatchChatNotifier`**, **74. `IMatchChatRelay`** (salvo el
  nombre de la pregunta de la 62) y **75. `IMatchChatService`** (ya documentada): cumplen. **Sin cambios.**
- **70. `IChatModerator`**: no es un servicio (`I…Moderator`), sin documentación. Pasada 3 (se pregunta): `Screen` en un
  juego se lee como «pantalla»; el método valida el mensaje, lo recorta y lo devuelve.
- **71. `ILobbyChatRoom`**: Pasada 4 (se pregunta, anotado en el archivo 9): `ListRecent(int count)`; la sala ya guarda
  solo `MaximumRecentMessages` y el único llamador de producción pide justo eso.
- **72. `ILobbyChatService`**: servicio sin documentación → **R-27** (7.1.1, 7.2.1, 7.2.2).
- **77. `LobbyChatRoom`**: **5.3.1:** `ListRecent` encadena `.ToList()` dentro del `lock`.
- **78. `LobbyChatService`**: **10.1.1 (incumplimiento):** crea `new ChatModerator(unitOfWork)` dentro del constructor, en
  lugar de recibir `IChatModerator` como `MatchChatService` (la raíz de composición ya registra `IChatModerator`).
  `PrivateChatService` hace lo mismo (se ve en su revisión). **5.3.1:** `OpenLobbyChat` encadena `.Select(…).ToList()`.
  **R-14:** `return _chatRoom.Post(new ChatLine(…));` y `return new LobbyChatHistory(entries, _chatRoom.CountListeners(),
  _moderator.FindMute(…));` llevan llamadas en los argumentos. **7.1.2:** `<inheritdoc/>`.
- **79. `MatchChatRelay`**: cumple (salvo el nombre de la 62). **Sin cambios.**
- **80. `MatchChatService`**: documentado con `<inheritdoc/>`. **R-14:** `return _matchChatRelay.Post(…, new ChatLine(…), …);`.
- Pasada 2 (se pregunta): «moderar + esperar + `TooFast`» se repite en `LobbyChatService`, `MatchChatService` y
  `PrivateChatService`, cada uno con sus comprobaciones antes (participación, amistad).

**Decisiones del usuario (61 a 81):** `TryClaimTurn` → `TryStartCooldown` en todas las salas, con campos
`_lastMessageAtByAccountId`/`lastMessageAt` y `_cooldownLock`; `Screen` → `ScreenMessage`; `ListRecent()` sin parámetro
(la sala devuelve `new List<PostedChatLine>(_history)`); la repetición se queda en cada servicio. Se aplicaron la
10.1.1 (`LobbyChatService` recibe `IChatModerator`), la 5.3.1 ×3, la R-14 ×4, la R-11 ×4 y la R-27 (documentación de
`ILobbyChatService` e `<inheritdoc/>`). También cambian `IPrivateChatRoom`, `PrivateChatRoom` y `PrivateChatService`
(solo los renombres; su `new ChatModerator` se ve en `PrivateChat`) y tres archivos de pruebas (dos nombres de prueba
`TryClaimTurn_…` → `TryStartCooldown_…`, y `…_FirstTurn_…` → `…_FirstMessage_…`). Se quitó el `using System.Linq` que
dejó de usarse en `LobbyChatRoom`. Compila el servidor (carpeta aparte) y pasan 158 + 220 pruebas. Commit `2bb2c4f`,
sin push.

### 82 a 84. `Common` (2026-11-10)

`IPlayerActivity` (tres preguntas `Has`/`Is`), `IUnitOfWork` (los repositorios y `SaveChanges`) y `PlayerActivity` (reúne
el notificador, la cola y el registro de salas; tres parámetros). Cumplen y se usan. **Cerrados sin cambios.**

### 85 a 108. `Friends` (2026-11-10)

CU-21, CU-22, CU-24 y la presencia de amigos. En orden alfabético:
- **Records con referencias → R-11 (8):** `FriendPresenceChange` (87), `FriendRequestBoard` (91), `FriendRequestSummary` (94),
  `FriendRoster` (95), `FriendStatus` (96), `FriendSummary` (97), `PlayerIdentity` (107), `PlayerSearchResult` (108).
  Ninguno se copia con `with`.
- **Enumeraciones** `FriendPresence` (86), `FriendRelationship` (89), `FriendRequestOutcome` (92), `FriendshipRejection` (99):
  cumplen. `FriendshipRejectedException` (98): 9.6.1 con datos. **Sin cambios.**
- **Puertos** `IFriendNotifier` (101), `IFriendRequestRepository` (103), `IFriendshipRepository` (105), `IPlayerPresence`
  (106): cumplen, se usan. **Sin cambios.**
- **Servicios sin documentación → R-27:** `IFriendListService` (100), `IFriendPresenceService` (102),
  `IFriendRequestService` (104), con `<inheritdoc/>` en sus implementaciones.
- **85. `FriendListService`**: **5.3.1:** `ListFriends` encadena `.Select().OrderBy().ToList()`. Pasada 3 (se pregunta):
  en `RemoveFriend`, `if (friend is null || !_unitOfWork.Friendships.Remove(…))` borra dentro de la condición.
- **88. `FriendPresenceService`**: cumple (solo la R-27).
- **90. `FriendRelationshipResolver`**: **5.1.1 (incumplimiento):** la lambda de `FirstOrDefault` ocupa dos líneas →
  ayudante privado `Involves(request, accountId)`. **R-04:** `return request.IsSentBy(…) ? … : …;` → `if` y `return`.
- **93. `FriendRequestService`**: **5.3.1 ×4** (`SearchPlayers`, `ListFriendRequests` dos veces, `CreateRelationshipResolver`).
  Pasada 2 (se pregunta): en `ListFriendRequests` el filtro `ExpiresAt > now` se repite dos veces; `RejectFriendRequest`
  y `CancelFriendRequest` son iguales salvo quién es el solicitante; normalizar, validar y buscar por código se repite en
  `FindPlayerByCode`, `FindPlayers` y `PrivateChatService.FindPartner`; «verificar la sesión y buscar la identidad o
  `InvalidSessionException`» se repite en `FriendListService`, `VerifyPlayer` y `PrivateChatService`. Pasada 3 (se
  pregunta): `FindPendingRequest` también **borra** la solicitud caducada, y el nombre no lo dice.
  **Lectura L-17:** `return … ?? throw new …;` (`VerifyPlayer`, `FindPlayerByCode`).
- **107. `PlayerIdentity`** (6.4, se pregunta): vive en `Friends`, pero es la identidad pública de una cuenta y la usan
  cuentas, chat privado, el Host y los adaptadores.
- Nota para `Sessions`: `ConnectedPlayer` es una clase inmutable → 2.8.1 (`record`).

**Decisiones del usuario (85 a 108):**
- Nueva clase estática **`FriendCodeLookup.FindPlayer(accounts, enteredCode)`** en `Friends`. Normaliza, valida y busca,
  y devuelve `null` si el código no es válido o no tiene dueño. La usan `FindPlayerByCode`, `FindPlayers` y
  `PrivateChatService.FindPartner`.
- Dos ayudantes privados en `FriendRequestService`: `ListUnexpired(requests, now)` y
  `RemoveRequest(requesterAccountId, recipientAccountId, now)`.
- `return x ?? throw new X();` se admite (**R-28**).
- `PlayerIdentity` se mueve a `Accounts` (6.4).
- **`ISessionVerifier.VerifyIdentity`**, que devuelve `PlayerIdentity` desde la misma cuenta que lee `Verify`
  (privado `FindSessionAccount`). La usan `FriendListService.ListFriends`, `SendFriendRequest` y
  `AcceptFriendRequest`; `PrivateChatService` la adopta en su revisión.
- `FindPendingRequest` → `FindPendingRequestAndRemoveExpired`.
- `RemoveFriend` separa el borrado en `bool isRemoved`.

Se aplicaron la R-11 ×8, la R-27 ×3 (más `<inheritdoc/>`), la 5.3.1 ×5, la 5.1.1 (ayudante `Involves`) y la R-04 en
`FriendRelationshipResolver`. Los `using Bastion.Server.Application.Accounts` se agregaron en orden con un script
(`scratchpad/tools/add_using.py`). Se quitaron los `using …Friends` que quedaron sin uso y el `using Bastion.Domain.Friends`
de `PrivateChatService`. `FakeSessionVerifier` gana `Add(token, PlayerIdentity)` y `VerifyIdentity`, y las pruebas de
`FriendListService` y `FriendRequestService` registran la identidad en el verificador. Compila el servidor (carpeta
aparte) y pasan 158 + 220 pruebas. Commit `d486e69`, sin push.

### 109 a 115. `Matches` (2026-11-10)

- **109. `AbandonmentNotice`** (`record (string AbandoningNickname, bool IsMatchOver)`): **R-11**.
- **110. `IMatchAbandonmentService`**: ya documentada, pero **7.2.2 (incumplimiento):** faltaba
  `<exception cref="ArgumentNullException">` del `sessionToken`, que el método deja salir.
- **111. `IMatchEndNotifier`**, **112. `IMatchStore`** (sus ocho métodos se usan), **114. `MatchNotJoinedException`**
  (tres constructores estándar) y **115. `MatchStoreException`**: cumplen. El cuarto constructor
  `MatchStoreException(Exception)` lo usa `MatchStore` y fija el mensaje en inglés (9.6.1). **Sin cambios.**
- **113. `MatchAbandonmentService`**: documentado y con `<inheritdoc/>`; bitácora Warn/Info con `Clave=valor`.
  **5.3.1:** `new List<int>(recipientAccountIds)` se materializaba dentro de los argumentos de la llamada → en su propia
  instrucción.

Cerrados sin preguntas. Compila el servidor (carpeta aparte) y pasan 220 pruebas de aplicación. Commit `8e57acb`, sin
push.

### 116 a 134. `Matchmaking` (2026-11-10)

CU-09 (cola clasificatoria, emparejamiento y aviso de presencia). En orden alfabético:
- **Records con referencias → R-11:** `CreatedMatch` (116), `CreatedMatchParticipant` (117), `MatchPairing` (124),
  `QueueReview` (130). `PresenceRequest` (129) solo tiene valores (R-16). **Sin cambios.**
- **Cumplen, sin cambios:** `IMatchSearchService` (118, ya documentada con sus excepciones), `IMatchmakingNotifier` (119),
  `IMatchmakingPlayerVerifier` (120), `IMatchmakingQueue` (121), `IRankedMatchCreator` (122: patrón Try con
  `[NotNullWhen(true)]` en el `out` de referencia, como `Dictionary.TryGetValue`; la R-06 descartó atributos para el
  `DateTime` de `Account`, que es otro caso), `ITurnOrderShuffler` (123, genérico `TPlayer`, 2.13.1), `MatchSearchService`
  (125), `MatchmakingDispatcher` (126), `MatchmakingPlayerVerifier` (127), `SearchEndReason` (132), `SearchRejectedException`
  (133) y `SearchRejection` (134).
- **128. `MatchmakingQueue`**: lo anotado en el archivo 32: el resultado de `StartPresenceCheck` va en
  `DateTime presenceDeadline`. `TakePairings` cumple la 5.3.1 (un operador por línea y `new List`). Pasada 2 (se
  pregunta, candidato anotado): `MatchmakingPolicy.PlayersPerMatch = 2` es el `PlayerCount` de `CLASSIC` en el catálogo.
- **131. `RankedMatchCreator`**: **5.3.1 ×2:** `string.Join(…, pairing.Players.Select(…))` pasa la consulta sin guardarla, y
  `CreateEntrants` encadena `.ToArray()`. **R-14:** `return new CreatedMatch(matchId, format, ToParticipants(…));`. Captura
  solo `MatchStoreException` (9.3.1) y registra con la excepción aparte (11.3.1). Nota para `Rooms`: `PrivateMatchCreator`
  repite la búsqueda del Elo con `ModeStatistic.DefaultEloRating`.

**Decisión del usuario:** `PlayersPerMatch` se queda. La cola trabaja en memoria, y si el catálogo cambia,
`Match.SeatEntrants` rechaza la partida, el fallo se registra y se avisa a los jugadores. Se aplicaron la R-11 ×4,
`presenceDeadline` y, en `RankedMatchCreator`, la 5.3.1 ×2 y la R-14. Compila el servidor (carpeta aparte) y pasan 220
pruebas de aplicación. Commit `fa4b91d`, sin push.

### 135 y 136. `Moderation` (2026-11-10)

`IBannedWordRepository.ListChatTerms` e `ISanctionRepository.ListChatSanctions`: puertos que cumplen y se usan.
**Cerrados sin cambios.**

### 137 a 148. `PrivateChat` (2026-11-10)

- **Records con referencias → R-11 (6):** `ConversationPartner` (137), `ConversationSummary` (138), `PrivateConversation`
  (145), `PrivateMessageDelivery` (146), `PrivateMessageDraft` (147), `PrivateMessageEntry` (148).
- **139. `IMessageRepository`**: Pasada 3 (se pregunta, anotado en el archivo 14): `MarkRead(MessageParticipants
  readMessages, …)` se lee como una colección de mensajes (2.1.2), y es la pareja autor-destinatario.
- **140. `IPrivateChatRoom`**, **142. `IPrivateMessageNotifier`**, **143. `PrivateChatRoom`**: cumplen. **Sin cambios.**
- **141. `IPrivateChatService`**: servicio sin documentación → **R-27**.
- **144. `PrivateChatService`**:
  - **10.1.1 (incumplimiento, anotado en el archivo 78):** crea `new ChatModerator(unitOfWork)`. Recibirlo daría cuatro
    parámetros al constructor (verificador, unidad de trabajo, sala y moderador), y la **2.2.2** pide un DTO a partir de
    tres (se pregunta).
  - **5.1.1 (incumplimiento):** `ListConversations` tiene una lambda de seis líneas dentro de `Select`; además encadena
    `.ToList()` dos veces (5.3.1), una dentro de un argumento, y `.ToDictionary` al final.
  - **5.3.1:** `OpenConversation` encadena `.ToList()`. **R-14:** `return new PrivateConversation(new …, entries,
    _moderator.FindMute(…));`. **R-04:** `IsFriend` devuelve `ListFriendAccountIds(…).Contains(…)`.
  - Decidido en `Friends`: `SendPrivateMessage` usa `VerifyIdentity` en lugar de buscar la identidad al final.
    `FindPartner` e `IsFriend` pasan a recibir el `accountId`.

**Decisiones del usuario (137 a 148):**
- **`PrivateChatChannel(IPrivateChatRoom Room, IChatModerator Moderator)`** como DTO del constructor (2.2.2 con 10.1.1):
  `PrivateChatService(ISessionVerifier, IUnitOfWork, PrivateChatChannel)`. La raíz de composición registra
  `services.AddScoped<PrivateChatChannel>()`, y el contenedor lo arma por su constructor, sin `GetRequiredService`.
- `ListConversations` con un bucle `foreach`.
- `readMessages` → `participants`.
- **L-01 → R-29:** el diccionario de compañeros se crea con `var partnersById = new Dictionary<int,
  PlayerIdentity>(partnerIdentities.Count);` y se llena con un `foreach`, en lugar de `ToDictionary`. El usuario preguntó
  si el bucle saturaría la rutina con muchos datos: no, `ToDictionary` hace el mismo recorrido lineal por dentro y
  reserva la capacidad cuando conoce el tamaño; con la capacidad en el `new` el costo es igual. Aquí el tamaño es el
  número de conversaciones del jugador.

Se aplicaron la R-11 ×6, la R-27 (documentación de `IPrivateChatService` e `<inheritdoc/>`), la 5.3.1, la R-14 y la R-04.
Cambian `MessageRepository`, `ServiceRegistration`, `FakeMessageRepository` y `TestPrivateChatService`, que arma el
canal y registra la identidad en el verificador. Compila el servidor (carpeta aparte) sin avisos y pasan 158 + 220
pruebas. Commit `85ffd48`, sin push.
Quedan `ToDictionary` en dos consultas de EF (`MatchStore` línea 96 y `MessageRepository` línea 60). La 5.3.1 dice que
las consultas `IQueryable` siguen solo la 3.5; se ven al revisar esos archivos.

### 149 a 174. `Rooms` (2026-11-10)

CU-10 y CU-11 (salas privadas, código, listos, ajustes y partida privada). En orden alfabético:
- **Cumplen, sin cambios:** `IPrivateMatchCreator` (149), `IPrivateRoomService` (150, ya documentada), `IRoomCodeGenerator`
  (151), `IRoomKeeper` (152), `IRoomMatchService` (153, ya documentada), `IRoomMatchStarter` (154), `IRoomNotifier` (155),
  `IRoomPlayerVerifier` (156), `IRoomSettingsValidator` (158), `IRoomStore` (159), `RequestedRoomSettings` (162, solo
  valores, R-16), `RoomMatchStarter` (166), `RoomRejectedException` (170, dos constructores con datos), `RoomRejection`
  (171), `RoomSettingsValidator` (172) y `RoomStoreException` (174, como `MatchStoreException`).
- **9.4.1 (incumplimiento):** no comprueban `sessionToken` al inicio, porque lo dejan al verificador:
  `PrivateRoomService.SetReady`, `LeaveRoom` y `FindOwnRoom` (161), `RoomMatchService.StartMatch` (165) y
  `RoomPlayerVerifier.VerifyPlayerCanEnterRoom` (168).
- **160. `PrivateMatchCreator`**: **5.3.1 ×2** (`Select().ToArray()` dentro de un argumento, `Select().ToList()`), **R-14**
  (`return new CreatedMatch(…, ToParticipants(…))`) y **R-23** (`(byte)(Match.FirstTurnOrder + memberIndex)`).
- **161. `PrivateRoomService`**: **R-04** en `JoinRoom` (`return _roomKeeper.Join(player, code.Trim().ToUpper(…), now);`).
  Pasada 2 (se pregunta): esa normalización del código de sala es una regla del dominio, como `FriendCodePolicy.Normalize`.
- **163. `RoomDeparture`**: **R-11**.
- **164. `RoomKeeper`**: Pasada 2 (se pregunta, anotado en el archivo 47): `ChangeSettings` comprueba
  `hostedRoom.Members.Count > settings.GameMode.PlayerCount` antes de guardar, y `RoomRegistry.ChangeSettings` vuelve a
  comprobar `WaitingRoom.CanSeatAllMembers`: la misma regla en dos lugares.
- **165. `RoomMatchService`**: **R-04:** `return _matchStarter.StartMatch(…).MatchId;`.
- **167. `RoomMemberSnapshot`**: record posicional de **cinco** parámetros → **R-09/2.2.2 (incumplimiento):** se pregunta si
  se agrupa o pasa a propiedades `init`.
- **169. `RoomRegistry`**: **R-04** en `FindRoomOf` (`?:` con llamadas) y en `FindHostedRoom` (llamada anidada); **R-14** en los
  dos `new RoomDeparture(RoomSnapshot.Capture(room), …)`; **5.3.1** en `RemoveRoom` (`foreach` sobre un `Select` sin guardar;
  basta recorrer `room.Members`). Pasada 4 (se pregunta): `StartMatch<TResult>` es genérico y solo se usa con
  `CreatedMatch`. Nota: `_failedAttemptsByAccountId` nunca se vacía, así que guarda un historial por cada jugador que falló
  un código mientras el servidor sigue encendido.
- **173. `RoomSnapshot`**: **R-11**; **R-17:** `SeatCount =>` → método; **5.3.1** en `Capture` y en `ListAccountIdsExcept`
  (además, R-12); **R-14** en `CaptureMember` (`room.IsHost(…)` dentro del `new`).
- Pasada 2 (se pregunta): `MatchmakingPlayerVerifier.VerifyPlayerCanSearch` y `RoomPlayerVerifier.VerifyPlayerCanEnterRoom`
  hacen casi las mismas comprobaciones (canal de avisos, partida sin terminar, en sala), con distinta excepción.

**Decisiones del usuario (149 a 174):**
- `RoomMemberSnapshot` pasa a propiedades `required { get; init; }` con inicializador (R-09), en `CaptureMember` y en dos
  pruebas.
- `RoomPolicy.NormalizeCode` (recorta y pasa a mayúsculas invariantes) en el dominio.
- `RoomSnapshot.CanSeatAllMembers(settings)`, que usa `RoomKeeper.ChangeSettings`.
- `StartMatch<TResult>` se queda genérico (el registro no depende de Matchmaking).
- Los verificadores de jugador se quedan separados.
- `RoomRegistry` borra el historial de códigos fallidos de un jugador cuando queda vacío (`ForgetEmptyHistory`, después
  de revisar el límite). Queda una limitación: el historial de quien falló y no vuelve a intentar se queda hasta su
  siguiente intento.

Se aplicaron la 9.4.1 (cinco métodos), la 5.3.1 (`PrivateMatchCreator` ×2, `RoomSnapshot` ×2 y `RemoveRoom`, que ahora
recorre `room.Members`), la R-04 (`FindRoomOf` con `if`, `FindHostedRoom`, `RoomMatchService`, `JoinRoom`), la R-14, la
R-17 (`GetSeatCount()`, también en `RoomTranslator`), la R-23 y la R-11 (`RoomDeparture`, `RoomSnapshot`). Se quitó el
`using System.Linq` sin uso de `RoomRegistry`. `var closedRoom = RoomSnapshot.Capture(room);` usa `var` porque es un
método estático que devuelve su propio tipo (3.4.1). Compila el servidor (carpeta aparte) sin avisos y pasan 158 + 220
pruebas. Commit `1fd9813`, sin push.

### 175 a 182. `Security` y `Sessions` (2026-11-10)

- **175. `GeneratedToken`** y **178. `ConnectedPlayer`**: clases inmutables que no son de EF → **2.8.1:** `sealed record`
  (mismo constructor con `ThrowIfNull`). Commit `d4b645e`.
- **176. `IPasswordHasher`** (`Verify`, excepción de la 2.2.3), **177. `ISessionTokenGenerator`**, **179. `ISessionRepository`**,
  **180. `ISessionVerifier`**, **181. `InvalidSessionException`** (tres constructores estándar) y **182. `SessionVerifier`**
  (cambiado en `Friends` con `VerifyIdentity` y `FindSessionAccount`): cumplen. **Sin cambios.**

### Cierre de la capa `Bastion.Server.Application` (2026-11-10)

Según la R-27, se activó la verificación de la 7.3.1:
- `Bastion.Server.Application.csproj` pone `GenerateDocumentationFile` en `true`.
- `.editorconfig` apaga CS1591 en `[*.cs]` y lo hace error en `[I*Service.cs]`.

Las 11 interfaces `I…Service` de la capa están documentadas y compila sin avisos. Se comprobó que funciona: al quitar
el `<summary>` de `ILoginService`, la compilación falla con `error CS1591`; luego se restauró el archivo. Pasan
158 + 220 + 136 pruebas. Commit `7171c56`, sin push.

**Pendiente para la revisión de la configuración** (no se preguntó ni se cambió, por indicación del usuario): en
`.editorconfig`, «# 3.4.1 At most 120 characters per line» y «# 3.5.1 var only…» citan la numeración vieja (8.1.2). En
v2.4, la 3.4.1 es `var` y la 3.5.1 dice que no hay largo máximo de línea.

**Capa `Bastion.Server.Application` terminada** (archivos 53 a 182). Sigue `Bastion.Server.Adapters` (32 archivos). Pendientes
anotados para esa capa:
- `UnitOfWork.SaveChanges` no traduce las excepciones de EF.
- Los `ToDictionary` sobre `IQueryable` en `MatchStore` y `MessageRepository`.
- La proyección de caducidad en `FriendRequestRepository`.
- `FriendshipRepository.Remove` (orden menor/mayor y nombres `accountAId`/`accountBId`).
- `MessageConfiguration.TextLength = 500` frente a los 200 del dominio (4.4.2).

## Capa `Bastion.Server.Adapters`

### 183 a 200. Registro, contexto, configuraciones y convertidor (2026-11-10)

- **183. `AdaptersRegistration`** (raíz de composición de los adaptadores, 10.2.1) y **184. `TurnOrderShuffler`**
  (`ToArray` sobre una lista, no una consulta encadenada): cumplen. **Sin cambios.**
- **185. `BastionDbContext`**: Pasada 1 (se pregunta, anotado en la R-20): trece `DbSet<T> X => Set<T>();` con `=>`.
- **186 a 198. Configuraciones de EF:**
  - **9.4.1 (incumplimiento):** `Configure(builder)` es público y no comprueba `builder` en ocho de trece: `AccessLog`,
    `Account`, `BannedWord`, `FriendRequest`, `Friendship`, `Message`, `Sanction` y `Session`. Las otras cinco sí lo hacen.
  - Pasada 2 (se pregunta): `.HasConversion(new UpperSnakeCaseEnumConverter<X>()).HasMaxLength(N).IsUnicode(false)` se repite
    doce veces; `EndReasonLength = 15` está en `MatchConfiguration` y en `ParticipationConfiguration` para la misma
    enumeración (`MatchEndReason`).
  - **4.4.2 (se pregunta, anotado en el archivo 9):** `MessageConfiguration.TextLength = 500`, que coincide con
    `Message.Text NVARCHAR(500)` de la base, mientras que el dominio limita a 200 (`ChatPolicy.MaximumMessageLength`).
- **199. `UpperSnakeCaseEnumConverter`**: la 5.2.1 no aplica a `value => ToCode(value)`: `ValueConverter` recibe
  `Expression<Func<…>>`, y un grupo de método no se convierte en árbol de expresión. **R-25:** `ToCode` y `FromCode` son
  públicos y solo los usa la clase → `private`.
- **200. `DeletedRowCount`**: objeto de datos para `SqlQuery` (2.11.3, `get; set;`). **Sin cambios.**

**Decisiones del usuario (183 a 200):**
- Los `DbSet<T> X => Set<T>()` se quedan como patrón de EF (**R-31**).
- `MessageConfiguration` usa `ChatPolicy.MaximumMessageLength` y el script `02_create_tables.sql` pasa
  `Message.Text` a `NVARCHAR(200)`. Los mensajes de prueba miden como mucho 77 caracteres. **De momento solo el
  script**: la base local sigue con `NVARCHAR(500)`, y cambiarla pide quitar y recrear `CK_Message_Text`.
- `EndReasonLength` es una sola constante pública en `MatchConfiguration`, que usa `ParticipationConfiguration`.
- Las 14 columnas de enumeración (no eran 12) usan el nuevo **`EnumColumnMapping.HasUpperSnakeCaseConversion(largo)`**:
  - Tiene dos sobrecargas, para `PropertyBuilder<TEnum>` y `PropertyBuilder<TEnum?>`, porque `TEnum?` es
    `Nullable<TEnum>` y no cumple `struct`.
  - El cuerpo está una sola vez, en el privado `StoreAsCode<TEnum>(PropertyBuilder, largo)`, sobre la clase base.
  - El usuario preguntó la diferencia entre las dos: no son constructores, sino sobrecargas para propiedades que no
    admiten nulos y para las que sí.

Se aplicaron la 9.4.1 (ocho `Configure`) y la R-25 (`ToCode`/`FromCode` privados; los árboles de expresión del
convertidor siguen funcionando). Se quitó el `using …Conversions` de las configuraciones que ya no usan el convertidor.
Una lectura de la base local confirmó las enumeraciones, también las anulables y una dentro de una consulta, y el largo
200 del modelo. Compila el servidor (carpeta aparte) sin avisos y pasan 158 + 220 pruebas. Commit `12b9ebe`, sin push.

**PR #15 fusionado** en `main` (`2eb1167`). La revisión sigue en la rama **`review-standard-v2.4-repositories`**, creada
desde ese `main`. Por indicación del usuario, en esta rama solo se hacen commits locales; el push espera a que él lo pida.

### 201 a 208. Repositorios de `Adapters` (2026-11-10)

Son consultas de EF sobre `IQueryable`. La 5.3.1 las exceptúa («se rige solo por la Sección 3.5»), pero la R-04 y la 5.1.1 sí
aplican.
- **201. `AccessLogRepository`** y **208. `SessionRepository`** (`FirstOrDefault` con una lambda de una línea, R-21): cumplen.
  **Sin cambios.**
- **Lectura L-18 (R-04 en consultas de EF):** casi todos los métodos devuelven la cadena entera
  (`return _context.X.Where(…).Select(…).ToList();`), en `AccountRepository` (4), `BannedWordRepository`, `FriendRequestRepository`
  (2), `FriendshipRepository` (3), `MessageRepository` (2) y `SanctionRepository`.
- **Lectura L-19 (5.1.1 en consultas de EF):** hay lambdas de varias líneas en condiciones largas: `AccountRepository.SelectActivePlayers`,
  `FriendRequestRepository.FindBetween` (pareja en los dos sentidos), `FriendshipRepository.ListFriends` (condición y proyección),
  `MessageRepository.ListConversation` y `MarkRead`, y la proyección de `FriendRequestRepository.ListSummaries` (cuatro
  líneas). En EF no se puede usar un grupo de método, porque la consulta necesita un árbol de expresión.
- Pasada 2: `new PlayerIdentity(account.AccountId, account.Nickname, account.FriendCode)` se repite en seis proyecciones
  (`AccountRepository` ×4, `FriendRequestRepository`, `FriendshipRepository`). `ListSummaries` repite la fórmula de
  caducidad de `FriendRequest.GetExpirationTime` (anotado en el archivo 16). `FriendshipRepository.Remove` repite el orden
  menor/mayor del constructor de `Friendship`, con variables `accountAId`/`accountBId` (anotado en el archivo 17).
- **3.4.1:** `MessageRepository.ListConversation` usa `var latestFirst = ….ToList();`, y `ToList` no está en la lista de la 3.4.1.
- **5.1.2 (hallazgo nuevo):** lambda dentro de lambda en `MessageRepository`: `conversation.Max(message => …)` y
  `setters.SetProperty(message => message.ReadAt, readAt)`.

**Decisiones del usuario (201 a 208):**
- **R-32 (L-18 → D):** toda consulta de EF sigue la forma de la 5.3.1. La consulta va en un `IQueryable<T>` con nombre en
  plural y el método devuelve `new List<T>(consulta)`. Las de valor único hacen `FirstOrDefault()` en una variable o en
  un ayudante. Los métodos privados que arman una consulta (`Select…`) la guardan en una variable y devuelven la
  variable, o una sola llamada (`a.Concat(b)`).
- **R-33 (L-19 → A):** las consultas de EF se parten en pasos simples:
  - una condición `&&` por `.Where`; EF las une con `AND`;
  - una pareja en los dos sentidos se resuelve con `Concat` de dos consultas de un sentido (`UNION ALL`), o con dos
    búsquedas por clave unidas con `??` (9.4.2);
  - `GroupBy(clave, elemento)` y `.Select(ids => ids.Max())`, sin lambda anidada (5.1.2);
  - `ExecuteUpdate(setters => setters.SetProperty(_readAt, readAt))`, con el selector en un campo estático
    `Expression<…>`;
  - las proyecciones anidadas traen la entidad y arman el resultado en memoria con un método (grupo de método, 5.2.1).
- `FriendshipRepository.Remove`: `smallerAccountId`/`largerAccountId`.

**Aplicado** en la rama `review-standard-v2.4-repositories` (sin commit todavía):
- `AccountRepository`: cuatro consultas con D; los ayudantes privados `FindIdentity(IQueryable<Account>)` y
  `ListIdentities(IQueryable<Account>)`; `SelectActivePlayers` con dos `.Where` y `AsNoTracking`.
- `BannedWordRepository` y `SanctionRepository` siguen D; el `&&` de la sanción quedó en dos `.Where`.
- `FriendRequestRepository`:
  - `FindBetween` es `FindSent(a, b) ?? FindSent(b, a)`, con `DbSet.Find` por la clave (RequesterId, RecipientId);
  - `ListSummaries` hace el `Join` hacia el tipo privado anidado `RequestWithCounterpart` (constructor explícito, R-11);
  - el mapeo va en memoria con `ToSummary`, que usa `GetExpirationTime()` y ya no copia la fórmula de caducidad.
- `FriendshipRepository`: `ListFriends` lleva dos `.Where` y mapea en memoria (`ToFriendSummary`);
  `SelectFriendAccountIds` tiene dos consultas con nombre y un `Concat`; los nombres de `Remove` cambiaron.
- `MessageRepository`:
  - `ListConversation` hace un `Concat` de `SelectMessagesFrom` en los dos sentidos (`conversationMessages`, plural);
  - `ListLatestPerPartner` usa `GroupBy` con un selector de elemento;
  - `CountUnreadByAuthor` proyecta a `KeyValuePair<int, int>` y devuelve `new Dictionary<int, int>(consulta)`;
  - `MarkRead` usa el campo `_readAt`.
- **Pasada 2:** `new PlayerIdentity(account.AccountId, account.Nickname, account.FriendCode)` estaba **ocho** veces: seis en
  `Adapters` y dos en `Application` (`FriendPresenceService`, `SessionVerifier`). Ahora es la fábrica
  `PlayerIdentity.FromAccount(Account)` (`Application`, con `ThrowIfNull`).

**Verificación:**
- Se hizo una foto de lo que devuelven los repositorios en la base local antes y después, solo leyendo: 43 líneas
  **idénticas**.
- Se revisó el SQL: `INNER JOIN` en `ListSummaries`, `GROUP BY … COUNT(*)` con `KeyValuePair`, `MAX` sin lambda
  anidada, dos `SELECT TOP(1)` por clave en `FindBetween` y `UPDATE … SET ReadAt` en `MarkRead`. `MarkRead` se probó
  con las cuentas -1 y -2, que no existen, dentro de una transacción deshecha: no tocó ninguna fila.
- Compila sin avisos de código (solo los NU1902/NU1903 de NuGet, que ya estaban). Pasan 158 + 220 + 136 pruebas.
- Precio conocido del mapeo en memoria: las lecturas de identidad traen todas las columnas de `Account`, también
  `PasswordHash`, `PasswordSalt` y `Email`.

**Preguntas antes del commit:**
1. Dónde vive el mapeo a `PlayerIdentity`. Está aplicada la fábrica en `PlayerIdentity`. El usuario preguntó si
   convenía un **ensamblado propio** como referencia central para `Application` y `Adapters`, y se analizó así:
   - Las referencias son `Application → Domain`, `Adapters → Domain, Application` y `Host → Contracts, Application, Adapters`.
   - El mapeo necesita `Account` (`Domain`) y `PlayerIdentity` (`Application`). Un ensamblado que solo tenga el mapeo
     tendría que referenciar `Application`, y entonces `Application` no podría usarlo (referencia circular). Sus dos
     copias se quedarían.
   - Para que sirva a las dos capas, `PlayerIdentity` tendría que mudarse a ese ensamblado. Eso cambia 30 archivos que
     usan el tipo (3 de `Adapters`, 16 de `Application`, 2 de `Host` y 9 de pruebas), agrega un octavo proyecto para un
     método de seis líneas y saca de `Application` un tipo que forma parte de su puerto `IAccountRepository`.
   - No hay más mapeos repetidos que lo llenen: las demás construcciones desde entidades (`ConnectedPlayer`, `Session`,
     `Friendship`, `RoomSnapshot`, `MatchFormat`) aparecen una sola vez.
   - Por analogía con la 4.4.2 («en la capa más interna que lo necesita»), la capa más interna que conoce los dos
     tipos es `Application`, y `Adapters` ya la referencia. **Se recomendó mantener la fábrica.** Falta la respuesta
     del usuario.
   - El usuario preguntó si la variante 1 llevaba **inyección de dependencias** para reducir el acoplamiento. Como se
     describió, no la llevaba: era una referencia directa. Se analizó con inversión de dependencias:
     - La interfaz `IPlayerIdentityMapper` iría en `Application`; la 2.14.2 admite el sustantivo porque su lista es
       abierta. La implementación iría en `Bastion.Server.Mapping → Application, Domain` y se registraría en `Host`.
       Con eso desaparece la referencia circular.
     - Cambia mucho:
       - `FriendPresenceService` y `SessionVerifier` pasan de dos a tres parámetros, el tope de la 2.2.2;
       - `UnitOfWork` pasa de uno a dos y le pasa el mapper a tres repositorios, que también pasan de uno a dos;
       - `Host` registra el servicio y referencia el proyecto nuevo;
       - dos pruebas tendrían que referenciar ese proyecto, o un falso que copie el mapeo por novena vez.
     - **No reduce el acoplamiento:** cinco clases suman una dependencia más y no se elimina ninguna. La 10.1.1 pide
       inyectar solo un servicio externo (entrada y salida, estado compartido o resultado no determinista), y un mapeo
       puro no es ninguno de los tres; no tiene otra implementación que cambiar ni nada que simular en una prueba.
       La inyección sería obligatoria si el mapeo llegara a necesitar un servicio externo, por ejemplo la presencia
       o un dato guardado aparte.
     - La variante ligera sería la misma interfaz con la implementación en `Adapters`, sin proyecto nuevo. Tiene el
       mismo costo en constructores y pruebas.
2. `CountUnreadByAuthor`: **el usuario eligió A** (`new Dictionary<int, int>(IQueryable<KeyValuePair<…>>)`, ya aplicada).

**Decisión final de la pregunta 1:** el usuario mantuvo la fábrica `PlayerIdentity.FromAccount` (**R-34**), sin ensamblado
propio y sin inyección.

Commit `f570f4f`, sin push.

### 209. `MatchStore` (2026-11-10)

Abre un contexto nuevo por operación (`IDbContextFactory`), porque lo usan servicios que viven más que una petición.
- **Pasada 1:**
  - **Sin hallazgos:** §1, §3, §5.1/5.2, §6 y §8 (no tiene comentarios).
  - **§9:** traduce `DbUpdateException` y `DbException` a `MatchStoreException`, conservando la interna (9.2.1). Las
    dos jerarquías no se relacionan, así que el orden da igual (9.1.2). Tiene `using` en el contexto (9.5.1) y
    `ThrowIfNull` en los públicos (9.4.1).
  - **§10:** `IDbContextFactory` se inyecta (10.1.1).
  - **No aplican:** §7 (no es un servicio), §11 (no escribe bitácora) y §12.
  - **2.14.2 (incumplimiento, no se vio al revisar `Application`):** la regla fija que "Store guarda y recupera datos
    locales del cliente". `MatchStore` y `RoomStore` guardan en SQL Server, desde el servidor. El uso correcto está en
    el cliente: `LanguagePreferenceStore`. La familia `IMatchStore`/`MatchStore`/`MatchStoreException`/`FakeMatchStore`
    y la de `Room` aparecen en 34 archivos: 3 de `Adapters`, 17 de `Application`, 5 de `Host` y 9 de pruebas.
  - **R-32/R-33, aplicadas:** seis consultas. `LoadEloRatingsByAccountId` pasa de `ToDictionary` a
    `new Dictionary<int, short>(consulta de KeyValuePair)`, y cada `&&` va en su propio `.Where`.
- **Pasada 2:**
  - `!participation.Result.HasValue` se repetía en dos consultas; ahora es `SelectUnfinishedParticipations`
    (4.4.1, aplicado, como `SelectActivePlayers`).
  - `Add` + `SaveChanges` + `return id` aparece en `AddMatch`, `AddMatchChatMessage` y `RoomStore.AddRoomInContext`
    (se pregunta).
  - `RunInNewContext` es idéntico en `RoomStore` salvo por el tipo de excepción; se pregunta en el archivo 210.
- **Pasada 3:** `UpdateMatch` también termina la sala de una partida privada, y su nombre no lo dice (se pregunta).
- **Pasada 4:** sus ocho métodos se usan (archivo 112). Nadie usa el `int` que devuelve `UpdateMatch` (las filas de
  `SaveChanges`); existe porque `RunInNewContext` pide un resultado. `RoomStore.UpdateRoom` hace lo mismo (se pregunta).
- **Verificación:** una foto de las lecturas en la base local, antes y después, solo leyendo: 48 líneas idénticas.
  Cubre las cuentas 1 a 14, los tres modos, el Elo de cuatro modos y nueve partidas más una inexistente. El SQL quedó
  igual: `EXISTS`, `TOP(1)`, `IN (…)` y `TOP(1)` con `LEFT JOIN`. Compila sin avisos de código. Ninguna prueba cubre
  `Adapters`.

**Preguntas (209):**
1. 2.14.2: renombrar la familia `Store` del servidor (recomendado: `Repository`, en un commit aparte, también `Room`).
2. `UpdateMatch`: nombre y `int` sin uso (recomendado: `UpdateMatchAndRoom`, y mantener el `int` que pide el runner).
3. `Add` + `SaveChanges` repetido (recomendado: dejarlo).

**Decisiones del usuario (209): A en las tres.**
- `UpdateMatch` → `UpdateMatchAndRoom`; el `int` se queda. `Add` + `SaveChanges` se queda en cada método.
  Commit `49b5d37`, sin push.
- **R-35** (2.14.2): renombre en un commit aparte, `c229563`, sin push:
  - las familias `Match` y `Room` pasan de `Store` a `Repository` (interfaz, clase, excepción y falso);
  - cambian también los campos `_matchStore`/`_roomStore`, los mensajes de las excepciones y de bitácora de `Host`
    y el `<exception>` de `IMatchChatService`;
  - en las pruebas, `StoreFailureMessage` → `RepositoryFailureMessage`, y cuatro nombres `…StoreFails…`/`…InStore…`
    pasan a `Repository`.
  - Son 36 archivos (ocho con `git mv`). Git ve las dos excepciones como alta y baja porque se parecen solo un 40%.
  - Compila sin avisos de código, pasan 158 + 220 + 136 pruebas, y la foto de las lecturas sigue idéntica con el nombre
    nuevo.
- **Quedan para la revisión de las pruebas:** las propiedades `AccountStore`, `BannedWordStore` y `SanctionStore` del
  falso de la unidad de trabajo, y su método `Store(…)`.
- **Observación:** `MatchRepository` y `RoomRepository` siguen en `Persistence/`, no en `Persistence/Repositories/`
  con los de la unidad de trabajo. Lo único que se decidió fue el nombre.

### 210. `RoomRepository` (antes `RoomStore`) (2026-11-10)

Como `MatchRepository`, abre un contexto por operación. `CloseOpenRooms` solo se usa al arrancar el servidor
(`RoomBackgroundService.CloseRoomsLeftOpen`).
- **Pasada 1:**
  - **Sin hallazgos:** §1, §2 (con R-35 ya aplicada), §3, §6 y §8.
  - **§9:** `using` en el contexto y en la transacción de `AddRoomMatch` (9.5.1), traducción con la excepción interna
    (9.2.1) y `ThrowIfNull` en los públicos (9.4.1).
  - **§10:** correcta.
  - **No aplican:** §7, §11 y §12.
  - **5.1.2 (incumplimiento, corregido):** `ChangeRoomSettings` y `CloseRoom` escribían `room => …` dentro de
    `context => UpdateRoom(…)`. Ahora la acción va antes, en `Action<Room> changeSettings` / `closeRoom`. Partirlo en
    métodos privados no servía: tendrían cuatro parámetros (2.2.2).
  - **5.1.1 y 5.1.2 (incumplimiento, corregido):** `CloseOpenRoomsInContext` tenía una lambda de tres líneas con dos
    lambdas adentro. Ahora usa `ExecuteUpdate(setters => SetClosed(setters, closedAt))`, y cada `SetProperty` va en su
    línea dentro de un método aparte. Es distinto del campo `Expression` de la R-33, porque esa forma dejaba una línea de
    unos 130 caracteres; se pregunta.
  - **R-32/R-33:** los dos `Any(a && b)` pasan a consulta con nombre, un `.Where` por condición y `Any()`.
- **Pasada 2:**
  - `room.Code == code` se repetía en dos consultas; ahora es `SelectRoomsWithCode` (aplicado, 4.4.1).
  - `RunInNewContext` es idéntico al de `MatchRepository` salvo el tipo de excepción (se pregunta).
  - El `ExecuteUpdate` de `CloseOpenRooms` copia en SQL lo que hace `Room.Close` (`Closed` y `LastActivityAt`)
    (se pregunta).
- **Pasada 3:**
  - `UpdateRoom` solo aplica el cambio si la sala está abierta.
  - `AddRoomMatch` agrega la partida y además pasa la sala a `InMatch`, como `UpdateMatchAndRoom`.
  - Los privados están en otro orden que los públicos (se pregunta).
- **Pasada 4:** los siete métodos se usan. El `int` de `UpdateRoom` se queda, como el de `UpdateMatchAndRoom` (209, P2).
- **Verificación:**
  - Se usó una foto con un interceptor que bloquea toda escritura y solo imprime su SQL.
  - La base solo tiene dos salas, las dos cerradas, así que la foto incluye el SQL de cada lectura.
  - Antes y después salen 22 líneas idénticas: `EXISTS` con `Code` y `Status`, `TOP(1)` por `RoomId`, y el `UPDATE … SET
    Status, LastActivityAt WHERE Status = 'OPEN'`, que se bloqueó.
  - `CloseRoom` y `ChangeRoomSettings` se llamaron sobre salas cerradas y una inexistente, y no escribieron.
  - Compila sin avisos de código.

**Preguntas (210):**
1. `RunInNewContext` repetido (recomendado: clase base genérica `ContextPerOperationRepository<TFailure>`).
2. Carpeta (recomendado: mover los dos a `Persistence/Repositories/`).
3. Nombres y orden de los privados (recomendado: `UpdateOpenRoom`, `AddMatchAndStartRoom` y el orden de los públicos).
4. `CloseOpenRooms` (recomendado: cargar las salas abiertas y llamar a `Room.Close` en cada una).

**Decisiones del usuario (210): P2 A, P3 A y P4 A.** Aplicadas, sin commit todavía:
- `MatchRepository` y `RoomRepository` se movieron con `git mv` a `Persistence/Repositories/`, con el espacio de nombres
  `…Persistence.Repositories`. `AdaptersRegistration` tiene el `using` nuevo.
- `UpdateRoom` → `UpdateOpenRoom` y `AddRoomMatch` → `AddMatchAndStartRoom`. Los privados siguen el orden de los
  públicos.
- `CloseOpenRoomsInContext` carga las salas abiertas, llama a `Room.Close` en cada una y devuelve `SaveChanges()`. Se
  quitaron `SetClosed` y el `using …Query`.
- **Verificación:** la foto de `MatchRepository` sigue idéntica. La de `RoomRepository` cambia solo en `CloseOpenRooms`:
  antes era el `UPDATE` (bloqueado) y ahora es el `SELECT … WHERE Status = 'OPEN'`. El resultado sigue en 0. Como no hay
  salas abiertas, el camino de escritura no se pudo probar sin escribir. Compila sin avisos de código.

**P1, pendiente:** el usuario preguntó si en lugar de la clase base se puede hacer una **clase auxiliar** que maneje las
excepciones en un solo lugar. Sí se puede, por composición:
- `NewContextRunner<TFailure> where TFailure : Exception`, en `Persistence/`, recibe `IDbContextFactory` y
  `Func<Exception, TFailure>`;
- su `Run<TResult>(operation)` tiene el único `try`/`catch` de `DbUpdateException` y `DbException`;
- cada repositorio guarda un campo `_newContextRunner` y lo crea en su constructor con
  `innerException => new MatchRepositoryException(innerException)`. Lo permite la excepción de la 10.2.1: crea una parte
  que comparte su tiempo de vida.

Se recomendó sobre la clase base: el mismo código queda en un solo lugar, sin herencia, y con un poco menos en cada
repositorio. Falta la respuesta del usuario.

El usuario pidió **más propuestas**, cada una con su técnica, pros, contras y razonamiento. Datos que se usaron:
- Las dos excepciones se atrapan en 10 lugares (1 en `Application`, 9 en `Host`). Solo `RoomService` atrapa las dos, y
  las convierte en el mismo `FaultException`; lo único que cambia es el texto de la bitácora.
- `IRoomMatchService` documenta las dos con significados distintos.
- Hay 13 `catch (DbException|DbUpdateException)` en `Host`/`Application`, porque `UnitOfWork.SaveChanges` no traduce
  (archivo 211). Ese archivo necesita la misma traducción, pero no un contexto nuevo por operación.

Las propuestas:
- **D.** Separar un `DatabaseFailureTranslator<TFailure>` (solo el `try`/`catch`, SRP), que `NewContextRunner` usa y que
  `UnitOfWork` podría usar en 211. **Recomendada.**
- **E.** Unir las dos excepciones en una sola y usar un ejecutor no genérico inyectado por interfaz. Cambia el contrato
  en `Application` y `Host`; conviene decidirlo con la 211.
- **F.** Un proxy dinámico (`DispatchProxy`, AOP). **G.** Interceptores de EF. **H.** Esperar a la regla de tres.
- **Descartadas:** un `catch (Exception) when` (la 9.3.1 lo prohíbe), un tipo `Result` (va contra la §9) y juntar los dos
  repositorios en una clase.

**Decisión del usuario: P1 → D (R-36).** Commit `7c50e46`, sin push, que también lleva P2, P3 y P4:
- Hay dos clases nuevas en `Persistence/`:
  - `DatabaseFailureTranslator<TFailure>`, con el único `try`/`catch` de `DbUpdateException`/`DbException`;
  - `NewContextRunner<TFailure>`, que abre el contexto y lo usa.
- Los dos repositorios guardan `_newContextRunner` y ya no tienen `_contextFactory`, `RunInNewContext` ni
  `using System.Data.Common`.
- **Verificación:** las fotos de `MatchRepository` (48 líneas) y de `RoomRepository` (frente a P4) siguen idénticas.
  Compila sin avisos de código y pasan 158 + 220 + 136 pruebas.

**Hallazgo nuevo (de la prueba de falla, se pregunta):**
- Contra una base que no existe, los dos repositorios dejan salir una `InvalidOperationException` que envuelve la
  `SqlException` ("likely due to a transient failure… EnableRetryOnFailure").
- La estrategia de ejecución de SQL Server envuelve así los errores transitorios cuando no hay reintentos, y la
  aplicación usa `UseSqlServer` sin `EnableRetryOnFailure`.
- Ese tipo no es `DbUpdateException` ni `DbException`, así que no se traduce y no lo atrapa ningún
  `catch (…RepositoryException)`.
- Es anterior a la D, porque los `catch` eran los mismos. La D deja un solo lugar donde corregirlo.

Se probaron estrategias de EF contra fallas reales, sin tocar la base:

| Falla | Por defecto | `NonRetryingExecutionStrategy` | `EnableRetryOnFailure(2, 1 s)` |
| --- | --- | --- | --- |
| Base que no existe (transitoria) | `InvalidOperationException` ← `SqlException` (se escapa) | `MatchRepositoryException` ← `SqlException` | `RetryLimitExceededException` (hereda de `Exception`, se escapa) |
| Puerto cerrado (no transitoria) | `MatchRepositoryException` | `MatchRepositoryException` | — |

**Consecuencias de que se escape:**
- `RankedMatchCreator` solo atrapa `MatchRepositoryException`. `MatchmakingDispatcher` no atrapa nada, y
  `MatchmakingBackgroundService.ExecuteAsync` tampoco. En .NET, una excepción en un `BackgroundService` detiene el host
  por defecto, y no hay `HostOptions` configuradas: **se cae el servidor**.
- `Host` no tiene `IErrorHandler`. En un servicio WCF, la excepción llega a CoreWCF como falla genérica, y en un canal
  con sesión el canal queda en `Faulted`.

Propuestas que se dieron al usuario:
- **A.** Un `catch` con filtro en el traductor.
- **B.** Reintentos de EF.
- **C.** Dejarlo pendiente.
- **D.** `NonRetryingExecutionStrategy` en `AdaptersRegistration`: corrige la causa en la raíz de composición y ya cubre
  también `UnitOfWork` y los 13 `catch (DbException|DbUpdateException)` de `Host`. **Recomendada.**
- **E.** Reintentos limitados más `RetryLimitExceededException`.
- **F.** Desenvolver la cadena en el traductor.
- **G.** `IErrorHandler` como escudo de excepciones en `Host`, complementaria.
- **H.** Comprobar la conexión al arrancar (fail fast), complementaria.
- **Descartadas:** atrapar en cada servicio de `Host`, `BackgroundServiceExceptionBehavior.Ignore` y agregar Polly.

**Decisión del usuario: D (R-37).** Commit `63ab7f3`, sin push:
- `AdaptersRegistration` llama `UseSqlServer(connectionString, UseNonRetryingStrategy)`.
- El método privado configura `ExecutionStrategy(dependencies => new NonRetryingExecutionStrategy(dependencies))`.
  Es un método aparte para no anidar lambdas (5.1.2) y lleva un `//` en inglés con el porqué (8.1.1).
- **Verificación con el registro real** (`AddBastionAdapters` y el contenedor):
  - con la base local, los dos repositorios y la unidad de trabajo leen igual;
  - con una base inexistente salen `MatchRepositoryException` ← `SqlException`, `RoomRepositoryException` ←
    `SqlException`, y la unidad de trabajo deja la `SqlException`, que atrapan los `catch (DbException)` de `Host`;
  - con la estrategia anterior, la unidad de trabajo dejaba salir `InvalidOperationException`.
  - Compila sin avisos de código y pasan 158 + 220 + 136 pruebas.
- **Para la revisión de `Host`:** la G (`IErrorHandler`) y la H (comprobar la conexión al arrancar) quedan como
  complementarias.

### 211. `UnitOfWork` (2026-11-10)

- **Pasada 1:**
  - **Sin hallazgos:** §1, §2, §3, §4, §6 (campo, constructor, propiedades y método en orden) y §8.
  - **No aplican:** §5 (no hay lambdas ni LINQ) y §7 (`IUnitOfWork` no es `I…Service`).
  - **9.4.1:** el constructor comprueba `context`.
  - **9.5.1:** no es dueña del contexto; lo crea el contenedor, que lo libera al cerrar el ámbito.
  - **10.2.1:** crea sus ocho repositorios sobre el mismo contexto, que es justo el ejemplo de la excepción de la regla.
- **Pasada 2:** no hay repetición en el archivo.
- **Pasada 3:** los nombres son claros.
- **Pasada 4:** se usan las ocho propiedades (`Accounts` 6, `Sessions` 2, `AccessLogs` 1, `Friendships` 11,
  `FriendRequests` 9, `Sanctions` 1, `BannedWords` 1, `Messages` 6) y `SaveChanges` (5).
- **El pendiente (traducción):** `SaveChanges` no traduce, pero tampoco las lecturas de sus repositorios: las 37
  llamadas de lectura también dejan salir `DbException`.
  - Traducir solo `SaveChanges` no evitaría que `Host` siga atrapando `DbException`.
  - `Host` atrapa `DbUpdateException` y `DbException` en 13 lugares de nueve servicios, y todos los convierten en el mismo
    `FaultException(ServerFailureReason)`. Solo cambia el texto de la bitácora ("could not be saved" o "could not be
    reached").
  - Ninguna clase de `Application` reacciona a una falla de la unidad de trabajo. En cambio, `RankedMatchCreator` sí
    reacciona a `MatchRepositoryException`.

**Preguntas (211):**
1. Cómo traducir (recomendado: no traducir en la unidad de trabajo; el borde, `Host`, maneja los errores de la base;
   anotarlo como regla). Alternativas:
   - traducir solo `SaveChanges`;
   - traducir todo (lecturas y guardado) con una excepción de `Application`;
   - sobrescribir `SaveChanges` del contexto;
   - interceptores de EF.
2. Si se elige no traducir, ¿`DatabaseFailureTranslator` queda aparte o vuelve a `NewContextRunner`? (recomendado:
   aparte).

**Decisiones del usuario (211): A en las dos.**
- **R-38.** La unidad de trabajo no traduce: `Host` maneja `DbException`/`DbUpdateException`.
- `DatabaseFailureTranslator` sigue como clase aparte, aunque hoy tenga un solo usuario.
- **Sin cambios de código ni commit.**
- **Para la revisión de `Host`:** los 13 pares de `catch` repetidos en nueve servicios (posible `IErrorHandler`, la G del
  hallazgo de la R-37).

### 212. `RoomCodeGenerator` (2026-11-10)

`return RandomNumberGenerator.GetString(RoomPolicy.CodeAlphabet, RoomPolicy.CodeLength);`: es una sola llamada con
argumentos simples. El azar va detrás de una interfaz inyectada (10.1.1), y lo usa `RoomRegistry`. Cumple las cuatro
pasadas. **Sin cambios.**

### 213 y 214. `PasswordHasher` y `SessionTokenGenerator` (2026-11-10)

- **R-04 (incumplimiento, corregido):**
  - `PasswordHasher.DeriveHash` pasaba `Encoding.UTF8.GetBytes(password)` dentro del `return`; ahora va antes, en
    `passwordBytes`.
  - `SessionTokenGenerator.Hash` hacía `return SHA256.HashData(Encoding.UTF8.GetBytes(token));`; ahora usa `tokenBytes`.
- **R-14 (incumplimiento, corregido):** `return new GeneratedToken(token, Hash(token));` → `tokenHash` antes.
- **4.4.2:** `PasswordHasher.HashLength`/`SaltLength` y `SessionTokenGenerator.TokenHashLength` son públicas porque las
  usan las configuraciones de EF para el largo de las columnas. Es la única definición. La R-25 no aplica.
- **2.2.3:** `Verify` ya quedó como excepción en el archivo 176.
- **Seguridad, sin hallazgos:**
  - PBKDF2-SHA512 con 210 000 iteraciones;
  - `FixedTimeEquals`;
  - sal y hash señuelo para que una cuenta sin contraseña tarde lo mismo;
  - token de 32 bytes aleatorios, guardado como SHA-256.
- **Pasada 3 (se pregunta):** `SessionTokenGenerator.TokenLength = 32` son bytes aleatorios. El token, en Base64, mide
  44 caracteres. El nombre hace pensar en el largo del texto.
- **4.2.1 frente a la seguridad (se pregunta):** `Verify` no sale antes cuando falta la contraseña guardada, a propósito,
  para no revelar por el tiempo de respuesta si la cuenta tiene contraseña. No hay nada que lo explique, y alguien podría
  "corregirlo" con una guarda.
- **Verificación con datos sintéticos** (ninguna contraseña real): 12 líneas idénticas antes y después. Cubre `Verify`
  correcta, incorrecta, vacía, sin hash, sin sal y con acentos, el hash de dos tokens conocidos, y el largo y la
  coincidencia del token generado. Compila sin avisos de código y pasan 158 + 220 + 136 pruebas.

**Preguntas (213 y 214):**
1. `Verify` sin guarda (recomendado: un `//` en inglés que explique el porqué, 8.1.1).
2. `TokenLength` (recomendado: `TokenByteCount`).

**Respuesta del usuario:** P2 A, aplicada (`TokenByteCount`). Para P1 eligió la A, pero pidió **evitar a toda costa los
comentarios** y quiere propuestas que se lean mejor sin ellos. Queda como regla **R-39**. Lo mismo aplica al `//` que se
agregó en `AdaptersRegistration` (R-37, commit `63ab7f3`), que es el único comentario escrito a mano en el código. El
encabezado de `Strings.Designer.cs` lo genera la herramienta de recursos.

Propuestas sin comentario para `Verify`:
- **A.** Nombres que revelan la intención (renombrar los señuelos).
- **B.** Extraer `IsMatchInConstantTime(...)`, con variables explicativas. **Recomendada.**
- **C.** Un objeto de caso especial (`StoredPassword.Missing`).
- **D.** Poner la garantía en el contrato: `IPasswordHasher.VerifyInConstantTime`.
- **E.** Una prueba como documentación. No es viable: la prueba de tiempo sería inestable y no hay proyecto de pruebas
  de `Adapters`.

Para `AdaptersRegistration`: renombrar `UseNonRetryingStrategy` → `KeepTransientErrorsAsDbException` y quitar el `//`.

**Respuesta del usuario:** la B vale para los dos, pero los nombres siguen siendo ambiguos, también `Verify`. Pidió nombres
más claros.

**Dato nuevo:** cuando la cuenta no existe, `LoginService` llama `_passwordHasher.Verify(password, null, null)` y
descarta el resultado. Solo sirve para que la respuesta tarde lo mismo y no se pueda averiguar qué cuentas existen. La
prueba `LogIn_UnknownIdentifier_StillChecksAPassword` lo comprueba con `FakePasswordHasher.VerifyCount`.

**Propuestas:**
- `Verify` → `IsPasswordCorrect(enteredPassword, storedHash, storedSalt)`. Cumple la 2.2.3, así que se quita la
  excepción del archivo 176.
- Un método nuevo en el puerto, `SimulatePasswordCheck(enteredPassword)`, para la llamada de `LoginService`.
- El ayudante pasa a `IsHashEqualWithoutTimingLeak`, y los señuelos a `_saltWhenNoPasswordStored` /
  `_hashWhenNoPasswordStored`.
- El método del registro pasa a `KeepDatabaseErrorsAsDbException`. Se descarta `DisableRetriesAndErrorWrapping`, porque
  la estrategia por defecto tampoco reintentaba.
- Archivos que toca: `IPasswordHasher`, `LoginService`, `PasswordHasher`, `AdaptersRegistration`, `FakePasswordHasher` y
  `TestLoginService`.

**Decisión del usuario: aplicar los cuatro nombres.**
- **Commit `0f27c74`** (213 y 214, con el puerto y el inicio de sesión):
  - `IPasswordHasher.IsPasswordCorrect(enteredPassword, storedHash, storedSalt)` y `SimulatePasswordCheck(enteredPassword)`.
  - `LoginService` llama `SimulatePasswordCheck(password)` cuando la cuenta no existe.
  - En `PasswordHasher`: `IsHashEqualWithoutTimingLeak`, `_saltWhenNoPasswordStored`/`_hashWhenNoPasswordStored` y las
    variables `isHashEqual`, `hasStoredPassword`, `isPasswordEntered`, `enteredHash`.
  - En `SessionTokenGenerator`: `TokenByteCount` y las variables de la R-04 y la R-14.
  - En las pruebas, `FakePasswordHasher.SimulatedCheckCount` y `LogIn_UnknownIdentifier_SimulatesAPasswordCheck`.
  - Con `IsPasswordCorrect`, **la excepción de la 2.2.3 del archivo 176 ya no hace falta**.
- **Commit `2efd55e`:** `AdaptersRegistration.KeepDatabaseErrorsAsDbException`, sin el `//`. En el código ya no queda
  ningún comentario escrito a mano (R-39).
- **Verificación:**
  - Las 12 líneas de la foto de seguridad siguen idénticas.
  - La comprobación real tarda 102 ms y la simulada 98 ms.
  - El registro real sigue traduciendo con una base inexistente.
  - Compila sin avisos de código y pasan 158 + 220 + 136 pruebas.

**Capa `Bastion.Server.Adapters` terminada** (archivos 183 a 214). No tiene servicios, así que la R-27 no activa nada.
Sigue `Bastion.Server.Host`. Pendientes anotados para esa capa:
- los 13 pares `catch (DbUpdateException)` / `catch (DbException)` repetidos en nueve servicios;
- la G (`IErrorHandler`) y la H (comprobar la conexión al arrancar) de la R-37.

## Capa `Bastion.Server.Host`

Son 25 archivos (215 a 239), en orden de carpeta. Datos generales:
- **6.3:** solo `AccountService` y `LoginTranslator` tenían los `using` de terceros antes que los de `Bastion`.
- **Nulos:** todos los servicios convierten un argumento nulo en una falla tipada (`if (x is null) throw …Translator.ToFault(…)`).
- **Cliente:** cualquier `FaultException` genérica se convierte en `ServerErrorException`, sin usar su texto.
- **Cruzados, se preguntan al terminar el grupo que los tiene:**
  - los pares de `catch` de la base, al terminar los servicios;
  - el `new FaultException<T>(detalle, new FaultReason(mensaje))` que se repite en cada traductor, al terminar los
    traductores.

### 215 a 217. `AccountService`, `LoginTranslator` y `CallerAddress` (2026-11-10)

- **6.3 (incumplimiento, corregido):** `AccountService` y `LoginTranslator`.
- **7.1.2 (incumplimiento, corregido):** `AccountService` implementa el contrato `IAccountService` y no tenía
  `<inheritdoc/>`. Ahora lo lleva en la clase y en `LogIn`. El `<summary>` de `IAccountService` se escribe al revisar
  `Contracts`.
- **10.3.1:** `IServiceScopeFactory` y `GetRequiredService` dentro de un ámbito por llamada. Es justo la excepción de la
  frontera de red. Cumple.
- **9.2.1:** bitácora y `throw new FaultException(ServerFailureReason)` sin la excepción interna, igual que el ejemplo
  correcto de frontera de red. Cumple.
- **R-14 (incumplimiento, corregido), en `LoginTranslator`:**
  - `ToConnection` y `ToAttempt` llevaban `??` y `Trim()` en los argumentos;
  - los dos `ToFault` creaban `new …Fault()` y `new FaultReason(…)` dentro del `return`.
  - Ahora cada paso va en su variable.
- **`CallerAddress`:** cumple.
  - La condición de tres `||` con `TryGetValue` y `is not` no mezcla `&&` (R-24 no aplica).
  - `"0.0.0.0"` está en una constante.
- **Lectura L-20 (9.4.1 en la frontera de red, se pregunta):** `LogIn` no usa `ThrowIfNull`. Si `credentials` o `device`
  llegan nulos, lanza la falla de credenciales inválidas. Todos los servicios siguen esta forma.
- **R-10 en los textos (se pregunta):**
  - `ServerFailureReason = "The server could not complete the sign-in."` y la bitácora "The sign-in could not be saved".
  - La R-10 renombra los nombres con `SignIn`, pero no dice nada de los textos.
  - Hay textos con "sign-in" en `Host` (2), `Client` (3 en la bitácora) y `Client.Networking` (1 excepción). La interfaz
    (`Strings.resx`) usa "Sign in".
- **Compilación:** sin avisos de código. Ninguna prueba cubre `Host`.

**Preguntas (215 a 217):**
1. L-20 (recomendado: aceptar la falla tipada como forma de la 9.4.1 en una operación de servicio).
2. R-10 en los textos (recomendado: "log in" en la bitácora, las excepciones y las fallas; la interfaz sigue con "Sign in").

**Decisiones del usuario (215 a 217): A en las dos.**
- **R-40:** en una operación de servicio WCF, un argumento nulo se convierte en la falla tipada que corresponde.
- **R-41:** los textos del programa usan "login".
- `AccountService` ya dice "The server could not complete the login." y "The login could not be saved.". Los textos de
  `Client` y `Client.Networking` cambian al revisar sus archivos.
- Commit `81757eb`, sin push.

### 218 y 219. `ChatService` y `ChatTranslator` (2026-11-10)

- **Cumplen:**
  - **6.3:** `using` en orden.
  - **7.1.2:** `<inheritdoc/>` en la clase y en los tres miembros.
  - **10.3.1:** ámbito por llamada.
  - **R-40:** `RequireSessionToken` y `RequireText` convierten un nulo en falla tipada.
  - **R-28:** `return x ?? throw …`.
  - **4.3.2:** `default` con `ArgumentOutOfRangeException`.
  - **§11:** la bitácora sigue el formato "acción. Clave=valor".
- **Lectura L-21 (R-04 en el cuerpo de una lambda, se pregunta):**
  - `chat => ChatTranslator.ToReceipt(chat.SendMessage(token, checkedText, GetUtcNow()))` anida tres llamadas en una
    línea. El mismo patrón está en los servicios con un `Run` privado.
  - Se comprobó en un proyecto aparte que el compilador infiere `Run(nombre, (IServicio s) => s.Hacer(…), Traductor.ToX)`
    sin escribir los tipos.
- **Pasada 3:** `checkedText` → `messageText`. Va dentro de la pregunta 1.
- **5.3.1 y R-14 en los arreglos de los contratos (se pregunta para todos los traductores):**
  - `Messages = history.Entries.Select(ToMessage).ToArray()` dentro del `return`.
  - Hay 9 casos en 6 traductores. Los contratos usan arreglos (`LobbyChatMessage[]?`).
- **R-14 en las fallas (se pregunta para todos los traductores):** `new FaultException<T>(new …Fault(), new
  FaultReason(rejection.Message))` se repite en cada `ToFault`. En `LoginTranslator` ya se corrigió con variables.
- **Pasada 3 (se pregunta):** `entry.Line.Line.Sender.Nickname`. `ChatHistoryEntry.Line` es un `PostedChatLine`, y
  `PostedChatLine.Line` es un `ChatLine`. Aparece en 4 lugares.

**Preguntas (218 y 219):**
1. L-21 (recomendado: que `Run` reciba la llamada y la traducción por separado).
2. Arreglos de contrato (recomendado: un ayudante `ContractArray.ConvertAll(origen, convertidor)` en `Host`).
3. Fallas (recomendado: `FaultExceptionFactory.Create(detalle, rechazo)` en `Host`).
4. `Line.Line` (recomendado: `ChatHistoryEntry.Line` → `PostedLine` y variables en `ToMessage`).

**Respuesta del usuario:** acepta la A en las preguntas 2, 3 y 4. **Rechaza la A de la 1:**
- `return Run(nameof(…), (ILobbyChatService chat) => …, ChatTranslator.ToReceipt);` viola varias reglas: un `return`
  con una lambda y un grupo de método como argumentos no es "una sola llamada con argumentos simples" (R-04, R-14).
- Además se lee mal.
- `Run` es un nombre demasiado genérico.
- La forma actual (`return Run<…>(nameof(…), chat => …)`) tiene el mismo problema.

**Aplicado, sin commit:**
- **R-42:** `Host/Common/ContractArray.ConvertAll(IReadOnlyList<TSource>, Func<TSource, TItem>)`, hecho con un `for`.
  `ChatTranslator.ToChatLog` lo usa. Los otros 8 casos cambian al revisar su archivo.
- **R-43:** `Host/Common/FaultExceptionFactory.Create(detalle, rechazo)`. Lo usan `ChatTranslator` y `LoginTranslator`.
- **`ChatHistoryEntry.Line` → `PostedLine`:**
  - el registro de `Application`;
  - `LobbyChatService`, donde la lambda ahora se llama `postedLine`;
  - `TestLobbyChatService`;
  - `ChatTranslator.ToMessage`, con las variables `postedLine` y `line`.
- Compila sin avisos de código y pasan 158 + 220 + 136 pruebas.

**Opciones nuevas para la pregunta 1** (en todas, el `return` es una variable o una sola llamada con argumentos simples):
1. Un traductor de fallas por servicio (`TranslateChatFailures`), con un método privado por operación que abre su
   ámbito (`…InRequestScope`). **Recomendada.**
2. Una variable con la llamada (`Func<IServicio, Resultado>`), un ayudante con nombre (`CallInRequestScope`) y la
   traducción del resultado aparte.
3. Un escudo de fallas con `IErrorHandler` y sin `try`/`catch` en los servicios. Es lo que mejor se lee, pero es un cambio
   grande y hay que probarlo de punta a punta.
4. **Descartadas:** una clase por operación, y solo renombrar `Run`.

**El usuario pidió una variante de la opción 1** con un auxiliar que evite repetir el ámbito en cada operación.
- **Propuesta:** `Host/Common/RequestScope<TService> : IDisposable`.
  - Crea el ámbito en su constructor, resuelve `TService` en la propiedad `Service` y libera el ámbito en `Dispose`.
  - Cada operación abre `using var lobbyChat = new RequestScope<ILobbyChatService>(_scopeFactory);`.
  - Un método no sirve, porque el ámbito se cerraría al devolver el servicio.
- **Lo que no cubre:** la parte común de los `TranslateXFailures` entre servicios (sesión inválida y base de datos) se
  pregunta al terminar los servicios.

**El usuario pidió investigar** con los mismos criterios y una propuesta parecida que quite la repetición.
- **Experimento** en el scratchpad (`corewcf-probe`), con las mismas versiones del proyecto: CoreWCF 1.9.1 en el
  servidor y System.ServiceModel 10.0.652802 en el cliente, sobre net.tcp en el puerto 18765.
  - El servicio es `PerCall` y está registrado `Transient`, como los de `Host`. Recibe una dependencia `Scoped` en el
    constructor.
  - El contenedor usa `ValidateScopes = true`.
- **Resultados:**
  1. **CoreWCF crea un ámbito por llamada:** tres llamadas dieron tres instancias distintas, y cada una se liberó al
     terminar (liberadas: 0, 1, 2). Esto contradice la premisa de la excepción de la 10.3.1 ("el framework no permite
     inyectar dependencias con un ámbito por llamada"), por lo menos para los servicios `PerCall`.
  2. **`IErrorHandler` funciona:**
     - el cliente recibió `FaultException<ProbeFault>` con su detalle y su razón;
     - una excepción inesperada llegó como falla genérica;
     - el canal siguió `Opened` en los dos casos y aceptó la llamada siguiente.
  3. **Una sola línea registra el escudo:** `services.AddSingleton<IServiceBehavior, …>()` lo aplica a todos los
     servicios.
- Los ocho servicios de `Host` son `PerCall`. Hoy abren el ámbito a mano en 13 lugares (o con un `Run`).
  `FriendPresenceReporter` es un singleton fuera de WCF (es la L-08) y queda aparte.
- **Propuesta:** inyección por constructor de los servicios de aplicación, más un escudo de fallas (`FaultShield` +
  `ServiceErrorHandler` + `FaultTranslatorRegistry`) registrado una vez en `ServiceRegistration`.
  - Los servicios quedan sin `IServiceScopeFactory`, sin `Run`, sin `try`/`catch` y sin bitácora propia.
  - **Variantes parciales:** solo la inyección (los `try`/`catch` siguen en cada servicio), o solo el escudo (el ámbito
    a mano sigue).

**El usuario preguntó si se pueden evitar las fallas genéricas y escribir los errores en la bitácora.** Segundo
experimento:
- **Falla de servidor tipada:** con `ServerFailureFault { Kind, ErrorId }` y su `[FaultContract]` en la operación, el
  cliente recibió `FaultException<ServerFailureFault>`:
  - `Kind=DatabaseUnavailable` para una `DbException`;
  - `Kind=Unexpected` para cualquier otra excepción.
- **Sin el `[FaultContract]`:** el cliente recibió una falla sin tipo. Por eso cada operación tiene que declararla.
- **Bitácora:** el manejador tiene `OperationContext` en `ProvideFault` y en `HandleError`. Escribió la acción, la
  dirección de quien llama, el `ErrorId` (el mismo que recibió el cliente), el tipo de falla y el de la excepción.
- El canal siguió `Opened`.
- **11.1.1:** un rechazo es una excepción manejada, así que va como mínimo en **Warn**. Una falla del servidor va en
  **Error**, con la excepción como segundo parámetro.
- **Datos:** hoy el código ya manda fallas sin tipo (`FaultException(ServerFailureReason)`). Los contratos tienen 30
  operaciones y 44 `[FaultContract]`. El cliente convierte cualquier `FaultException` en `ServerErrorException`.
- **Propuesta ajustada:**
  - `ServerFailureFault` + `ServerFailureKind` en `Contracts`, con su `[FaultContract]` en las 30 operaciones;
  - el escudo convierte los rechazos en su falla tipada (Warn) y cualquier otra excepción en `ServerFailureFault`
    (Error con `ErrorId`);
  - los servicios lanzan la excepción del rechazo, por ejemplo `?? throw new InvalidSessionException()`, en lugar de
    llamar al traductor;
  - el cliente atrapa `FaultException<ServerFailureFault>` al revisar `Client.Networking`.

**El usuario prefiere**, antes que una falla tipada nueva, la propagación y las fallas propias del lenguaje y del
framework. Tercer experimento:
- Para las fallas del servidor, el manejador usa la `FaultException` de WCF con
  `FaultCode.CreateReceiverFaultCode(new FaultCode("DatabaseUnavailable" | "Unexpected"))` y la razón
  `"The server could not complete the request. ErrorId=…"`.
- El cliente recibió `IsReceiverFault=True`, el `SubCode` y el `ErrorId` en todas las operaciones, también en la que no
  declara ningún `[FaultContract]`. El canal siguió `Opened`.
- **Propuesta (propagación):**
  - adentro, las excepciones se propagan; se usan las predefinidas (9.3.2) y las propias solo para los rechazos que
    cruzan el contrato (ya existen) y para la R-38;
  - los servicios no atrapan nada, y la R-40 lanza la excepción del rechazo;
  - el escudo es el único punto donde termina la propagación y donde se escribe en la bitácora (11.1.1). Un rechazo
    registrado se convierte en su falla tipada de hoy y va en Warn. Cualquier otra excepción se convierte en una falla
    *receiver* con subcódigo y `ErrorId` y va en Error, con la excepción;
  - los contratos no cambian. Los nombres de los subcódigos van en una sola clase de constantes en `Contracts`, que
    comparten el servidor y el cliente (2.10.1, 4.4.2).

**El usuario pidió que el contrato sí declare las fallas del servidor.** Cuarto experimento, con el tipo propio de WCF
`System.ServiceModel.ExceptionDetail`:
- **Contrato:** `[FaultContract(typeof(ExceptionDetail))]` en la operación.
- **Servidor:** `new FaultException<ExceptionDetail>(detalle, razón, código receiver)`. El detalle se arma con
  `new ExceptionDetail(new InvalidOperationException("The server could not complete the request. ErrorId=…"))`, que es
  una excepción limpia y no la real.
- **Cliente:** recibió `FaultException<ExceptionDetail>` con `IsReceiverFault=True`, el `SubCode`,
  `Detail.Type=System.InvalidOperationException` y `Detail.Message` con el `ErrorId`. **Sin la traza ni la excepción
  interna.**
- La operación que **no** lo declara también lo recibió tipado, porque el cliente de WCF ya conoce `ExceptionDetail`.
  Declararlo deja escrito en el contrato lo que puede pasar, y una prueba por reflexión puede exigirlo en las 30
  operaciones.
- El canal siguió `Opened`.

**El usuario pidió una sola propuesta, basada en una técnica válida para el proyecto, que reúna todo lo que pidió:**
1. Cada `return` es una variable o una sola llamada con argumentos simples (R-04, R-14) y se lee bien (D-06).
2. Sin nombres genéricos como `Run`.
3. Sin repetición: ni el ámbito, ni los `Run`, ni los `catch`.
4. Sin fallas genéricas, y con cada error en la bitácora.
5. Propagación y excepciones propias del lenguaje antes que fallas tipadas.
6. El contrato declara las fallas del servidor.
7. Sin comentarios (R-39).
8. Dentro del estándar.

**Técnica propuesta: barrera de fallas** (*Fault Barrier*, Barry Ruzek, *Effective Java Exceptions*, Oracle, 2007),
que distingue entre *contingencias* y *fallas*. En .NET y WCF se implementa como el patrón *Exception Shielding*
(Microsoft patterns & practices), con `IErrorHandler`.
- **Contingencias:** los rechazos de negocio de hoy. Se convierten en las fallas tipadas que ya existen.
- **Fallas:** las excepciones predefinidas y las de la R-38. Se propagan sin atraparse hasta la barrera, que las
  registra una vez en Error y responde con `FaultException<ExceptionDetail>` (código receiver, subcódigo y `ErrorId`).
- Los servicios reciben sus dependencias por constructor, porque CoreWCF da un ámbito por llamada.
- Los contratos declaran `ExceptionDetail` en sus 30 operaciones, y una prueba por reflexión lo exige.
- **Límite:** los servicios en segundo plano (`MatchmakingBackgroundService`, `RoomBackgroundService` y
  `FriendPresenceReporter`) no pasan por WCF, así que necesitan su propia barrera. Se revisan en su archivo.

**El usuario no acepta cuatro contras** y pidió investigar a fondo cómo evitarlos:
1. usar `ExceptionDetail` como error público;
2. que el `ErrorId` viaje dentro del mensaje;
3. que un rechazo nuevo sin registrar salga como falla del servidor;
4. que los servicios en segundo plano necesiten su propia barrera con `catch` de tipos conocidos.

**Investigación:**
- **9.3.1:** no tiene excepción para manejadores de nivel superior; todo `catch` es del tipo específico.
- **9.6.1:** pide heredar de `Exception` y ser `sealed`, pero no impide implementar una interfaz.
- **Microsoft Learn**, "Specifying and Handling Faults in Contracts and Services":
  - para los errores que el cliente maneja, recomienda fallas **declaradas** con `[FaultContract]` y un tipo de detalle
    propio;
  - `ExceptionDetail` / `IncludeExceptionDetailInFaults` son solo para depurar y pueden exponer información interna.
- **Microsoft Learn**, "Unhandled exceptions from a BackgroundService" (.NET 6): la excepción se registra en el
  `ILogger` y el host se detiene. El valor por defecto es `StopHost`; la única alternativa es `Ignore`.
- La página sobre `IErrorHandler` dio 404 y no se reintentó.
- **Excepciones del servidor:** hay 11 propias. Nueve son rechazos y cada uno tiene exactamente una falla tipada en
  `Contracts`. Las otras dos son fallas (`MatchRepositoryException`, `RoomRepositoryException`).
- **Experimento `barrier-check`:**
  - con un rechazo marcado y sin traductor, el arranque se detuvo con la lista de los que faltaban;
  - con el catálogo completo, arrancó;
  - en un `BackgroundService`, la misma barrera atrapó la `DbException`, la registró con `ErrorId` y el ciclo siguió;
  - un error de programación lo registró .NET y el host se detuvo.
- **Propuesta resultante:**
  - `ServerFailureFault { Kind, ErrorId }` declarada en las 30 operaciones;
  - la interfaz marcadora `IContractRejection` en los 9 rechazos;
  - una guarda de arranque en las dos direcciones: cada rechazo marcado tiene traductor, y cada falla declarada en
    `Contracts` tiene quien la produce;
  - una prueba que clasifica cada excepción propia como rechazo o como falla;
  - una sola clase `FaultBarrier`, que usan el manejador de WCF y los servicios en segundo plano
    (`ContainBackgroundFailures`).
- **Lo que no se puede quitar sin cambiar el estándar:** que un error de programación en segundo plano detenga el host.
  Se registra, pero mantener vivo el ciclo pediría `catch (Exception)`, que la 9.3.1 prohíbe.

**El usuario no quedó convencido con ninguna** (2026-11-11). Pidió revisar si las repeticiones originales se pueden
sacar a un método privado y luego hacer de ese método su propia clase.
- **Repeticiones en los ocho servicios WCF (código de hoy):**
  - `catch` en las operaciones con respuesta:
    - `InvalidSessionException`: 8;
    - `DbException`: 8;
    - `DbUpdateException`: 3;
    - `MatchRepositoryException`: 4;
    - `RoomRepositoryException`: 1;
    - en total, 24 bloques.
  - Ámbito con `CreateScope` y `GetRequiredService`: 9 lugares.
  - `RequireSessionToken`: 4 métodos y 3 `if` en línea.
  - `GetUtcNow`: 5 métodos y 3 expresiones en línea.
  - `ServerFailureReason` y `_logger`: uno por servicio.
  - **No son la misma repetición:**
    - las operaciones de un solo sentido registran y no lanzan (`RunOneWay` y `LeaveRoom`);
    - los `catch` de los servicios en segundo plano tienen su contexto propio.
- **Propuesta:**
  - **Técnicas:** *Extract Method* seguido de *Extract Class* (Fowler, *Refactoring*, 2.ª ed., 2018), con el `try`/`catch`
    como *Execute Around Method* (Beck, *Smalltalk Best Practice Patterns*, 1997).
  - **`Host/Common/RequestFailureTranslator`:** clase estática con `TranslateSessionAndDatabaseFailures(nombre, operación)`,
    con una sobrecarga para `Func<TResult>` y otra para `Action`.
    - Atrapa los cinco tipos comunes.
    - En los cuatro de base de datos registra Error con `Operation=` y lanza `FaultException(ServerFailureReason)`.
  - **Cada servicio conserva un método privado (`TranslateChatFailures`)** solo con sus propios rechazos, alrededor de
    la llamada a la clase.
  - **Piezas de apoyo:**
    - `RequestScope<TService> : IDisposable` para el ámbito;
    - `SessionTranslator.RequireSessionToken`;
    - `OperationWithoutResult.ToFunction(Action)` para las operaciones `void`.
  - Cada operación es un `Func`/`Action` en variable y un `…InRequestScope` privado.
- **Comprobado en el scratchpad** (`extract-class`, copia de `src` del servidor):
  - **Compilación:** `ChatService`, `FriendshipService` (con operaciones con resultado y `void`), `MatchService` y
    `SessionService` compilan sin avisos de código, incluida la CA1502.
  - **Ejecución:** con servicios de aplicación falsos que lanzan, los nueve casos dieron lo mismo que hoy:
    - la sesión inválida, el rechazo del chat y el rechazo de amistad llegaron como su falla tipada;
    - la base de datos y el repositorio llegaron como falla sin tipo, con su registro Error;
    - el error de programación se propagó sin cambios;
    - se crearon 8 ámbitos y se liberaron 8.
- **Mejora de paso:** `RoomService.FindOwnRoom` hoy solo atrapa la sesión inválida, así que una falla de base de datos
  sale sin registro. Con la clase queda registrada.
- **Preguntas:**
  1. la forma (dos capas);
  2. los nombres;
  3. un texto de falla del servidor o uno por servicio;
  4. el contexto de la bitácora (`MatchId`, `IpAddress`);
  5. `RequestScope`;
  6. `RequireSessionToken`;
  7. las operaciones de un solo sentido;
  8. `GetUtcNow`.

**Decisión del usuario (218 y 219, pregunta 1):** la **opción 1 tal como se propuso al principio**, sin la clase
compartida ni `RequestScope`. Pidió ver de nuevo las opciones originales y eligió esa.
- **R-44:** cada operación de un servicio WCF:
  - deja su llamada en una variable `Func<…>` que apunta a un método privado `…InRequestScope`;
  - devuelve `Translate…Failures(nameof(…), variable)`.
- **`…InRequestScope`:** abre el ámbito, pide el servicio de aplicación, llama y traduce el resultado. Cada línea es un
  paso.
- **`Translate…Failures`:** solo convierte excepciones en fallas, con los `catch` de hoy sin cambios.
- **Aplicado en `ChatService`:**
  - `checkedText` → `messageText`;
  - en `SendMatchChatMessage`, el texto va en su variable antes del `MatchChatSubmission`;
  - `ServerFailureReason`, `_logger` y los textos de la bitácora siguen igual.
- **Verificación:**
  - `Host` compila sin avisos de código;
  - pasan 158 + 220 + 136 pruebas;
  - la sonda del scratchpad dio los mismos cinco resultados del chat que antes, con la bitácora de `ChatService`.
- **Queda para cuando se revisen los otros servicios:** la repetición del ámbito y de los `catch` comunes entre
  servicios (lo que cubrían `RequestScope` y `RequestFailureTranslator`).

**Commit de `Chat`:** `83ee729` (2026-11-11), sin push.

### 220 a 222. `FriendPresenceReporter`, `FriendshipService` y `FriendshipTranslator` (2026-11-11)

- **`FriendshipTranslator` (222), aplicado con reglas ya decididas:**
  - **R-42:** los cuatro `Select(…).ToArray()` pasan a `ContractArray.ConvertAll`, en variables: `friends`,
    `entries`, `receivedRequests` y `sentRequests`.
  - **R-43:** `ToFault` usa `FaultExceptionFactory.Create`.
  - **R-14:** `ToNotification`, `ToSearchEntry` y `ToEntry` llamaban a un convertidor dentro del `return new …`. Ahora
    va antes, en `presence` o `relationship`.
  - **6.3:** sale `System.Linq` y entra `Bastion.Server.Host.Common`.
  - **Verificado:** con datos de prueba, el traductor viejo (de `HEAD`) y el nuevo dan el mismo JSON en `ToFriendList`,
    `ToFriendRequestList`, `ToSearchEntries`, `ToNotification` y en el detalle y la razón de `ToFault`.
  - **Cumple:** 4.3.2 (`default` con `ArgumentOutOfRangeException`), complejidad (`ToReason` = 9) y pasada 4 (los ocho
    públicos se usan, en el servicio o en `NotificationChannelRegistry`).
- **`FriendshipService` (221):**
  - **7.1.2 (incumplimiento, corregido):** no tenía `<inheritdoc/>`; ahora lo lleva en la clase y en las ocho
    operaciones.
  - **R-44 (pendiente de la pregunta 1):** `Run(…, services => { …; return true; })` y `RunResponse` usan lambdas de
    varias líneas (5.1.1) y `GetRequiredService` encadenado.
    - Cuatro operaciones son `void`, y la R-44 no dice cómo pasa una `Action` por `Translate…Failures`.
  - **Repetición:** la guarda del código de amigo aparece en tres formas:
    - `RequireRequestCode` (×3, `RequestNotFound`);
    - un `if` en `SendFriendRequest` (`PlayerNotFound`);
    - un `if` en `RemoveFriend` (`NotFriends`).
  - **Pasada 3:** `code` no dice de quién es el código; `requestService` puede ser cualquier servicio.
- **`FriendPresenceReporter` (220):**
  - **L-08 (10.3.1):** es un singleton que crea el contenedor, no CoreWCF.
    - La excepción de la 10.3.1 habla de la frontera de red.
    - Necesita un ámbito por operación porque `IFriendPresenceService` es `Scoped` (usa el `DbContext`).
  - **`Run`:** el mismo nombre genérico que se quitó con la R-44.
    - Recibe la llamada como lambda en línea (`presenceService => …`).
    - No traduce nada: registra y sigue.
  - **Cumple:** 11.1.1 (`DbException` en Error y `ObjectDisposedException` en Warn, sin relanzar), 11.3.1, 9.1.1 y
    10.4.1.
- **Pasada 3, `FriendshipTranslator`:**
  - `ToEntry` (junto a `ToRequestEntry` y `ToSearchEntry`);
  - `ToState` (devuelve `PresenceState`);
  - `ToNotification` (junto a `ToRequestNotification` y `ToFriendshipStartedNotification`);
  - `ToResult` (devuelve `FriendRequestResult`).
- **6.2:** los privados de `FriendshipTranslator` no siguen el orden de los públicos (lo que se decidió en
  `RoomRepository`).
- **Prototipo en el scratchpad** (`friends-proposal`):
  - la propuesta de `FriendshipService` y la de `FriendPresenceReporter` compilan sin avisos de código;
  - la sonda dio:
    - `ListFriends` devuelve lo mismo y, con una `DbUpdateException`, la falla del servidor con su Error;
    - `AcceptFriendRequest` (`void`) da las fallas tipadas de rechazo y de sesión, y la del servidor con Error en la
      base;
    - los nulos (`RemoveFriend`, `SendFriendRequest` y `CancelFriendRequest`) dan su falla sin llegar al servicio de
      aplicación.

**Preguntas (220 a 222):**
1. Operaciones `void` con la R-44 (recomendado: una sobrecarga con `Action` que pasa a `Func<bool>` con
   `CompleteOperation`).
2. Guarda del código de amigo (recomendado: un `RequireFriendCode(friendCode, rejectionWhenMissing)`).
3. Nombres (recomendado: renombrar en el servicio y en el traductor).
4. Orden de los privados del traductor (recomendado: el de los públicos).
5. L-08 (recomendado: leer la excepción de la 10.3.1 como válida también para un singleton que necesita un servicio
   `Scoped` por operación).
6. Forma de `FriendPresenceReporter` (recomendado: la de la R-44, con `…InOwnScope` y `LogPresenceFailures`).

**Decisiones del usuario (220 a 222): A en las seis.**
- **R-45:** las operaciones `void` usan la sobrecarga con `Action` y `CompleteOperation`.
- **Guarda:** `RequireFriendCode(friendCode, rejectionWhenMissing)` reemplaza a `RequireRequestCode` y a los dos `if`.
- **Nombres:**
  - en el servicio: `requesterCode`, `recipientCode`, `removedFriendCode`, `friendRequests` y `friendList`;
  - en el traductor: `ToFriendListEntry`, `ToPresenceState`, `ToPresenceNotification` (también en
    `NotificationChannelRegistry`) y `ToFriendRequestResult`.
- **R-47:** los privados del traductor siguen el orden de los públicos.
- **R-46:** `FriendPresenceReporter` queda con `…InOwnScope` y `LogPresenceFailures`.
- **No respondido:** si `ChatTranslator.ToNotification` pasa a `ToLobbyChatNotification`. Se pregunta de nuevo.
- **Verificación:**
  - `Host` compila sin avisos de código;
  - la sonda dio 19 resultados iguales a los de antes:
    - el traductor da el mismo JSON que en `HEAD`;
    - los cuatro casos de las operaciones `void` y los tres nulos dan la misma falla;
    - en `FriendPresenceReporter`, la `DbException` va en Error, el proveedor liberado en Warn, ninguna se relanza y el
      error de programación sigue de largo.


**Commit de `Friends`:** `0f43b0f` (2026-11-11), sin push.
- **`ChatTranslator.ToNotification` → `ToLobbyChatNotification`** (aprobado el 2026-11-11): commit `b2e3e79`, sin push.

### 223 y 224. `MatchService` y `MatchTranslator` (2026-11-11)

- **`MatchTranslator` (224):**
  - **R-43, aplicado:** `ToFault` usa `FaultExceptionFactory.Create` con el detalle en una variable.
  - **Cumple:** 6.3, 2.2.2 (`ToAbandonedNotification` tiene tres parámetros) y la pasada 4 (cada método tiene un uso).
  - **Pasada 3:** el parámetro de `ToFault` se llama `exception`. En los demás traductores y en `FaultExceptionFactory`
    se llama `rejection`.
- **`MatchService` (223):**
  - **Cumple:** 7.1.2, 6.3 y 11.1.1.
  - **R-44 (pendiente):** la única operación abre el ámbito y atrapa todo dentro del método público.
    - Es `void`, y el servicio no tiene ninguna operación con resultado.
    - Con la R-45 al pie de la letra quedaría una sobrecarga `Func<TResult>` que solo usaría el adaptador.
  - **Bitácora:** hoy registra el `MatchId`. La forma de la R-44 solo pasa `nameof(…)`.
  - **Texto:** `ServerFailureReason = "The server could not close the match."`. Desde las partidas de cuatro, abandonar
    no siempre cierra la partida (`AbandonmentNotice.IsMatchOver`).
  - **Para la revisión de `Contracts`:** el `<summary>` de `IMatchService.AbandonMatch` dice "that player loses and the
    rival wins". Tampoco vale para cuatro jugadores.
- **Comprobado:**
  - `Host` compila sin avisos;
  - la propuesta compila aparte;
  - una sonda comparó el servicio de `HEAD` con la propuesta en siete casos: con éxito, token nulo, sesión inválida, no
    juega la partida, repositorio, base de datos y error de programación;
  - todos dan lo mismo, salvo los dos textos que se preguntan (la bitácora y la razón de la falla).

**Preguntas (223 y 224):**
1. Servicio con solo operaciones `void` (recomendado: un solo `TranslateMatchFailures(…, Action)` con los `catch`, sin
   sobrecarga `Func` ni `CompleteOperation`; la R-45 se precisa así).
2. `MatchId` en la bitácora (recomendado: `TranslateMatchFailures(nameof(AbandonMatch), matchId, abandonMatch)` y los
   textos de `ChatService` con `Operation=…; MatchId=…`).
3. Razón de la falla (recomendado: "The server could not record the match abandonment.").
4. `exception` → `rejection` en `MatchTranslator.ToFault` (recomendado: sí).

**Decisiones del usuario (223 y 224): A en las cuatro.**
- **R-45 precisada:** `MatchService` tiene un solo `TranslateMatchFailures(string, int, Action)` con los `catch`, sin
  sobrecarga `Func` ni `CompleteOperation`.
- **Bitácora:** el envoltorio recibe `operationName` y `matchId`; los textos son los de `ChatService` con
  `Operation=AbandonMatch; MatchId=…`.
- **Razón de la falla:** "The server could not record the match abandonment."
- **Nombre:** el parámetro de `MatchTranslator.ToFault` se llama `rejection`.
- **Verificación:**
  - `Host` compila sin avisos de código (solo NU1902/NU1903 de NuGet);
  - la sonda volvió a dar los siete casos: cinco iguales y los dos de falla del servidor con los textos nuevos, como se
    decidió.

**Commit de `Matches`:** `e03286a` (2026-11-11), sin push.

### 225 a 227. `MatchmakingBackgroundService`, `MatchmakingService` y `MatchmakingTranslator` (2026-11-11)

- **`MatchmakingTranslator` (227), aplicado por D-07:**
  - **R-43:** `ToFault` usa `FaultExceptionFactory.Create`.
  - **R-42:** los participantes van con `ContractArray.ConvertAll` en la variable `participants`; sale `System.Linq` y
    entra `Bastion.Server.Host.Common`.
  - **R-14:** `searchEndedReason` va en una variable antes del `return`. El `Reason = ToReason(…)` de la falla se queda
    como en `FriendshipTranslator`, porque es una asignación y no un `return`.
  - **R-47:** `ToReason(SearchRejection)` sube antes de `ToMatchFoundParticipant`, porque `ToFault` es el primer público.
  - **Cumple:** 4.3.2 (los dos `switch` con `default`) y la pasada 4 (cada método tiene un uso).
  - **Pasada 3 (pregunta 3):** tres sobrecargas `ToNotification` devuelven tres notificaciones distintas. Quien llama
    (`NotificationChannelRegistry`) solo sabe cuál arma por el tipo del argumento.
- **`MatchmakingService` (226):**
  - **Cumple:** 7.1.2, 6.2, 6.3, 9.1.2, 10.4.1 y 11.3.1.
  - **R-44 y R-45 (forma decidida, propuesta en la copia aparte):** `StartSearch` deja su llamada en `startSearch` hacia
    `StartSearchInRequestScope` y pasa por `TranslateMatchmakingFailures(nameof(StartSearch), startSearch)`. Las tres
    operaciones son `void`, así que hay un solo envoltorio con `Action`, sin `CompleteOperation` (R-45 precisada).
  - **Bitácora de `StartSearch`:** pasa a `Operation=StartSearch` como en los demás servicios. Se conserva el verbo de hoy,
    «could not be read», porque `StartSearch` solo lee el repositorio de partidas.
  - **Operaciones de un sentido (pregunta 1):** `CancelSearch` y `ConfirmPresence` son `IsOneWay`. Una falla no llega al
    cliente, así que hoy no traducen: registran y siguen, por `RunOneWay` y `RunInRequestScope`. La R-44 quitó los
    `Run`, y falta decidir la forma de estas. `RoomService.LeaveRoom` tiene el mismo caso.
  - **Pasada 3 (pregunta 2):** `IMatchSearchService searchService`. En la solución también existe la búsqueda de jugadores
    (`FriendshipService.SearchPlayers`).
  - **Para `Contracts`:** el `<exception cref="FaultException">` de `StartSearch` dice solo "could not reach the
    database"; también sale cuando falla el repositorio de partidas.
- **`MatchmakingBackgroundService` (225):**
  - **Cumple:** 2.3.1, 2.3.2 (`ReviewIntervalSeconds` es `const`; el `TimeSpan` es `static readonly` porque no puede ser
    `const`), 2.14.3, 3.4.1 (`using var timer = new …`), 10.4.1 y R-23 (la llamada con `GetUtcNow()` como argumento se
    deja).
  - **10.1.1 (pregunta 4):** recibe la clase concreta `MatchmakingDispatcher`. La regla define servicio externo como el
    colaborador que hace E/S, guarda estado compartido o no es determinista, y el despachador revisa la cola compartida,
    crea partidas en la base y avisa por la red. `RoomBackgroundService` recibe `IRoomKeeper`.
  - **Fallas:** las conocidas se atrapan abajo (`RankedMatchCreator` atrapa `MatchRepositoryException`;
    `NotificationChannelRegistry.NotifyPlayer` atrapa `CommunicationException` y `TimeoutException`). Un error de
    programación detiene el host, que es lo que hace .NET por omisión. Sin cambio: el usuario descartó las barreras.
- **Comprobado:**
  - `Host` del repositorio (con el traductor) y `Host` de la propuesta compilan sin avisos de código (solo NU1902/NU1903);
  - una sonda comparó `HEAD` con la propuesta:
    - traductor: 11 resultados iguales (las tres fallas, las tres razones de fin, la presencia y la partida encontrada);
    - servicio: 21 casos iguales (siete por operación: con éxito, token nulo, sesión inválida, rechazo, repositorio,
      base de datos y error de programación), también en cuántas veces llega al servicio de aplicación;
    - bitácora: iguales en las operaciones de un sentido; en `StartSearch` cambia solo el texto, como se dijo arriba.

**Preguntas (225 a 227):**
1. Forma de las operaciones de un sentido (recomendado: A, `LogOneWayFailures(nameof(…), sessionToken, operación)`, que
   tiene la guarda del token nulo y los `catch`, y cada operación pasa su `…InRequestScope` como grupo de método en una
   variable `Action<string>`). Pasaría a regla para `RoomService.LeaveRoom`.
2. `searchService` → `matchSearch` (recomendado: sí, como `lobbyChat`, `friendRequests` y `friendList`).
3. `ToNotification` ×3 → `ToMatchFoundNotification`, `ToPresenceRequestedNotification` y `ToSearchEndedNotification`,
   con sus tres llamadas en `NotificationChannelRegistry` (recomendado: sí, y como regla para `PrivateChatTranslator`).
4. 10.1.1 en `MatchmakingBackgroundService` (recomendado: A, `IMatchmakingDispatcher` en `Application`, registrado como
   `AddSingleton<IMatchmakingDispatcher, MatchmakingDispatcher>()`).

**Decisiones del usuario (225 a 227): acepta la 2, la 3 y la 4.** Sobre la 1 preguntó si la forma A enmascara los
errores y si no usa la propagación.
- **2:** `matchSearch` (en la propuesta del servicio).
- **3 (R-48):** `ToMatchFoundNotification`, `ToPresenceRequestedNotification` y `ToSearchEndedNotification`, con sus tres
  llamadas en `NotificationChannelRegistry`.
- **4 (R-49):** `IMatchmakingDispatcher` (nuevo, en `Application/Matchmaking`), `MatchmakingDispatcher` lo implementa,
  `ServiceRegistration` registra `AddSingleton<IMatchmakingDispatcher, MatchmakingDispatcher>()` y el servicio en segundo
  plano recibe la interfaz.
- **Verificación:** `Host` compila; pasan las 220 pruebas de aplicación. Queda un aviso nuevo, IDE0007, en
  `NotificationChannelRegistry.cs:105` (ver la pregunta 5).

**Prueba de CoreWCF sobre la pregunta 1** (`oneway-experiment` en el scratchpad): servidor CoreWCF 1.9.1 y cliente
`System.ServiceModel` 10.0.652802, net.tcp con `SecurityMode.None` y el extremo configurado en código. Una operación
`IsOneWay` que atrapa y registra, otra que deja salir un `InvalidOperationException` y otra que lanza `FaultException`.
- **Canal por llamada, como `ServiceChannel` del cliente (llamar y `Close`):** en los tres casos el cliente no recibe nada.
  No hay excepción ni en la llamada ni en el `Close`.
- **Mismo canal usado otra vez:** después de la excepción que se escapa, la llamada siguiente falla con
  `CommunicationException` y el canal queda `Faulted`. Con la `FaultException` o con la falla atrapada, el canal sigue y
  responde.
- **Bitácora del servidor:** con CoreWCF en `Trace` (370 líneas), no hay ningún registro de las dos excepciones que se
  escapan.
- **Lectura:** en una operación de un sentido, dejar que la excepción se propague fuera del servicio la pierde: no llega
  al cliente ni a la bitácora. La excepción sí se propaga sin `catch` desde `Application` hasta `Host`. `Host` es el último
  lugar que puede registrarla (11.1.1: se registra donde se maneja al final). `LogOneWayFailures` atrapa solo dos tipos
  conocidos (9.3.1); lo demás (un error de programación) sigue de largo y CoreWCF lo pierde, hoy y con A o B.
- **Del cliente:** `MatchSearchViewModel.CancelSearch` termina la búsqueda en pantalla en cuanto envía el mensaje; no espera
  respuesta.

**Pregunta 5 (L-01, 3.4.1):** `MatchFoundNotification notification = MatchmakingTranslator.ToMatchFoundNotification(…)`.
IDE0007 pide `var` porque el nombre del método contiene el tipo. La letra de la 3.4.1 da tres casos (`new`, un cast, un
método estático que devuelve el tipo que lo declara). También dice que el tipo va explícito en «llamadas a métodos cuyo
tipo de retorno no aparece en la expresión», y que la definición coincide con la de IDE0007. Precedente sin revisar:
`var friend = FriendContractTranslator.ToPlayerTag(…)` en `NotificationCallback` (cliente).

**Decisión del usuario sobre la pregunta 1 (después de la prueba de CoreWCF): A (R-50).**
- `CancelSearch` y `ConfirmPresence` guardan su `…InRequestScope` en una variable `Action<string>` (grupo de método) y
  llaman `LogOneWayFailures(nameof(…), sessionToken, operación)`, que tiene la guarda del token nulo (Warn) y los dos
  `catch` de hoy, sin relanzar. Los textos de la bitácora no cambian.
- `MatchmakingService` pasó al repositorio con la R-44 en `StartSearch`, `matchSearch` y el orden de Chat y Friends.
- **Verificación con el código final:**
  - `Host` compila sin errores;
  - la sonda dio los 11 resultados del traductor y los 21 casos del servicio iguales a `HEAD`;
  - en la bitácora solo cambia el texto de `StartSearch` (`Operation=StartSearch`).
- **Sin commit:** falta la pregunta 5; el aviso IDE0007 de `NotificationChannelRegistry.cs:105` sigue en una compilación
  completa (`--no-incremental`).

**Decisión del usuario sobre la pregunta 5: `var` (R-51).** `var notification = MatchmakingTranslator.ToMatchFoundNotification(…)`.
`Host` compila sin avisos de código en una compilación completa (solo NU1902/NU1903); pasan 220 pruebas de aplicación y
158 de dominio.

**Commit de `Matchmaking`:** `8a231a1` (2026-11-11), sin push.

### 228 y 229. `ConversationService` y `PrivateChatTranslator` (2026-11-11)

- **`ConversationService` (228), aplicado por D-07:**
  - **7.1.2:** `<inheritdoc/>` en la clase y en las cuatro operaciones.
  - **R-44 y R-45:** sale `Run`. Cada operación deja su llamada en una variable hacia su `…InRequestScope` y pasa por
    `TranslateConversationFailures`. `MarkConversationRead` es `void` y el servicio tiene operaciones con resultado: usa la
    sobrecarga con `Action` y `CompleteOperation`. Así sale también la lambda de varias líneas con `return true;` (5.1.1).
  - **R-04:** cada `…InRequestScope` guarda el resultado de `Application` en una variable (`summaries`, `conversation`,
    `message`) antes de traducirlo.
  - **R-28, R-40:** el `if (text is null)` pasa a `RequireText`, igual al de `ChatService`.
  - **Nombre nuevo:** la variable del servicio se llama `privateChat`, como `lobbyChat` y `matchChat` en `ChatService`.
  - **Cumple:** 2.2.2 (`SendPrivateMessage` tiene tres parámetros), 6.2, 6.3, 9.1.2, 10.4.1 y 11.3.1.
- **`PrivateChatTranslator` (229), aplicado por D-07:**
  - **R-42 ×2:** `entries` y `messages` con `ContractArray.ConvertAll`; sale `System.Linq` y entra `Host.Common`.
  - **R-14 ×2:** `lastMessage` y `sentAt` en variables antes del `return new`.
  - **R-48:** `ToNotification` → `ToPrivateMessageNotification`, con su llamada en `NotificationChannelRegistry`.
  - **3.4.1:** `var sentAt = DateTime.SpecifyKind(…)`. Es el tercer caso de la regla (un método estático que devuelve el
    tipo que lo declara), como `var clockTime = TimeSpan.FromMinutes(…)`.
  - **Cumple:** R-47 (`ToConversationEntry` y `ToChatMessage` en el orden de uso) y la pasada 4.
- **Pasada 2:** `RequireText` y `RequireSessionToken` son iguales a los de `ChatService`. Se preguntan con la repetición
  entre servicios, al terminar `Host`.
- **Notas para después:**
  - **`Contracts` (R-27):** `IConversationService` no tiene ningún `<summary>` (7.1.1).
  - **`SpecifyKind`:** es el único de la solución. Marca como UTC las fechas que vienen de la base. Las demás fechas leídas
    de la base (por ejemplo `LastSeenAt` de amigos) salen sin `Kind`. No se cambia aquí.
- **Comprobado:**
  - `Host` compila sin avisos de código en una compilación completa (solo NU1902/NU1903);
  - una sonda comparó `HEAD` con el código nuevo: 4 resultados del traductor (con una fecha de la base sin `Kind` y otra
    en UTC) y 33 casos del servicio (con éxito, sesión inválida, rechazo, sin guardar, base de datos, error de
    programación, token nulo, código nulo, texto nulo), todos iguales, también la bitácora y cuántas veces llega a
    `Application`.

**Preguntas (228 y 229):**
1. `code` → `partnerCode` en `OpenConversation` y `MarkConversationRead`, y `recipientCode` en `SendPrivateMessage`
   (recomendado: sí, como `requesterCode` y `recipientCode` en `FriendshipService`).
2. `ToChatMessage` → `ToPrivateChatMessage`, porque devuelve `PrivateChatMessage` (recomendado: sí; por la R-51,
   `lastMessage` pasaría a `var`).
3. Texto de `DbUpdateException`: "The private message could not be saved." sale también en `OpenConversation` y en
   `MarkConversationRead`, que guardan las marcas de leído (recomendado: "The conversation could not be saved.").

**Decisiones del usuario (228 y 229): A en las tres.**
- **Nombres:** `partnerCode` en `OpenConversation` y `MarkConversationRead` (y en sus `…InRequestScope`), `recipientCode`
  en `SendPrivateMessage`.
- **`ToChatMessage` → `ToPrivateChatMessage`.** Lo que dije de `lastMessage` resultó falso: con `var`, IDE0008 pide el tipo
  explícito, porque la llamada no está calificada. Se queda `PrivateChatMessage lastMessage`, y la R-51 se corrigió para
  decirlo.
- **Texto:** "The conversation could not be saved. Operation=…".
- **Verificación:**
  - `Host` compila sin avisos de código en una compilación completa;
  - la sonda volvió a dar los 37 resultados iguales a `HEAD`;
  - en la bitácora solo cambia el texto de `DbUpdateException`.

**Commit de `PrivateChat`:** `c5c0a5e` (2026-11-11), sin push.

### 230. `Program` (2026-11-11)

- **Cumple:**
  - 2.3.1 y 2.3.2 (cuatro `const` en PascalCase);
  - 2.6.1 (`_logger`);
  - 3.4.1 (`var` con `new` y con `ServerCertificate.Load`, que devuelve su propio tipo);
  - 4.2.1 (guardas en `GetConnectionString` y `GetNetTcpPort`);
  - 5.2.1 (`certificate.ConfigureServices` como grupo de método);
  - 6.2, 6.3 y 9.3.2 (`InvalidOperationException` para la configuración que falta);
  - 10.2.1 (es la raíz de composición);
  - 11.3.1;
  - R-23 (la llamada anidada de `XmlConfigurator.Configure` se deja).
- **Pasada 4:** cada miembro se usa.
- **11.1.1 (pregunta 1):** una falla del arranque termina el proceso y debe ir en Fatal. Hoy no queda en la bitácora:
  - si falta la cadena de conexión, el puerto o el certificado, la excepción sale de `Main`;
  - lo mismo si no se puede abrir el puerto.
- **11.3.1 (pregunta 2):** "Game server started" se registra antes de `app.Run()`, que es lo que abre el puerto. Si el
  puerto está ocupado, la bitácora dice que arrancó y luego falla.
- **9.4.1 (pregunta 3):** `Main(string[] args)` es `public` y `args` es de referencia no anulable. La regla pide
  `ArgumentNullException.ThrowIfNull` en todo miembro `public`.
- **2.10.1 (pregunta 4):** `netTcpPort <= 0` usa un literal con significado (el valor que da `GetValue<int>` cuando falta
  la clave), y no hay tope: un puerto mayor que 65535 llega hasta `UseNetTcp`.
- **Prueba (`startup-crash-experiment` en el scratchpad):** con el `log4net.config` del servidor, un `Main` que lanza
  `InvalidOperationException` después de configurar log4net.
  - **Sin manejador:** `server.log` solo tiene la línea Info anterior.
  - **Con `AppDomain.CurrentDomain.UnhandledException`:** queda `FATAL … The game server stopped because of an unhandled
    exception.` con la excepción completa.
  - **En los dos casos:** el proceso termina igual, con el código de excepción no controlada.
  - **No se probó con el servidor real:** al arrancar, `RoomBackgroundService` cierra en la base las salas abiertas, y el
    servidor del usuario está corriendo.
- **Propuesta en la copia aparte** (compila sin avisos de código):
  - `Main` empieza con `ArgumentNullException.ThrowIfNull(args)`;
  - registra `AppDomain.CurrentDomain.UnhandledException += LogUnhandledException;` después de `ConfigureLogging()`;
  - cambia `app.Run()` por `app.Start(); _logger.Info(…); app.WaitForShutdown();`;
  - `GetNetTcpPort` compara con `IPEndPoint.MinPort` y `IPEndPoint.MaxPort`.

**Preguntas (230):**
1. Fatal en el arranque (recomendado: A, `AppDomain.CurrentDomain.UnhandledException` con un `LogUnhandledException`
   privado que registra en Fatal sin atrapar nada; B, `try` en `Main` con `catch` de tipos conocidos, Fatal y `throw;`).
2. Registrar "Game server started" después de `app.Start()` y esperar con `app.WaitForShutdown()` (recomendado: sí).
3. `ArgumentNullException.ThrowIfNull(args)` en `Main` (recomendado: sí; la otra salida, hacer `Main` privado, solo
   esquiva la regla).
4. `IPEndPoint.MinPort` y `IPEndPoint.MaxPort` en `GetNetTcpPort`, con el texto "The net.tcp port is missing or out of
   range. Key=…; Port=…" (recomendado: sí).

**Decisiones del usuario (230): A en las cuatro (R-52).** La propuesta pasó al repositorio tal cual.
- **Verificación:**
  - `Host` compila sin avisos de código en una compilación completa.
  - **Prueba con el servidor real (la compilación de la carpeta aparte):**
    - se lanzó con `--Server:NetTcpPort=70000`; antes se comprobó, contando la clave sin leer valores, que los secretos
      no definen el puerto;
    - `server.log` tiene `FATAL … The game server stopped because of an unhandled exception.` con
      `InvalidOperationException: The net.tcp port is missing or out of range. Key=Server:NetTcpPort; Port=70000`;
    - el proceso terminó antes de cargar el certificado y de tocar la base.

**Commit de `Program`:** `edd69af` (2026-11-11), sin push.

### 231 a 233. `RoomBackgroundService`, `RoomService` y `RoomTranslator` (2026-11-11)

- **`RoomTranslator` (233), aplicado por D-07 en el repositorio:**
  - R-43: `FaultExceptionFactory.Create`.
  - R-42: `members` con `ContractArray.ConvertAll`; sale `System.Linq`.
  - R-14 ×5: `gameModeCode`, `options`, `seatCount`, `state`, `gameMode`.
  - R-23: `double retryAfterSeconds = Math.Ceiling(…)` y después `(int)retryAfterSeconds`.
  - R-47: los privados en el orden de los públicos.
- **`RoomTranslator`, 4.3.2 (pregunta 5):** el `default` de `ToReason` devuelve `ToPlacementReason(rejection)`. La
  regla prohíbe usar el `default` para valores válidos, y ocho valores válidos pasan por ahí. Se partió en dos `switch`
  para no pasar de complejidad 10 (14 casos). `RoomContractTranslator` del cliente tiene el mismo caso.
- **`RoomService` (232):**
  - **Cumple:** 7.1.2, 2.2.2, 6.3, 9.1.2, 10.4.1 y 9.4.2 (`code ?? string.Empty`: el código vacío lo rechaza
    `Application` con `RoomNotFound`).
  - **Forma decidida (propuesta en la copia aparte):**
    - **R-44 y R-45:** salen `RunRequest`, `RunGuarded<TService, TResult>` y los dos `RunInRequestScope`. Quedan siete
      `…InRequestScope`, `TranslateRoomFailures` con sus dos sobrecargas y `CompleteOperation`.
    - **R-50:** `LeaveRoom` usa `LogOneWayFailures`.
    - **R-28:** `RequireSession` pasa a `RequireSessionToken` con `??`, como en los demás servicios.
    - **4.2.1:** en `FindOwnRoomInRequestScope`, una guarda `if (room is null) return null;` en lugar de
      `room is null ? null : …` en el `return`.
  - **Pregunta 1 (pasada 3):** cómo se llaman las variables de `IPrivateRoomService` y `IRoomMatchService`; hoy son los
    parámetros `roomService` y `matchService` de las lambdas.
  - **Pregunta 2:** hoy `FindOwnRoom` solo atrapa `InvalidSessionException`, así que una `DbException` (la sesión se
    verifica en la base) se escapa sin registro. Con la R-44 pasa por `TranslateRoomFailures`.
  - **Pregunta 3 (R-50):**
    - los textos de `LeaveRoom` no dicen la operación;
    - `LeaveRoom` no atrapa `DbException`, así que esa falla se pierde (lo mostró `oneway-experiment`).
  - **Pregunta 4 (11.1.1):** `LogRejection` registra en Info cada rechazo y en Warn el de `InvalidSettings`, dentro del
    `catch` que traduce y relanza. La 11.1.1 dice que ese `catch` no registra: se registra donde se maneja al final. Los
    demás servicios no registran sus rechazos.
- **`RoomBackgroundService` (231):**
  - **Cumple:** 2.6.1, 5.1.2 (se suscribe con grupo de método y se desuscribe en `StopAsync`), 9.3.1, 10.4.1 y 11.3.1
    (`AccountId` en el contexto).
  - **Pregunta 6 (pasada 3):** se llama `…BackgroundService`, pero implementa `IHostedService`, no hereda de
    `BackgroundService`. Hace dos cosas: al arrancar cierra las salas que dejó abiertas la ejecución anterior, y saca de su
    sala al jugador que se desconecta.
  - **10.1.1:** recibe la clase concreta `NotificationChannelRegistry`, por su evento `PlayerDisconnected`. Se pregunta
    con la R-49 al revisar `Sessions`.
- **Notas para `Contracts`:**
  - el `<summary>` de `FindOwnRoom` no documenta la `FaultException`;
  - el contrato dice `RoomOptions`/`ChangeOptions` y `Application` dice `RoomSettings`/`ChangeSettings`.
- **Comprobado:**
  - `Host` del repositorio (con el traductor) y de la propuesta compilan sin avisos de código;
  - la sonda comparó `HEAD` con la propuesta:
    - 96 resultados iguales:
      - el traductor con los 14 rechazos, un valor fuera del enum, los tres modos y las tres conversiones de sala;
      - siete operaciones con éxito, token nulo, sesión inválida, dos rechazos, dos repositorios, base de datos y
        error de programación;
      - las opciones nulas, el código nulo y la sala que no existe;
    - 6 diferencias, todas las de las preguntas 2 y 3: cinco de `FindOwnRoom` ahora salen como falla, y la
      `DbException` de `LeaveRoom` ahora queda en Error;
    - bitácora: salen las 5 líneas Info y la Warn de rechazos (pregunta 4); los textos de `LeaveRoom` llevan
      `Operation=` (pregunta 3).

**Preguntas (231 a 233):**
1. Variables de los servicios de `Application` (recomendado: A, `privateRoomService` y `roomMatchService`; B,
   `privateRooms` y `roomMatches`, como `friendRequests`, pero se leen como listas).
2. `FindOwnRoom` pasa por `TranslateRoomFailures` (recomendado: sí).
3. `LeaveRoom` con `Operation=` en sus textos y un `catch (DbException)` más (recomendado: sí, como `MatchmakingService`).
4. `LogRejection` (recomendado: A, quitarlo, como en los demás servicios; la Warn de opciones nulas de `RequireSettings`
   se queda porque es una guarda y no un `catch`. B: dejar solo la Warn de `InvalidSettings` con un filtro `when`. C:
   dejarlo).
5. 4.3.2 en `ToReason` (recomendado: A, una tabla `_reasonsByRejection` de `IReadOnlyDictionary` con `TryGetValue`, y
   `ArgumentOutOfRangeException` si falta el valor; B, dejar los dos `switch`).
6. `RoomBackgroundService` → `RoomCleanupService`, con su registro en `ServiceRegistration` (recomendado: sí).

**Decisiones del usuario (231 a 233): A en las seis.**
- **1:** `privateRoomService` y `roomMatchService`.
- **2:** `FindOwnRoom` pasa por `TranslateRoomFailures`.
- **3:** `LeaveRoom` con los textos de un sentido y `Operation=`, más el `catch (DbException)`.
- **4 (R-53):** sale `LogRejection`.
- **5 (R-54):** `ToReason` con la tabla `_reasonsByRejection`.
- **6:** `RoomCleanupService`, con `git mv` y su registro. El nombre del registrador de log4net cambia con la clase.
- **Verificación:**
  - `Host` compila sin avisos de código en una compilación completa;
  - la sonda volvió a dar 96 resultados iguales a `HEAD` y las 6 diferencias aprobadas (cinco de `FindOwnRoom` y la
    `DbException` de `LeaveRoom`).

**Commit de `Rooms`:** `e8d9d4c` (2026-11-11), sin push.

**Push y PR (2026-11-11, a pedido del usuario):**
- La rama `review-standard-v2.4-repositories` se subió en `e8d9d4c`, con 16 commits sobre `main` (`2eb1167`).
- Se abrió el PR #16 (https://github.com/Arclyne/bastion/pull/16), sin rastro de IA, en el formato del PR #15. Está
  abierto y se puede fusionar sin conflictos; el repositorio no tiene CI.
- **Comprobado antes de subir:**
  - autor y committer son solo la identidad del usuario, y ningún mensaje tiene trailers ni menciones;
  - la auditoría de la frontera da lo de siempre (hooks sin instalar y los 3 avisos SQL de `HEAD`);
  - pasan 514 pruebas.
- **Falta de `Host`:** `ServerCertificate`, `ServiceRegistration` y `Sessions`.

**Rama nueva (2026-11-11, a pedido del usuario):** la revisión sigue en `review-standard-v2.4-host`, creada desde
`e8d9d4c` (la punta del PR #16). Solo commits locales hasta que el usuario pida subirla.

### 234 y 235. `ServerCertificate` y `ServiceRegistration` (2026-11-11)

Se revisan juntos porque los dos listan los mismos ocho servicios WCF.
- **`ServerCertificate` (234):**
  - **R-14, aplicado:** `X509Certificate2 certificate = X509CertificateLoader.LoadPkcs12FromFile(…)` antes del
    `return new ServerCertificate(certificate)`. El tipo va explícito por la R-51: el método no está en la clase que
    devuelve.
  - **Cumple:**
    - 2.3.1, 2.6.1, 4.2.1, 5.2.1 (`ApplyCertificateTo` como grupo de método) y 6.2;
    - 9.4.1 (`Load` y `ConfigureServices` comprueban; el constructor es privado);
    - 9.5.1 (es dueña del certificado y lo libera; `Program` usa `using var`).
  - **Pregunta 1 (11.3.1, 9.4.2):** la guarda junta la ruta y la contraseña, pero el mensaje solo nombra
    `Server:CertificatePath`. Si falta la contraseña, el mensaje señala la clave equivocada.
  - **Pregunta 2 (pasada 2 y 3, 4.4.2):**
    - `ConfigureServices` agrega los ocho servicios WCF, y `ServiceRegistration.AddBastionServiceModel` los vuelve a
      listar para el contenedor;
    - para agregar un servicio hay que tocar dos archivos;
    - quien busque dónde se registran los servicios no lo encuentra en una clase llamada `ServerCertificate`.
- **`ServiceRegistration` (235):**
  - **Cumple:**
    - 6.3 y 9.4.1;
    - 10.2.1 (es raíz de composición, así que puede pedir `GetRequiredService`);
    - pasada 4 (cada registro tiene un uso).
  - **Pregunta 3 (pasada 3):** `AddBastionApplication` también registra tipos de `Host`:
    - `FriendPresenceReporter`;
    - `NotificationChannelRegistry` y sus ocho puertos;
    - los dos servicios en segundo plano.

    `AddBastionServiceModel`, en cambio, registra `TimeProvider` y los ocho servicios WCF.
  - **Pregunta 4 (4.4.1, 5.2.1, 3.5.1):** `provider => provider.GetRequiredService<NotificationChannelRegistry>()` se
    repite ocho veces, la mitad en una línea y la otra mitad en dos.
- **Pendiente para `Sessions` (R-49):** `NotificationChannelRegistry` se registra como clase concreta.
- **Propuesta en la copia aparte** (compila sin avisos de código):
  - **`ServerCertificate`:**
    - dos guardas, una con cada clave (la contraseña con `?? throw`);
    - `ApplyTo(IServiceBuilder)` en lugar de `ConfigureServices`, y sin los `using` de los servicios.
  - **`ServiceRegistration`:**
    - `AddBastionApplication` solo con tipos de `Application`;
    - `AddBastionServiceModel` pasa a `AddBastionHost`, con los tipos de `Host`;
    - un `AddBastionServices(this IServiceBuilder)` nuevo, con los ocho `AddService`, junto a los ocho `AddTransient`;
    - un privado `GetChannelRegistry` que se usa como grupo de método en los ocho puertos.
  - **`Program`:** llama `AddBastionHost` y
    `app.UseServiceModel(serviceBuilder => ConfigureServiceModel(serviceBuilder, certificate))`, con un
    `ConfigureServiceModel` privado que llama `AddBastionServices()` y `certificate.ApplyTo(serviceBuilder)`.
- **Sonda (`registration-probe`):**
  - **Contenedor:** los 49 registros son iguales como conjunto; los servicios en segundo plano siguen en el mismo
    orden; los ocho puertos resuelven la misma instancia del registro, antes y después.
  - **CoreWCF:** con el `ServiceBuilder` real de CoreWCF quedan los mismos ocho servicios, en el mismo orden, y
    `ConfigureAllServiceHostBase` se aplica sin error.
  - **`Load` con un certificado de prueba:**
    - carga bien;
    - ruta faltante, ruta en blanco, contraseña vacía o equivocada dan el mismo tipo de excepción;
    - cuando falta la contraseña, el mensaje ahora nombra `Server:CertificatePassword`.

**Preguntas (234 y 235):**
1. Separar la guarda de `Load` para que el mensaje nombre la clave que falta (recomendado: sí).
2. Pasar la lista de servicios WCF a `ServiceRegistration.AddBastionServices`, dejar en `ServerCertificate` solo
   `Load`, `ApplyTo` y `Dispose`, y componer en `Program` (recomendado: A; B, dejarla en `ServerCertificate`; C, un solo
   arreglo de tipos para las dos listas, que se lee peor).
3. Dejar `AddBastionApplication` con los tipos de `Application` y pasar los de `Host` a `AddBastionHost` (recomendado:
   sí).
4. `GetChannelRegistry` como grupo de método en los ocho puertos (recomendado: sí).

**Respuesta del usuario (2026-11-11):** «Sí, A en todas». Queda como regla R-55.

**Aplicado en el repositorio** (la propuesta de la copia aparte, sin cambios):
- **`ServerCertificate`:**
  - dos guardas, una con cada clave; la contraseña con `?? throw`;
  - `ApplyTo(IServiceBuilder)` en lugar de `ConfigureServices`, sin los `using` de los servicios.
- **`ServiceRegistration`:**
  - `AddBastionApplication` solo con tipos de `Application`;
  - `AddBastionHost` (antes `AddBastionServiceModel`) con `TimeProvider`, `FriendPresenceReporter`, el registro de
    canales y sus ocho puertos, los dos servicios en segundo plano y los ocho `AddTransient`;
  - `AddBastionServices(this IServiceBuilder)` con los ocho `AddService`;
  - `GetChannelRegistry` como grupo de método.
- **`Program`:** `AddBastionHost()` y el privado `ConfigureServiceModel`.
- **Verificación:**
  - `Host` compila sin avisos de código en una compilación completa (solo los avisos NU1902/NU1903 de
    `System.Security.Cryptography.Pkcs`, que ya estaban);
  - la sonda volvió a dar los mismos resultados sobre los archivos del repositorio;
  - pasan 514 pruebas (158 de dominio, 220 de aplicación y 136 del cliente).

**Commit de `ServerCertificate` y `ServiceRegistration`:** `08f2766` (2026-11-11), en `review-standard-v2.4-host`,
sin push.

### 236 a 239. `Sessions`: `NotificationChannelRegistry`, `PlayerDisconnectedEventArgs`, `SessionService` y `SessionTranslator` (2026-11-11)

Es la última carpeta de `Host`. También se resuelve aquí la repetición entre servicios que quedó pendiente en `Chat` y
`PrivateChat`.
- **`NotificationChannelRegistry` (236):**
  - **Cumple:**
    - 1.3.1, 2.1–2.2 (ningún método pasa de tres parámetros), 2.6, 2.12.1 y 2.12.2 (`PlayerDisconnected` con
      `EventHandler<T>`);
    - §3, §4 (el cast es directo, sin `as`), 5.1.1, 5.2.1 y §6;
    - 5.1.2: las lambdas de `Closed` y `Faulted` no se cancelan nunca, porque el canal muere con ellas;
    - 9.1, 9.3.1 (`Exception cause` es un parámetro, no un `catch`), 9.4.1, 10.4.1, 11.1.1 y 11.3.1.
    - §7, §8 y §12 no aplican: no es un servicio (R-39) y no es una prueba.
  - **R-23, aplicado:** `((ICommunicationObject)callback).Abort()` juntaba el cast con la llamada. Ahora va en
    `var callbackChannel = (ICommunicationObject)callback;` y luego `callbackChannel.Abort();`, como en `RegisterChannel`.
  - **Pasada 4:** cada miembro público tiene uso. `CountListeners` lo usa `LobbyChatRoom`, `HasNotificationChannel` lo
    usa `PlayerActivity`, `IsPlayerConnected` lo usa `FriendListService` y `PlayerDisconnected` lo usa
    `RoomCleanupService`.
- **`PlayerDisconnectedEventArgs` (237):** cumple 2.14.1, 2.11.1, R-03, 6.x y 9.4.1 (no tiene parámetros de referencia).
  Sin cambios.
- **`SessionService` (238):**
  - **R-44 y R-45, aplicados:** `Subscribe` deja su llamada en `Action subscribe = () => SubscribeInRequestScope(token);`
    y llama `TranslateSessionFailures(nameof(Subscribe), subscribe)`. Es un servicio solo con operaciones `void`, así
    que tiene un único `Translate…Failures(…, Action)`.
  - **Bitácora:** "The database could not be reached while subscribing." pasa a la forma de los demás servicios:
    "The database could not be reached. Operation=Subscribe".
  - **D-06:** en `SubscribeInRequestScope`, la hora y el canal de devolución van cada uno en su variable antes de usarlos.
  - **Cumple:** 7.1.2, 10.3.1 (la excepción de la frontera de red) y R-40. `KeepAlive` es de un solo sentido y está
    vacío: no hay nada que pueda fallar, así que no lleva la R-50.
- **`SessionTranslator` (239):** **R-43, aplicado.** `var fault = new InvalidSessionFault();` y luego
  `FaultExceptionFactory.Create(fault, rejection)`.
- **Pregunta 1 (10.1.1, R-49):** la 10.1.1 define como servicio externo todo colaborador con E/S (red, disco, base) o
  con estado compartido.
  - `NotificationChannelRegistry` hace las dos cosas: llama a los clientes y guarda los canales.
  - `FriendPresenceReporter` escribe en la base.
  - Aun así se reciben como clases concretas: `SessionService` y `RoomCleanupService` reciben el registro, y el registro
    recibe el informador. Las únicas excepciones de la regla son las de `Adapters` y el `ILog`.
- **Pregunta 2 (pasada 2, D-06):** en el registro, 5 de los 11 `Notify…` pasan el traductor como argumento
  (`NotifyPlayer(request.AccountId, MatchmakingTranslator.To…(…))`), y los otros 6 arman antes la variable
  `notification`.
- **Pregunta 3 (4.4.1):** `RegisterChannel` escribe dos veces la misma lambda
  `(_, _) => UnregisterChannel(player.AccountId, callback)`, una para `Closed` y otra para `Faulted`.
- **Pregunta 4 (pasada 3):**
  - `Broadcast(PostedChatLine line)` se lee `line.Line.Sender`. En `ChatTranslator`, en `NotifyMatchChatMessage` y en
    `LobbyChatRoom` el mismo valor se llama `postedLine`.
  - `foreach (KeyValuePair<int, INotificationCallback> subscription …)` usa `subscription.Key` y `subscription.Value`.
  - En `SessionService`, la variable se llama `verifier`; en los demás servicios, la variable lleva el nombre del rol.
  - La bitácora dice "Player left notifications.", que no es claro y no hace pareja con "Player subscribed to
    notifications.".
- **Pregunta 5 (pasada 2 entre servicios, pendiente desde 218–219 y 228–229):**
  - `RequireSessionToken`: 6 métodos privados iguales (`Chat`, `Friendship`, `Conversation`, `Room`, `Match`,
    `Matchmaking`), más el `if` en línea de `SessionService`.
  - `RequireText`: 2 iguales, en `ChatService` y `ConversationService`.
  - `GetUtcNow`: 7 privados iguales y 5 expresiones en línea (`_timeProvider.GetUtcNow().UtcDateTime`).
  - El ámbito (`CreateScope` + `GetRequiredService`) ya lo decidió la R-44, así que no se pregunta.
  - `SessionTranslator.RequireSessionToken` era una de las piezas de apoyo de la clase compartida que el usuario no
    eligió en 218–219. Aquí se propone sola, sin esa clase y sin `RequestScope`.
- **Pregunta 6 (R-47):** los privados del registro están en este orden: `GetUtcNow`, `NotifyPlayers`, `NotifyPlayer`,
  `DeliverNotification`, `AbortFailedChannel`, `UnregisterChannel` y `OnPlayerDisconnected`.
  - Salvo `GetUtcNow`, forman una cadena en la que cada uno va debajo del que lo llama.
  - Con la R-47 al pie de la letra, `UnregisterChannel` iría primero, porque lo usa `RegisterChannel`, el primer
    público. Eso rompe la cadena.
- **Propuesta en la copia aparte** (`Host` compila sin avisos de código en una compilación completa; solo
  NU1902/NU1903):
  - **Pregunta 1:**
    - `Sessions/INotificationChannelRegistry` (evento `PlayerDisconnected` y `RegisterChannel`) y
      `Friends/IFriendPresenceReporter` (`ReportConnected` y `ReportDisconnected`);
    - las tres clases reciben las interfaces;
    - `ServiceRegistration` registra `AddSingleton<IFriendPresenceReporter, FriendPresenceReporter>()` y
      `AddSingleton<INotificationChannelRegistry>(GetChannelRegistry)`;
    - el constructor de `SessionService` pasa a una línea por parámetro, como `RoomCleanupService`.
  - **Pregunta 2:** los 11 `Notify…` arman `notification` en su variable. `NotifyPrivateMessage` también guarda
    `int recipientAccountId = delivery.Message.RecipientId.GetValueOrDefault();`.
  - **Pregunta 3:** `EventHandler unregisterChannel = (_, _) => UnregisterChannel(player.AccountId, callback);` se usa en
    `Closed` y en `Faulted`.
  - **Pregunta 4:**
    - `postedLine` en `Broadcast` y en `IChatBroadcaster` (y en `FakeChatBroadcaster` de las pruebas, al aplicarlo);
    - `foreach ((int accountId, INotificationCallback callback) in _callbacksByAccountId)`, la primera deconstrucción de
      la solución;
    - `sessionVerifier`;
    - "Player unsubscribed from notifications. AccountId=…".
  - **Pregunta 5:**
    - `SessionTranslator.RequireSessionToken` y `ChatTranslator.RequireText` son públicos y estáticos; los 8 privados
      salen;
    - cada operación llama `string token = SessionTranslator.RequireSessionToken(sessionToken);`;
    - `GetUtcNow` se queda.
  - **Pregunta 6:** la cadena va junta, de arriba abajo (`NotifyPlayers` … `OnPlayerDisconnected`), y `GetUtcNow` pasa
    al final, como en `MatchmakingService`.
- **Sonda (`sessions-probe`):** compara `HEAD` (las clases `Old…`) con la propuesta: 36 casos iguales y 2 diferencias,
  que son los textos de bitácora de las preguntas 4 y de la R-44.
  - **Registro, en un mismo escenario:**
    - tres canales, la difusión sin el remitente y los 11 `Notify…` con el contenido de cada notificación;
    - `CommunicationException` y `TimeoutException` al entregar, con su `Abort`, la baja, el aviso de presencia, la cola
      y el evento;
    - `Closed` y `Faulted`, y un segundo canal del mismo jugador que el cierre del primero no borra.
    - Todo es igual. Solo cambia el texto Info de la baja (4 líneas).
  - **`Subscribe`:** el token nulo, la sesión inválida, el error de programación y la llamada fuera de WCF dan lo mismo.
    La base caída da la misma falla; solo cambia el texto Error, que ahora lleva `Operation=Subscribe`.
  - **Token nulo en las 28 operaciones de los 7 servicios, y texto nulo en las 4 que tienen un parámetro `text`:** todo
    es igual. Sale la falla de sesión, la falla de chat `InvalidMessage` en las 3 que exigen texto, o nada en las
    operaciones de un solo sentido. `SearchPlayers` no exige el texto y llega al ámbito en las dos versiones.
  - **Registro del contenedor:**
    - los 9 tipos (`INotificationChannelRegistry` y los 8 puertos) resuelven el mismo registro;
    - `IFriendPresenceReporter` es un singleton;
    - con `AddBastionAdapters` también se arman `SessionService` y los dos servicios en segundo plano.

**Preguntas (236 a 239):**
1. 10.1.1: `INotificationChannelRegistry` e `IFriendPresenceReporter` (recomendado: A, las dos interfaces; B, separar el
   registro en dos interfaces por rol; C, dejar las clases concretas).
2. Los 11 `Notify…` con su variable `notification` (recomendado: sí).
3. Una sola variable `unregisterChannel` para `Closed` y `Faulted` (recomendado: sí).
4. Los cuatro nombres y el texto de la bitácora (recomendado: sí en los cuatro).
5. `SessionTranslator.RequireSessionToken` y `ChatTranslator.RequireText` compartidos; `GetUtcNow` se queda
   (recomendado: A; B, dejar todo; C, también `GetUtcNow` con un método de extensión en `Host/Common`).
6. R-47 con cadenas: los privados que se llaman en cadena van juntos y de arriba abajo; `GetUtcNow` al final
   (recomendado: A; B, la R-47 al pie de la letra; C, dejar el orden de hoy).

**Respuesta del usuario (2026-11-11):** «Sí, A en todas». La R-49 se amplía a `Host`, la R-47 se precisa con las cadenas
y la pregunta 5 queda como R-56.

**Aplicado en el repositorio** (la propuesta de la copia aparte, sin cambios):
- `Sessions/*`, `Friends/FriendPresenceReporter` y las dos interfaces nuevas;
- `RoomCleanupService` y `ServiceRegistration`;
- los seis servicios sin sus `RequireSessionToken` y `RequireText` privados, y `ChatTranslator.RequireText`;
- `IChatBroadcaster.Broadcast(PostedChatLine postedLine)`, y el mismo nombre en `FakeChatBroadcaster` de las pruebas.
- **Verificación:**
  - `Host` compila sin avisos de código en una compilación completa (solo NU1902/NU1903);
  - la sonda dio 36 casos iguales y las 2 diferencias de texto esperadas;
  - pasan 514 pruebas (158 + 220 + 136).

**Commit de `Sessions`:** `ebb0e3b` (2026-11-11), en `review-standard-v2.4-host`, sin push.

**Cierre de la capa `Host` (2026-11-11):** los archivos 215 a 239 están revisados. En `review-standard-v2.4-host` hay
dos commits locales (`08f2766` y `ebb0e3b`). Sigue `Contracts`, con las notas que se dejaron para esa capa (R-27 en
`IConversationService` y en los demás contratos sin `<summary>`, la `FaultException` de `FindOwnRoom` y de
`StartSearch`, el `<summary>` de `AbandonMatch` y `RoomOptions` frente a `RoomSettings`).

## Capa `Bastion.Contracts`

Son 61 archivos (240 a 300), en orden de carpeta: `Accounts`, `Chat`, `Friends`, `Matches`, `Matchmaking`,
`Notifications`, `PrivateChat`, `Rooms`, `ServiceEndpoints` y `Sessions`. Datos generales:
- **Marco:** `netstandard2.0`, con `LangVersion latest` y `Nullable` de `Directory.Build.props`. No hay
  `ArgumentNullException.ThrowIfNull`, pero los contratos no tienen métodos con cuerpo.
- **Clases de datos:** los `[DataContract]` son objetos de transferencia: la 2.11.3 (get y set públicos) y la R-03 no
  piden constructor.
- **R-27 al cerrar la capa:** con `GenerateDocumentationFile` activo en la copia aparte, solo faltan
  `IFriendshipService` (9 errores CS1591) e `IConversationService` (5). Los `cref` de `IAccountService` resuelven.
- **Para preguntar en su carpeta:** tres `<summary>` dicen "signed-in player" (`IMatchService`, `IMatchmakingService`
  e `ISessionService`). La R-41 fija "login" en los textos del programa, pero no menciona la documentación XML.

### 240 a 246. `Accounts` (2026-11-11)

- **Cumple:**
  - 1.3.1, 2.4.1, 2.11.1 y 2.11.3 (objetos de transferencia con get y set públicos);
  - 2.15.1 (`RestrictionReason` en singular), 3.6.1 (un atributo por línea), 6.1, 6.3 y 6.4.
  - §8 y §9 no aplican: no hay comentarios ni cuerpos de método.
- **Pasada 3:**
  - `RestrictionReason.Pending` usa el mismo término que `AccountStatus.Pending` del dominio y que `ILoginService`.
  - `LockMinutes` es el nombre de `AccountRestrictedException` en `Application` y en `Client.Networking`.
  - `Identifier` es el nombre de `LoginViewModel` y de `ILoginService` ("nickname or email").
  - Se quedan.
- **Pasada 4:** cada propiedad tiene uso.
  - `LockMinutes` lo usa `LoginViewModel`, y `PreferredLanguage` lo usa `ApplyPreferredLanguage`.
  - `DeviceFingerprint` y `ClientVersion` los usa `LoginTranslator.ToConnection`.
  - `AccountClient.ToRestriction` traduce los cuatro valores de `RestrictionReason`.
- **7.1.1 (R-27), aplicado:** `IAccountService` no tenía documentación. Ahora lleva:
  - el `<summary>` del servicio: "Logs registered players in and opens their session.";
  - el `<summary>` de `LogIn`, con el registro en la bitácora de accesos;
  - los dos `<param>` y el `<returns>`;
  - tres `<exception>`, con el mismo texto que `ILoginService`: `InvalidCredentialsFault` (también por credenciales o
    dispositivo faltantes), `AccountRestrictedFault` y la `FaultException` del servidor.
- **Pregunta 1 (9.4.1, pasada 2):** `LogIn(PlayerCredentials credentials, ClientDevice device)` es la única operación con
  argumentos de red sin `?`. `AccountService` los compara con `null` (R-40), y los demás contratos los declaran
  anulables (`RoomOptions? options`, `string? sessionToken`).
- **Pregunta 2 (R-44, pasada 2):** `AccountService` se revisó en 215–217, antes de que existiera la R-44. Es el único
  servicio que todavía tiene el `try` dentro de la operación y la hora como argumento.
- **Propuesta en la copia aparte** (`Host` compila sin avisos de código):
  - **Pregunta 1:** `PlayerCredentials? credentials, ClientDevice? device` en el contrato y en `AccountService`.
  - **Pregunta 2:**
    - `DateTime now` y `string password` van cada uno en su variable;
    - `Func<PlayerSession> logIn = () => LogInInRequestScope(attempt, password);`;
    - `return TranslateLoginFailures(nameof(LogIn), connection.IpAddress, logIn);`, con la IP como contexto, como el
      `MatchId` de `MatchService`.
    - Las guardas de credenciales y dispositivo, `ToConnection` y `ToAttempt` siguen fuera del `try`, como hoy.
- **Sonda (`accounts-probe`):** compara `HEAD` con la propuesta en 10 casos: éxito, contraseña nula, credenciales nulas,
  dispositivo nulo, credenciales inválidas, cuenta bloqueada (15 min) y vetada, login sin guardar, base caída y error de
  programación.
  - Son iguales la respuesta, la falla y su detalle, y el intento que recibe `ILoginService` (identificador recortado,
    IP, dispositivo, hora y largo de la contraseña).
  - Solo cambian los dos textos Error, que ahora llevan `Operation=LogIn;` antes de `IpAddress=`.

**Preguntas (240 a 246):**
1. Argumentos anulables en `LogIn` (recomendado: sí).
2. La R-44 en `AccountService`, con `Operation=LogIn; IpAddress=…` (recomendado: sí).

**Respuesta del usuario (2026-11-11):** «Sí, A en las dos». Se aplicó la propuesta sin cambios (`IAccountService` y
`AccountService`).
- **Verificación:**
  - `Host` y `Client.Networking` compilan sin avisos de código en una compilación completa (solo NU1902/NU1903);
  - pasan 514 pruebas.

**Commit de `Accounts`:** `2a59451` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 247 a 253. `Chat` (2026-11-11)

Los archivos son `ChatChannelForbiddenFault`, `ChatMessageReceipt`, `ChatMessageRejectedFault`, `ChatRejectionReason`,
`IChatService`, `LobbyChatLog` y `LobbyChatMessage`.
- **Cumple:**
  - 1.3.1, 2.4.1, 2.11.1 y 2.11.3, 2.15.1, 3.6.1 y §6;
  - §8 y §9 no aplican.
- **`IChatService` (7.1–7.2, R-27):** ya estaba documentado. Se comparó cada `<exception>` con lo que hace `ChatService`, y
  todo coincide:
  - `SendChatMessage` y `OpenLobbyChat` solo leen la base: las sanciones y las palabras vetadas. El chat general guarda
    los mensajes en memoria (`LobbyChatRoom`), así que basta "could not reach the database".
  - `SendMatchChatMessage` guarda por `MatchRepository`, que traduce a `MatchRepositoryException` (R-36), así que
    "could not read or write the database" también es correcto.
  - `ChatChannelForbiddenFault` sale cuando el autor no tiene una participación sin terminar en la partida
    (`FindAccountIdsWithUnfinishedParticipation`).
- **Pasada 3:**
  - `LobbyChatLog` se queda. "Chat log" es el historial de mensajes, en inglés común, y cada capa tiene su propio
    nombre (`LobbyChatHistory` en `Application`, `LobbyChatTranscript` en el cliente), así que los traductores no tienen
    dos tipos con el mismo nombre.
  - **Pregunta 2:** `LobbyChatLog.ConnectedPlayers` es un `int`, pero el nombre en plural se lee como una lista
    (2.1.2). El proyecto llama `…Count` a los conteos (`GameMode.PlayerCount`, `closedRoomCount`). El nombre viaja por
    toda la cadena:
    - `LobbyChatHistory` y `LobbyChatService` en `Application`;
    - `ChatTranslator` en `Host`;
    - `LobbyChatTranscript` y `ChatContractTranslator` en `Client.Networking`;
    - `LobbyChatViewModel`;
    - dos pruebas.
- **Pasada 4:**
  - `IsMuted` y `MutedUntil` hacen falta los dos: una sanción permanente da `IsMuted = true` con `MutedUntil = null`
    (`ChatMute.FromSanctionsInEffect`).
  - **Pregunta 1:** el cliente no lee ningún `MessageId`. Hay 6 contratos con ese campo:
    - `ChatMessageReceipt` y `LobbyChatMessage`;
    - `ChatMessageNotification`, `MatchChatMessageNotification` y `PrivateMessageNotification`;
    - `PrivateChatMessage`.
  - De los recibos, el cliente solo usa `SentAt` (`ChatClient`, `ConversationClient`).
  - La CU-27 no lo necesita: el reporte apunta a la partida o a la sala, no a un mensaje (RN-01).
  - Quitarlo arrastra a `Application`: `LobbyChatRoom` numera los mensajes solo para el contrato, y lo prueba
    `TestLobbyChatRoom`.

**Preguntas (247 a 253):**
1. `MessageId` sin lectura en el cliente (recomendado: A, se queda en los 6 contratos como identidad del mensaje en la
   red y queda como regla, para no volver a preguntarlo en `Notifications` y `PrivateChat`; B, quitarlo de los 6, con su
   arrastre en los traductores y en `LobbyChatRoom`).
2. `ConnectedPlayers` → `ConnectedPlayerCount` (recomendado: A, en toda la cadena, con la variable `connectedPlayerCount`
   y la constante de la prueba; B, solo en el contrato; C, dejarlo). Es un renombre: se verifica con la compilación
   completa y las pruebas al aplicarlo.

**Respuesta del usuario (2026-11-11):** «Sí, A en las dos».
- **Pregunta 1:** queda como regla R-57, sin cambios en el código.
- **Pregunta 2:** `ConnectedPlayerCount` en 9 archivos:
  - `LobbyChatLog`, `LobbyChatHistory` (con el parámetro `connectedPlayerCount`) y `LobbyChatService`;
  - `ChatTranslator`;
  - `LobbyChatTranscript`, `ChatContractTranslator` y `LobbyChatViewModel`;
  - `TestChatContractTranslator` (con la constante) y `TestLobbyChatService`.
- **Verificación:**
  - `Host` y `Client` compilan sin avisos de código en una compilación completa (solo NU1902/NU1903);
  - pasan 514 pruebas;
  - la copia aparte recibió los cuatro archivos del servidor.

**Commit de `Chat`:** `1326770` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 254 a 264. `Friends` (2026-11-11)

Los archivos son:
- `FriendList`, `FriendListEntry`, `FriendRequestEntry` y `FriendRequestList`;
- `FriendRequestResult`, `FriendshipRejectedFault` y `FriendshipRejectionReason`;
- `IFriendshipService`, `PlayerRelationship`, `PlayerSearchEntry` y `PresenceState`.

Revisión:
- **Cumple:**
  - 1.3.1, 2.4.1, 2.11.1 y 2.11.3, 2.15.1 (las cuatro enumeraciones en singular), 3.6.1 y §6;
  - §8 y §9 no aplican.
- **Pasada 3:** los nombres se leen solos y siguen el vocabulario de `Application`:
  - `OwnFriendCode`, `ListedAt`, `LastSeenAt`, `RequestedAt` y `ExpiresAt`;
  - `PlayerRelationship.Self` y `FriendshipRejectionReason.OwnAccount`;
  - en las operaciones, `requesterFriendCode` y `recipientFriendCode`.
- **Pasada 4:** cada propiedad y cada valor tiene uso.
  - `FriendContractTranslator` traduce los 8 rechazos, las 5 relaciones, los 2 resultados y las 2 presencias.
  - `ListedAt` lo usan `FriendRowViewModel` y `FriendRequestRowViewModel` para los textos relativos.
- **7.1.1 (R-27), aplicado en la copia aparte:** `IFriendshipService` no tenía documentación. Ahora lleva el `<summary>`
  del servicio y los de sus ocho operaciones, con `<param>`, `<returns>` y `<exception>`.
  - El texto sigue el de `IFriendListService` e `IFriendRequestService`.
  - Agrega lo que pasa en `Host`: un código faltante llega como el rechazo de cada operación (`PlayerNotFound`,
    `RequestNotFound` o `NotFriends`), y una búsqueda sin texto no da resultados.
  - Las notificaciones: la solicitud y la amistad llegan al otro jugador.
  - Las operaciones que solo leen dicen "could not reach the database", y las que guardan, "could not read or write
    the database", como en `IChatService`. `FriendshipService` atrapa `DbUpdateException` y `DbException`.
  - Compila con `GenerateDocumentationFile`: los errores CS1591 de `IFriendshipService` desaparecen. Solo quedan los
    5 de `IConversationService`.
- **Pregunta 1 (2.1.2, incumplimiento):** `FriendRequestList.Received` y `.Sent` son arreglos, pero sus nombres son
  participios, no sustantivos en plural.
  - Lo mismo pasa en `FriendRequestBoard` de `Application` (85–108, no se vio entonces) y en `FriendRequestListing` del
    cliente.
  - `FriendshipTranslator` ya llama `receivedRequests` y `sentRequests` a sus variables.
  - Los campos `_received` y `_sent` de `FriendRequestsViewModel` se ven al revisar `Client`.

**Pregunta (254 a 264):**
1. `Received`/`Sent` → `ReceivedRequests`/`SentRequests` (recomendado: A, en toda la cadena:
   - `FriendRequestBoard`, con sus parámetros;
   - `FriendshipTranslator`;
   - el contrato;
   - `FriendRequestListing` y `FriendContractTranslator`;
   - el uso en `FriendRequestsViewModel`;
   - tres pruebas.

   B, solo en el contrato; C, dejarlo.) Es un renombre: se verifica con la compilación completa y las pruebas al
   aplicarlo.

**Respuesta del usuario (2026-11-11):** «Sí, toda la cadena».
- **Aplicado:**
  - la documentación de `IFriendshipService`, desde la copia aparte;
  - `ReceivedRequests`/`SentRequests` en `FriendRequestBoard` (con los parámetros `receivedRequests`/`sentRequests`),
    en las variables de `FriendRequestService.ListFriendRequests`, en `FriendshipTranslator`, en el contrato, en
    `FriendRequestListing` y `FriendContractTranslator`, en `FriendRequestsViewModel` y en
    `TestFriendContractTranslator` y `TestFriendRequestService`.
- **Verificación:**
  - `Host` y `Client` compilan sin avisos de código en una compilación completa (solo NU1902/NU1903);
  - pasan 514 pruebas.

**Commit de `Friends`:** `43e62a0` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 265 y 266. `Matches` (2026-11-11)

- **`MatchNotJoinedFault` (266):** cumple. Lleva el mismo nombre que `MatchNotJoinedException` de `Application`, y lo usa
  `MatchClient`.
- **`IMatchService` (265):**
  - **Cumple:** 7.1.1, el orden de la 7.2.1 y 3.6.1.
  - **7.2 (corregido en la copia aparte), pendiente desde 223–224:** el `<summary>` de `AbandonMatch` decía "that player
    loses and the rival wins". Ahora sigue a `IMatchAbandonmentService`: con dos jugadores el rival gana y la partida
    termina; con cuatro, sigue mientras queden dos.
  - **7.2.2 (corregido en la copia aparte):** la `FaultException` decía "could not reach the database". `MatchService`
    también la lanza cuando falla `MatchRepository`, que lee y guarda la partida. Ahora dice "could not read or write the
    database", como las demás operaciones que guardan.
  - Compila con `GenerateDocumentationFile`.
  - **Pregunta 1 (R-41 en la documentación):**
    - la R-41 pide "login" y "log in" en la bitácora, en las excepciones y en las fallas, pero no menciona la
      documentación XML;
    - tres `<summary>` de servicio dicen "signed-in player": `IMatchService`, `IMatchmakingService` e `ISessionService`;
    - la copia aparte ya dice "logged-in player" en `IMatchService`.

**Pregunta (265 y 266):**
1. La R-41 también en la documentación XML (recomendado: A, "logged-in player" en los tres, cada uno al revisar su
   carpeta; B, dejar "signed-in", porque la documentación no es un texto que vea el jugador).

**Respuesta del usuario (2026-11-11):** «Sí, logged-in». La R-41 se amplía a la documentación XML.
- **Aplicado:** `IMatchService`, desde la copia aparte. Es un cambio solo de documentación; `Host` compila sin avisos de
  código.

**Commit de `Matches`:** `40e3763` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 267 a 269. `Matchmaking` (2026-11-11)

- **`SearchRejectedFault` y `SearchRejectionReason` (268 y 269):** cumplen. Repiten los tres valores de
  `SearchRejection` de `Application`, y `MatchmakingClient` traduce los tres.
- **`IMatchmakingService` (267):** sin preguntas. Se aplicaron reglas ya decididas y la nota pendiente desde 225–227:
  - **R-41:** "signed-in player" → "logged-in player" en el `<summary>` del servicio.
  - **7.2.2 (nota de 225–227):** la `FaultException` de `StartSearch` dice ahora "could not reach the database to check
    the session or the unfinished matches of the player". `MatchmakingService` la lanza por `DbException` y por
    `MatchRepositoryException`, y `StartSearch` solo lee.
  - **7.2:** `SearchRejectedFault` nombra sus tres casos, como `IChatService` e `IFriendshipService`: no tiene canal de
    notificaciones, tiene una partida sin terminar o está en una sala.
  - Las tres `<exception>` de `StartSearch` van en varias líneas, como en el resto del archivo y en `IChatService`.
  - `CancelSearch` y `ConfirmPresence` son de un solo sentido: no dejan salir excepciones (R-50), así que no llevan
    `<exception>`.
- **Verificación:** compila con `GenerateDocumentationFile` (solo quedan los 5 CS1591 de `IConversationService`), y
  `Contracts` compila en el repositorio. Solo cambió documentación.

**Commit de `Matchmaking`:** `3878797` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 270 a 286. `Notifications` (2026-11-11)

Son 17 archivos: `Notification` (la base abstracta con los 12 `[KnownType]`), las 12 notificaciones,
`MatchFoundParticipant`, `RoomClosedReason`, `SearchEndedReason` e `INotificationCallback`.
- **Cumple:**
  - 1.3.1, 2.4.1, 2.11.1 y 2.11.3, 2.14.1 (cada notificación termina en `Notification`, su clase base), 2.15.1,
    3.6.1 (un `[KnownType]` por línea) y §6;
  - §8 y §9 no aplican.
- **Pasada 3:**
  - `SearchEndedReason` se queda aunque `Application` y el cliente digan `SearchEndReason`. En `Contracts` las razones
    usan el participio (`RoomClosedReason`), y cada capa tiene su propio tipo (como `LobbyChatLog`).
  - `RoomClosedNotification.Code` se lee como el código de la sala: lo dice el nombre del tipo.
- **Pasada 4:**
  - `NotificationCallback` y los traductores del cliente leen cada propiedad. `MessageId` se queda por la R-57.
  - `RoomClosedReason` solo tiene `HostLeft`, pero `RoomContractTranslator.ToCloseReason` lo traduce.
- **Pregunta 1 (7.1.1):** `INotificationCallback` es un `[ServiceContract]`, el contrato de devolución que el cliente
  atiende, y no tiene documentación.
  - La R5 de la regla del proyecto admite `<summary>` en todo contrato `[ServiceContract]`, pero la glob de CS1591 solo
    cubre `I*Service.cs`.
  - Si se documenta, la clase del cliente que lo implementa (`NotificationCallback`) lleva `<inheritdoc/>` en la clase y
    en `ReceiveNotification` (7.1.2).
  - En la copia aparte, el `cref` a `Sessions.ISessionService.Subscribe` resuelve con `GenerateDocumentationFile`.

**Pregunta (270 a 286):**
1. Documentar `INotificationCallback`, con `<inheritdoc/>` en `NotificationCallback` (recomendado: A; B, dejarlo, porque
   la 7.1.1 dice "servicio" y la glob solo cubre `I*Service.cs`).

**Respuesta del usuario (2026-11-11):** «Sí, documéntalo».
- **Aplicado:**
  - `INotificationCallback`, desde la copia aparte;
  - `<inheritdoc/>` en `NotificationCallback`, sobre la clase y sobre `ReceiveNotification`.
- **Verificación:** `Client.Networking` compila sin avisos de código en una compilación completa (solo NU1902/NU1903) y
  pasan las 136 pruebas del cliente. Solo cambió documentación.

**Commit de `Notifications`:** `ac2a8b4` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 287 a 290. `PrivateChat` (2026-11-11)

Los archivos son `ConversationEntry`, `IConversationService`, `PrivateChatMessage` y `PrivateConversationLog`.
- **Cumple:**
  - 1.3.1, 2.4.1, 2.11.1 y 2.11.3, 3.6.1 y §6;
  - §8 y §9 no aplican.
- **Pasada 3:**
  - `PrivateConversationLog` se queda por la misma razón que `LobbyChatLog`;
  - `UnreadCount` sigue la forma `…Count`;
  - `ConversationEntry`, `ConversationSummary` y `ConversationPreview` son el mismo dato con un tipo por capa.
- **Pasada 4:** `ConversationContractTranslator` lee cada propiedad. `MessageId` se queda por la R-57.
- **7.1.1 (R-27), aplicado sin preguntas:** `IConversationService` no tenía documentación (nota de 228–229).
  - Ahora lleva el `<summary>` del servicio y los de sus cuatro operaciones, con `<param>`, `<returns>` y `<exception>`.
  - El texto sigue a `IPrivateChatService`, y le agrega:
    - el código faltante, que `ConversationService` rechaza con `PlayerNotFound`;
    - el aviso al destinatario;
    - "could not reach the database" en `ListConversations`, que solo lee;
    - "could not read or write the database" en las otras tres: `OpenConversation` y `MarkConversationRead` marcan los
      mensajes como leídos, y `SendPrivateMessage` guarda el mensaje.
  - Con esto, `Contracts` compila sin errores con `GenerateDocumentationFile` (ni CS1591 ni avisos IDE).
- **Verificación:** `Contracts` compila en el repositorio. Solo cambió documentación.

**Commit de `PrivateChat`:** `9e3f09c` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 291 a 297. `Rooms` (2026-11-11)

Los archivos son `IRoomService`, `RoomGameMode`, `RoomMemberState`, `RoomOptions`, `RoomRejectedFault`,
`RoomRejectionReason` y `RoomState`. Con esto, `ServiceEndpoints` es el 298 y `Sessions` son el 299 y el 300.
- **Cumple:**
  - 1.3.1, 2.4.1, 2.11.1 y 2.11.3, 2.15.1, 3.6.1 y §6;
  - §8 y §9 no aplican.
- **Pasada 4:**
  - `RoomContractTranslator` y `RoomClient` leen cada propiedad, los 14 rechazos y los 3 modos.
  - `RetryAfterSeconds` sirve para `TooManyAttempts`.
  - "six-character code" coincide con `RoomPolicy.CodeLength = 6`.
- **7.2 y 7.2.2 (corregido en la copia aparte; incluye la nota de 231–233):**
  - el `<summary>` del servicio ahora también nombra lo que hace el anfitrión: cambiar las opciones e iniciar la partida;
  - `SetReady` y `FindOwnRoom` no documentaban la `FaultException`. Las dos pasan por `TranslateRoomFailures` (R-44),
    así que ahora dicen "could not reach the database";
  - `CreateRoom` y `ChangeOptions` guardan la sala (`RoomRepositoryException`), así que dicen "could not read or write
    the database";
  - `StartMatch` dice "could not reach the database or save the match; the room stays open";
  - `JoinRoom` se queda con "could not reach the database": no guarda nada;
  - los rechazos se quedan con "the detail says why", porque son 14 y la enumeración los nombra.
  - Compila con `GenerateDocumentationFile`.
- **Pregunta 1 (pasada 3, nota de 231–233):** el contrato y el cliente dicen "options" (`RoomOptions`, `ChangeOptions`,
  `RoomState.Options`, `PrivateRoomOptions`). El servidor dice "settings" (`RoomSettings` del dominio,
  `RequestedRoomSettings`, `ChangeSettings`, `RoomSettingsValidator`).
  - Dentro del contrato se mezclan las dos palabras: la prosa de `ChangeOptions` decía "settings" (la copia aparte ya
    dice "options"), y `RoomRejectionReason` tiene `InvalidSettings`.
  - Si el contrato se llamara `RoomSettings`, chocaría con el `RoomSettings` del dominio en `RoomTranslator`, que usa los
    dos.

**Pregunta (291 a 297):**
1. "Options" frente a "settings". Recomendado: A.
   - **A:** cada capa conserva su palabra (como `LobbyChatLog`) y el contrato usa solo "options":
     - la prosa en la copia aparte;
     - `RoomRejectionReason.InvalidSettings` → `InvalidOptions`, con su línea en `RoomTranslator` y su `case` en
       `RoomContractTranslator`.
     - El `RoomRejection.InvalidSettings` del cliente se ve al revisar `Client`.
   - **B:** solo la prosa; `InvalidSettings` se queda.
   - **C:** "settings" en todo: el contrato, el cliente y sus pantallas. Es el arrastre más grande, y el choque de
     nombres en `RoomTranslator` obliga a un alias.

**Respuesta del usuario (2026-11-11):** «Sí, A».
- **Aplicado:**
  - la documentación de `IRoomService`, desde la copia aparte;
  - `RoomRejectionReason.InvalidOptions`, con su entrada en la tabla de `RoomTranslator`
    (`[RoomRejection.InvalidSettings] = RoomRejectionReason.InvalidOptions`) y su `case` en `RoomContractTranslator`.
  - Queda para la revisión de `Client`: el `RoomRejection.InvalidSettings` del cliente.
- **Verificación:**
  - `Host` y `Client` compilan sin avisos de código en una compilación completa (solo NU1902/NU1903);
  - pasan 514 pruebas.

**Commit de `Rooms`:** `ab66fbb` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 298. `ServiceEndpoints` (2026-11-11)

- **Cumple:** 2.3.1, 2.3.2 (todas son `const`) y 6.2. Cada constante y `CreateAddress` se usan, todos en
  `ServerAddress` del cliente.
- **9.4.1 (incumplimiento, corregido sin preguntas):** `CreateAddress(string host, int port, string path)` no comprobaba
  sus parámetros de referencia. `netstandard2.0` no tiene `ThrowIfNull`, así que van dos guardas
  `if (x is null) { throw new ArgumentNullException(nameof(x)); }`.
- **R-04 (corregido):** `return new UriBuilder(…).Uri` pasa a `var addressBuilder = new UriBuilder(…);` y luego
  `return addressBuilder.Uri;`.
- **Para la revisión de configuración (4.4.2):**
  - `ServiceModel.config` del servidor repite en XML las ocho rutas (`/accounts`…);
  - `appsettings.json` repite el puerto 8000 de `DefaultPort`.
  - La configuración XML no puede leer las constantes de C#.

### 299 y 300. `Sessions` (2026-11-11)

- **`InvalidSessionFault` (300):** cumple.
- **`ISessionService` (299):**
  - **R-41:** "signed-in player" → "logged-in player".
  - El resto ya estaba documentado y coincide con `SessionService`: la `FaultException` de `Subscribe` sale por
    `DbException`, y `KeepAlive` es de un solo sentido y no hace nada.

**Commit de `ServiceEndpoints` y `Sessions`:** `6d689a1` (2026-11-11), sin push.

### Cierre de la capa `Bastion.Contracts` (2026-11-11)

- **R-27:** `Bastion.Contracts.csproj` activa `GenerateDocumentationFile`, en el commit `ab0c785`.
  - CS1591 ya es error en `I*Service.cs` por el `.editorconfig`.
  - `Contracts` compila sin avisos, tampoco IDE0005.
  - `Host` y `Client` compilan sin avisos de código, y pasan 514 pruebas.
- **Commits de la capa en `review-standard-v2.4-host`** (todos locales, sin push): `2a59451`, `1326770`, `43e62a0`,
  `40e3763`, `3878797`, `ac2a8b4`, `9e3f09c`, `ab66fbb`, `6d689a1` y `ab0c785`.
- **Reglas nuevas o ampliadas en la capa:**
  - R-57 (`MessageId`);
  - R-41 en la documentación XML.
- **Notas para `Client.Networking` y `Client`:**
  - `RoomRejection.InvalidSettings` del cliente;
  - los campos `_received` y `_sent` de `FriendRequestsViewModel`;
  - R-41 en los textos de `Client` y `Client.Networking`;
  - R-54 en `RoomContractTranslator`.
- **Sigue `Client.Networking`.**

## Capa `Bastion.Client.Networking`

Son 85 archivos (301 a 385), en orden de carpeta. El primer conteo decía 87; se corrigió al revisar `Chat`:

| Carpeta | Archivos |
| --- | --- |
| `Accounts` | 301–310 |
| `Channels` | 311–317 |
| `Chat` | 318–327 |
| `Friends` | 328–341 |
| `Matches` | 342–344 |
| `Matchmaking` | 345–349 |
| `Notifications` | 350–366 |
| `PrivateChat` | 367–373 |
| `Rooms` | 374–383 |
| `ServerConnection` | 384 |
| `Sessions` | 385 |

Datos generales:
- **Composición:** `BastionGame` crea `ServerConnection`, y este crea los ocho clientes. `ServerConnection` hace de clase
  de registro de los servicios del cliente (10.2.1).
- **Canales:** cada cliente de petición y respuesta crea su propio `ServiceChannel<T>` con `new`. `NotificationClient`
  crea su `DuplexChannelFactory` (pregunta 3 de 301–310).

### 301 a 310. `Accounts` (2026-11-11)

Los archivos son:
- `AccountClient`, `IAccountClient`, `LoginCredentials` y `SignedInSession`;
- `AccountRestriction` y `AccountRestrictedException`;
- `ConnectionLostException`, `InvalidCredentialsException`, `ServerErrorException` y `ServerUnreachableException`.

Revisión:
- **Cumple:**
  - 2.x, 3.x, 4.3.2 (`ToRestriction` con `default` que lanza) y 9.1.2 (los `catch` van del más derivado al menos
    derivado);
  - 9.4.1;
  - 9.6.1: las excepciones sin datos tienen los tres constructores de CA1032; `AccountRestrictedException` tiene datos,
    y su único constructor los recibe.
  - `IAccountClient` no es `I…Service` ni `[ServiceContract]`, así que no lleva documentación (R-39, R5).
- **Se aplican sin preguntar, al cerrar el grupo:**
  - **R-10:** `SignedInSession` → `LoggedInSession`, con `git mv`, y `ToSignedInSession` → `ToLoggedInSession`. Cambian
    unos 20 archivos de `Client` y tres pruebas, entre ellos el campo `_signedInSession` de `ScreenNavigator`.
  - **R-41:** "The account cannot sign in." → "The account cannot log in.", igual que en el servidor.
  - **R-14:** `ToSignedInSession` lleva `??` en sus tres argumentos, que pasan a variables antes del `return new`.
- **Pregunta 1 (6.4):** `ConnectionLostException`, `ServerErrorException` y `ServerUnreachableException` están en
  `Accounts`.
  - Son fallas de red de todos los clientes: aparecen en 16 a 19 archivos.
  - Las crea `Channels/ServiceFailureTranslator`.
  - La 6.4 pide que el espacio de nombres refleje la responsabilidad del archivo.
- **Pregunta 2 (pasada 2):** `AccountClient.LogIn` repite en sus `catch` la traducción general de
  `ServiceFailureTranslator` (`EndpointNotFoundException` → `ServerUnreachable`, `FaultException` → `ServerError`,
  comunicación y tiempo → `ConnectionLost`).
  - Los otros seis clientes usan un `Call` privado que atrapa `CommunicationException` y `TimeoutException`, y un
    `ToClientException` con sus fallas propias, que al final llama a `ServiceFailureTranslator`.
  - La única diferencia sería una `FaultException<InvalidSessionFault>`, que `LogIn` no puede recibir.
- **Pregunta 3 (10.1.1 y 10.2.1):** los siete clientes de petición y respuesta crean su `ServiceChannel<T>` con `new`
  en un campo. `ServiceChannel` hace E/S de red, así que es un servicio externo (10.1.1), y se construye fuera de la
  raíz de composición. Es el "código incorrecto" de la regla.
  - Ninguna excepción lo cubre: la de `Adapters` permite recibir el tipo del framework, no crearlo.
  - Hoy ningún cliente se puede probar con un canal falso.

**Preguntas (301 a 310):**
1. Las tres fallas de red generales (recomendado: A, pasarlas a `Channels` junto a `ServiceFailureTranslator`, con
   `git mv`, su espacio de nombres y los `using`; B, una carpeta nueva solo para ellas; C, dejarlas).
2. `AccountClient` con `Call` y `ToClientException`, como los otros clientes (recomendado: sí).
3. Canales recibidos por constructor. Recomendado: A.
   - **A:** un `IServiceChannel<TContract>` con las dos `Call`, que implementa `ServiceChannel<TContract>`.
     - Cada cliente lo recibe por constructor y deja de ser `IDisposable`.
     - `ServerConnection` crea los siete canales, se los pasa a los clientes y los libera (9.5.1: el dueño libera).
     - Va en un commit aparte que toca los siete clientes, `ServerConnection` y la interfaz nueva.
     - Se prueba con una sonda de canal falso.
     - `NotificationClient` tiene otra forma (dúplex, con estado de sesión) y se pregunta en su carpeta.
   - **B:** dejarlo así.

**Respuesta del usuario (2026-11-11):** «Sí, A en todas».

**Commit 1, `e83e6d3` (`Accounts`):**
- **R-10:** `SignedInSession` → `LoggedInSession`, con `git mv`, en 19 archivos. Incluye el campo `_loggedInSession` de
  `ScreenNavigator` y tres pruebas.
- **R-41:** "The account cannot log in. Restriction=…".
- **R-14:** `ToLoggedInSession` guarda `token`, `nickname` y `preferredLanguage` en variables.
- **Pregunta 1:** `ConnectionLostException`, `ServerErrorException` y `ServerUnreachableException` pasan a `Channels`,
  con `git mv` y su espacio de nombres.
  - 17 archivos reciben `using Bastion.Client.Networking.Channels;` en orden, y seis pierden el `using …Accounts;` que
    ya no usan.
  - Un script en `scratchpad/tools/move_network_exceptions.py` lo hizo solo donde se usan los tipos.
- **Pregunta 2:** `AccountClient` tiene `Call`, `ToClientException` (sus dos fallas y luego `ServiceFailureTranslator`),
  `ToRestriction` y `ToLoggedInSession`, en el orden de la cadena (R-47).
- **Sonda `client-probes/account-mapping`:** compara la traducción de `HEAD` con la nueva en 11 casos.
  - Son iguales 10: el tipo, el mensaje, la excepción interna, la restricción y los minutos.
  - La única diferencia es la esperada: una `FaultException<InvalidSessionFault>`, que `LogIn` no puede recibir, ahora
    da `InvalidSessionException` en lugar de `ServerErrorException`.

**Commit 2, `c54aba2` (pregunta 3):**
- `Channels/IServiceChannel<TContract>` tiene las dos `Call`, y `ServiceChannel<TContract>` la implementa.
- Los siete clientes reciben `IServiceChannel<…>` por constructor (después, el `INotificationClient` donde lo había),
  y dejan de ser `IDisposable`. Pierden el `using Bastion.Contracts;`, que solo servía para `ServiceEndpoints`.
- `ServerConnection` crea los siete canales en campos y se los pasa a los clientes desde sus propiedades.
  - Libera primero `NotificationClient` y luego los canales, en el mismo orden de antes.
  - Ya no guarda campos de los clientes.
- **Sonda `client-probes/channel-injection`:** los siete clientes con un canal falso.
  - Con éxito, cada uno devuelve el valor traducido.
  - El endpoint caído, la sesión inválida, la falla del servidor y el tiempo agotado dan `ServerUnreachable`,
    `InvalidSession`, `ServerError` y `ConnectionLost`, con la excepción original adentro.
  - El canal falso recibió las 35 llamadas.
  - `ServerConnection` real se crea y se libera sin errores.

**Verificación de los dos commits:**
- `Client` compila sin avisos de código en una compilación completa (solo NU1902/NU1903);
- pasan 514 pruebas.

### 311 a 317. `Channels` (2026-11-11)

Los archivos son `ChannelCloser`, `ChannelSettings`, `DeviceIdentity`, `ServerAddress`, `ServiceChannel`,
`ServiceFailureTranslator` y `ThumbprintCertificateValidator`. `IServiceChannel` y las tres excepciones movidas ya se
vieron en 301–310.
- **Cumple:**
  - **9.5.2:** `ChannelCloser` aborta si el canal no está abierto, cierra con `Close` y aborta si falla.
    `ServiceChannel` cierra cada canal al terminar y lo aborta ante una falla de comunicación o de tiempo, con `throw;`.
  - **4.3.2:** `ServiceFailureTranslator` tiene un `default` que lanza `ArgumentOutOfRangeException`. Los casos van del
    tipo más derivado al menos derivado.
  - **9.3.2 y 1.3.1:** `ThumbprintCertificateValidator` lanza `SecurityTokenValidationException` (predefinida) y rechaza
    todo si no hay huella configurada.
  - **10.1.1:** `DeviceIdentity` y `ServerAddress` son estáticas y leen el equipo y las variables de entorno. Su resultado
    es fijo en cada máquina, y desde `c54aba2` se usan al crear los canales en la raíz de composición.
  - 2.3.2, 2.10.1 (cada texto y cada número están en constantes), 9.4.1 y 11.1.1/11.3.1 (`ChannelCloser` registra en
    Warn con `Channel=`).
- **Aplicado sin preguntas (reglas decididas):**
  - **R-14:** `ChannelSettings.CreateAddress` guarda `address` e `identity` antes del `return new EndpointAddress(…)`.
  - **R-04 y R-02:** `DeviceIdentity.GetFingerprint` ya no anida tres llamadas en el `return`. Ahora usa
    `byte[] encodedSource`, luego `byte[] hash` y al final `return Convert.ToHexString(hash)`.
  - **R-28:** `ServerAddress.GetCertificateThumbprint` guarda la variable de entorno en `thumbprint` y devuelve
    `thumbprint?.Trim() ?? string.Empty`.
  - **R-04:** `GetHost` y `GetPort` devolvían un `?:`. Pasan a una guarda con `return` anticipado, como `FindRoomOf`
    (169) y `GetPartnerId` (12).
- **Sonda `client-probes/server-address`:** compara antes y después, y da el mismo resultado:
  - 10 valores del puerto, 4 del host y 3 de la huella;
  - la huella del equipo (64 caracteres) y la versión;
  - la dirección completa de `ChannelSettings`.
- **Pregunta 1 (falla encontrada por la sonda):** `GetPort` solo rechaza los puertos menores o iguales a 0.
  - Con `BASTION_SERVER_PORT=65536` o `70000`, `UriBuilder` lanza `ArgumentOutOfRangeException` cuando
    `ServerConnection` crea los canales. Como `BastionGame` crea `ServerConnection` en un campo, el cliente se cae al
    arrancar en lugar de usar el puerto por defecto.
  - El servidor ya valida el rango con `IPEndPoint.MinPort` e `IPEndPoint.MaxPort` (R-52, 230).
  - Además, la variable `text` se lee mejor como `portText`.
- **Pregunta 2 (2.14.3):** `ThumbprintCertificateValidator` hereda de `X509CertificateValidator`, pero no termina con el
  nombre completo de esa clase. La regla solo exceptúa las bases cuyo nombre no agrega información (`Game`, `Panel`) y
  los controles. Solo la usa `ChannelSettings`.

**Preguntas (311 a 317):**
1. Rango del puerto (recomendado: A, `IPEndPoint.MinPort < port && port <= IPEndPoint.MaxPort`, con `portText`, y si no
   cae en el rango se usa `DefaultPort`; B, dejarlo).
2. `ThumbprintCertificateValidator` → `ThumbprintX509CertificateValidator` (recomendado: A, por la letra de la regla;
   B, dejarlo, porque "CertificateValidator" ya muestra la relación con la base).

**Respuesta del usuario (2026-11-11):** «Sí, A en las dos». En los puertos pidió además rechazar los reservados, que no se
deben usar bajo ningún motivo.
- Se le preguntó qué rangos cuentan como reservados. IANA (RFC 6335) define tres: del sistema (0–1023), registrados
  (1024–49151) y dinámicos (49152–65535). Windows y Linux usan los dinámicos como puertos efímeros de salida.
- **Eligió solo 1024–49151, en el cliente y en el servidor.** Queda como regla R-58.

**Aplicado:**
- **`ServiceEndpoints`** (`Contracts`): `FirstRegisteredPort = 1024`, `LastRegisteredPort = 49151` (los dos límites de
  la pareja quedan públicos, R-25) y `IsRegisteredPort(int port)`. Es una sola definición (4.4.2).
- **`ServerAddress.GetPort`:** `portText`, `bool isNumber = int.TryParse(…)`, y
  `if (!isNumber || !ServiceEndpoints.IsRegisteredPort(port))` devuelve `DefaultPort`.
- **`Program.GetNetTcpPort`** (servidor):
  - usa `ServiceEndpoints.IsRegisteredPort`, en lugar de `IPEndPoint.MinPort/MaxPort` (sale `using System.Net`);
  - el mensaje es "The net.tcp port is missing or is not a registered port. Key=…; Port=…; FirstPort=1024;
    LastPort=49151".
  - Cambia la R-52 de 230 en este punto.
- **Pregunta 2:** `ThumbprintX509CertificateValidator`, con `git mv` y su uso en `ChannelSettings`.

**Verificación:**
- **Compilación:** `Host` y `Client` compilan sin avisos de código en una compilación completa (solo NU1902/NU1903).
- **Pruebas:** pasan 514.
- **Sonda `server-address`:** con 15 valores del puerto, solo 1024, 8000 y 49151 quedan en la dirección. Los demás usan
  8000: sin valor, vacío, texto, 0, −5, 80, 1023, 49152, 65535, 65536, 70000 y " 8100". Antes, 65536 y 70000 hacían caer
  al cliente.
- **Servidor:** el ejecutable de `host-build` con `--Server:NetTcpPort=` 80, 1023, 49152 y 70000 se detiene con el mensaje
  nuevo, antes del certificado y de la base. No se probó con un puerto válido, porque eso arranca el servidor real.

**Commit de `Channels`:** `5382eac` (2026-11-11), en `review-standard-v2.4-host`, sin push.

**Justificación de la R-58 (2026-11-11, a pedido del usuario):** el usuario preguntó si la validación hace falta, si hay
un ataque que la exija y qué técnica la respalda.
- **Seguridad:**
  - Ningún ataque realista usa el puerto para entrar. Quien puede cambiarlo controla la máquina del servidor o el
    entorno del jugador, y un servidor falso usaría un puerto válido.
  - Contra la suplantación protegen TLS (`SecurityMode.Transport`) y la huella del certificado, no el puerto.
  - La materia pide "prácticas seguras de escritura de código" y "seguridad en la BD", no proteger el puerto.
  - La validación es robustez de la configuración, no seguridad.
- **Técnica: fallar pronto.** Shore (2004), IEEE Software 21(5), pp. 21–25, leído del PDF:
  - el ejemplo de la propiedad de configuración mal escrita, en pp. 21–22, "Immediate and visible failure";
  - con usuarios finales, un manejador global en lugar de una caída, en pp. 24–25, "Robust failure".
- **Práctica de .NET:** Microsoft Learn, *Options pattern*, sección "Options validation".
  - Muestra `[Range]` y `ValidateOnStart`, y su ejemplo `ServerOptions` limita `Port` con `[Range(1, 65535)]`.
  - En Bastión el puerto se necesita antes de `Build()`, así que la revisión explícita en `GetNetTcpPort` cumple esa
    función.
- **El rango:**
  - RFC 6335, sección 6: los tres rangos. Sección 8.1.2: un puerto dinámico "MUST NOT be used as a service identifier",
    y no hay que suponer que esté libre.
  - Microsoft (artículo del rango dinámico y artículo del agotamiento de puertos): Windows usa 49152–65535 para las
    conexiones de salida.
  - Excluir 0–1023 es decisión del proyecto: el RFC los asigna a servicios conocidos, pero no lo prohíbe.
- **Corregido:** el permiso de administrador en Linux y los bloques reservados por Hyper-V/WSL no salen en estas fuentes,
  así que no se usan como argumento.
- **Decisión del usuario:** «Sí, mantenla». La R-58 se queda como está.
- **Pendiente para la revisión de `Client`:** hoy el cliente vuelve al 8000 sin avisar, que es el "valor por defecto" que
  Shore desaconseja. Se propondrá que registre el problema y le diga al jugador qué variable está mal.

### 318 a 327. `Chat` (2026-11-11)

Los archivos son:
- `ChatAuthor`, `ChatMessage`, `ChatMute` y `LobbyChatTranscript`;
- `ChatClient`, `IChatClient` y `ChatContractTranslator`;
- `ChatChannelForbiddenException`, `ChatMessageRejectedException` y `ChatRejection`.

Revisión:
- **Cumple:**
  - 2.x, 4.3.2 (`ToRejection`, con 6 casos y `default`), 9.6.1 (las dos excepciones) y 9.4.1 en los públicos;
  - R-47 en el traductor;
  - **2.11.4:** los `add =>` y `remove =>` del evento de `ChatClient` son accesores que solo reenvían. La sección
    "Alcance" de la regla los excluye de forma expresa.
  - **Pasada 3:** `ChatMute.EndsAt` repite el nombre del `ChatMute` de `Application`.
- **Aplicado sin preguntas (reglas decididas):**
  - **R-11:** `ChatAuthor`, `ChatMessage` y `LobbyChatTranscript` pasan a constructor explícito con `ThrowIfNull` y
    propiedades `{ get; }`. Ninguno se copia con `with`, ni se deconstruye ni se crea con argumentos con nombre.
    `ChatMute (bool, DateTime?)` se queda posicional por la R-16.
  - **R-14 y 5.3.1** en `ChatContractTranslator.ToTranscript`:
    - antes: `messages.Select(ToChatMessage).ToList()` y un `new ChatMute(…)` dentro del `return`;
    - ahora: `IEnumerable<ChatMessage> chatMessages`, luego `var messageList = new List<ChatMessage>(chatMessages)`,
      luego `var mute`, y al final `return new LobbyChatTranscript(messageList, …, mute)`.
  - **R-14:** el `??` del texto va en su variable en `ToChatMessage(LobbyChatMessage)` y en `ToReceivedMessage`.
  - **R-14:** en `ChatClient.ToClientException`, `ChatRejection rejection` va antes del `new ChatMessageRejectedException`.
  - **R-47:** en `ChatClient`, `Call` va antes de `ToClientException`, en el orden de la cadena, como en `AccountClient`.
- **Verificación:**
  - `Client` compila sin avisos de código en una compilación completa;
  - pasan las 136 pruebas del cliente, 12 de ellas sobre `ChatContractTranslator`.

**Commit de `Chat`:** `542c757` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 328 a 341. `Friends` (2026-11-11)

Los archivos son:
- seis registros: `FoundPlayer`, `FriendListing`, `FriendRequestListing`, `ListedFriend`, `PendingFriendRequest` y
  `PlayerTag`;
- cuatro enumeraciones: `FriendPresence`, `FriendRelationship`, `FriendRequestOutcome` y `FriendshipRejection`;
- `FriendshipRejectedException`, `IFriendClient`, `FriendClient` y `FriendContractTranslator`.

Revisión:
- **Cumple:**
  - 2.x y 2.15.1;
  - 4.3.2: los cuatro `switch` tienen `default`, y `ToRejection` tiene 8 casos, con complejidad 9;
  - 9.6.1 y 9.4.1;
  - pasada 4: cada valor se usa.
  - `FriendRelationship.None` no es una enumeración de indicadores. La 2.15.2 solo exige `None` en esas, y no lo prohíbe
    en las demás; dentro de `FriendRelationship` se lee como "sin relación".
- **Aplicado sin preguntas (reglas decididas, sin commit):**
  - **R-11:** los seis registros pasan a constructor explícito con `ThrowIfNull` y propiedades `{ get; }`.
    - Ninguno usa `with`, deconstrucción ni argumentos con nombre.
    - El de `FriendRequestListing` va con un parámetro por línea.
    - Se generaron con `scratchpad/tools/explicit_records.py` (sesión `0da7ac4a`).
  - **R-14 y 5.3.1 en `FriendContractTranslator`:**
    - `ToFriendListing`, `ToFoundPlayers` y `ToPendingRequests` guardan la consulta en un `IEnumerable<T>` con nombre y
      la materializan con `new List<T>(…)`;
    - `ToFriendRequestListing` guarda `receivedRequests` y `sentRequests` en variables;
    - `ToListedFriend` (las dos) y `ToFoundPlayer` guardan `presence` y `relationship` antes del `return new`;
    - `ToPlayerTag` guarda sus dos textos en variables.
  - **R-47 en el traductor:** los privados van por cadenas:
    - `ToListedFriend` y luego `ToPresence`;
    - `ToFoundPlayer` y luego `ToRelationship`;
    - `ToPendingRequests` y luego `ToPendingRequest`.
  - **5.1.1 y R-45 en `FriendClient`:** `Call(Action)` tenía una lambda de cuatro líneas. Ahora es
    `Func<IFriendshipService, bool> operationAsFunction = service => CompleteOperation(operation, service);`, con un
    privado `CompleteOperation`, como en los servicios del servidor.
  - **R-14:** en `ToClientException`, `FriendshipRejection rejection` va antes del `new`.
  - **R-47 en `FriendClient`:** `Call<TResult>`, luego `ToClientException`, luego `Call(Action)` y luego
    `CompleteOperation`.
  - **`ConversationClient` tiene la misma lambda de varias líneas.** Se corrige en `PrivateChat`.
- **Verificación:**
  - `Client` compila sin avisos de código;
  - pasan las 136 pruebas del cliente;
  - la sonda `channel-injection` pasó `FriendClient.AcceptFriendRequest`, que usa `Call(Action)`, y `SearchPlayers`
    por el canal falso: con éxito y con las cuatro fallas, cada una con la excepción original adentro.
- **Pregunta 1 (4.4.1):** el traductor repite seis veces
  `new PlayerTag(nombre ?? string.Empty, código ?? string.Empty)`, una por cada tipo de contrato que trae un jugador.

**Pregunta (328 a 341):**
1. Un privado `ToPlayerTag(string? nickname, string? friendCode)` para las seis (recomendado: A). Lo usan casi todos, así
   que va al final, como `GetUtcNow` (R-47). El público `ToPlayerTag(FriendshipStartedNotification)` lo llamaría.
   B: dejarlo.

**Respuesta del usuario (2026-11-11):** «Sí, sácalo».
- **Aplicado:**
  - el privado `ToPlayerTag(string? nickname, string? friendCode)` va al final, con `tagNickname` y `tagFriendCode`
    antes del `return new`;
  - los seis lugares lo llaman con `PlayerTag x = ToPlayerTag(…)`, con tipo explícito por la R-51 (llamada sin
    calificar dentro de la clase);
  - el público `ToPlayerTag(FriendshipStartedNotification)` devuelve la llamada.
- **Verificación:**
  - `Client` compila sin avisos de código;
  - pasan 514 pruebas, 8 de ellas sobre `FriendContractTranslator`.

**Commit de `Friends`:** `bae09c1` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 342 a 344. `Matches` (2026-11-11)

Los archivos son `IMatchClient`, `MatchClient` y `MatchNotJoinedException`. Cumplen y no cambian.
- **`MatchClient`:**
  - tiene una sola operación, `AbandonMatch`, con su `try`, sus dos `catch` y `ToClientException`, que termina en
    `ServiceFailureTranslator`. No repite la traducción general (la pregunta 2 de 301–310 no aplica);
  - la lambda es de una línea y usa `IServiceChannel.Call(Action)`;
  - los accesores del evento cumplen por el "Alcance" de la 2.11.4.
- **`MatchNotJoinedException`:** cumple la 9.6.1, porque no lleva datos y tiene los tres constructores estándar.
- **`IMatchClient`:** cumple; no lleva documentación (R5).
- No hay commit.

### 345 a 349. `Matchmaking` (2026-11-11)

Los archivos son `IMatchmakingClient`, `MatchmakingClient`, `SearchEndReason`, `SearchRejectedException` y
`SearchRejection`.
- **Cumple:**
  - las dos enumeraciones y `SearchRejectedException` (9.6.1, con datos);
  - `ToRejection`, con 3 casos y `default`;
  - los accesores de los cuatro eventos (2.11.4, "Alcance");
  - `Call(Action)` con sus dos `catch`, sin lambda de varias líneas;
  - pasada 4: `SearchEndReason` lo usa `SearchEndedEventArgs`.
- **Aplicado sin preguntas:**
  - **R-14:** `SearchRejection rejection = ToRejection(…)` va antes del `new SearchRejectedException`.
  - **R-47:** el orden es `Call`, luego `ToClientException`, luego `ToRejection`.
- **Verificación:**
  - `Client` compila sin avisos de código;
  - pasan las 136 pruebas del cliente;
  - la sonda `channel-injection` pasó `StartSearch` por el canal falso, con éxito y con las cuatro fallas.

**Commit de `Matchmaking`:** `19ac951` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 350 a 366. `Notifications` (2026-11-11)

Son 17 archivos: 13 `…EventArgs`, `FoundMatchFormat`, `FoundMatchParticipant`, `INotificationClient`,
`NotificationCallback` y `NotificationClient`.
- **Cumple:**
  - **Los `…EventArgs`:** 2.14.1, sellados, con constructor que comprueba sus referencias y propiedades `{ get; }`.
  - **Los dos registros:** `FoundMatchFormat (byte ×3)` se queda posicional por la R-16, y `FoundMatchParticipant` ya
    tiene constructor explícito.
  - **`NotificationClient`:** cumple en lo demás:
    - 5.1.2: se suscribe a `Faulted` con un grupo de método y se desuscribe en `Disconnect`;
    - 10.4.1: el `TimeProvider` se inyecta y crea el temporizador;
    - el temporizador atrapa la comunicación, el tiempo y `ObjectDisposedException`;
    - 11.1.1 en Warn;
    - R-47: los privados forman cadenas que usa `Connect`.
- **Aplicado sin preguntas (reglas decididas, sin commit):**
  - **R-48 en `NotificationCallback`:** había ocho sobrecargas `ToEventArgs`, cada una con un tipo de salida distinto.
    Ahora cada método dice qué arma: `ToChatMessageReceivedEventArgs`, `ToMatchChatMessageReceivedEventArgs`,
    `ToMatchAbandonedEventArgs`, `ToMatchFoundEventArgs`, `ToPresenceRequestedEventArgs`, `ToSearchEndedEventArgs`,
    `ToPrivateMessageReceivedEventArgs` y `ToFriendPresenceChangedEventArgs`.
  - **R-14:** cada `To…EventArgs` y `ToFoundMatchParticipant` guarda en variables las llamadas, los `??` y la resta
    `Deadline - OccurredAt` antes del `return new`. El tipo es explícito o `var` según la R-51.
  - **5.3.1:** los participantes pasan de `.Select(…).ToArray()` a un `IEnumerable<FoundMatchParticipant>` con
    nombre, materializado con `new List<…>(…)`.
  - **R-47:** los privados van por la cadena de cada `TryDispatch…`: el despachador, luego su `To…EventArgs`, luego
    su `On…`. `ToReason` va debajo de `ToSearchEndedEventArgs`.
  - **R-23 en `NotificationClient`:** `((ICommunicationObject)channel).Faulted += …` y `((ICommunicationObject)channel).Abort()`
    pasan a `var communicationObject = (ICommunicationObject)channel;` y luego la línea que lo usa.
- **Sonda `client-probes/notification-callback`** (sesión `0da7ac4a`): compara el `NotificationCallback` de `HEAD` con
  el nuevo.
  - Son 21 notificaciones, con campos vacíos, un `SearchEndedReason` desconocido, una sala nula y una notificación nula.
  - Las 21 dan el mismo evento con los mismos datos, o la misma excepción.
  - Pasan `TestNotificationCallback` y `TestRoomNotifications`.
- **Pregunta 1 (10.1.1, pendiente desde 301–310):** `NotificationClient` crea con `new` su
  `DuplexChannelFactory<ISessionService>` (E/S de red) y el `NotificationCallback`.
- **Pregunta 2 (9.4.1 y R-50):** `ReceiveNotification(Notification notification)` es un método público sin
  `ThrowIfNull`.
  - Es una operación de un solo sentido de WCF que atiende el cliente. Hoy una notificación nula, o de un tipo que
    ningún despachador conoce, se ignora sin dejar rastro.
  - Un `ThrowIfNull` lanzaría dentro del despacho de WCF y podría dañar el canal dúplex.
  - La R-50 resolvió el caso de los servidores de un solo sentido con una guarda que registra en Warn.
- **Pregunta 3 (pasada 2):** nueve ramas despachan con `OnX(ToXEventArgs(y))`. Cuatro arman el argumento dentro de la
  rama: la solicitud de amistad, la amistad nueva, la sala actualizada y la sala cerrada; esta última con `??` en el
  argumento.

**Preguntas (350 a 366):**
1. El canal dúplex por constructor. Recomendado: A.
   - **A:**
     - `Channels/ISessionChannelFactory` (`ISessionService CreateChannel()`);
     - `Channels/SessionChannelFactory : ISessionChannelFactory, IDisposable`, que envuelve el `DuplexChannelFactory`
       con `ChannelSettings` y se libera con `ChannelCloser`;
     - `ServerConnection` crea el `NotificationCallback`, la fábrica y
       `NotificationClient(callback, sessionChannelFactory, timeProvider)`, y libera la fábrica después del cliente.
     - `NotificationClient` sigue siendo `IDisposable` por su canal y su temporizador.
   - **B:** dejarlo.
2. La notificación nula. Recomendado: A.
   - **A:** la forma de la R-50: un `ILog`, `if (notification is null)` con Warn y `return`, y Warn cuando ningún
     despachador conoce el tipo.
   - **B:** `ThrowIfNull`, por la letra de la 9.4.1, con el riesgo de dañar el canal.
   - **C:** dejarlo.
3. Las cuatro ramas por su `To…EventArgs`. Recomendado: A.
   - **A:** `ToFriendRequestReceivedEventArgs`, `ToFriendshipStartedEventArgs`, `ToRoomUpdatedEventArgs` y
     `ToRoomClosedEventArgs`, para que cada rama se lea igual.
   - **B:** dejarlo.

**Respuesta del usuario (2026-11-11):** «Sí, A en todas».

**Aplicado:**
- **Pregunta 1:**
  - `Channels/ISessionChannelFactory` (`ISessionService CreateChannel()`);
  - `Channels/SessionChannelFactory : ISessionChannelFactory, IDisposable`, que recibe el `INotificationCallback`, arma
    el `DuplexChannelFactory` con `ChannelSettings` y se libera con `ChannelCloser`;
  - `NotificationClient(NotificationCallback, ISessionChannelFactory, TimeProvider)`, con un parámetro por línea.
    `Dispose` solo desconecta, porque la fábrica ya no es suya. Sale `using Bastion.Contracts;`.
  - `ServerConnection` crea `var notificationCallback = new NotificationCallback();`, la fábrica y el cliente. Libera el
    cliente, luego la fábrica y luego los siete canales: el mismo orden de antes.
  - `NotificationCallback` sigue siendo concreto: no es un servicio externo, solo lanza eventos.
- **Pregunta 2:**
  - `NotificationCallback` tiene su `ILog`, y `ReceiveNotification(Notification? notification)` sale con Warn si llega
    nula. El parámetro también es anulable en `INotificationCallback`, como en `LogIn` (9.4.1).
  - Una sala actualizada sin sala registra Warn. Antes caía hasta el final sin rastro.
  - `DispatchMatchmakingNotification` pasa a `TryDispatchMatchmakingNotification`, que devuelve `bool` y entra en la
    cadena de `||`. Si nadie conoce el tipo, se registra "A notification of an unknown type was ignored. Type=…".
- **Pregunta 3:** `ToFriendRequestReceivedEventArgs`, `ToFriendshipStartedEventArgs`, `ToRoomUpdatedEventArgs(RoomState)`
  y `ToRoomClosedEventArgs`, cada uno junto a su `On…` (R-47). Cada rama queda como `OnX(ToXEventArgs(y))`.

**Verificación:**
- `Host` y `Client` compilan sin avisos de código en una compilación completa, CA1502 incluida. Pasan 514 pruebas.
- **Sonda `notification-callback`:** con 22 notificaciones, contando un tipo desconocido, los eventos y sus datos son
  iguales a los de `HEAD`. Solo se agregan los tres Warn nuevos: la nula, la sala sin sala y el tipo desconocido.
- **Sonda `notification-client`,** con una fábrica y un temporizador falsos:
  - al conectar, `Subscribe(token)`, el manejador de `Faulted` y un temporizador de 60 s;
  - el tick envía `KeepAlive`;
  - una falla del canal detiene el temporizador y avisa `Disconnected` una sola vez;
  - al desconectar quita el manejador y cierra el canal;
  - si `Subscribe` falla, aborta el canal y lanza `ConnectionLostException` o `ServerUnreachableException`;
  - si `KeepAlive` agota el tiempo, avisa `Disconnected`;
  - `Dispose` desconecta;
  - el `ServerConnection` real se crea y se libera sin errores.

**Commit de `Notifications`:** `fb4c3ec` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 367 a 373. `PrivateChat` (2026-11-11)

Los archivos son:
- `ConversationClient`, `IConversationClient` y `ConversationContractTranslator`;
- los registros `ConversationContact`, `ConversationPreview`, `ConversationTranscript` y `PrivateMessage`.

Revisión:
- **Cumple:**
  - 2.x y 9.4.1 en los públicos;
  - el `?:` de `lastMessage` en `ToPreview`: elige entre dos valores sin efectos secundarios (4.5.1) y no es un `return`.
- **Aplicado sin preguntas (reglas decididas, sin commit):**
  - **R-11:** los cuatro registros pasan a constructor explícito con `ThrowIfNull`.
    - `PrivateMessage` se copia con `with { SentAt = … }` en `PrivateConversationViewModel`, así que solo `SentAt` lleva
      `{ get; init; }`, como `WallsPerPlayer` en `MatchFormat`.
  - **R-14 y 5.3.1 en el traductor:**
    - `ToPreviews` y `ToTranscript` guardan la consulta en un `IEnumerable<T>` con nombre y la materializan con
      `new List<T>(…)`;
    - `ToTranscript` guarda el `ChatMute` en una variable;
    - `ToSender` y los dos `ToPrivateMessage` guardan los `??` en variables antes del `return new`.
  - **5.1.1 y R-45 en `ConversationClient`:** `MarkConversationRead` tenía una lambda de cuatro líneas que devolvía
    `true`.
    - Ahora es `Call(service => service.MarkConversationRead(…))`, con un `Call(Action)` y un `CompleteOperation`, como
      en `FriendClient`.
    - **R-14:** `ChatRejection rejection` va en su variable.
    - **R-47:** el orden es `Call<TResult>`, luego `ToClientException`, luego `Call(Action)` y luego `CompleteOperation`.
- **Verificación:**
  - `Client` compila sin avisos de código;
  - pasan las 136 pruebas del cliente;
  - la sonda `channel-injection` pasó `ListConversations` y `MarkConversationRead` (`Call(Action)`) por el canal falso,
    con éxito y con las cuatro fallas.
- **Nota para `Client`:** `PrivateConversationViewModel` crea el mensaje con `DateTime.UtcNow`, y la 10.4.1 pide usar el
  `TimeProvider` inyectado.
- **Pregunta 1 (4.4.1, repetición entre clases):**
  - el traductor arma `new PlayerTag(nombre ?? string.Empty, código ?? string.Empty)` tres veces más (el compañero de
    `ToTranscript`, `ToSender` y el compañero de `ToPreview`). Es lo mismo que el privado `ToPlayerTag` que se acaba de
    crear en `FriendContractTranslator` (328–341).
  - `ConversationClient.ToClientException` y `ChatClient.ToClientException` repiten las mismas tres líneas que convierten
    `FaultException<ChatMessageRejectedFault>` en `ChatMessageRejectedException`.

**Pregunta (367 a 373):**
1. Compartir esas dos piezas entre las clases. Recomendado: A.
   - **A:**
     - `FriendContractTranslator.ToPlayerTag(string? nickname, string? friendCode)` pasa a público, y
       `ConversationContractTranslator` lo usa en sus tres lugares;
     - un `ChatContractTranslator.ToMessageRejectedException(FaultException<ChatMessageRejectedFault> fault)` público
       que usan `ChatClient` y `ConversationClient`.
   - **B:** solo el `ToPlayerTag`.
   - **C:** dejarlo.

**Respuesta del usuario (2026-11-11):** «Sí, las dos».
- **Aplicado:**
  - `FriendContractTranslator.ToPlayerTag(string?, string?)` es público y va junto al otro `ToPlayerTag`.
  - `ConversationContractTranslator` lo usa en `ToTranscript`, `ToSender` y `ToPreview`, con
    `var partner = FriendContractTranslator.ToPlayerTag(…)` (R-51). Solo queda un `new PlayerTag(` en el cliente, dentro
    de ese método.
  - `ChatContractTranslator.ToMessageRejectedException(FaultException<ChatMessageRejectedFault> fault)` es público, con
    `ThrowIfNull` y `ChatRejection rejection` en su variable. `ChatClient` y `ConversationClient` lo devuelven desde su
    `ToClientException`.
- **Verificación:**
  - `Client` compila sin avisos de código;
  - pasan 514 pruebas;
  - la sonda `channel-injection` agregó la falla `ChatMessageRejectedFault` (`Muted`, con fecha). Los dos clientes del
    chat la dan como `ChatMessageRejectedException`, con el motivo y la fecha; los demás, como `ServerErrorException`,
    igual que antes.

**Commit de `PrivateChat`:** `4bfb855` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 374 a 383. `Rooms` (2026-11-11)

Los archivos son:
- `IRoomClient`, `RoomClient` y `RoomContractTranslator`;
- `PrivateRoom`, `PrivateRoomMember` y `PrivateRoomOptions`;
- `PrivateRoomGameMode`, `RoomCloseReason`, `RoomRejection` y `RoomRejectedException`.

Revisión:
- **Pasada 4 (dato):** la interfaz del juego todavía no usa el cliente de salas. `IRoomClient`, `PrivateRoom` y sus eventos
  solo los usan `ServerConnection` y `TestRoomNotifications`. Nadie lee `PrivateRoom.SeatCount`. Se queda, porque la
  pantalla de salas (CU-10, CU-11, Must) está por hacerse y el servidor ya lo implementa.
- **Cumple:**
  - `PrivateRoomOptions (enum, byte, byte)` se queda posicional por la R-16;
  - `RoomRejectedException` cumple la 9.6.1 (con datos);
  - los accesores de los eventos cumplen la 2.11.4;
  - `ToCloseReason` y los dos `switch` de modo tienen `default`.
- **Aplicado sin preguntas (reglas decididas, sin commit):**
  - **R-54:** `ToRejection` partía 14 casos en dos `switch`, con un `default` que delegaba en `ToPlacementRejection`.
    - Ahora es una tabla `_rejectionsByReason` (`IReadOnlyDictionary`) con `TryGetValue`, y
      `ArgumentOutOfRangeException` si falta el valor.
    - Sale `ToPlacementRejection`.
  - **R-48:** `ToContract(PrivateRoomOptions)` y `ToContract(PrivateRoomGameMode)` eran sobrecargas con salidas distintas.
    Pasan a `ToRoomOptions` y `ToRoomGameMode`, y `ToGameMode` pasa a `ToPrivateRoomGameMode` para que haga pareja.
    `RoomClient` usa `var contractOptions = RoomContractTranslator.ToRoomOptions(…)` (R-51, IDE0007).
  - **R-14 y 5.3.1:**
    - `ToRoomOptions` guarda el modo en una variable;
    - `ToPrivateRoom` guarda el código, las opciones y los miembros en variables;
    - los miembros pasan de `.Select(…).OrderBy(…).ToList()` en una línea a un `IEnumerable<PrivateRoomMember>` con un
      operador por línea, materializado con `new List<…>(…)`;
    - `ToMember` guarda su `??` en una variable.
  - **R-14 en `RoomClient.ToClientException`:** `RoomRejection rejection` y `var retryDelay = TimeSpan.FromSeconds(…)`.
  - **R-04:** `CallForRoom` guarda `RoomState state` antes de traducir, y `FindOwnRoom` cambia el `?:` del `return` por
    una guarda.
  - **R-45:** `Call(Action)` repetía los dos `catch` de `Call<TResult>`. Ahora los adapta con `CompleteOperation`, como
    `FriendClient`.
  - **R-47:** el orden es `CallForRoom`, `Call<TResult>`, `ToClientException`, `Call(Action)` y `CompleteOperation`.
    En el traductor: `ToRoomGameMode`, `ToPrivateRoomGameMode` y `ToMember`.
- **Verificación:**
  - `Client` compila sin avisos de código;
  - pasan las 136 pruebas del cliente.
  - **Sonda `client-probes/room-client`** (sesión `0da7ac4a`):
    - el traductor de `HEAD` frente al nuevo da 23 resultados iguales: los 14 rechazos y uno desconocido, los 3 modos y
      uno inválido, la sala completa, desordenada y con un apodo vacío, la vacía y la de modo inválido, y `HostLeft`;
    - `RoomClient` con un canal falso cuyo `Call(Action)` falla si se usa: `CreateRoom`, `FindOwnRoom` (con sala y sin
      sala) y `StartMatch` funcionan;
    - el rechazo da `TooManyAttempts` con 30 s de espera, y el endpoint caído y el tiempo agotado se traducen.
- **Pregunta 1 (pendiente de 291–297):** el cliente dice "options" (`PrivateRoomOptions`, `ChangeOptions`), pero su
  enumeración sigue con `RoomRejection.InvalidSettings`. Solo lo usa la tabla del traductor.
- **Pregunta 2 (2.2.2 y R-09):** `PrivateRoom (string, PrivateRoomOptions, int, IReadOnlyList<PrivateRoomMember>)` y
  `PrivateRoomMember (string, int, bool, bool)` son registros posicionales de cuatro parámetros. Solo los crea el
  traductor.
  - La R-09 permite agrupar los campos en otro registro o pasar a propiedades `init` con inicializador de objeto.
  - En el servidor, `RoomMemberSnapshot` usa propiedades `required … { get; init; }`.

**Preguntas (374 a 383):**
1. `RoomRejection.InvalidSettings` → `InvalidOptions` en el cliente, con su entrada en la tabla (recomendado: A; B,
   dejarlo).
2. Los dos registros de cuatro campos. Recomendado: A.
   - **A:** propiedades `required … { get; init; }` e inicializador de objeto en el traductor, como `RoomMemberSnapshot`.
   - **B:** agrupar `SeatCount` y `Members` en un registro `PrivateRoomSeating`, y buscar otra forma para el miembro.
   - **C:** dejarlos.

**Respuesta del usuario (2026-11-11):** «Sí, A en las dos».
- **Aplicado:**
  - `RoomRejection.InvalidOptions` en el cliente, con su entrada en `_rejectionsByReason`;
  - `PrivateRoom` y `PrivateRoomMember` con propiedades `required … { get; init; }`, y el traductor los crea con un
    inicializador de objeto (R-14: cada asignación es una variable o una propiedad).
- **Verificación:**
  - `Client` compila sin avisos de código;
  - pasan 514 pruebas;
  - la sonda `room-client` dio las mismas 42 líneas que antes del cambio. Las únicas diferencias son las tres esperadas:
    el rechazo se llama `InvalidOptions`. La sala y sus miembros se serializan igual.

**Commit de `Rooms`:** `84e8f0d` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 384 y 385. `ServerConnection` y `Sessions/InvalidSessionException` (2026-11-11)

- **`InvalidSessionException` (385):** cumple la 9.6.1, porque no lleva datos y tiene los tres constructores estándar.
- **`ServerConnection` (384):**
  - **Cumple:** es la clase de registro de los servicios del cliente (10.2.1). Crea los canales, la fábrica dúplex y
    los ocho clientes, y libera lo suyo en el orden de antes.
  - **D-06 (aplicado sin preguntas):** los siete canales se creaban en la declaración de sus campos (desde `c54aba2`),
    y el resto, en el constructor. Ahora todo se crea en el constructor, en el mismo orden, después de comprobar el
    `TimeProvider`.
  - **Verificación:**
    - `Client` compila sin avisos de código;
    - pasan las 136 pruebas del cliente;
    - la sonda `notification-client` crea y libera el `ServerConnection` real sin errores.
- **Commit:** `031592a` (2026-11-11), sin push.

### Cierre de la capa `Bastion.Client.Networking` (2026-11-11)

- **Archivos:** los 85 están revisados (301–385).
- **Commits locales en `review-standard-v2.4-host`:** `e83e6d3`, `c54aba2`, `5382eac`, `542c757`, `bae09c1`, `19ac951`,
  `fb4c3ec`, `4bfb855`, `84e8f0d` y `031592a`. Con `Contracts` y `Host`, la rama lleva 22 commits sobre la punta del
  PR #16.
- **R-27 no aplica:** la capa no tiene interfaces `I…Service`. `NotificationCallback` hereda la documentación del
  contrato con `<inheritdoc/>`.
- **Reglas nuevas o ampliadas en la capa:**
  - R-58 (puertos registrados);
  - R-50 en el callback del cliente (guarda con Warn);
  - la forma `CompleteOperation` (R-45) en los clientes con `Call(Action)`.
- **Notas para la revisión de `Client`:**
  - los campos `_received` y `_sent` de `FriendRequestsViewModel` (2.1.2);
  - avisar al jugador cuando el puerto configurado no sirve (Shore, 2004);
  - `DateTime.UtcNow` en `PrivateConversationViewModel` (10.4.1);
  - la pantalla de salas todavía no existe;
  - R-41 en los textos;
  - la R-52 en el `Program` del cliente;
  - los valores por omisión de `NoticeBox` y `AddFriendViewModel`.
- **Sigue `Client`.**

## Capa `Bastion.Client`

Son 108 archivos con 10 260 líneas, sin contar `Strings.Designer.cs`, que se genera solo. Van del 386 al 493, por
carpeta:

| Carpeta | Archivos |
| --- | --- |
| raíz (`BastionGame`, `Program`) | 386–387 |
| `Controls` | 388–392 |
| `Localization` | 393–398 |
| `Screens` (raíz) | 399–404 |
| `Screens/Login` | 405–407 |
| `Screens/MainMenu` (raíz) | 408–414 |
| `Screens/MainMenu/Chat` | 415–434 |
| `Screens/MainMenu/Friends` | 435–457 |
| `Screens/Matches` (con `Scene`) | 458–476 |
| `Theme` | 477–493 |

Datos generales:
- **Reglas propias de la capa:** 3.7.1 (inicializador de objeto en los controles de Gum, con IDE0017), la excepción de
  enlace de datos de la 2.11.4 (MVVM), 9.7.1 (`async void` solo en manejadores, todo dentro de un `try`) y 10.4.1.
- **6.3:** solo tres archivos tienen los `using` fuera de orden: `BastionGame`, `MainMenuView` y `VersusViewModel`.
- **Nombres de manejadores:** 32 archivos usan `Handle…`; solo `BastionGame.OnClientSizeChanged` y
  `PickerSkin.OnListItemsChanged` usan `On…`, que en el proyecto es el nombre del método que lanza un evento.

### 386 y 387. `BastionGame` y `Program` (2026-11-11)

- **Cumple:**
  - **10.2.1 y 10.4.1:** `BastionGame` es la inicialización del juego, así que puede crear `ServerConnection`,
    `LanguageService` y `ScreenNavigator` y usar `TimeProvider.System`.
  - **5.1.2:** se suscribe a `ClientSizeChanged` con un grupo de método y se desuscribe en `Dispose`.
  - **2.6.3:** `_screenNavigator` y `_boardScene` son anulables y se crean en `Initialize` y `LoadContent`, cuando
    MonoGame ya tiene el dispositivo gráfico.
  - **2.10.1:** cada tamaño y cada escala están en constantes.
- **Aplicado sin preguntas (reglas decididas, sin commit):**
  - **6.3:** los `using` de `Bastion.*` van antes que los de `Gum` y `Microsoft.Xna.Framework`, como se corrigió en
    `AccountService`.
  - **D-06:** `_serverConnection` se creaba en la declaración y `_graphics` en el constructor. Ahora los dos se crean en
    el constructor.
  - **R-47:** `DrawShownMatchBoard` baja después de la cadena de `Initialize` (`OnClientSizeChanged`,
    `KeepMinimumWindowSize` y `ApplyUiScale`), porque lo usa `Draw`.
- **Verificación:** `Client` compila sin avisos de código. El juego no se ejecutó, porque es una ventana.
- **Pregunta 1 (R-52, pendiente desde 230):** el `Program` del cliente no registra la excepción que termina el proceso.
  El servidor ya lo hace con un manejador de `AppDomain.CurrentDomain.UnhandledException` en Fatal.
- **Pregunta 2 (pasada 3):** `OnClientSizeChanged` es un manejador. En el proyecto, `On…` nombra al método que lanza un
  evento (`OnPlayerDisconnected`, `OnRoomUpdated`), y los manejadores se llaman `Handle…`.

**Preguntas (386 y 387):**
1. La R-52 en el cliente (recomendado: A, un `ILog`, `AppDomain.CurrentDomain.UnhandledException += LogUnhandledException`
   justo después de `ConfigureLogging()`, y un `LogUnhandledException` que registra en Fatal "The game stopped because of
   an unhandled exception."; B, no).
2. `OnClientSizeChanged` → `HandleClientSizeChanged` (recomendado: A, y lo mismo con `PickerSkin.OnListItemsChanged`
   cuando se revise `Theme`; B, dejarlos).

**Respuesta del usuario (2026-11-11):** «Sí, A en ambas».
- **Aplicado:**
  - `Program` tiene `_logger`, se suscribe a `AppDomain.CurrentDomain.UnhandledException` justo después de
    `ConfigureLogging()` y tiene `LogUnhandledException`, con Fatal "The game stopped because of an unhandled
    exception.". Es la misma forma del servidor.
  - `HandleClientSizeChanged` en `BastionGame`. `PickerSkin.OnListItemsChanged` cambia al revisar `Theme`.
- **Verificación:**
  - `Client` compila sin avisos de código;
  - pasan las 136 pruebas del cliente.
  - No se forzó una caída del juego para ver el registro Fatal. La misma forma se comprobó en el servidor (230).

**Commit de la raíz del cliente:** `32cbc25` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 388 a 392. `Controls` (2026-11-11)

Archivos: `LanguagePicker`, `ModalLayer`, `NoticeBox`, `PasswordField` y `TextField`.

- **Cumple:**
  - **4.3.2 (nota pendiente de `Client.Networking`):** el `default` de `PickFill` y `PickAccent` devuelve
    `Palette.Card` y `Palette.Border` para `NoticeTone.None`. Entra en la excepción de presentación: son miembros con
    nombre, neutros y distintos de los otros casos. `PickAccent` es, letra por letra, el `SelectBorderColor` del ejemplo
    correcto del estándar. Queda resuelta la mitad de la nota «valores por omisión de `NoticeBox`».
  - **2.11.4 («Alcance»):** los `get =>` y `set =>` de `HasError`, `Title` y `Message` son accesores que reenvían.
  - **5.1.2:** `LanguagePicker` se suscribe con un grupo de método.
  - **Pasada 2 (4.4.1):** `PasswordField` y `TextField` repiten las mismas líneas, pero heredan de bases distintas de
    Gum (`PasswordBox` y `TextBox`) y la lógica común ya vive en `FieldSkin`.
  - **`Dock(Gum.Wireframe.Dock.Fill)`:** el nombre completo es obligado. Dentro de una clase que hereda de `Panel`,
    `Dock` es el método heredado y tapa al tipo. Pasa lo mismo en las cuatro pantallas que lo usan.
- **Aplicado sin preguntas (reglas decididas, sin commit):**
  - **3.3.1 (también en `05-pendientes.md`):** los dos inicializadores de una línea de `NoticeBox` (`StackPanel` y
    `Label`) pasan a varias líneas. La regla pide `new` y el tipo en una línea y la llave en la siguiente. En `src`
    solo quedan inicializadores de una línea en `Client`, en 19 archivos de `Screens`; se corrigen al revisar cada
    carpeta.
  - **R-23:** `((LabelVisual)_title.Visual).Color = accent;` y `style.ApplyTo((LabelVisual)label.Visual);` guardan
    primero el cast en `titleVisual` y `labelVisual`.
- **Verificación:** `Client` compila sin avisos de código. Pasan las 514 pruebas (136 + 158 + 220). El juego no se
  abrió.
- **Pregunta 1 (2.10.1):** `ModalLayer` llama `Shapes.CreateRounded(Palette.Overlay, 0)`. El `0` es el único radio
  literal del cliente; `NoticeBox` tiene su `Radius`.
- **Pregunta 2 (10.1.1):** `GumService.Default` se lee fuera de la raíz de composición. El estándar llama servicio
  externo a lo que «guarda estado compartido entre clases» o hace entrada o salida. Hay cuatro usos:
  - `LanguagePicker`: `LocalizationService`, que guarda el idioma actual. `LanguageService` ya lo recibe por
    constructor desde `BastionGame`.
  - `ModalLayer`: `ModalRoot`, el contenedor de los diálogos.
  - `FriendCodeFooter`: `Clipboard`, que es entrada y salida con el sistema operativo.
  - `ScreenNavigator`: `Root` y `ModalRoot`.
- **Pregunta 3 (suscripción):** `LanguagePicker` nunca se desuscribe de `CurrentLanguageChanged`, y `LocalizationService`
  vive todo el juego. Hoy `ShowLogin` solo se llama una vez, al arrancar. Después de entrar al menú, el selector
  queda suscrito y retiene la pantalla de inicio. Pero ya nada cambia el idioma, así que el manejador no vuelve a
  correr. El estándar no exige desuscribirse, solo un grupo de método si hay que hacerlo (5.1.2).

**Preguntas (388 a 392):**
1. El radio `0` de `ModalLayer`:
   - recomendado, A: `private const float OverlayCornerRadius = 0;`, como `NoticeBox.Radius`;
   - B: dejar el `0`;
   - C: `Shapes.CreateFilled(Color)` en `Theme`.
2. `GumService.Default` y la 10.1.1:
   - recomendado, A: `Root` y `ModalRoot` son el árbol visual del framework y se quedan. `LocalizationService` y
     `Clipboard` son servicios y se inyectan. Para `LanguagePicker`, `ILanguageService` ganaría un evento
     `LanguageChanged`, que `LanguageService` lanza después de cambiar el idioma de Gum. El selector lo recibiría por
     constructor, y `LoginView` también, desde `ScreenNavigator`, que ya tiene `_languages`. Toca `Localization` y
     `Login` antes de su turno, y no se puede comprobar sin abrir el juego;
   - B: inyectar todo, también las raíces. `ScreenNavigator` ya tiene 3 parámetros, así que necesitaría un DTO;
   - C: dejarlo todo y anotar `GumService.Default` como el framework, igual que el `ILog`. Se aparta de la letra de la
     10.1.1.
3. La suscripción que no se cancela:
   - recomendado, A: dejarla y anotarla para cuando haya un camino de vuelta a la pantalla de inicio (pasada 4: hoy no
     existe);
   - B: cancelarla ya. Hace falta que alguien libere la vista, y `ScreenNavigator` hoy solo libera los modelos de
     vista.

**Justificación de la pregunta 2, pedida por el usuario (2026-11-11):** ¿por qué separar las raíces de los servicios?
- **La separación no es obligatoria.** Fue un criterio propio para bajar el costo, no una estrategia con nombre.
  Medida contra las fuentes, solo la mitad se sostiene.
- **Razones que se usaron:**
  - Gum se construye sobre raíces globales. Por reflexión, `FrameworkElement.ModalRoot` y `PopupRoot` son `static`.
    La documentación del paquete (`GumCommon.xml` 2026.10.1.1) las llama «global roots», y el `ListBox` del `ComboBox`
    y el `Tooltip` de Gum usan `PopupRoot`. Inyectar `ModalRoot` en `ModalLayer` no quita el global del programa.
  - La inyección sirve para poder sustituir la dependencia. Nadie sustituye el árbol visual, y las pruebas del cliente
    solo usan modelos de vista y `Networking`, nunca controles ni vistas.
  - Costo: cuatro vistas crean `ModalLayer`, y `ScreenNavigator` ya tiene 3 parámetros.
- **Criterios con que se midió:**
  - **10.1.1:** servicio externo es lo que hace entrada o salida, guarda estado compartido entre clases o no es
    determinista.
  - **Seemann (2006):** una dependencia volátil necesita preparar el entorno, está en desarrollo, no está en todas las
    máquinas o no es determinista. Las estables, como las del framework, no hace falta aislarlas.
  - **Seemann (2019):** el Ambient Context (acceso global estático a una dependencia) pasó a ser antipatrón en la
    segunda edición del libro. Estaba en la primera porque la BCL lo usa (`CultureInfo.CurrentCulture`,
    `HttpContext.Current`).
  - **Microsoft (2026), «Recommendations»:** evitar el acceso estático a los servicios.
- **Resultado por uso:**

| Uso | 10.1.1 | Seemann (2006) | Conclusión |
| --- | --- | --- | --- |
| `Clipboard` | entrada y salida | volátil (necesita el portapapeles del sistema) | se inyecta; los criterios coinciden |
| `LocalizationService` | estado compartido (el idioma actual) | estable (en memoria y determinista) | se inyecta por la 10.1.1 y por coherencia con `LanguageService` |
| `Root` y `ModalRoot` | estado compartido | volátil (necesita `GumService.Initialize` con la ventana) | por la letra, se inyectan; dejarlas es una excepción |

- **Corrección de la opción A:** dejar las raíces no lo respalda ninguna fuente. Es una excepción, de la misma
  naturaleza que la C pero más chica, y habría que escribirla como regla con su porqué.
- **Fuentes:**
  - Microsoft. (2026). *.NET dependency injection guidelines*. Microsoft Learn.
    https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection-guidelines (sección
    «Recommendations»; actualizada el 2026-03-30).
  - Seemann, M. (2006, 24 de agosto). *Volatile dependencies* [Entrada de blog archivada]. Microsoft Learn.
    https://learn.microsoft.com/en-us/archive/blogs/ploeh/volatile-dependencies (párrafos 2 a 8).
  - Seemann, M. (2019, 21 de enero). *Some thoughts on anti-patterns*. ploeh blog.
    https://blog.ploeh.dk/2019/01/21/some-thoughts-on-anti-patterns/ (sección «Ambient Context»).
  - Gum. (2026). *GumCommon* (versión 2026.10.1.1) [Documentación XML del paquete NuGet FlatRedBall.GumCommon]
    (miembros `FrameworkElement.PopupRoot`, `ModalRoot` y `AdditionalPopupRootPairs`).
- **Huecos:**
  - Las secciones 1.3.1, 1.3.2 y 5.3 de Seemann y van Deursen (2019) no se ven en la vista previa de Manning.
  - La página de 2006 no muestra el nombre del autor. Se atribuye a Seemann por el blog `ploeh`, que es el suyo.

**Propuesta sin antipatrón para la pregunta 2, pedida por el usuario (2026-11-11), sin aplicar:**
- **Idea:** solo dos lugares tocan los globales de Gum: `BastionGame`, que es la raíz de composición, y dos gateways que
  adaptan Gum. Todas las demás clases reciben interfaces del proyecto por constructor.
- **Tipos nuevos (carpeta `Platform`):**
  - `IModalHost` (`OpenModal`, `CloseModal`) e `IScreenHost : IModalHost` (`ShowScreen`);
  - `GumScreenHost`, que recibe `Root` y `ModalRoot` y es el único que toca `InteractiveGue.CurrentInputReceiver`;
  - `IClipboard` (`TryCopyText`) y `GumClipboard`, que recibe el `IGumClipboard?` de Gum;
  - `ILanguageService.LanguageChanged`, que `LanguageService` lanza después de cambiar el idioma de Gum.
- **Comprobado:** `GumService.Default.Root` y `ModalRoot` son `InteractiveGue` y `Clipboard` es `IGumClipboard`
  (`SetText`, `GetText`). Gum lanza `CurrentLanguageChanged` dentro del setter de `CurrentLanguage`, así que el evento
  nuevo corre después de que Gum retraduce, en el mismo orden que hoy (prueba `gum-roots-probe` en el scratchpad).
- **Consumidores:**
  - `LanguagePicker(ILanguageService)` y `ModalLayer(IModalHost)`;
  - `FriendsPanelViewModel(session, clients, IClipboard)` con `CopyOwnCode()`; `FriendCodeFooter` solo lo llama;
  - `LoginView(LoginViewModel, ILanguageService, IModalHost)`;
  - `MainMenuView(MainMenuScreenModels, IModalHost)` y `MatchView(MatchScreenModels, IModalHost)`;
  - `ScreenNavigator(ServerConnection, LocalServices, IScreenHost)`.
- **Límite de 3 parámetros (2.2.2):** tres records con constructor explícito (R-09, R-11), como los `SocialClients` y
  `ChatClients` que ya existen:
  - `LocalServices(ILanguageService, IClipboard, TimeProvider)`;
  - `MainMenuScreenModels`, con los 3 modelos de vista del menú;
  - `MatchScreenModels`, con los 3 de la partida.
- **Lo que sigue siendo estático, y por qué no es el antipatrón:**
  - `BastionGame` lee `GumService.Default` porque es la raíz de composición (Seemann, 2011; 10.2.1);
  - `GumScreenHost` y `GumClipboard` reciben tipos concretos de Gum porque son los gateways que lo adaptan (Fowler,
    2003). Es la misma razón de la excepción de adaptadores de la 10.1.1, aplicada al cliente por analogía;
  - los controles de Gum siguen usando `PopupRoot` por dentro, pero eso es el framework, no código del proyecto.
- **Punto débil:** `LocalServices` es un objeto de parámetros. Seemann (2010) dice que eso solo mueve los parámetros, y
  que lo mejor es un Facade Service con comportamiento propio. Cumple la 2.2.2 y sigue el precedente del proyecto.
- **Alternativa P2:** en lugar de `LocalServices`, partir `ScreenNavigator` en constructores de pantalla (Facade
  Service). Se acerca más a Seemann, pero rediseña el navegador.
- **Pregunta 3:** con `GumScreenHost` reemplazando las pantallas, puede liberar la pantalla saliente si es
  `IDisposable`. `LoginView` liberaría el selector, que se desuscribe de `LanguageChanged`. Es opcional.
- **Alcance:** unos 15 archivos de `Controls`, `Localization`, `Screens` y `BastionGame`, más
  `TestFriendsPanelViewModel` y una prueba nueva de `CopyOwnCode`. Va en un solo commit, porque los constructores
  cambian en cadena. No se compiló todavía. Los diálogos y el selector solo se pueden ver abriendo el juego.
- **Fuentes nuevas:**
  - Fowler, M. (2003). *Gateway*. En *Catalog of Patterns of Enterprise Application Architecture*.
    https://martinfowler.com/eaaCatalog/gateway.html
  - Microsoft. (2024). *Ioc* [MVVM Toolkit]. Microsoft Learn.
    https://learn.microsoft.com/en-us/dotnet/communitytoolkit/mvvm/ioc (sección «What about viewmodels?»).
  - Seemann, M. (2010, 2 de febrero). *Refactoring to aggregate services*. ploeh blog.
    https://blog.ploeh.dk/2010/02/02/RefactoringtoAggregateServices/ (párrafo «I call such a type a Facade Service»).
  - Seemann, M. (2011, 28 de julio). *Composition Root*. ploeh blog. https://blog.ploeh.dk/2011/07/28/CompositionRoot/
- **Hueco:** la página de Fowler sobre *Introduce Parameter Object* solo tiene el diagrama, sin texto. Para el objeto de
  parámetros se cita la 2.2.2 del estándar.

**Propuesta D1 para la pregunta 2, más simple, pedida por el usuario (2026-11-11), sin aplicar:**
- **Técnica:** inversión de control (Fowler, 2005) y Humble Object (Fowler, 2020), con gateways (Fowler, 2003) en la
  raíz de composición (Seemann, 2011). Las pantallas declaran sus diálogos y una sola clase los muestra en Gum.
- **Piezas:**
  - `ScreenView : Panel`, clase base de las cuatro pantallas. Su constructor hace `Dock(Fill)` y tiene
    `AddDialog(content, viewModel, isOpenProperty)` y `Dialogs`. Quita los cuatro `Create…Layer` casi iguales, sus
    cuatro campos y los cuatro `Dock(Gum.Wireframe.Dock.Fill)` (4.4.1). `Panel` está exceptuado en la 2.14.3.
  - `ModalLayer` ya no toca Gum: su `IsOpen` lanza `IsOpenChanged`.
  - `IScreenHost` y `GumScreenHost` son la única clase, aparte de `BastionGame`, que toca `Root`, `ModalRoot` y
    `CurrentInputReceiver`. `ShowScreen(ScreenView)` quita la pantalla anterior, se suscribe a los diálogos de la nueva
    con grupo de método (5.1.2), coloca los que ya estén abiertos y se desuscribe al cambiar de pantalla.
  - `IClipboard` y `GumClipboard`: `FriendsPanelViewModel` recibe el portapapeles y tiene `CopyOwnCode()`. El pie solo
    reenvía el clic, que es lo que pide el Humble Object.
  - `ScreenNavigator(ServerConnection, LocalServices, IScreenHost)`. `LocalServices` (idioma, portapapeles y reloj) es
    el único objeto de parámetros.
- **`LanguagePicker`, verificado:**
  - la documentación de Gum 2026.10.1.1 dice que `ListBoxItem.UpdateToObject` no aplica localización;
  - en `main` de Gum, `ComboBox` muestra su texto con `TextNoTranslate`, y `RefreshLocalization` solo retraduce
    elementos con clave guardada;
  - los nombres de idioma son autónimos y solo están en `Strings.resx`, así que nunca cambian.
  - **L0:** si al abrir el juego los nombres siguen bien sin el refresco, se borra la suscripción y no queda ninguna
    dependencia de Gum en el selector. La pregunta 3 desaparece.
  - **L1:** si hace falta, `ILanguageService.LanguageChanged` y `LanguagePicker(ILanguageService)`.
  - El commit `4ab3f67`, que trajo el refresco, no explica por qué. Ya usaba la misma versión de Gum.
- **Alternativas:**
  - **D2:** la P1 anterior (`IModalHost` en `ModalLayer` y en las vistas, con dos DTO de modelos de vista);
  - **D3:** el navegador lanza un evento y el host se suscribe en `BastionGame`;
  - **D4:** un servicio de diálogos en los modelos de vista (sin fuente verificada: la documentación de Prism dio 404);
  - **D5:** solo Humble Object, con la API de instancia de Gum (`AddToRoot`). Esa API resuelve `IGumService.Default`
    por dentro, así que el global sigue en nuestras llamadas.
- **Fuentes nuevas:**
  - Fowler, M. (2005, 26 de junio). *Inversion of control*. martinfowler.com.
    https://martinfowler.com/bliki/InversionOfControl.html
  - Fowler, M. (2020, 29 de abril). *Humble object*. martinfowler.com. https://martinfowler.com/bliki/HumbleObject.html
  - Gum. (2026). *MonoGameGum* (versión 2026.10.1.1) [Documentación XML del paquete NuGet Gum.MonoGame] (miembro
    `ListBoxItem.UpdateToObject`).
  - vchelaru. (2026). *Gum* [Código fuente]. GitHub. https://github.com/vchelaru/Gum (rama `main`, consultada el
    2026-11-11: `MonoGameGum/Forms/Controls/ComboBox.cs`, `ListBoxItem.cs` y `GumService.cs`).
- **Huecos:**
  - la rama `main` de Gum no es la versión 2026.10.1.1; para `ListBoxItem` la confirma la documentación instalada;
  - las páginas de Fowler de *Pull Up Method* y *Extract Superclass* solo tienen diagrama. Para quitar la repetición se
    cita la 4.4.1;
  - no se compiló, y el selector y los diálogos solo se pueden ver abriendo el juego.

**Respuesta del usuario (2026-11-11):** «Sí, D1».
- **Aplicado (sin commit):**
  - `Screens/ScreenView` (base de `LoginView`, `MainMenuView`, `MatchView` y `VersusView`), `Screens/IScreenHost`,
    `Screens/IClipboard` y `Screens/LocalServices`. Las interfaces viven con quien las usa; las implementaciones de Gum,
    en `Platform/GumScreenHost` y `Platform/GumClipboard`. Así `Platform` depende de `Screens`, sin ciclo.
  - `ModalLayer` solo lanza `IsOpenChanged`.
  - `ScreenNavigator(ServerConnection, LocalServices, IScreenHost)`. Su `ShowScreen` ya no recibe un `Func`: lo tenía
    para construir la pantalla después de limpiar los diálogos (commit `2fe1026`, el diálogo de rival que abandona
    durante la cuenta atrás). Ahora `GumScreenHost` limpia primero y después coloca los diálogos que ya llegan abiertos.
    La vista vieja sale antes de liberar sus modelos de vista, como antes.
  - `FriendsPanelViewModel` recibe `IClipboard` y `MarkCodeCopied` pasa a `CopyOwnCode`, con el Warn que tenía el pie.
  - **L0:** `LanguagePicker` ya no se suscribe al cambio de idioma (−23 líneas).
  - `BastionGame` crea `GumClipboard`, `LocalServices` y `GumScreenHost`. Fuera de él, el único acceso estático a Gum es
    `InteractiveGue.CurrentInputReceiver`, dentro de `GumScreenHost`.
  - Pruebas: `FakeClipboard` y dos pruebas de `CopyOwnCode` (portapapeles disponible y sin portapapeles).
- **Verificación:**
  - `Client` compila sin avisos de código;
  - pasan las 516 pruebas (138 + 158 + 220);
  - los archivos nuevos quedaron en LF.
- **Falta comprobar en el juego (antes del commit):**
  - L0: cambiar de idioma en el inicio de sesión y ver que el selector y su lista siguen mostrando «English (US)» y
    «Español (MX)». Si falla, se aplica L1;
  - que se abran y cierren el diálogo del inicio de sesión, el de quitar amigo, el de presencia y el del rival que
    abandona, incluido el caso del abandono durante la cuenta atrás;
  - copiar el código de amigo.
- **Siguen abiertas:** la pregunta 1 (radio `0`). La pregunta 3 se resuelve con L0 si la comprobación pasa.

**Comprobación en el juego (2026-11-11, el usuario: «Hazlo tú»):**
- **Cómo:** el servidor estaba apagado y no se arrancó, porque escribe en la base. Se abrió el cliente compilado con
  computer use y se comparó con una copia de `HEAD` compilada aparte en el scratchpad (`git archive`). La preferencia
  `%APPDATA%\Bastion\language.txt` era `es-MX` y se dejó igual. Las copias se borraron al terminar.
- **L0 falla:** con D1 sin el refresco, el selector arranca con «Selected Item», la interfaz sale en inglés y la
  preferencia se guarda como `en-US`. Con D1 y el refresco de antes, todo sale como en `HEAD`. El refresco sí hace
  falta, y la documentación de Gum no lo anticipaba.
- **Se aplicó L1 (sin commit):**
  - `ILanguageService.LanguageChanged`, que `LanguageService.ApplyLanguage` lanza después de cambiar el idioma de Gum;
  - `LanguagePicker(ILanguageService, width, height)` se suscribe con grupo de método y conserva `RefreshListItems`;
  - `LoginView(LoginViewModel, ILanguageService)` guarda `_languages`; `CreateHeader` y `CreateLanguagePicker` dejan de
    ser estáticos;
  - `ScreenNavigator.ShowLogin` le pasa `_languages`.
- **Resultado con D1 y L1, igual que `HEAD`:**
  - arranca en español, con «Español (MX)» en el selector y `es-MX` guardado;
  - al elegir inglés, la interfaz y el selector cambian a «English (US)», y la lista muestra los dos nombres;
  - al volver a español, todo regresa y se guarda `es-MX`;
  - con los campos vacíos, los dos campos se marcan en rojo (`HasError`);
  - con datos inventados y el servidor apagado, se abre el diálogo «No pudimos conectar con el servidor» sobre la
    capa oscura. «Aceptar» lo cierra, se vuelve a abrir y a cerrar, y mientras está abierto «Mostrar» no hace nada,
    así que bloquea lo de atrás.
- **Defecto que ya existía (también en `HEAD`):** la primera vez que se abre la lista del selector, los dos elementos
  dicen «ListBox Item», hasta el primer cambio de idioma. Hipótesis sin comprobar: `PickerSkin.StyleListItem` pone
  `LocalizeText = false` después de `UpdateToObject`, y Gum vuelve a escribir el texto por defecto. Se revisa con
  `Theme`.
- **No se pudo comprobar sin servidor:** los diálogos de quitar amigo, de presencia y de rival que abandona, y copiar
  el código de amigo.
- **Pregunta 3:** sigue abierta. Con L1, el selector se suscribe a `LanguageService`, que vive todo el juego, y no se
  desuscribe, igual que antes con el servicio de Gum.
- **Verificación final:** `Client` compila sin avisos de código, pasan las 516 pruebas y todo queda en LF.

**Respuesta del usuario (2026-11-11):** «Sí, A en ambas» (preguntas 1 y 3).
- **Pregunta 1, aplicada:** `ModalLayer` tiene `private const float OverlayCornerRadius = 0;`.
- **Pregunta 3, anotada:** la suscripción del selector a `LanguageService` no se cancela. Se revisa cuando exista un
  camino de vuelta a la pantalla de inicio.
- **Verificación:** `Client` compila sin avisos de código y pasan las 516 pruebas.
- **Notas para lo que sigue:**
  - el defecto «ListBox Item» del selector, al revisar `PickerSkin` en `Theme`;
  - la R-27 de `ILanguageService`, que ahora también tiene `LanguageChanged`, al cerrar la capa;
  - quedan inicializadores de una línea en 19 archivos de `Screens` (3.3.1).

**Commit de `Controls`:** `eb9d572` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 393 a 398. `Localization` (2026-11-11)

Archivos: `ILanguagePreferenceStore`, `ILanguageService`, `LanguagePreferenceStore`, `LanguageService`,
`SupportedLanguage` y `SupportedLanguages`. `Strings.Designer.cs` se genera solo y no se revisa.

- **Cumple:**
  - **R-35:** el sufijo `Store` es para datos locales del cliente, como `LanguagePreferenceStore`.
  - **10.1.1:** `LanguageService` recibe la preferencia y la base de textos de Gum por constructor.
    `LanguagePreferenceStore` es el que hace la entrada y salida con el disco, y se recibe por su interfaz.
  - **9.1.2:** los dos `catch` de cada método (`UnauthorizedAccessException` e `IOException`) no se heredan uno del
    otro, así que el orden no importa.
  - **Pasada 2:** cada par de `catch` repite una línea, que ya está extraída (`LogReadFailure`, `LogSaveFailure`). Juntarlos
    pediría atrapar `Exception` (9.3.1).
  - **9.3.2, 9.4.2 y 11.3.1:** `IndexOf` lanza `ArgumentException`, los `??` tienen alternativa válida, y la bitácora
    dice acción y contexto.
- **Aplicado sin preguntas (reglas decididas, sin commit):**
  - **R-27:** `ILanguageService` queda documentada (summary de la interfaz y de cada miembro, `param` y las dos
    excepciones de `ChangeLanguage`), y `LanguageService` lleva `<inheritdoc/>` en la clase y en sus cinco miembros.
    `GenerateDocumentationFile` se activa al cerrar la capa.
  - **R-11:** `SupportedLanguage` pasa a constructor explícito con `ThrowIfNull` y propiedades `{ get; }`. No se copia
    con `with`.
  - **R-04:** `return File.ReadAllText(_filePath).Trim();` guarda primero `savedText`.
  - **R-23:** `keys.Add((string)entry.Key);` guarda primero `string key`. IDE0008 pide el tipo explícito con los tipos
    del lenguaje (R-51).
  - **R-47:** los privados de `LanguageService` siguen el orden de `LoadInitialLanguage`: `LoadTextDatabase`,
    `ReadKeys`, `Translate`, `ResolveInitialLanguage`, `ApplyLanguage` e `IndexOf`.
  - **2.11.4:** `Languages => SupportedLanguages.All` pasa a `{ get; }`, asignada en el constructor, y
    `Default => English` pasa a `{ get; } = English`. Las dos reenviaban otra propiedad: no son catálogo de diccionario
    ni exponen un campo (R-26).
- **Verificación:** `Client` compila sin avisos de código y pasan las 516 pruebas. El juego no se abrió; el
  comportamiento no cambia.
- **Pregunta 1 (2.4.1 y 2.1.2):** `SupportedLanguages` es una clase con nombre en plural, que la 2.4.1 pone como
  ejemplo incorrecto (`BoardTiles`). Además, su colección `All` no es un sustantivo en plural. Precedente:
  `ServiceEndpoints` (298) se dio por bueno en plural sin discutirlo. Usos: 5 en `LanguageService` y 1 en
  `LoginViewModel`.
- **Pregunta 2 (2.11.4):** `Spanish` y `English` guardan en `{ get; } =` un `SupportedLanguage` que lleva el texto del
  recurso (`Strings.LanguageNameSpanish`). La regla prohíbe guardar una entrada del diccionario en una propiedad
  autoimplementada, porque no se actualiza al cambiar de idioma. Aquí los nombres son autónimos y solo están en
  `Strings.resx`, así que nunca cambian.
- **Pregunta 3 (pasada 3 y lectura):** `Translate(key)` no traduce un texto: devuelve las traducciones de una clave
  en cada idioma. Además, `GetResourceSet(CultureInfo.InvariantCulture, true, true)` no dice qué significan los dos
  `true`.

**Preguntas (393 a 398):**
1. El nombre de `SupportedLanguages` y de `All`:
   - recomendado, A: `LanguageCatalog`, con `Languages` en lugar de `All` (singular y colección en plural);
   - B: dejar la clase como `ServiceEndpoints` y renombrar solo `All` (por ejemplo `AllLanguages`);
   - C: dejar los dos.
2. Los nombres guardados de `Spanish` y `English`:
   - recomendado, A: dejarlos y anotar por qué no aplica la razón de la 2.11.4 (autónimos que no cambian);
   - B: que `SupportedLanguage` guarde la clave del recurso y lea el nombre en cada acceso;
   - C: constantes en el código, con lo que el texto de la interfaz sale de `Strings.resx`.
3. Los nombres en la carga de textos:
   - recomendado, A: `Translate` → `ReadTranslations`, que hace pareja con `ReadKeys`, y argumentos con nombre
     `createIfNotExists: true, tryParents: true`;
   - B: dejarlos.

**Respuesta del usuario (2026-11-11):** «Sí, A en todas».
- **Pregunta 1, aplicada:** `SupportedLanguages` pasa a `LanguageCatalog` (`git mv`) y `All` a `Languages`. Cambian sus
  usos en `LanguageService` y `LoginViewModel`.
- **Pregunta 2, anotada:** `Spanish` y `English` guardan su nombre una sola vez. Es correcto porque los nombres son
  autónimos («English (US)», «Español (MX)») y solo existen en `Strings.resx`, así que no cambian con el idioma, que es
  la razón de la 2.11.4. Si algún día se traducen, el nombre debe leerse en cada acceso.
- **Pregunta 3, aplicada:** `Translate` pasa a `ReadTranslations`, y `GetResourceSet` recibe
  `createIfNotExists: true, tryParents: true`, un argumento por línea (3.5.1).
- **Arreglos:** `new[] { Spanish, English }` se queda en una línea, igual que los arreglos de `RoomPolicy` y
  `FriendRequestService` en su revisión. La 3.3.1 se aplicó a inicializadores de objeto.
- **Verificación:** `Client` compila sin avisos de código y pasan las 516 pruebas.

**Commit de `Localization`:** `e3f891a` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### 399 a 404. Raíz de `Screens` (2026-11-11)

Archivos: `IEscapeKeyReceiver`, `INavigator`, `NoticeTone`, `ScreenNavigator`, `UiThread` y `ViewFactory`, más los
cuatro que trajo D1 (`IClipboard`, `IScreenHost`, `LocalServices` y `ScreenView`), que ya se escribieron con el
estándar.

- **Cumple:**
  - `IEscapeKeyReceiver`, `INavigator` y `NoticeTone` (2.5.1, 2.15.1; `None` es el primer valor y no es `[Flags]`);
  - `UiThread.Run`: el `_` de la lambda no se usa (2.7.2), y no es un reenvío que pida grupo de método (5.2.1), porque
    la firma de `Post` es otra;
  - `ScreenNavigator`: 5.3.1 en `DisposeViewModelsExcept`. La condición de tres `||` de `HandleCountdownFinished`
    no mezcla `&&` (R-24);
  - `ViewFactory`: 3.7.1 (`CreateVersionLabel` asigna `X` e `Y` después de `Anchor`, y los controles que devuelve
    una fábrica se ajustan después). La cadena de `version` es una asignación de varios pasos sin cast, que la R-23
    deja.
- **Aplicado sin preguntas (reglas decididas, sin commit):**
  - **9.4.1:** `CreateLabel` (`textKey` y `style`), `CreateButton` (`textKey`) y `CenterVertically` (`element`) no
    comprobaban sus parámetros. `CreateBoundLabel` y `CreateBoundUntranslatedLabel` comprueban `style` ellos mismos,
    en lugar del privado `CreateFixedWidthLabel`.
  - **R-23:** los cuatro casts a `LabelVisual` van primero en `labelVisual`.
  - **2.10.1:** `element.Y = 0` pasa a `MiddleOffsetY`, como el radio de `ModalLayer` (pregunta 1 de `Controls`).
  - **4.2.1 y 4.7.1:** `ReceiveEscapeKey` descarta con `is not IEscapeKeyReceiver receiver` y `return`.
- **Pasada 2, para `Theme`:**
  - el par `var labelVisual = (LabelVisual)label.Visual; style.ApplyTo(labelVisual);` se repite en `ViewFactory` (2)
    y `NoticeBox`;
  - `LocalizeText = false` se repite en `ViewFactory` (2), `FriendCodeFooter` y `PickerSkin`.
  - Un `TextStyle.ApplyTo(Label)` lo resolvería; se pregunta al revisar `Theme`.
- **Verificación:** `Client` compila sin avisos de código y pasan las 516 pruebas.
- **Pregunta 1 (pasada 3, pendiente en `05-pendientes.md`):** `UiThread.Run(uiContext, action)` publica la acción en
  el contexto de la interfaz, o la corre en el acto si no hay contexto (las pruebas). `revisor-estandar` sugirió
  `RunOnContext`. Se usa en 8 lugares.

**Pregunta (399 a 404):**
1. El nombre de `UiThread.Run`:
   - recomendado, A: dejarlo; con la clase se lee «correr en el hilo de la interfaz», que es lo que pide quien llama;
   - B: `RunOnContext`, que nombra el parámetro y no el propósito;
   - C: `Post`, que dice que se encola, pero sin contexto corre en el acto, así que engañaría en las pruebas.

**Respuesta del usuario (2026-11-11):** «Sí, A». `UiThread.Run` se queda con su nombre, y la nota de
`05-pendientes.md` queda resuelta.

**Commit de la raíz de `Screens`:** `12338cd` (2026-11-11), en `review-standard-v2.4-host`, sin push.

### Pruebas de interfaz de la carga de idioma (2026-11-11, pedidas por el usuario)

Con el cliente de `12338cd` (después de `Localization`), con computer use y el servidor apagado (no se arranca porque
escribe en la base). El sistema está en `en-US`; la preferencia guardada al empezar era `es-MX` y quedó en `es-MX`.

| Caso | Resultado |
| --- | --- |
| Arranque con `es-MX` guardado | Interfaz en español, «Español (MX)» en el selector, «Bastión 0.1.0» abajo |
| Cambio a inglés | Interfaz y selector en inglés; la lista muestra los dos nombres; se guarda `en-US` |
| Reinicio con `en-US` guardado | Arranca en inglés; el diálogo sale entero en inglés («Try again», «OK») |
| Sin archivo de preferencia | Arranca en inglés (idioma del sistema) y no crea el archivo hasta que se elige uno |
| Cultura desconocida guardada (`xx-XX`) | Arranca en inglés (idioma del sistema) y no toca el archivo |
| Vuelta a español | Interfaz en español y se guarda `es-MX` |

- **Defecto que ya existía (también en `32cbc25`, antes de D1):** si cambias de idioma con la pantalla abierta, el
  diálogo del inicio de sesión sale después con el título y el mensaje en el idioma nuevo, pero con los botones en el
  anterior («Reintentar», «Aceptar»).
  - Causa: Gum solo retraduce lo que está en `Root`, `PopupRoot` y `ModalRoot`, y un diálogo cerrado no está en
    ninguno.
  - El título y el mensaje se salvan porque se enlazan al abrir.
  - Arreglo posible, de una línea en `GumScreenHost.PlaceDialog`: llamar `dialog.Visual.RefreshLocalization()` antes
    de meterlo en `ModalRoot`. Según la documentación de Gum, retraduce el elemento y sus descendientes.
- **Defecto conocido, se repite:** la lista del selector dice «ListBox Item» hasta el primer cambio de idioma (para
  `Theme`).
- **Escape** no cierra la lista del selector en la pantalla de inicio de sesión, igual que antes: ninguna vista de esa
  pantalla atiende la tecla.
- **No se pudo probar sin servidor:**
  - `LoginViewModel.ApplyPreferredLanguage`, que aplica el idioma de la cuenta al iniciar sesión;
  - las demás pantallas.
- **No se puede probar en la interfaz sin cambiar el idioma de Windows:** el respaldo por idioma parecido (por ejemplo,
  sistema `es-ES` → «Español (MX)»). Una prueba unitaria de `LanguageCatalog.FindClosest` lo cubriría.

**Arreglo y prueba con servidor y base (2026-11-11, el usuario: «arréglalo, y también prueba con servidor y base de
datos»):**
- **Arreglo (sin commit):** `GumScreenHost.PlaceDialog` llama `dialog.Visual.RefreshLocalization()` antes de meter el
  diálogo en `ModalRoot`. En el juego, con el servidor apagado, el diálogo sale con «Try again»/«OK» después de pasar a
  inglés, y con «Reintentar»/«Aceptar» después de volver a español. Pasan las 516 pruebas.
- **No es defecto:** cambiar de idioma borra la contraseña a propósito (`LoginViewModel.SelectedLanguage`).
- **Servidor:** `dotnet run --project src/Bastion.Server.Host` desde esta rama. Arrancó en el puerto 8000, y
  `RoomCleanupService` cerró 0 salas.
  - Los clientes son copias en `scratchpad/client-a` y `client-b`, con `BASTION_SERVER_THUMBPRINT`, que es la huella
    SHA-256 de 64 caracteres; con 40 caracteres, el cliente rechaza el certificado.
  - Las contraseñas semilla pasan por el portapapeles con `scratchpad/tools/seed_password_to_clipboard.ps1`, que no
    las imprime, y luego se vacía el portapapeles.
  - **Incidente:** al leer el bloque de comentarios del script semilla, la máscara no las tapó y salieron en la salida
    de una herramienta. No se repitieron en los mensajes.
- **Resultados:**
  - **`sofia_salto` (idioma `en`), con la interfaz en español:** al iniciar sesión el menú pasa a inglés. Es la ruta del
    idioma parecido (`en` → «English (US)»), que sin servidor no se podía probar.
  - **Copiar el código de amigo:** el botón pasa a «Copied» y el portapapeles queda con el código (`SF-5T2Z`).
  - **Diálogo de quitar amigo:** se abre como modal y «Cancel» lo cierra sin quitar a nadie.
  - **`pedro_peon` (`es-MX`), con el cliente arrancado en inglés:** el menú pasa a español.
  - **Partida clasificatoria `pedro_peon` contra `marta_muros`:** se emparejan al instante, pasan por la cuenta atrás y
    llegan al tablero 3D. Pedro sale de la partida. Marta ve el diálogo modal «Partida terminada… Ganaste.», y «Volver
    al menú» la regresa. Queda en la base una partida FINISHED por abandono.
- **Defecto que ya existía (también en `32cbc25`):** cuando el idioma de la cuenta se aplica al iniciar sesión, los
  textos que el código arma con `Strings` y `CultureInfo.CurrentCulture` en un clic o en un temporizador salen en el
  idioma anterior. Los de Gum salen bien. Casos:
  - el título y el mensaje de «¿Eliminar a…?» en español con `sofia_salto`;
  - «Your turn» y «10 walls» en inglés con `pedro_peon`.
  - Causa probable: `ApplyLanguage` corre dentro del flujo `async` de `RequestSession`, y en .NET `CurrentCulture` y
    `CurrentUICulture` viajan con el flujo asíncrono. Al terminar, el hilo de la interfaz vuelve a su cultura
    anterior.
  - **Comprobado con una prueba aparte** (`scratchpad/gum-roots-probe`): un método `async` que pone
    `CurrentUICulture = en-US` después de un `await` la ve en `en-US`, pero quien lo llamó sigue en `es-MX` al volver.
    Fijar solo `DefaultThreadCurrentUICulture` no basta: los hilos que ya tienen una cultura propia la conservan.
  - **Arreglo propuesto, sin aplicar:** que `LanguageService.ApplyLanguage` fije también `Strings.Culture`. Las
    búsquedas en el archivo de recursos dejan de depender del hilo. Los formatos de número y fecha seguirían el hilo.
  - Alternativa: aplicar el idioma de la cuenta fuera del flujo `async` (publicarlo en el contexto de la interfaz).
    Depende de cómo Gum corre lo publicado, y no está comprobado.
- **Diálogo de presencia:** el servidor lo pide a los 15 minutos de búsqueda (`MatchmakingPolicy.PresenceCheckMinutes`).
  Marta quedó buscando para probarlo; el resultado se anota aparte.
- **Commit del arreglo del diálogo:** `05219b2` («Translate a dialog again when it opens»).

**Push y PR pedidos por el usuario (2026-11-11):**
- `origin/main` sigue en `2eb1167`. PR #16 (`review-standard-v2.4-repositories`, `e8d9d4c`) sigue abierto. Esta rama
  lleva 27 commits sobre él y 43 sobre `main`, todos de poijn y sin líneas de atribución.
- **La frontera rechazó el pre-push**, simulado a mano porque los hooks no están instalados:
  ```
  pre-push rechazado (context/01-regla-sin-rastro-de-ia.md):
    - src/Bastion.Client.Networking/Notifications/NotificationCallback.cs:16: [7.1.1] documentación XML fuera de un servicio (solo I*Service y su implementación la llevan)
    - src/Bastion.Client.Networking/Notifications/NotificationCallback.cs:46: [7.1.1] documentación XML fuera de un servicio (solo I*Service y su implementación la llevan)
  ```
- **Falso positivo:** `NotificationCallback` implementa `INotificationCallback`, que es un `[ServiceContract]`. La tabla R5
  de la regla admite `<inheritdoc/>` en la clase que implementa el servicio, y la 7.1.2 lo pide. El patrón `SERVICIO` de
  `frontera.py` solo reconoce clases que implementan `I*Service`.
- **No se hizo el push.** La regla dice que el control no se salta y que solo el usuario decide si se ajusta
  `frontera.py` o hace él la operación.
- **Ajuste propuesto** (`context/herramientas/frontera.py`, fuera del repositorio): que `SERVICIO` también reconozca
  `class … : … I*Callback`.
- **Respuesta del usuario:** «Sí, ajústalo».
  - `SERVICIO` ahora reconoce `class … : … I*Service` e `I*Callback`. Sigue rechazando las vistas y los modelos de vista
    (comprobado con cuatro casos).
  - El pre-push pasa (exit 0), y el texto del PR pasa la revisión de mensajes de la frontera.
- **Push:** `review-standard-v2.4-host` subió a `origin` en `05219b2`, con seguimiento.
- **PR #17:** https://github.com/Arclyne/bastion/pull/17
  - Título: «Review the host, contracts and client code against the coding standard v2.4».
  - Base `main` y 43 commits: incluye los de #16 hasta que ese se fusione.
  - Estado: abierto y `mergeable_state: clean`. Sin CI. Autor: poijn23.
  - Se abrió con la API REST y el token de Git Credential Manager (`scratchpad/tools/open_pull_request.py`), que no se
    imprimió.
  - El cuerpo, en inglés y sin rastro de IA, tiene Summary, Server host, Contracts, Client networking, Client,
    Verification y Known issues (el idioma tras el inicio de sesión y «ListBox Item»).
  - No se pudo vincular a la sesión, porque la sesión no trabaja en el checkout.

**Arreglo del idioma después de iniciar sesión (2026-11-11, el usuario: «Sí, arréglalo»):**
- **Prueba primero (roja):** `TestLanguageService.ChangeLanguage_InsideAsyncFlow_KeepsTextsInNewLanguageAfterward`.
  - Arranca `LanguageService` con `es-MX` guardado y la base de textos de Gum (`LocalizationService`).
  - Cambia a inglés dentro de un método `async`, después de un `await`, y al volver compara `Strings.LoginTagline`.
  - Sin el arreglo falla: espera «Maze of walls» y obtiene «Laberinto de muros».
  - Va en la colección `GlobalCultureCollection`, sin paralelismo, porque toca estado global. `Dispose` deja
    `Strings.Culture` y las culturas por defecto en `null`. La preferencia la da un `FakeLanguagePreferenceStore`.
- **Arreglo:** `LanguageService.ApplyLanguage` también fija `Strings.Culture = culture`. La clase de recursos usa esa
  cultura en todos los hilos y flujos, en lugar de `CurrentUICulture`.
- **Verificación:**
  - pasan las 517 pruebas (139 + 158 + 220) y `Client` compila sin avisos;
  - la frontera pasa `pre-commit` y `commit-msg`;
  - en el juego, cliente C con el arreglo: `sofia_salto` (idioma `en`) entra con la interfaz en español, y «Remove
    marta_muros?» sale con título y mensaje en inglés (antes salía «¿Eliminar a…?»). Se canceló sin quitar a nadie.
  - No se repitió el caso de «Your turn» de pedro, porque necesitaba otra partida y marta estaba esperando la
    presencia.
- **Formatos:** los números y las fechas con `CultureInfo.CurrentCulture` siguen la cultura del hilo. Para los textos de
  hoy no cambia nada visible.
- **Commit:** `a6b56e5` («Keep the chosen language for resource texts after the login»).
- **Diálogo de presencia, primer intento:** el aviso llegó a los 15 minutos, pero se miró a los 15:08, después de los 60
  segundos de respuesta. La búsqueda mostraba «Se canceló la búsqueda porque no respondiste a tiempo». Se lanzó otra
  búsqueda para verlo a tiempo.
