---
tipo: estandar-texto
seccion: 5
verificado: 2026-11-13 (copia literal de pdftotext del PDF v2.4; ver [[estandar-v2.4]]); 5.3.1 y sus ejemplos cambiados el 2026-11-18 (D-084a)
---
# 5. Prácticas de Programación Funcional

```text
5.     Prácticas de Programación Funcional
5.1.     Expresiones Lambda
5.1.1.    Regla: solo para operaciones concisas de una línea
   Regla: Las lambdas (=>) solo para operaciones que quepan en una línea. Prohibido un cuerpo
de bloque con varias instrucciones (Martin, 2008).
   Código correcto:
_players.RemoveAll(player => !player.IsActive);

     Código incorrecto:
_players.RemoveAll(player =>
{
    bool shouldRemove = !player.IsActive;
    _logger.Debug($"Player evaluated. Player={player.Name}.");
    return shouldRemove;
});



                                              40
5.1.2.   Regla: contextos en los que se prohíbe una expresión lambda
    Regla: Se prohíbe la expresión lambda en tres contextos: la suscripción a un evento que deba
cancelarse, la asignación sobre el estado capturado y la lambda escrita dentro de otra lambda.
    Descripción: Las lambdas se retiran del código sobre todo por pérdida de legibilidad,
dificultad para depurar y degradación del rendimiento (Zheng et al., 2021); los tres contextos
prohibidos concentran esas causas en defectos que el compilador no señala.
    Prohibido — evento cuya suscripción deba cancelarse: Cada aparición de una lambda
crea un delegado distinto, por lo que -= no retira lo que registró +=; el manejador se declara como
método con nombre (Microsoft, 2015).
    Código correcto:
public sealed class ScoreBoardView
{
    private readonly ITurnManager _turnManager;

    public ScoreBoardView(ITurnManager turnManager)
    {
        _turnManager = turnManager;
    }

    public void Attach()
    {
        _turnManager.TurnChanged += HandleTurnChanged;
    }

    public void Detach()
    {
        _turnManager.TurnChanged -= HandleTurnChanged;
    }

    private void HandleTurnChanged(object? sender, TurnChangedEventArgs e)
    {
        Render(e.CurrentPlayer);
    }

    private void Render(Player currentPlayer)
    {
    }
}

    Código incorrecto:
public sealed class ScoreBoardView
{
    private readonly ITurnManager _turnManager;

    public ScoreBoardView(ITurnManager turnManager)
    {
        _turnManager = turnManager;
    }

    public void Attach()
    {
        _turnManager.TurnChanged += (sender, e) => Render(e.CurrentPlayer);
    }

    public void Detach()
    {


                                                41
         _turnManager.TurnChanged -= (sender, e) => Render(e.CurrentPlayer);
    }

    private void Render(Player currentPlayer)
    {
    }
}

    Prohibido — asignación sobre el estado capturado: El cuerpo de una lambda solo lee
sus entradas y devuelve un resultado; para modificar una variable capturada o un campo se usa
foreach o un método con nombre (Microsoft, 2026g).
    Código correcto:
public int CalculateTotalScore()
{
    return _players.Sum(player => player.Score);
}

    Código incorrecto:
public int CalculateTotalScore()
{
    int totalScore = 0;
    _players.ForEach(player => totalScore += player.Score);
    return totalScore;
}

    Prohibido — lambda dentro de otra lambda: La lambda interior se extrae a un método
privado y se pasa como grupo de método (Sección 5.2).
    Código correcto:
public IReadOnlyList<Player> FindPlayersWithWinningCard()
{
    IEnumerable<Player> winners = _players.Where(HasWinningCard);
    return [.. winners];
}

private bool HasWinningCard(Player player)
{
    return player.Cards.Any(card => card.IsWinning);
}

    Código incorrecto:
public IReadOnlyList<Player> FindPlayersWithWinningCard()
{
    IEnumerable<Player> winners = _players.Where(player => player.Cards.Any(card => card.IsWinning));
    return [.. winners];
}



5.2.     Referencias a Métodos
5.2.1.    Regla: grupo de método sobre lambda de reenvío
    Regla: Si una lambda solo reenvía sus argumentos a otro método, se usa el grupo de método
(el nombre directamente) en vez de la lambda (Microsoft, 2024).
    Código correcto:
_players.ForEach(RegisterPlayerScore);

    Código incorrecto:
_players.ForEach(player => RegisterPlayerScore(player));



                                                       42
5.3.     Consultas LINQ a Objetos
5.3.1.    Regla: un operador por línea y materialización aparte
    Regla: En LINQ a objetos, una consulta que devuelve una secuencia se guarda en una variable
IEnumerable<T> con nombre en plural (Sección 2.1.2) y solo se materializa cuando se necesita
una colección, en una instrucción aparte con la expresión de colección [.. consulta] (Sección
3.4.2); un diccionario se materializa con new Dictionary<TKey, TValue>(consulta), porque la
expresión de colección no admite diccionarios con elementos. Si la consulta encadena
dos o más operadores, como Where, Select, OrderBy o Chunk, la colección de origen queda en la
primera línea y cada operador va en su propia línea, con un nivel más de indentación (Sección
3.5). Prohibido escribir en una sola línea una cadena de dos o más operadores, así como encadenar
ToList() o ToArray() al final de la consulta (Microsoft, 2025h).
    Descripción: Los operadores que devuelven una secuencia no se ejecutan al declarar la
consulta, sino cuando esta se recorre (Microsoft, 2025h); materializarla aparte deja a la vista
ese momento, y un operador por línea permite leerla como una lista de pasos. Se necesita una
colección cuando el resultado se devuelve o se guarda como lista, o se recorre más de una vez;
una secuencia que se recorre una sola vez con foreach no se materializa.
    Excepción: Una cadena que termina en un operador de valor único, como Count, Any, First
o Sum, se ejecuta en ese momento y devuelve un valor, no una secuencia: conserva un operador
por línea, pero no se guarda en IEnumerable<T> ni se materializa. Una consulta de EF Core
sobre IQueryable<T> no es LINQ a objetos, porque se traduce a SQL (Microsoft, 2025h), y se
rige solo por la Sección 3.5.
    Código correcto:
public IReadOnlyList<string> GetActivePlayerNames()
{
    IEnumerable<string> activeNames = _players
        .Where(player => player.IsActive)
        .Select(player => player.Name);
    return [.. activeNames];
}

public void NotifyWaitingPlayers()
{
    IEnumerable<Player> waitingPlayers = _players
        .Where(player => !player.IsActive)
        .OrderBy(player => player.Name);
    foreach (Player player in waitingPlayers)
    {
        NotifyWaiting(player);
    }
}

    Código incorrecto:
public IReadOnlyList<string> GetActivePlayerNames()
{
    return _players.Where(player => player.IsActive).Select(player => player.Name).ToList();
}

public void NotifyWaitingPlayers()
{
    IEnumerable<Player> waitingPlayers = _players
        .Where(player => !player.IsActive)
        .OrderBy(player => player.Name)
        .ToList();
    foreach (Player player in waitingPlayers)
    {
        NotifyWaiting(player);
    }
}




                                                      43
```
