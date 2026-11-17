---
tipo: estandar-texto
seccion: 9
verificado: 2026-11-13 (copia literal de pdftotext del PDF v2.4; ver [[estandar-v2.4]])
---
# 9. Manejo de Errores y Excepciones

```text
9.     Manejo de Errores y Excepciones
9.1.     Convenciones
9.1.1.    Regla: variable de excepción nombrada ex
    Regla: Toda variable de excepción que sí se utiliza en el bloque catch se nombra ex.
    Descripción: Convención propia del proyecto para mantener los bloques catch predecibles
en todo el equipo (McConnell, 2004).
    Código correcto:
try
{
    _board.MovePlayer(player, destination);
}
catch (InvalidMoveException ex)
{
    _logger.Warn($"Move rejected. Player={player.Name}.", ex);
}

      Código incorrecto:
try
{
    _board.MovePlayer(player, destination);
}
catch (InvalidMoveException exception)
{
    _logger.Warn($"Move rejected. Player={player.Name}.", exception);
}


9.1.2.    Regla: orden de las cláusulas catch
    Regla: Varias cláusulas catch en un mismo try se ordenan del tipo más derivado al menos
derivado (Microsoft, 2025a).
    Descripción: Con herencia directa entre los tipos, como abajo, el compilador rechaza el
orden incorrecto con un error: no es solo preferencia de estilo.
    Código correcto:
try
{
    _board.MovePlayer(player, ParsePosition(rawDestination));
}
catch (ArgumentOutOfRangeException ex)
{
    _logger.Warn($"Position is outside the board. Player={player.Name}.", ex);


                                            50
}
catch (ArgumentException ex)
{
    _logger.Warn($"Position format is invalid. Player={player.Name}.", ex);
}

      Código incorrecto (no compila — CS0160):
try
{
    _board.MovePlayer(player, ParsePosition(rawDestination));
}
catch (ArgumentException ex)
{
    _logger.Warn($"Position format is invalid. Player={player.Name}.", ex);
}
catch (ArgumentOutOfRangeException ex)
{
    _logger.Warn($"Position is outside the board. Player={player.Name}.", ex);
}


9.2.     Excepciones Encadenadas
9.2.1.    Regla: preservar la excepción original como causa
    Regla: Cuando una excepción se traduce a otro tipo porque la capa actual puede aportar
contexto útil, se conserva la excepción original como innerException. Se prefiere un tipo predefi-
nido de .NET y solo se utiliza una excepción personalizada cuando el llamador necesita distinguir
una condición propia del dominio (Microsoft, 2025a).
    Excepción: En la frontera de red, el servicio que responde a un cliente remoto descarta la
excepción original al traducirla al fallo que recibe el cliente, siempre que antes la registre con
Error (Sección 11.1). La causa original contiene la traza de la pila, nombres de tablas y mensajes
del motor de base de datos; enviarla al cliente expone información interna (MITRE, 2026), y
como innerException de un fallo de red no llega al cliente.
    Código correcto:
try
{
    _board.SaveState(currentState);
}
catch (IOException ex)
{
    throw new InvalidOperationException("Failed to persist game state.", ex);
}

      Código incorrecto:
try
{
    _board.SaveState(currentState);
}
catch (IOException ex)
{
    throw new InvalidOperationException("Failed to persist game state: " + ex.Message);
}

      Código correcto (frontera de red):



                                               51
public MatchSummary SaveMatch(MatchResult result)
{
    try
    {
        return _matchArchive.Save(result);
    }
    catch (DbUpdateException ex)
    {
        _logger.Error($"The match could not be saved. MatchId={result.MatchId}", ex);
        throw new FaultException(MatchServerFailureReason);
    }
}

      Código incorrecto (frontera de red):
public MatchSummary SaveMatch(MatchResult result)
{
    try
    {
        return _matchArchive.Save(result);
    }
    catch (DbUpdateException ex)
    {
        throw new FaultException(ex.ToString());
    }
}


9.2.2.    Regla: throw; en lugar de throw ex;
   Regla: Al relanzar la misma excepción capturada, se usa throw; sin especificar la variable
(Microsoft, 2026a).
   Descripción: throw ex; reinicia la traza de la pila; throw; conserva la original completa
(Microsoft, 2025a).
   Código correcto:
try
{
    _board.MovePlayer(player, destination);
}
catch (InvalidMoveException ex)
{
    _logger.Error($"Move failed. Player={player.Name}.", ex);
    throw;
}

      Código incorrecto:
try
{
    _board.MovePlayer(player, destination);
}
catch (InvalidMoveException ex)
{
    _logger.Error($"Move failed. Player={player.Name}.", ex);
    throw ex;
}




                                             52
9.3.     Restricciones
9.3.1.    Regla: prohibido capturar o lanzar Exception genérica
    Regla: Prohibido lanzar directamente System.Exception u otro tipo genérico de excepción
base, o capturarlo en un bloque catch; siempre se usa el tipo más específico. Esta restricción
no impide heredar de Exception ni recibirla como parámetro innerException en el constructor
convencional de una excepción personalizada.
    Descripción: Capturar una excepción genérica lo detecta la regla de análisis CA1031 (Micro-
soft, 2016a) y lanzarla lo detecta CA2201 (Microsoft, 2016c). Las excepciones genéricas ocultan
problemas en tiempo de ejecución, obligan al llamador a capturar también los errores que no sabe
manejar y dificultan la depuración.
    Código correcto:
public void EstablishConnection()
{
    try
    {
        _database.Connect();
    }
    catch (TimeoutException ex)
    {
        _logger.Error("Database connection timed out.", ex);
        throw;
    }
}

   Código incorrecto:
public void EstablishConnection()
{
    try
    {
        _database.Connect();
    }
    catch (Exception ex)
    {
        _logger.Error("Database connection failed.", ex);
        throw;
    }
}


9.3.2.    Regla: preferir excepciones predefinidas
    Regla: Se usa una excepción predefinida cuando expresa correctamente el error. Para argumen-
tos nulos se usa ArgumentNullException; para argumentos inválidos, ArgumentException o una
derivada; y para una operación incompatible con el estado actual, InvalidOperationException.
Solo se crea una excepción personalizada cuando no existe una equivalente y el llamador necesita
tratar esa condición por separado (Microsoft, 2025a).
    Excepción: Un rechazo de negocio esperado, como unas credenciales inválidas, se comunica
con una excepción personalizada cuando debe cruzar un contrato de servicio WCF, porque el fallo
tipado (FaultException<T>) es el mecanismo que el contrato ofrece para que el cliente distinga
cada rechazo. Dentro del dominio, sin una frontera de red de por medio, sigue aplicándose la
regla general.
    Código correcto:
public void StartTurn(Player player)


                                              53
{
    ArgumentNullException.ThrowIfNull(player);

    if (!player.IsActive)
    {
        throw new InvalidOperationException("The player is not active.");
    }

    BeginTurn(player);
}

    Código incorrecto:
public void StartTurn(Player player)
{
    ArgumentNullException.ThrowIfNull(player);

    if (!player.IsActive)
    {
        throw new GameStateException("The player cannot start a turn.");
    }

    BeginTurn(player);
}


9.4.     Comprobación de Nulos
9.4.1.    Regla: referencias anulables y validación de argumentos
    Regla: El proyecto habilita referencias anulables con <Nullable>enable</Nullable>. Un
valor que puede ser nulo se declara con ?. Todo parámetro de tipo referencia no anulable
de un miembro public o protected, incluidos los constructores, se comprueba al inicio con
ArgumentNullException.ThrowIfNull, como exige la regla de análisis CA1062 (Microsoft, 2020).
Los miembros private e internal no repiten la comprobación, porque solo los invoca código
que el análisis estático ya revisó. En un servicio WCF, un argumento nulo recibido del cliente se
responde con el fallo que declara el contrato y no con ArgumentNullException, que el cliente
no puede distinguir. Las comparaciones se expresan con is null o is not null, y se prohíbe
ocultar advertencias con el operador ! sin una garantía demostrable (Microsoft, 2026f; Microsoft,
2026a).
    Descripción: Las anotaciones de nulabilidad solo existen en tiempo de compilación. Un
miembro público puede invocarse desde otro ensamblado o desde un deserializador que no las
respeta, por lo que la comprobación en tiempo de ejecución es la única garantía; CA1062 hace que
esta regla se verifique al compilar en lugar de depender de la revisión de código.
    Código correcto:
public Player? FindPlayer(Guid playerId)
{
    return _players.SingleOrDefault(player => player.Id == playerId);
}

public void StartTurn(Player player)
{
    ArgumentNullException.ThrowIfNull(player);
    _turnManager.Start(player);
}

    Código incorrecto:

                                               54
public Player FindPlayer(Guid playerId)
{
    return _players.SingleOrDefault(player => player.Id == playerId)!;
}

public void StartTurn(Player player)
{
    if (player == null)
    {
        throw new ArgumentNullException(nameof(player));
    }

    _turnManager.Start(player);
}


9.4.2.   Regla: valor alternativo con ?? cuando una expresión puede ser nula
    Regla: Cuando una expresión puede ser null y existe un valor alternativo válido para ese
caso, el resultado se obtiene con el operador ?? en una sola expresión. Prohibido comparar la
expresión con null mediante el operador ternario ?: o un if solo para elegir entre ella y su
alternativa. Si no existe un valor alternativo válido, el caso nulo se trata como un error (Sección
9.3.2).
    Descripción: El operador ?? evalúa su operando izquierdo una sola vez y evalúa el derecho
únicamente cuando el izquierdo es null (Microsoft, 2026h). Esta regla precisa la Sección 4.5:
cuando la única condición es que el valor sea nulo, se usa ?? en lugar de ?:.
    Datos deserializados: Una propiedad de un objeto de transferencia que se deserializa desde
la red o desde un archivo se declara anulable (string?) cuando el emisor puede omitirla, porque
el deserializador asigna null aunque el tipo diga lo contrario. Prohibido aplicar ?? sobre una
propiedad declarada no anulable: el tipo afirmaría algo que el código no cree.
    Verificación: Los analizadores IDE0029 e IDE0030 solo detectan el ternario escrito con !=
null o == null, no con is null ni is not null, que es la forma que exige la Sección 9.4.1. Esta
regla se comprueba en la revisión de código.
    Código correcto:
public sealed class PlayerProfile
{
    public PlayerProfile(string accountName, string? nickname)
    {
        AccountName = accountName;
        Nickname = nickname;
    }

    public string AccountName { get; }

    public string? Nickname { get; }

    public string GetDisplayName()
    {
        return Nickname ?? AccountName;
    }
}

    Código incorrecto:
public sealed class PlayerProfile
{


                                                55
    public PlayerProfile(string accountName, string? nickname)
    {
        AccountName = accountName;
        Nickname = nickname;
    }

    public string AccountName { get; }

    public string? Nickname { get; }

    public string GetDisplayName()
    {
        return Nickname is not null ? Nickname : AccountName;
    }
}


9.5.     Liberación de Recursos
9.5.1.    Regla: la clase dueña de un recurso lo libera
    Regla: Todo objeto IDisposable creado y usado dentro de un mismo método se declara
con using. Una clase que crea un objeto IDisposable y lo guarda en un campo es su dueña:
implementa IDisposable y lo libera en su Dispose. Una dependencia recibida por constructor
(Sección 10) no se libera, porque la clase no es su dueña (Microsoft, 2025g).
    Código correcto:
public sealed class ReplayRecorder : IDisposable
{
    private readonly FileStream _replayFile;

    public ReplayRecorder(string replayPath)
    {
        _replayFile = File.Create(replayPath);
    }

    public void Dispose()
    {
        _replayFile.Dispose();
    }
}

    Código incorrecto:
public sealed class ReplayRecorder
{
    private readonly FileStream _replayFile;

    public ReplayRecorder(string replayPath)
    {
        _replayFile = File.Create(replayPath);
    }
}


9.5.2.    Regla: cerrar un canal WCF con Close y Abort
   Regla: Un canal o cliente WCF no se libera con using ni con una llamada directa a Close
dentro de Dispose. Se llama a Close dentro de un try y, si falla con CommunicationException
o TimeoutException, se llama a Abort.

                                            56
   Descripción: Close puede lanzar una excepción cuando la red falla. Dentro del bloque
finally que genera using, esa excepción oculta la que se lanzó en el cuerpo y omite el código
que sigue; Abort libera el canal sin intentar comunicarse con el servidor (Microsoft, 2018).
   Código correcto:
public void Dispose()
{
    try
    {
        _channel.Close();
    }
    catch (CommunicationException)
    {
        _channel.Abort();
    }
    catch (TimeoutException)
    {
        _channel.Abort();
    }
}

    Código incorrecto:
public void Dispose()
{
    _channel.Close();
}


9.6.     Diseño de Excepciones Propias
9.6.1.    Regla: constructores de una excepción propia
    Regla: Una excepción propia hereda de Exception, se declara sealed, termina en Exception
(Sección 2.14.1), fija su mensaje en inglés dentro del constructor y expone sus datos mediante
propiedades de solo lectura. Si no lleva datos, declara los tres constructores estándar que exige la
regla de análisis CA1032 (Microsoft, 2016b). Si lleva datos obligatorios, declara solo los constructores
que los reciben.
    Descripción: Un constructor sin parámetros dejaría una excepción con datos sin asignar,
lo que contradice la Sección 2.6.3. Como la clase es sealed, ninguna clase derivada necesita los
constructores restantes.
    Código correcto:
public sealed class TileOccupiedException : Exception
{
    public TileOccupiedException(Tile tile)
        : base($"The tile is already occupied. Row={tile.Row} Column={tile.Column}")
    {
        Tile = tile;
    }

    public Tile Tile { get; }
}

    Código incorrecto:
public class TileOccupiedException : Exception
{
    public TileOccupiedException()


                                                  57
    {
    }

    public Tile? Tile { get; set; }
}


9.7.     Manejadores async void
9.7.1.    Regla: un manejador async void no deja escapar excepciones
    Regla: async void se usa únicamente en manejadores de eventos. Todo su cuerpo queda
dentro de un try que captura cada excepción que la operación puede lanzar y la maneja según la
Sección 11.1.
    Descripción: Un método async void no devuelve una Task donde guardar la excepción:
la lanza directamente sobre el contexto de sincronización activo, ningún catch del llamador la
recibe y el proceso termina (Cleary, 2013).
    Código correcto:
private async void HandleRollClick(object? sender, EventArgs e)
{
    try
    {
        await _dice.RollAsync();
    }
    catch (TimeoutException ex)
    {
        _logger.Warn("The dice roll did not finish in time.", ex);
        ShowRetryNotice();
    }
}

    Código incorrecto:
private async void HandleRollClick(object? sender, EventArgs e)
{
    await _dice.RollAsync();
}
```
