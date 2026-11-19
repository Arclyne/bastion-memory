---
tipo: estandar-texto
seccion: 3
verificado: 2026-11-13 (copia literal de pdftotext del PDF v2.4; ver [[estandar-v2.4]]); 3.4.2 agregada el 2026-11-18 (D-084a)
---
# 3. Estilo de Codificación

```text
3.     Estilo de Codificación
3.1.     Indentación
3.1.1.    Regla: cuatro espacios por nivel
   Regla: Se adopta la configuración predeterminada de formato de C#: cada nivel de indentación
usa cuatro espacios, el ancho de tabulación es cuatro y no se insertan caracteres de tabulación.
La configuración equivalente es indent_style = space, indent_size = 4 y tab_width = 4
(Microsoft, 2025e).
   Código correcto:
public int RollDice()
{
    const int MinimumFaceValue = 1;
    const int MaximumFaceValue = 6;
    const int ExclusiveMaximumFaceValue = MaximumFaceValue + 1;
    int faceValue = Random.Shared.Next(MinimumFaceValue, ExclusiveMaximumFaceValue);

     if (faceValue == MaximumFaceValue)
     {
         return faceValue + BonusRoll();
     }

     return faceValue;
}

     Código incorrecto:
public int RollDice()
{
  const int MinimumFaceValue = 1;
  const int MaximumFaceValue = 6;
  const int ExclusiveMaximumFaceValue = MaximumFaceValue + 1;
  int faceValue = Random.Shared.Next(MinimumFaceValue, ExclusiveMaximumFaceValue);

    if (faceValue == MaximumFaceValue)
    {
        return faceValue + BonusRoll();
    }

    return faceValue;
}


3.2.     Espaciado
3.2.1.    Regla: espacio entre palabra reservada y paréntesis, y línea en blanco entre
          miembros
    Regla: Un espacio entre palabra reservada (if, for, while, switch) y su paréntesis, y
alrededor de cada operador binario. Una línea en blanco entre métodos o propiedades consecutivos
(Microsoft, 2025e).
    Código correcto:


                                              28
public sealed class ScoreBoard
{
    private int _totalScore;

    public void AddPoints(int points)
    {
        if (points > 0)
        {
            _totalScore = _totalScore + points;
        }
    }

    public int GetTotalScore()
    {
        return _totalScore;
    }
}

    Código incorrecto:
public sealed class ScoreBoard
{
    private int _totalScore;
    public void AddPoints(int points)
    {
        if(points>0)
        {
            _totalScore=_totalScore+points;
        }
    }
    public int GetTotalScore()
    {
        return _totalScore;
    }
}


3.3.     Posición de las Llaves
3.3.1.    Regla: estilo Allman
    Regla: Llave de apertura y cierre en su propia línea, alineadas con el bloque que delimitan.
Prohibido que else, catch o finally compartan línea con la llave anterior. La misma disposición
aplica a los inicializadores de objetos y colecciones: new y el tipo en una línea y la llave de apertura
en la siguiente (Microsoft, 2025e).
    Código correcto:
if (player.IsActive)
{
    ExecuteTurn(player);
}
else
{
    SkipTurn(player);
}

var settings = new MatchSettings
{


                                                  29
     PlayerCount = MaximumPlayers,
     TurnSeconds = DefaultTurnSeconds,
};

     Código incorrecto:
if (player.IsActive) {
    ExecuteTurn(player);
} else {
    SkipTurn(player);
}

var settings = new MatchSettings {
    PlayerCount = MaximumPlayers,
    TurnSeconds = DefaultTurnSeconds,
};


3.4.     Uso de var
3.4.1.    Regla: solo cuando el tipo es evidente
    Regla: Se usa var solo cuando el tipo es evidente en el lado derecho de la asignación. El tipo
es evidente únicamente en estos casos:

       una construcción con new y el nombre del tipo, con argumentos o con inicializador;

       una conversión explícita (T)expresion o el operador as T;

       una llamada a un método estático que devuelve el mismo tipo que lo declara, como
       Board.Create(...), que devuelve Board.

    En cualquier otro caso se escribe el tipo explícito: tipos integrados (int, string, bool y sus
arreglos), aunque se construyan con new, y llamadas a métodos cuyo tipo de retorno no aparece
en la expresión. Esta definición coincide con la que aplican las reglas IDE0007 e IDE0008 con
la opción csharp_style_var_when_type_is_apparent, de modo que la compilación la verifica
(Microsoft, 2022c).
    Código correcto:
var player = new Player("Alice");
var board = Board.Create(BoardSize);
var human = participant as HumanPlayer;
int remainingTurns = CalculateRemainingTurns();
string[] playerNames = new string[MaximumPlayers];

     Código incorrecto:
Player player = new Player("Alice");
Board board = Board.Create(BoardSize);
var remainingTurns = CalculateRemainingTurns();
var playerNames = new string[MaximumPlayers];

3.4.2.    Regla: expresión de colección para crear una colección
    Regla: Una colección vacía se crea con la expresión de colección [] y una con elementos
conocidos con [a, b], en lugar de new List<T>(), new Dictionary<TKey, TValue>(), new HashSet<T>()
o un inicializador como new List<T> { a }. Para llenarla con todos los elementos de otra
colección o de una consulta se usa el operador de propagación .., que se lee «todos los
elementos de»: [.. consulta] (Sección 5.3.1). El tipo queda escrito donde se declara el campo,
la propiedad, el parámetro o el valor de retorno; en una variable local se escribe el tipo
explícito, porque var no puede deducir el tipo de una expresión de colección (Sección 3.4.1).
    Descripción: La expresión de colección evita repetir tipos largos, como
Dictionary<int, List<Player>>, y usa la misma sintaxis para listas, conjuntos, diccionarios y
arreglos. El operador .. es el mismo que usan otros lenguajes para propagar una colección
(... en JavaScript, * en Python). No cambia el comportamiento: con destino List<T>, [] equivale
a new List<T>().
    Código correcto:
private readonly Dictionary<int, List<Player>> _playersByTeam = [];

List<Card> drawnCards = [];
IEnumerable<Player> winners = _players.Where(HasWinningCard);
return [.. winners];

     Código incorrecto:
private readonly Dictionary<int, List<Player>> _playersByTeam = new Dictionary<int, List<Player>>();

var drawnCards = new List<Card>();
IEnumerable<Player> winners = _players.Where(HasWinningCard);
return new List<Player>(winners);


3.5.     División de Líneas
3.5.1.    Regla: cómo continuar una instrucción en varias líneas
   Regla: El estándar no fija una longitud máxima de línea. Cuando una instrucción se divide
en varias líneas para que se lea mejor, se siguen estas convenciones:


                                               30
       un operador binario (&&, ||, ??, +) se coloca al inicio de la línea de continuación, no al final
       de la anterior;

       en una cadena de llamadas, cada .Metodo() va en su propia línea;

       si los argumentos de una llamada se dividen, la línea termina en el paréntesis de apertura y
       cada argumento va en su propia línea;

       la llamada : base(...) o : this(...) va en su propia línea, debajo de la firma del
       constructor;

       cada línea de continuación lleva un nivel más de indentación que la línea donde empieza la
       instrucción.

    La opción dotnet_style_operator_placement_when_wrapping = beginning_of_line apli-
ca la primera convención en el editor (Microsoft, 2025e).
    Código correcto:
bool canMove = player.IsActive
    && board.IsInside(target)
    && !board.IsOccupied(target);

builder.Property(piece => piece.Kind)
    .HasMaxLength(KindLength)
    .IsUnicode(false);

throw Reject(
    new MoveLog(MoveResult.Blocked, attempt, player.PlayerId),
    MoveRejection.Blocked);

   Código incorrecto:
bool canMove = player.IsActive &&
    board.IsInside(target) &&
    !board.IsOccupied(target);

builder.Property(piece => piece.Kind).HasMaxLength(KindLength)
    .IsUnicode(false);

throw Reject(new MoveLog(MoveResult.Blocked, attempt,
    player.PlayerId), MoveRejection.Blocked);


3.6.     Atributos
3.6.1.    Regla: un atributo por línea, encima del elemento
    Regla: Cada atributo se escribe entre sus propios corchetes y en su propia línea, encima del
elemento al que se aplica. No se agrupan varios atributos en unos mismos corchetes ni se escribe
el atributo en la misma línea que la declaración (Microsoft, 2025e).
    Código correcto:
[DataContract]
public sealed class MoveRequest
{
    [DataMember]
    public int PieceId { get; set; }
}

   Código incorrecto:

                                                  31
[DataContract] public sealed class MoveRequest
{
    [DataMember, Required]
    public int PieceId { get; set; }
}


3.7.     Controles de Gum
3.7.1.    Regla: inicializador de objeto al crear un control de Gum
    Regla: Un control de Gum que se crea con new, como StackPanel, Panel, Label o Button,
se declara con var (Sección 3.4) y recibe en un inicializador de objeto las propiedades cuyo valor
se conoce al crearlo: tamaño, unidades, posición, separación y texto. Prohibido construirlo vacío
y asignarle esas propiedades una por una en las instrucciones siguientes (Microsoft, 2026k). Con
dotnet_style_object_initializer = true:warning, la regla IDE0017 señala en la compilación
las asignaciones escritas justo después de la construcción (Microsoft, 2023g).
    Descripción: El inicializador reúne en un solo bloque cómo es el control al aparecer. Después
de él van las llamadas a métodos (AddChild, SetBinding, Anchor, Dock) y las suscripciones a
eventos, que un inicializador no admite, y las propiedades del objeto Visual del control, que no
se anidan en el inicializador.
    Excepción: Anchor reescribe la posición del control y Dock reescribe su posición y su tamaño,
por lo que una propiedad que deba quedar sobre el anclaje, como el desplazamiento X de un control
anclado a la izquierda, se asigna después de la llamada. Un control que devuelve un método de
fábrica ya está creado: sus propiedades se asignan después de la llamada y su declaración sigue la
Sección 3.4.
    Código correcto:
var menu = new StackPanel
{
    Width = MenuWidth,
    WidthUnits = DimensionUnitType.Absolute,
    Spacing = ButtonSpacing,
};
menu.Anchor(Anchor.Left);
menu.X = MenuX;

var playButton = new Button
{
    Text = Strings.PlayButton,
    Width = ButtonWidth,
    Height = ButtonHeight,
};
playButton.Click += HandleClick;
menu.AddChild(playButton);

   Código incorrecto:
var menu = new StackPanel();
menu.Width = MenuWidth;
menu.WidthUnits = DimensionUnitType.Absolute;
menu.Spacing = ButtonSpacing;
menu.Anchor(Anchor.Left);
menu.X = MenuX;

var playButton = new Button();
playButton.Text = Strings.PlayButton;


                                               32
playButton.Width = ButtonWidth;
playButton.Height = ButtonHeight;
playButton.Click += HandleClick;
menu.AddChild(playButton);
```
