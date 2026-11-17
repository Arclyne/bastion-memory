---
tipo: estandar-texto
seccion: 11
verificado: 2026-11-13 (copia literal de pdftotext del PDF v2.4; ver [[estandar-v2.4]])
---
# 11. Bitácoras

```text
11.       Bitácoras
    Todo registro de eventos del juego se realiza con log4net mediante una dependencia ILog,
representada como _logger. Los mensajes forman parte del programa y se redactan siempre en
inglés (Apache Software Foundation, s. f.-a).

11.1.     Niveles de Registro
11.1.1.    Regla: elección del nivel según la severidad del evento
   Regla: Cada mensaje se registra mediante el método de log4net que corresponde a su severidad,
de menor a mayor (Apache Software Foundation, s. f.-a):

      Debug: información útil en desarrollo (resultado intermedio de un cálculo).

      Info: flujo normal del juego (inicio de partida, cambio de turno).

      Warn: anomalía que no impide continuar (movimiento inválido).

      Error: fallo que impide completar una operación, pero permite que el proceso continúe.

      Fatal: fallo irrecuperable que obliga a terminar la sesión o el proceso.

    Regla: excepción y severidad. El objeto de excepción se adjunta como segundo parámetro
de la llamada de registro únicamente en Warn, Error y Fatal, los niveles que se originan en un
bloque catch; Debug e Info documentan flujo normal y no reciben una excepción. Toda excepción
que se captura y se maneja sin volver a lanzarse se registra, como mínimo, en Warn. Cuando el
catch solo traduce la excepción a otro tipo y la relanza (Sección 9.2), el registro ocurre en el
punto donde finalmente se maneja, no en cada traducción intermedia. Una excepción que obliga a
finalizar la sesión o el proceso completo — no solo la operación en curso — se registra en Fatal.
    Código correcto:
public sealed class TurnManager
{
    public void StartTurn(Player player)
    {
        _logger.Info($"Turn started. Player={player.Name}.");
    }

    public void RejectMove(Player player, Tile destination)
    {
        _logger.Warn($"Move rejected. Player={player.Name}; Destination={destination}."
            );
    }

    public void AbortSession(GameSession session, Exception ex)
    {
        _logger.Fatal($"Session aborted. SessionId={session.Id}.", ex);
    }
}

    Código incorrecto:
public sealed class TurnManager
{
    public void StartTurn(Player player)
    {
        _logger.Error($"Turn started. Player={player.Name}.");


                                                62
    }

    public void RejectMove(Player player, Tile destination)
    {
        _logger.Error($"Move rejected. Player={player.Name}; Destination={destination}.
            ");
    }

    public void AbortSession(GameSession session, Exception ex)
    {
        _logger.Debug($"Session aborted. SessionId={session.Id}.", ex);
    }
}


11.2.     Restricciones
11.2.1.    Regla: prohibido Console.WriteLine como bitácora
    Regla: Prohibido Console.WriteLine, Console.Error.WriteLine o Debug.Print para re-
gistrar eventos del juego; todo registro pasa por el colaborador de registro del proyecto (McConnell,
2004).
    Código correcto:
public void SaveGameState(GameState state)
{
    try
    {
        _repository.Save(state);
    }
    catch (IOException ex)
    {
        _logger.Error($"Save game failed. SessionId={state.SessionId}.", ex);
    }
}

    Código incorrecto:
public void SaveGameState(GameState state)
{
    try
    {
        _repository.Save(state);
    }
    catch (IOException)
    {
        Console.WriteLine($"Save game failed. SessionId={state.SessionId}.");
    }
}


11.3.     Formato de Mensajes
11.3.1.    Regla: acción, contexto y excepción separada
    Regla: Todo mensaje comienza con una oración breve en inglés que identifica la acción o el
resultado. El contexto variable se agrega como pares Key=Value separados por punto y coma.
Una excepción se entrega en el parámetro correspondiente de log4net y no se concatena su



                                                 63
propiedad Message. El PatternLayout agrega fecha, hilo, nivel y nombre del logger (Apache
Software Foundation, s. f.-b).
    Código correcto:
_logger.Error(
    $"Save game failed. SessionId={state.SessionId}; PlayerId={player.Id}.",
    ex);

   Código incorrecto:
_logger.Error("Error: " + ex.Message);
```
