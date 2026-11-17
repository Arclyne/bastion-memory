---
tipo: estandar-texto
seccion: 10
verificado: 2026-11-13 (copia literal de pdftotext del PDF v2.4; ver [[estandar-v2.4]])
---
# 10. Inyección de Dependencias

```text
10.       Inyección de Dependencias
    Una clase no construye ni localiza los servicios que usa: los recibe ya construidos. Así cada
clase puede probarse sustituyendo sus dependencias por dobles de prueba, y la decisión de qué
implementación concreta se usa queda en un único lugar del programa (Martin, 2008; van Deursen
& Seemann, 2019).

10.1.     Inyección por Constructor
10.1.1.    Regla: inyección por constructor y dependencia de abstracciones
    Regla: Toda clase que dependa de un servicio externo recibe esa dependencia por constructor,
declarada mediante una interfaz o una clase abstracta, en lugar de instanciarla dentro de la propia
clase. Un servicio externo es todo colaborador que realiza entrada o salida (red, disco, base de
datos), que guarda estado compartido entre clases o cuyo resultado no es determinista, como el
tiempo o el azar.



                                                58
    Descripción: Principio de inversión de dependencias de Martin: los módulos de alto nivel
dependen de abstracciones, no de módulos de bajo nivel (Martin, 2008). Las guías de .NET piden
además evitar instanciar directamente las clases de las que depende un servicio, porque eso acopla
el código a una implementación concreta (Microsoft, 2026i).
    Excepciones:

      Una clase de la capa de adaptadores puede recibir un tipo concreto del framework que ella
      misma adapta, como un DbContext de Entity Framework Core en un repositorio.

      El ILog de log4net se obtiene en un campo private static readonly con LogManager.GetLogger(typeof(
      uno por clase (Sección 11), y no se inyecta.

    Código correcto:
public sealed class TurnManager
{
    private readonly IDiceRoller _diceRoller;

    public TurnManager(IDiceRoller diceRoller)
    {
        _diceRoller = diceRoller;
    }

    public int PlayTurn()
    {
        return _diceRoller.Roll();
    }
}

    Código incorrecto:
public sealed class TurnManager
{
    private readonly DiceRoller _diceRoller;

    public TurnManager()
    {
        _diceRoller = new DiceRoller();
    }

    public int PlayTurn()
    {
        return _diceRoller.Roll();
    }
}


10.2.     Raíz de Composición
10.2.1.    Regla: los servicios se construyen solo en la raíz de composición
    Regla: Los servicios externos se crean con new o se registran en el contenedor únicamente
en la raíz de composición: el punto de arranque de cada aplicación, como Program, las clases de
registro de servicios del servidor o el método de inicialización del juego en el cliente. Ninguna
otra clase crea los servicios que consume.
    Descripción: La raíz de composición es el único lugar de la aplicación donde se arma el grafo
de objetos; concentrarla ahí permite cambiar una implementación sin tocar las clases que la usan
(van Deursen & Seemann, 2019).


                                               59
   Excepción: Una clase puede crear las partes que forman parte de ella y comparten su tiempo
de vida, como una unidad de trabajo que crea sus repositorios sobre el mismo contexto de base
de datos.
   Código correcto:
public sealed class BoardGame : Game
{
    private TurnManager? _turnManager;

    protected override void Initialize()
    {
        _turnManager = new TurnManager(new DiceRoller());
        base.Initialize();
    }
}

    Código incorrecto:
public sealed class MatchScreen
{
    private readonly TurnManager _turnManager = new TurnManager(new DiceRoller());
}


10.3.     Localizador de Servicios
10.3.1.    Regla: prohibido pedir servicios al contenedor
    Regla: Prohibido obtener una dependencia llamando a GetService o GetRequiredService
dentro de una clase; la dependencia se declara en el constructor.
    Descripción: El localizador de servicios oculta las dependencias de una clase: su constructor
ya no dice qué necesita y una dependencia faltante solo falla al ejecutar el método (van Deursen
& Seemann, 2019). Las guías de .NET recomiendan evitar este patrón cuando se puede usar
inyección (Microsoft, 2026i).
    Excepción: En la frontera de red, donde el framework crea el servicio y no permite inyectar
dependencias con un ámbito por llamada, se recibe IServiceScopeFactory por constructor, se
crea un ámbito por llamada y se resuelve de él el servicio de aplicación que atiende la petición
(Microsoft, 2026i).
    Código correcto:
public sealed class MatchService
{
    private readonly IMatchRepository _matchRepository;

    public MatchService(IMatchRepository matchRepository)
    {
        _matchRepository = matchRepository;
    }

    public Match FindMatch(Guid matchId)
    {
        return _matchRepository.FindById(matchId);
    }
}

    Código incorrecto:
public sealed class MatchService
{


                                               60
    private readonly IServiceProvider _services;

    public MatchService(IServiceProvider services)
    {
        _services = services;
    }

    public Match FindMatch(Guid matchId)
    {
        IMatchRepository matchRepository = _services.GetRequiredService<
            IMatchRepository>();
        return matchRepository.FindById(matchId);
    }
}


10.4.     Proveedor de Tiempo
10.4.1.   Regla: el tiempo se obtiene de un TimeProvider inyectado
    Regla: Prohibido leer el reloj del sistema con DateTime.Now, DateTime.UtcNow o
DateTimeOffset.UtcNow fuera de la raíz de composición. Una clase que necesita la hora actual
recibe un TimeProvider por constructor y llama a GetUtcNow(). En la raíz de composición se
registra TimeProvider.System.
    Descripción: El tiempo es un resultado no determinista y, por lo tanto, un servicio externo
(Sección 10.1). TimeProvider es la abstracción del tiempo que ofrece .NET; con ella el código
se vuelve predecible y una prueba puede fijar la hora mediante FakeTimeProvider (Microsoft,
2026j).
    Código correcto:
public sealed class TurnTimer
{
    private readonly TimeProvider _timeProvider;

    public TurnTimer(TimeProvider timeProvider)
    {
        _timeProvider = timeProvider;
    }

    public bool HasTurnExpired(DateTimeOffset turnDeadline)
    {
        return _timeProvider.GetUtcNow() > turnDeadline;
    }
}

    Código incorrecto:
public sealed class TurnTimer
{
    public bool HasTurnExpired(DateTimeOffset turnDeadline)
    {
        return DateTimeOffset.UtcNow > turnDeadline;
    }
}




                                              61
```
