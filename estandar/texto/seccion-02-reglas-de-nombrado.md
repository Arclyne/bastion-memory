---
tipo: estandar-texto
seccion: 2
verificado: 2026-11-13 (copia literal de pdftotext del PDF v2.4; ver [[estandar-v2.4]])
---
# 2. Reglas de Nombrado

```text
2.     Reglas de Nombrado
    El nombrado debe ser consistente y utilizar palabras descriptivas en inglés para evitar
ambigüedades, de manera que cada identificador sea autoexplicativo sin necesidad de comentarios
adicionales.




                                                5
2.1.     Variables
2.1.1.    Regla: camelCase y nombres descriptivos
    Regla: Variables locales y parámetros en camelCase. Se permite i únicamente como índice
de un ciclo corto, simple y no anidado. Se permiten j y k solo como segundo y tercer índice de
una operación posicional o matemática breve, sin significado de dominio. Cuando el contador
representa filas, columnas, jugadores, rondas u otro concepto del juego, o cuando el cuerpo del
ciclo no es inmediato, se usa un nombre descriptivo como rowIndex, columnIndex o playerIndex
(Microsoft, 2025c).
    Excepción: Los parámetros de un record posicional se escriben en PascalCase, como en
record DiceRolled(Player Player, int FaceValue), porque el compilador los convierte en
propiedades públicas del tipo (Microsoft, 2025c).
    Código correcto:
public void RevealTiles(IReadOnlyList<Tile> tiles)
{
    for (int i = 0; i < tiles.Count; i++)
    {
        tiles[i].Reveal();
    }
}

public void ResetBoard()
{
    for (int rowIndex = 0; rowIndex < BoardSize; rowIndex++)
    {
        for (int columnIndex = 0; columnIndex < BoardSize; columnIndex++)
        {
            _tiles[rowIndex, columnIndex].Reset();
        }
    }
}

   Código incorrecto:
public void ResetBoard()
{
    for (int i = 0; i < BoardSize; i++)
    {
        for (int j = 0; j < BoardSize; j++)
        {
            _tiles[i, j].Reset();
        }
    }
}


2.1.2.    Regla: nombres de colecciones en plural
   Regla: Toda colección (arreglo, lista, diccionario o cualquier IEnumerable<T>) se nombra
con un sustantivo en plural (Cwalina & Abrams, 2008).
   Código correcto:
public sealed class GameBoard
{
    private readonly List<Player> _players;

    public GameBoard(List<Player> players)


                                               6
    {
         _players = players;
    }
}

    Código incorrecto:
public sealed class GameBoard
{
    private readonly List<Player> _playerList;

    public GameBoard(List<Player> playerList)
    {
        _playerList = playerList;
    }
}


2.1.3.   Regla: una declaración por línea
   Regla: No se declara más de una variable en la misma sentencia, aunque compartan tipo
(McConnell, 2004).
   Código correcto:
int currentRow = startingRow;
int currentColumn = startingColumn;

    Código incorrecto:
int currentRow = startingRow, currentColumn = startingColumn;


2.1.4.   Regla: prefijos interrogativos para variables booleanas
    Regla: Toda variable bool se nombra como una pregunta cerrada, con uno de los prefijos
is, are, has, can o should (Martin, 2008). Es la misma lista que la de los métodos booleanos
(Sección 2.2.3), escrita en minúscula; are es la forma plural de is, como en areFieldsComplete.
    Código correcto:
bool isPlayerTurnActive = true;
bool hasReachedFinalTile = false;

    Código incorrecto:
bool playerTurnActive = true;
bool finalTileReached = false;


2.2.     Métodos
2.2.1.   Regla: PascalCase y verbo descriptivo
    Regla: El nombre de un método se escribe en PascalCase y comienza con un verbo o frase
verbal (Microsoft, 2025c). Se exceptúan las convenciones definidas expresamente en este estándar
y los nombres impuestos por una interfaz o por la plataforma .NET.
    Código correcto:
public int CalculateTotalScore(int basePoints, int bonusPoints)
{
    return basePoints + bonusPoints;
}


                                               7
   Código incorrecto:
public int totalScore(int basePoints, int bonusPoints)
{
    return basePoints + bonusPoints;
}

    Métodos de conversión: Un método que convierte un valor en otro tipo se nombra
To<Tipo> o From<Tipo>, como ToString o TimeSpan.FromHours. Es la convención de .NET para
las conversiones con nombre (Microsoft, 2019), por lo que To y From cuentan como frase verbal.
    Código correcto (conversión):
public static MoveSummary ToSummary(MoveResult moveResult)
{
    return new MoveSummary(moveResult.Player.Name, moveResult.Destination.Row);
}

   Código incorrecto (conversión):
public static MoveSummary SummaryOf(MoveResult moveResult)
{
    return new MoveSummary(moveResult.Player.Name, moveResult.Destination.Row);
}


2.2.2.   Regla: máximo de parámetros
    Regla: Un método no recibe más de tres parámetros; con más datos de entrada, se encapsulan
en un DTO. El límite aplica también a los constructores. Un parámetro params cuenta como uno
solo, sin importar cuántos argumentos reciba en la llamada.
    Descripción: McConnell señala que una lista larga de parámetros incrementa la probabilidad
de invocar el método con el orden o el valor incorrecto (McConnell, 2004). El riesgo es el mismo
al invocar un constructor. En cambio, los argumentos de un params son todos del mismo tipo y
cumplen el mismo papel, así que su orden no se puede confundir con el de otro parámetro.
    Código correcto: Archivo MoveRequest.cs:
public sealed record MoveRequest(Player Player, Tile Origin, Tile Destination);

   Archivo MoveExecutor.cs:
public sealed class MoveExecutor
{
    public MoveResult ExecuteMove(MoveRequest moveRequest)
    {
        return new MoveResult(moveRequest.Player, moveRequest.Destination);
    }
}

   Código incorrecto:
public sealed class MoveExecutor
{
    public MoveResult ExecuteMove(Player player, Tile origin, Tile destination, int
        diceRoll, bool isDoubleTurn)
    {
        return new MoveResult(player, destination);
    }
}




                                               8
2.2.3.    Regla: métodos booleanos como pregunta
    Regla: Un método que devuelve bool y expresa una pregunta se nombra con uno de los
prefijos Is, Are, Has, Can o Should (Martin, 2008). Es la misma lista que la de las variables
booleanas (Sección 2.1.4), escrita en mayúscula. Se exceptúan patrones convencionales de .NET
como Try... y miembros definidos por la plataforma o por una interfaz, como Equals.
    Excepción: Un método que verifica una contraseña, una firma o un certificado se nombra con
el verbo Verify, aunque devuelva bool. Así nombra .NET sus propias operaciones criptográficas
(RSA.VerifyData, X509Certificate2.Verify). En estos métodos importa el trabajo que realizan,
no solo la respuesta: una verificación señuelo se ejecuta aunque su resultado se descarte, para que
el tiempo de respuesta no revele si la cuenta existe.
    Código correcto:
public bool IsMoveValid(Tile origin, Tile destination)
{
    return destination.IsWithinBoard && !destination.IsOccupied;
}

   Código incorrecto:
public bool CheckMove(Tile origin, Tile destination)
{
    return destination.IsWithinBoard && !destination.IsOccupied;
}


2.3.     Constantes
2.3.1.    Regla: PascalCase para constantes
   Regla: Toda constante (de campo o local, incluidas private e internal) se escribe en
PascalCase, sin SCREAMING_SNAKE_CASE (Microsoft, 2025c).
   Código correcto:
public sealed class GameBoard
{
    private const int BoardSize = 8;
    private const string DefaultGameMode = "Classic";
}

   Código incorrecto:
public sealed class GameBoard
{
    private const int BOARD_SIZE = 8;
    private const string DEFAULT_GAME_MODE = "Classic";
}


2.3.2.    Regla: const frente a static readonly
    Regla: Un valor conocido en tiempo de compilación se declara const. Un valor privado
calculado una sola vez en tiempo de ejecución se declara como campo private static readonly.
Un valor público que no puede ser const, como un Color o un TimeSpan, se expone como propiedad
estática de solo lectura en PascalCase: public static T Nombre { get; } = valor;.
    Descripción: El compilador de C# exige que todo const sea evaluable en tiempo de
compilación; rechaza cualquier expresión que dependa de una llamada a método. Un valor público
se expone como propiedad y no como campo para que todo lo que una clase hace visible sea una


                                                9
propiedad, igual que en la sección de propiedades (Sección 2.11), y para poder cambiar después
cómo se obtiene sin cambiar a quien lo usa.
   Código correcto:
public sealed class DiceRoller
{
    private const int MinimumFaceValue = 1;
    private const int DefaultMaximumFaceValue = 6;
    private static readonly int _maximumFaceValue = LoadMaximumFaceValueFromConfig();

    private static int LoadMaximumFaceValueFromConfig()
    {
        return DefaultMaximumFaceValue;
    }
}

    Código incorrecto:
public sealed class DiceRoller
{
    private static readonly int _minimumFaceValue = 1;
    private static readonly int _maximumFaceValue = 6;
}

    Código correcto (valor público):
public static class TurnTiming
{
    private const int TurnLimitSeconds = 45;

    public static TimeSpan TurnLimit { get; } = TimeSpan.FromSeconds(TurnLimitSeconds);
}

    Código incorrecto (valor público):
public static class TurnTiming
{
    private const int TurnLimitSeconds = 45;

    public static readonly TimeSpan TurnLimit = TimeSpan.FromSeconds(TurnLimitSeconds);
}


2.4.     Clases
2.4.1.    Regla: PascalCase y sustantivo singular
   Regla: El nombre de una clase se escribe en PascalCase y es un sustantivo o frase nominal
en singular (Cwalina & Abrams, 2008). Las clases de prueba se exceptúan porque siguen la
convención específica del prefijo Test definida en este estándar.
   Código correcto:
public sealed class BoardTile
{
}

    Código incorrecto:
public sealed class BoardTiles
{
}


                                             10
   Excepción: Una clase static que solo agrupa valores predefinidos del mismo tipo se nombra
en plural, como Colors o Brushes en .NET. Una clase estática no representa un objeto, porque
no se pueden crear instancias de ella; representa el conjunto, y cada miembro se lee como un
elemento de ese conjunto: TileColors.Highlight.
   Código correcto (clase estática):
public static class TileColors
{
    public static Color Highlight { get; } = new Color(0xF0, 0xC4, 0x88);

    public static Color Blocked { get; } = new Color(0xB3, 0x26, 0x1E);
}

    Código incorrecto (clase estática):
public static class TileColorList
{
    public static Color Highlight { get; } = new Color(0xF0, 0xC4, 0x88);

    public static Color Blocked { get; } = new Color(0xB3, 0x26, 0x1E);
}


2.4.2.    Regla: sin prefijos ni abreviaturas poco claras
   Regla: Sin prefijos que indiquen que un tipo es una clase (CTile, ClsPlayer) ni abreviaturas
poco reconocidas (Cwalina & Abrams, 2008).
   Código correcto:
public sealed class TurnManager
{
}

    Código incorrecto:
public sealed class ClsTrnMgr
{
}


2.5.     Interfaces
2.5.1.    Regla: prefijo I
   Regla: Toda interfaz se escribe en PascalCase con prefijo I, seguido de un sustantivo, frase
nominal o adjetivo que describa la capacidad o rol (Cwalina & Abrams, 2008).
   Código correcto:
public interface IMovable
{
    void Move(Tile destination);
}

    Código incorrecto:
public interface Movable
{
    void Move(Tile destination);
}




                                              11
2.5.2.    Regla: correspondencia entre interfaz e implementación estándar
   Regla: Cuando una clase es la implementación estándar de una interfaz, su nombre coincide
exactamente con el de la interfaz, sin el prefijo I (Cwalina & Abrams, 2008).
   Código correcto: Archivo IDiceRoller.cs:
public interface IDiceRoller
{
    int Roll();
}

    Archivo DiceRoller.cs:
public sealed class DiceRoller : IDiceRoller
{
    private const int MinimumFaceValue = 1;
    private const int ExclusiveMaximumFaceValue = 7;

    public int Roll()
    {
        return Random.Shared.Next(MinimumFaceValue, ExclusiveMaximumFaceValue);
    }
}

    Código incorrecto: Archivo IDiceRoller.cs:
public interface IDiceRoller
{
    int Roll();
}

    Archivo RandomDiceGenerator.cs:
public sealed class RandomDiceGenerator : IDiceRoller
{
    private const int MinimumFaceValue = 1;
    private const int ExclusiveMaximumFaceValue = 7;

    public int Roll()
    {
        return Random.Shared.Next(MinimumFaceValue, ExclusiveMaximumFaceValue);
    }
}


2.6.     Campos Privados
2.6.1.    Regla: prefijo de guion bajo
    Regla: Todo campo private o internal no constante, sea de instancia o estático, se escribe
en camelCase con guion bajo inicial (_campo). No se emplea el prefijo especial s_ para campos
estáticos.
    Descripción: Facilita el análisis automático del código (autocompletado, analizadores de
estilo) y es la convención de nombrado oficial del equipo de .NET Runtime (Microsoft, 2025c).
    Código correcto:
public sealed class TurnManager
{
    private readonly List<Player> _players;
    private int _currentPlayerIndex;



                                             12
    public TurnManager(List<Player> players)
    {
        _players = players;
        _currentPlayerIndex = 0;
    }
}

    Código incorrecto:
public sealed class TurnManager
{
    private readonly List<Player> players;
    private int currentPlayerIndex;

    public TurnManager(List<Player> players)
    {
        this.players = players;
        currentPlayerIndex = 0;
    }
}


2.6.2.   Regla: misma convención para campos estáticos
   Regla: Un campo static privado o interno conserva el prefijo de guion bajo y no agrega
marcadores relacionados con su almacenamiento.
   Código correcto:
public sealed class GameSessionRegistry
{
    private static readonly List<Player> _connectedPlayers = new();
}

    Código incorrecto:
public sealed class GameSessionRegistry
{
    private static readonly List<Player> s_connectedPlayers = new();
}


2.6.3.   Regla: momento de inicialización de un campo
   Regla: Todo campo queda inicializado antes de que la instancia esté disponible para su uso.
Un campo cuyo valor no depende de los parámetros del constructor se inicializa en línea, en su
propia declaración. Un campo cuyo valor depende de un parámetro del constructor o de lógica de
construcción se inicializa en el cuerpo del constructor. Prohibido dejar un campo de referencia no
anulable sin asignar en el constructor para que un método posterior lo asigne por primera vez
(McConnell, 2004).
   Código correcto:
public sealed class GameSession
{
    private readonly Guid _sessionId = Guid.NewGuid();
    private readonly List<Player> _players;

    public GameSession(List<Player> players)
    {
        _players = players;


                                               13
    }
}

    Código incorrecto:
public sealed class GameSession
{
    private List<Player> _players;

    public GameSession(List<Player> players)
    {
    }

    public void Configure(List<Player> players)
    {
        _players = players;
    }
}


2.7.     Variables No Utilizadas
2.7.1.    Regla: excepción sin nombre en catch
    Regla: Prohibido asignar un nombre genérico (ex, ignored) a una variable de excepción no
usada; se omite el identificador y se deja solo el tipo (Microsoft, 2026a).
    Descripción: Un catch que descarta la excepción también debe evitar el patrón de control
de flujo por return: la sección de manejo de errores exige que toda excepción capturada y no
relanzada quede registrada (Sección 11.1), nunca silenciada mediante un simple valor de retorno.
    Código correcto:
public void ValidateMoveFormat(string rawInput)
{
    try
    {
        ParseMove(rawInput);
    }
    catch (FormatException)
    {
        _logger.Warn($"Move input has an invalid format. RawInput={rawInput}.");
    }
}

    Código incorrecto:
public void ValidateMoveFormat(string rawInput)
{
    try
    {
        ParseMove(rawInput);
    }
    catch (FormatException ignored)
    {
        _logger.Warn($"Move input has an invalid format. RawInput={rawInput}.");
    }
}




                                              14
2.7.2.    Regla: descarte _ en expresiones lambda
    Regla: Un parámetro de lambda se nombra con el descarte _ únicamente cuando no participa
en el cuerpo de la expresión: comunica de forma explícita al resto del equipo que ese valor es
irrelevante para la operación y evita que el analizador de estilo señale un parámetro sin usar
(Microsoft, 2025b). En una lambda con más de un parámetro no utilizado, cada uno se descarta
por separado con su propio _; el compilador los trata como posiciones independientes, no como
una variable compartida.
    Prohibido: Usar el descarte cuando el parámetro sí se lee en el cuerpo de la lambda, aunque
sea una sola vez. El compilador lo permite como un identificador válido, pero oculta la intención
del valor y obliga a quien lee el código a inferir por el contexto qué representa.
    Código correcto:
_players.RemoveAll(player => !player.IsActive);
_players.RemoveAll(_ => _players.Count > MaximumPlayers);

    Código incorrecto:
_players.RemoveAll(player => _players.Count > MaximumPlayers);
_players.RemoveAll(_ => !_.IsActive);


2.8.     Estructuras de Datos: class frente a record
2.8.1.    Regla: mutabilidad como criterio de elección
    Regla: Entidades cuyo estado cambia durante la partida se declaran class. Valores inmutables
o eventos que solo describen un hecho ocurrido se declaran record (Microsoft, 2026b). Un objeto
que viaja por la red como contrato de servicio es un objeto de datos y sigue la Sección 2.11.3.
    Código correcto: Archivo Player.cs:
public sealed class Player
{
    public Player(string name)
    {
        Name = name;
        Score = 0;
    }

    public string Name { get; }
    public int Score { get; private set; }

    public void AddScore(int points)
    {
        Score += points;
    }
}

    Archivo DiceRolled.cs:
public sealed record DiceRolled(Player Player, int FaceValue);

    Código incorrecto: Archivo Player.cs:
public sealed record Player
{
    public Player(string name)
    {
        Name = name;
        Score = 0;


                                               15
    }

    public string Name { get; }
    public int Score { get; private set; }

    public void AddScore(int points)
    {
        Score += points;
    }
}

    Archivo DiceRolled.cs:
public sealed class DiceRolled
{
    public DiceRolled(Player player, int faceValue)
    {
        Player = player;
        FaceValue = faceValue;
    }

    public Player Player { get; }
    public int FaceValue { get; }
}

    Excepción: Un valor inmutable que contiene un dato sensible (una contraseña, un token de
sesión o su hash) se declara sealed class, no record. El compilador genera para todo record
un ToString que escribe el nombre y el valor de cada propiedad pública (Microsoft, 2026b), así
que registrar el objeto en la bitácora o verlo en un mensaje de error expone el secreto. Además,
la igualdad que genera un record compara los arreglos por referencia, por lo que no sirve para
un hash guardado en un byte[].
    Código correcto (dato sensible):
public sealed class JoinRequest
{
    public JoinRequest(string playerName, string roomPassword)
    {
        PlayerName = playerName;
        RoomPassword = roomPassword;
    }

    public string PlayerName { get; }

    public string RoomPassword { get; }
}

    Código incorrecto (dato sensible):
public sealed record JoinRequest(string PlayerName, string RoomPassword);


2.9.     Identidad de los Objetos
2.9.1.    Regla: identidad mediante clave de negocio
    Regla: La identidad de una entidad se define mediante su clave de negocio (business key).
Prohibido sobrescribir Equals/GetHashCode con todos los atributos o con un identificador auto-
incremental sin significado en el dominio.



                                              16
   Descripción: Las guías de diseño de .NET recomiendan basar la igualdad en los atributos
que determinan la identidad en el dominio, no en la totalidad del estado interno (Cwalina &
Abrams, 2008).
   Código correcto:
public sealed class BoardTile : IEquatable<BoardTile>
{
    public BoardTile(int row, int column)
    {
        Row = row;
        Column = column;
    }

    public int Row { get; }
    public int Column { get; }
    public bool IsOccupied { get; private set; }

    public void SetOccupancy(bool isOccupied)
    {
        IsOccupied = isOccupied;
    }

    public bool Equals(BoardTile? other)
    {
        return other is not null && Row == other.Row && Column == other.Column;
    }

    public override bool Equals(object? obj)
    {
        return Equals(obj as BoardTile);
    }

    public override int GetHashCode()
    {
        return HashCode.Combine(Row, Column);
    }
}

    Código incorrecto:
public sealed class BoardTile : IEquatable<BoardTile>
{
    public BoardTile(int internalId, int row, int column)
    {
        InternalId = internalId;
        Row = row;
        Column = column;
    }

    public int InternalId { get; }
    public int Row { get; }
    public int Column { get; }
    public bool IsOccupied { get; private set; }

    public void SetOccupancy(bool isOccupied)
    {
        IsOccupied = isOccupied;
    }



                                            17
    public bool Equals(BoardTile? other)
    {
        return other is not null && InternalId == other.InternalId;
    }

    public override bool Equals(object? obj)
    {
        return Equals(obj as BoardTile);
    }

    public override int GetHashCode()
    {
        return InternalId.GetHashCode();
    }
}


2.10.     Valores Mágicos
2.10.1.    Regla: enumeradores y constantes en lugar de literales
   Regla: Prohibido usar valores numéricos o cadenas literales directamente en la lógica del
juego; todo valor con significado en el dominio se gestiona mediante enum o constante de clase
(Martin, 2008).
   Código correcto: Archivo TurnState.cs:
public enum TurnState
{
    WaitingForRoll,
    Moving,
    Finished
}

    Archivo TurnManager.cs:
public sealed class TurnManager
{
    private const int MaximumPlayers = 4;

    public bool CanAddPlayer(int currentPlayerCount)
    {
        return currentPlayerCount < MaximumPlayers;
    }
}

    Código incorrecto:
public sealed class TurnManager
{
    public bool CanAddPlayer(int currentPlayerCount)
    {
        return currentPlayerCount < 4;
    }

    public void SetState(int state)
    {
        if (state == 2)
        {
            FinishTurn();
        }


                                              18
    }

    private void FinishTurn()
    {
    }
}

    Aclaraciones:

        Los literales 0 y 1 se permiten como valores neutros: un contador que empieza en cero,
        un incremento o el primer índice. McConnell (2004) los señala como los únicos literales
        aceptables dentro de la lógica. Si el 0 o el 1 tiene significado en el dominio, como el primer
        turno de la partida, lleva nombre.

        Un literal se permite cuando es el valor de una definición con nombre: el inicializador de
        una constante, de una propiedad estática de solo lectura (Sección 2.3.2) o de un miembro
        de un enum. Esa definición es el lugar donde el valor recibe su nombre.

        Un valor que ya tiene nombre no se repite como literal en otro lugar, tampoco dentro de
        una cadena o de una expresión regular. La cadena se construye a partir de la constante,
        para que ambas no puedan quedar distintas.

    Código correcto (expresión regular):
public static class PlayerNameRules
{
    public const int MinimumLength = 3;
    public const int MaximumLength = 16;

    private static readonly Regex _namePattern = new Regex(
        $"^[A-Za-z0-9_]{{{MinimumLength},{MaximumLength}}}$");
}

    Código incorrecto (expresión regular):
public static class PlayerNameRules
{
    public const int MinimumLength = 3;
    public const int MaximumLength = 16;

    private static readonly Regex _namePattern = new Regex(@"^[A-Za-z0-9_]{3,16}$");
}


2.11.      Propiedades
2.11.1.     Regla: PascalCase y acceso mínimo necesario
    Regla: Las propiedades se nombran en PascalCase con un sustantivo, frase nominal o adjetivo.
Si su valor no cambia después de construir el objeto, se expone solo get o se utiliza init; no se
agrega un set público innecesario (Microsoft, 2025f).
    Código correcto:
public sealed class PlayerProfile
{
    public PlayerProfile(string displayName)
    {
        DisplayName = displayName;
    }


                                                  19
    public string DisplayName { get; }
}

    Código incorrecto:
public sealed class PlayerProfile
{
    public string displayName { get; set; }
}


2.11.2.   Regla: modificación controlada con private set
    Regla: Cuando una propiedad cambia durante la partida, se mantiene el get público y
se restringe el set al menor nivel necesario. La modificación del estado de dominio se realiza
mediante un método que expresa la operación (Microsoft, 2025f).
    Código correcto:
public sealed class Player
{
    public int Score { get; private set; }

    public void AddScore(int points)
    {
        Score += points;
    }
}

    Código incorrecto:
public sealed class Player
{
    public int Score { get; set; }
}


2.11.3.   Regla: propiedad totalmente mutable en objetos de datos
   Regla: Cuando la clase solo transporta datos y no protege ninguna invariante de dominio —
una configuración, un objeto de transferencia (DTO) —, la propiedad expone get y set públicos
mediante una propiedad autoimplementada, sin envolverla en un método de acceso manual
(Microsoft, 2025f).
   Código correcto:
public sealed class GameSettings
{
    public int BoardSize { get; set; }
    public bool SoundEnabled { get; set; }
}

    Código incorrecto:
public sealed class GameSettings
{
    private int _boardSize;
    private bool _soundEnabled;

    public int GetBoardSize() => _boardSize;
    public void SetBoardSize(int value) => _boardSize = value;


                                             20
    public bool GetSoundEnabled() => _soundEnabled;
    public void SetSoundEnabled(bool value) => _soundEnabled = value;
}


2.11.4.   Regla: cuerpo de expresión solo en catálogos de diccionario
    Regla: El cuerpo de expresión (=>) en una propiedad se usa únicamente en un catálogo de
diccionario: una clase cuyas propiedades de solo lectura exponen, cada una, una entrada de un
diccionario de clave y valor, como un archivo de recursos o una tabla de configuración. Cada
propiedad consulta su entrada en cada acceso mediante un método privado que recibe la clave.
Fuera de un catálogo de diccionario, un valor que se calcula a partir de otros miembros se obtiene
mediante un método (Sección 2.2.1). Prohibido almacenar la entrada del diccionario en una
propiedad autoimplementada, ya sea con un inicializador ({ get; } =) o desde el constructor
(Microsoft, 2025f).
    Descripción: El cuerpo de expresión consulta el diccionario en cada acceso, por lo que
la propiedad refleja cualquier cambio de su contenido, como un cambio de idioma durante la
partida; una propiedad autoimplementada guarda la entrada una sola vez y la conserva aunque el
diccionario cambie.
    Código correcto: Archivo TextCatalog.cs:
public sealed class TextCatalog
{
    private readonly ITextDictionary _dictionary;

    public TextCatalog(ITextDictionary dictionary)
    {
        _dictionary = dictionary;
    }

    public string BoardLabel => GetEntry(nameof(BoardLabel));

    public string TurnLabel => GetEntry(nameof(TurnLabel));

    private string GetEntry(string key)
    {
        return _dictionary.FindEntry(key) ?? key;
    }
}

    Archivo GameSession.cs:
public sealed class GameSession
{
    private readonly List<Player> _players;

    public GameSession(List<Player> players)
    {
        _players = players;
    }

    public int CountActivePlayers()
    {
        return _players.Count(player => player.IsActive);
    }
}

    Código incorrecto: Archivo TextCatalog.cs:

                                               21
public sealed class TextCatalog
{
    private readonly ITextDictionary _dictionary;

    public TextCatalog(ITextDictionary dictionary)
    {
        _dictionary = dictionary;
        BoardLabel = GetEntry(nameof(BoardLabel));
        TurnLabel = GetEntry(nameof(TurnLabel));
    }

    public string BoardLabel { get; }

    public string TurnLabel { get; }

    private string GetEntry(string key)
    {
        return _dictionary.FindEntry(key) ?? key;
    }
}

    Archivo GameSession.cs:
public sealed class GameSession
{
    private readonly List<Player> _players;

    public GameSession(List<Player> players)
    {
        _players = players;
    }

    public int ActivePlayerCount => _players.Count(player => player.IsActive);
}

    Qué es un catálogo de diccionario: Una clase cuyo único propósito es exponer entradas de
un diccionario cuyo contenido puede cambiar mientras el programa se ejecuta, como un archivo de
recursos que cambia con el idioma. Una clase que guarda valores fijos, aunque vengan de un archivo
de recursos que no cambia con el idioma, no es un catálogo y usa propiedades autoimplementadas
(Sección 2.3.2).
    Excepción: Se permite el cuerpo de expresión fuera de un catálogo cuando un tercero exige
que el valor sea una propiedad y no un método:
     Interfaz: la interfaz declara la propiedad, como IAccountRepository Accounts { get;
     }.
      Enlace de datos: la vista enlaza el valor por el nombre de la propiedad, como en un
      modelo de vista (MVVM).
      Framework: el framework necesita la propiedad para funcionar, como un DbSet<T> de
      Entity Framework Core, cuya alternativa obligaría a usar el operador ! que prohíbe la
      Sección 9.4.1.
    Alcance: La regla trata el cuerpo de expresión de la propiedad completa (public int
Total =>...;). No aplica a los accesores escritos con cuerpo de expresión (get =>_value; y
set =>_value = value;), que equivalen a get { return _value; } y solo reenvían a un estado
interno.
    Código correcto (enlace de datos):

                                               22
public sealed class LobbyViewModel : ViewModel
{
    public bool IsWaiting
    {
        get => Get<bool>();
        set => Set(value);
    }

    [DependsOn(nameof(IsWaiting))]
    public bool IsReady => !IsWaiting;
}

    Código incorrecto (enlace de datos):
public sealed class LobbyViewModel : ViewModel
{
    public bool IsWaiting
    {
        get => Get<bool>();
        set => Set(value);
    }

    public bool IsReady()
    {
        return !IsWaiting;
    }
}


2.12.     Eventos
2.12.1.    Regla: verbo y tiempo verbal
   Regla: Los eventos se nombran en PascalCase con un verbo o frase verbal. El presente
progresivo indica que la acción está por ocurrir (TurnChanging) y el pasado indica que ya ocurrió
(TurnChanged); no se usan prefijos como Before o After (Microsoft, 2023a).
   Código correcto:
public class TurnManager
{
    public event EventHandler? TurnChanged;

    protected virtual void OnTurnChanged(EventArgs e)
    {
        TurnChanged?.Invoke(this, e);
    }
}

    Código incorrecto:
public class TurnManager
{
    public event EventHandler? AfterTurnChange;

    protected virtual void RaiseTurnChanged(EventArgs e)
    {
        AfterTurnChange?.Invoke(this, e);
    }
}



                                               23
2.12.2.   Regla: EventHandler y EventArgs
    Regla: Se utiliza EventHandler<TEventArgs> para eventos con datos. La clase de datos
termina en EventArgs; los parámetros del manejador se llaman sender y e; el método que eleva
el evento comienza con On (Microsoft, 2023b). El método que maneja un evento se nombra Handle
seguido del nombre del evento, como HandleTurnChanged; el prefijo On queda reservado para el
método que lo eleva.
    Descripción: Las clases base de los frameworks declaran métodos protected virtual con
prefijo On, como OnActivated(object sender, EventArgs args) en la clase Game de Mono-
Game. Un manejador llamado OnClientSizeChanged(object? sender, EventArgs e) en una
clase derivada se confunde con una sobrescritura de ese framework.
    Excepción: sender y e son la única excepción admitida a la regla general de nombres
descriptivos para parámetros (Sección 2.1): siguen la firma estándar del delegado EventHandler
de .NET y no se renombran ni se sustituyen por un descarte.
    Código correcto:
public event EventHandler<TurnChangedEventArgs>? TurnChanged;

private void HandleTurnChanged(object? sender, TurnChangedEventArgs e)
{
    UpdateCurrentPlayer(e.CurrentPlayer);
}

   Código incorrecto:
public event Action<Player>? TurnChange;

private void HandleTurnChange(Player player)
{
    UpdateCurrentPlayer(player);
}

    Excepción: Cuando una biblioteca externa define un evento con un delegado distinto de
EventHandler, como un Action sin parámetros, el manejador sigue la firma que impone la
biblioteca y no lleva sender ni e. Su nombre sí sigue el prefijo Handle. Los eventos que declara el
propio proyecto siempre usan EventHandler o EventHandler<TEventArgs>.
    Código correcto (evento de una biblioteca externa):
public LanguageSelector(ILocalizationService localization)
{
    localization.CurrentLanguageChanged += HandleCurrentLanguageChanged;
}

private void HandleCurrentLanguageChanged()
{
    RefreshLabels();
}

   Código incorrecto (evento de una biblioteca externa):
public LanguageSelector(ILocalizationService localization)
{
    localization.CurrentLanguageChanged += OnCurrentLanguageChanged;
}

private void OnCurrentLanguageChanged()
{
    RefreshLabels();
}


                                                24
2.13.     Parámetros de Tipo Genérico
2.13.1.    Regla: prefijo T y nombre descriptivo
    Regla: Un único parámetro completamente genérico puede llamarse T. Cuando su función o
restricción aporta significado, se usa un nombre descriptivo en PascalCase con prefijo T, como
TEntity o TSession (Microsoft, 2023c).
    Código correcto:
public interface IRepository<TEntity>
    where TEntity : Entity
{
    TEntity FindById(Guid id);
}

    Código incorrecto:
public interface IRepository<E>
    where E : Entity
{
    E FindById(Guid id);
}


2.14.     Sufijos por Responsabilidad
2.14.1.    Regla: sufijos definidos por .NET
    Regla: Se aplican los sufijos establecidos por las guías de diseño de .NET: Attribute para
atributos, EventArgs para datos de eventos, EventHandler para delegados de eventos, Callback
para otros delegados, Exception para excepciones, Dictionary para diccionarios y Collection
para colecciones personalizadas (Microsoft, 2023c).
    Código correcto:
public sealed class TurnChangedEventArgs : EventArgs
{
    public TurnChangedEventArgs(Player currentPlayer)
    {
        CurrentPlayer = currentPlayer;
    }

    public Player CurrentPlayer { get; }
}

    Código incorrecto:
public sealed class TurnChangedData : EventArgs
{
    public TurnChangedData(Player currentPlayer)
    {
        CurrentPlayer = currentPlayer;
    }

    public Player CurrentPlayer { get; }
}




                                             25
2.14.2.   Regla: sufijos arquitectónicos del proyecto
     Regla: Para expresar una responsabilidad arquitectónica real, el proyecto adopta los sufijos
Service, Repository, Controller, Factory, Provider, Validator, View, ViewModel, Store y
Client. Se prohíbe añadirlos cuando la clase no desempeña esa responsabilidad.
     Descripción: La lista es abierta: una clase puede usar otro sustantivo que describa lo que
hace, como Translator, Hasher o Generator. Lo que fija la lista es el significado de cada sufijo
listado: View y ViewModel son las dos partes de una pantalla con el patrón MVVM, Store guarda
y recupera datos locales del cliente, y Client se comunica con un servicio remoto. Un sufijo
genérico que no describe ninguna responsabilidad, como Manager, Handler o Helper, no se usa
en una clase.
     Código correcto:
public sealed class SaveGameService
{
    public void Save(GameState state)
    {
        Persist(state);
    }
}

   Código incorrecto:
public sealed class SaveGameManager
{
    public void Save(GameState state)
    {
        Persist(state);
    }
}


2.14.3.   Regla: nombre de la clase base al final de la clase derivada
    Regla: Una clase que hereda de una clase base de .NET o de un framework termina con
el nombre de esa clase base, como ArgumentOutOfRangeException, que hereda de Exception
(Microsoft, 2023c). Se exceptúan las clases base cuyo nombre no agrega información, como Game o
Panel, y los controles de la interfaz, que se nombran por lo que muestran.
    Descripción: El sufijo muestra la relación con la clase base sin abrir el archivo. Las guías de
.NET piden usar el criterio para no aplicarlo a ciegas: Button hereda de Control y no termina
en Control (Microsoft, 2023c).
    Código correcto:
public sealed class MoveNotationConverter : ValueConverter<Move, string>
{
    public MoveNotationConverter()
        : base(move => move.ToNotation(), notation => Move.FromNotation(notation))
    {
    }
}

   Código incorrecto:
public sealed class MoveNotation : ValueConverter<Move, string>
{
    public MoveNotation()
        : base(move => move.ToNotation(), notation => Move.FromNotation(notation))
    {
    }


                                                26
}

   Nota: Las lambdas de este ejemplo no se pueden sustituir por grupos de método, porque el
constructor de ValueConverter recibe árboles de expresión.

2.15.     Enumeraciones
2.15.1.   Regla: singular, o plural con [Flags]
    Regla: Una enumeración se nombra en PascalCase con un sustantivo en singular. Solo una
enumeración de indicadores, marcada con [Flags], se nombra en plural. El nombre no lleva los
sufijos Enum, Flag ni Flags, y sus valores no llevan prefijo (Microsoft, 2023c).
    Descripción: Una variable de una enumeración simple guarda un solo valor, por eso el tipo
va en singular: TurnState state. Una de indicadores puede guardar varios valores combinados,
por eso va en plural: TileMarkers markers.
    Código correcto:
public enum TurnState
{
    WaitingForRoll,
    Moving,
    Finished
}

    Código incorrecto:
public enum TurnStatesEnum
{
    TsWaitingForRoll,
    TsMoving,
    TsFinished
}


2.15.2.   Regla: valor None en las enumeraciones de indicadores
   Regla: Una enumeración de indicadores lleva el atributo [Flags], usa potencias de dos
para sus valores y nombra None a su valor cero, que significa que ningún indicador está activo
(Microsoft, 2023f).
   Descripción: Las potencias de dos permiten combinar los valores con el operador | sin que
se mezclen entre sí. El valor cero es el que tiene la enumeración cuando no se le asigna nada, así
que su nombre debe decir que no hay ningún indicador.
   Código correcto:
[Flags]
public enum TileMarkers
{
    None = 0,
    Highlighted = 1,
    Blocked = 2,
    Targeted = 4
}

    Código incorrecto:
public enum TileMarkers
{
    Highlighted,
    Blocked,


                                               27
     Targeted
}
```
