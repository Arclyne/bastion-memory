---
tipo: estandar-texto
seccion: 4
verificado: 2026-11-13 (copia literal de pdftotext del PDF v2.4; ver [[estandar-v2.4]])
---
# 4. Complejidad

```text
4.     Complejidad
4.1.     Profundidad de Anidamiento
4.1.1.    Regla: máximo tres niveles de anidamiento
    Regla: No se anidan más de tres niveles de estructuras de control por método. Cuenta como
nivel toda estructura que abre un bloque: if, else, for, foreach, while, do, switch, try, catch,
finally, using y lock. El cuerpo del método es el nivel 0; la primera estructura dentro de él es
el nivel 1. Un else o un catch ocupa el mismo nivel que su if o su try. Cuando se supera el
límite, se combinan condiciones o se extrae la parte interna a un método privado (McConnell,
2004).
    Código correcto:
public void ProcessTurn(Player player)
{
    if (player is null || !player.IsActive)
    {
        return;
    }

     ExecuteTurn(player);
}

private void ExecuteTurn(Player player)
{
    try
    {
        _board.MovePlayer(player);
    }
    catch (InvalidMoveException ex)
    {
        _logger.Warn($"Move rejected. Player={player.Name}.", ex);
    }
}

     Código incorrecto:
public void ProcessTurn(Player player)
{
    if (player is not null)
    {
        if (player.IsActive)
        {
            try
            {
                if (_board.HasSpaceFor(player))
                {
                    _board.MovePlayer(player);
                }
            }
            catch (InvalidMoveException ex)


                                              33
             {
                 _logger.Warn($"Move rejected. Player={player.Name}.", ex);
             }
         }
    }
}


4.2.     Salida Anticipada (Early Exit)
4.2.1.    Regla: cláusula de guarda con retorno anticipado
    Regla: Todo método descarta primero, con return anticipado, los casos que no requieren
procesar el resto de la lógica. Prohibido anidar la lógica principal dentro de un if que solo
comprueba una precondición de entrada.
    Descripción: La industria de videojuegos prefiere early exit sobre el principio clásico de
salida única (SESE): la lógica de una partida evalúa constantemente precondiciones, y anidar
el método completo dentro de ellas solo añade profundidad sin claridad. McConnell recomienda
salir de una rutina en cuanto se determina que no hay más trabajo que hacer (McConnell, 2004).
    Criterio arquitectónico: El early exit es obligatorio cuando la condición evaluada es una
precondición de entrada: un requisito que, de no cumplirse, hace innecesario procesar el resto del
método (un argumento inválido, un objeto inactivo, una colección vacía). En ese caso el retorno
anticipado sustituye al anidamiento y no es opcional. Cuando la condición forma parte de la
decisión de negocio central del método — no de una precondición de entrada —, este estándar no
exige fragmentarla en salidas adicionales; la elección entre un return adicional y una estructura
if/else se decide por legibilidad caso por caso.
    Código correcto:
public void ProcessTurn(Player player)
{
    if (!player.IsActive)
    {
        return;
    }

    ExecuteTurn(player);
}

    Código incorrecto:
public void ProcessTurn(Player player)
{
    if (player.IsActive)
    {
        ExecuteTurn(player);
    }
}


4.3.     Estructuras de Control
4.3.1.    Regla: llaves obligatorias en todo bloque
    Regla: Llaves {} obligatorias en toda estructura de control, incluso con una única instrucción;
regla IDE0011 (Microsoft, 2023e).
    Código correcto:




                                                34
if (diceRoll == MaximumFaceValue)
{
    GrantExtraTurn();
}

   Código incorrecto:
if (diceRoll == MaximumFaceValue)
    GrantExtraTurn();


4.3.2.   Regla: rama default obligatoria en switch
    Regla: Todo switch incluye una rama default explícita, y esa rama atiende solo los valores
no contemplados: lanza ArgumentOutOfRangeException cuando el valor llegó como argumento, o
InvalidOperationException cuando proviene del estado del objeto (McConnell, 2004). Prohibido
usar la rama default para representar uno de los valores válidos; cada valor válido tiene su propio
case.
    Descripción: McConnell recomienda que la rama default detecte errores en lugar de esconder
un caso legítimo (McConnell, 2004). Si la rama default devuelve uno de los resultados válidos,
un valor agregado después al enum y olvidado en el switch recibe ese resultado en silencio, sin
que ninguna prueba ni excepción lo revele.
    Excepción: En código de presentación (colores, estilos, iconos), la rama default puede
devolver un valor neutro cuando un valor desconocido no tiene consecuencias de negocio ni de
seguridad. El valor neutro es un miembro con nombre, nunca un literal, y no coincide con el
resultado de ningún otro case.
    Código correcto:
public TurnBadge SelectBadge(TurnState state)
{
    switch (state)
    {
        case TurnState.WaitingForRoll:
            return TurnBadge.Dice;
        case TurnState.Moving:
            return TurnBadge.Arrow;
        case TurnState.Finished:
            return TurnBadge.Flag;
        default:
            throw new ArgumentOutOfRangeException(nameof(state), state, "Unsupported
                turn state.");
    }
}

public Color SelectBorderColor(NoticeTone tone)
{
    switch (tone)
    {
        case NoticeTone.Error:
            return Palette.Error;
        case NoticeTone.Success:
            return Palette.Success;
        default:
            return Palette.Border;
    }
}



                                                35
    Código incorrecto:
public TurnBadge SelectBadge(TurnState state)
{
    switch (state)
    {
        case TurnState.WaitingForRoll:
            return TurnBadge.Dice;
        case TurnState.Moving:
            return TurnBadge.Arrow;
        default:
            return TurnBadge.Flag;
    }
}


4.4.     Reutilización de Código
4.4.1.    Regla: principio DRY
    Regla: Principio DRY (Don’t Repeat Yourself ): prohibido duplicar un bloque de código; si la
lógica se repite en dos o más métodos, se extrae a un método privado reutilizable.
    Descripción: Hunt y Thomas formulan DRY como que todo conocimiento debe tener
una única representación autorizada en el sistema (Hunt & Thomas, 2019). Fowler describe
la extracción a un método con nombre propio como la refactorización elemental para eliminar
duplicación (Fowler, 2018).
    Código correcto:
public sealed class MoveValidator
{
    public bool CanMoveTo(Player player, Tile destination)
    {
        return CanEnterTile(destination);
    }

    public bool CanTeleportTo(Player player, Tile destination)
    {
        return CanEnterTile(destination);
    }

    private bool CanEnterTile(Tile tile)
    {
        return IsWithinBoardBounds(tile) && !tile.IsOccupied;
    }

    private bool IsWithinBoardBounds(Tile tile)
    {
        return tile.Row >= 0 && tile.Column >= 0;
    }
}

    Código incorrecto:
public sealed class MoveValidator
{
    public bool CanMoveTo(Player player, Tile destination)
    {
        return destination.Row >= 0 && destination.Column >= 0 && !destination.
            IsOccupied;


                                              36
    }

    public bool CanTeleportTo(Player player, Tile destination)
    {
        return destination.Row >= 0 && destination.Column >= 0 && !destination.
            IsOccupied;
    }
}


4.4.2.   Regla: una sola definición para cada dato
    Regla: DRY también aplica a los datos: un valor que representa un mismo conocimiento (el
largo máximo de un correo, el tamaño de un hash, un margen de pantalla compartido) se declara
una sola vez, como constante en la capa más interna que lo necesita, y el resto de las capas hace
referencia a esa constante. Dos constantes con el mismo número pero distinto significado no son
duplicación y se mantienen separadas, porque cambiar una no debe cambiar la otra (Hunt &
Thomas, 2019).
    Descripción: Si la regla de dominio y la configuración de la base de datos declaran cada una
su propio largo máximo, basta con cambiar una de ellas para que el dominio acepte un valor que
la base de datos rechaza al guardar.
    Código correcto: Archivo PlayerRules.cs:
public static class PlayerRules
{
    public const int MaximumNicknameLength = 30;
}

    Archivo PlayerConfiguration.cs:
public sealed class PlayerConfiguration : IEntityTypeConfiguration<Player>
{
    public void Configure(EntityTypeBuilder<Player> builder)
    {
        builder.Property(player => player.Nickname).HasMaxLength(PlayerRules.
            MaximumNicknameLength);
    }
}

    Código incorrecto: Archivo PlayerRules.cs:
public static class PlayerRules
{
    public const int MaximumNicknameLength = 30;
}

    Archivo PlayerConfiguration.cs:
public sealed class PlayerConfiguration : IEntityTypeConfiguration<Player>
{
    private const int NicknameLength = 30;

    public void Configure(EntityTypeBuilder<Player> builder)
    {
        builder.Property(player => player.Nickname).HasMaxLength(NicknameLength);
    }
}




                                               37
4.5.     Operador Ternario
4.5.1.    Regla: solo para seleccionar un valor simple
    Regla: El operador condicional ?: se usa cuando una condición sencilla selecciona entre dos
valores sin efectos secundarios: ni la condición ni sus ramas llaman a un método que modifique
estado. Se prohíben operadores ternarios anidados; cuando existen más decisiones o acciones, se
utiliza una estructura if/else (Microsoft, 2026e).
    Código correcto:
Color nameColor = player.IsActive ? Palette.Active : Palette.Inactive;

    Código incorrecto:
Color nameColor = player.IsActive ? player.HasWon ? Palette.Winner : Palette.Active :
    Palette.Inactive;


4.6.     Complejidad Ciclomática
4.6.1.    Regla: máximo de 10 por método
   Regla: La complejidad ciclomática de cada método es como máximo 10. Una complejidad
superior se divide mediante métodos con una única responsabilidad (Microsoft, 2022d).
   Configuración: El analizador CA1502 viene desactivado de forma predeterminada, por lo
que el umbral solo se aplica al compilar si se completan los tres pasos siguientes:
    1. Crear CodeMetricsConfig.txt en la raíz de la solución con la línea CA1502: 10.
    2. Declararlo como archivo adicional en Directory.Build.props, para que llegue a todos los
       proyectos.
    3. Activar el diagnóstico en .editorconfig.
    Archivo Directory.Build.props:
<ItemGroup>
    <AdditionalFiles Include="$(MSBuildThisFileDirectory)CodeMetricsConfig.txt" />
</ItemGroup>

    Archivo .editorconfig:
dotnet_diagnostic.CA1502.severity = warning

    Código correcto:
public int CalculateScore(Player player, int baseScore)
{
    int score = baseScore;

     if (player.HasShield)
     {
         score = ApplyShieldBonus(score);
     }

     if (player.HasCompanion)
     {
         score = ApplyCompanionBonus(score);
     }

     return score;
}


                                               38
    Código incorrecto:
public int CalculateScore(Player player, int baseScore)
{
    int score = baseScore;

    if (player.HasShield)
    {
        score = ApplyShieldBonus(score);
    }

    if (player.HasCompanion)
    {
        score = ApplyCompanionBonus(score);
    }

    if (player.HasCrown)
    {
        score = ApplyCrownBonus(score);
    }

    if (player.HasMap)
    {
        score = ApplyMapBonus(score);
    }

    if (player.HasKey)
    {
        score = ApplyKeyBonus(score);
    }

    if (player.HasTreasure)
    {
        score = ApplyTreasureBonus(score);
    }

    if (player.HasPotion)
    {
        score = ApplyPotionBonus(score);
    }

    if (player.HasCompletedQuest)
    {
        score = ApplyQuestBonus(score);
    }

    if (player.IsInCastle)
    {
        score = ApplyCastleBonus(score);
    }

    if (player.IsFinalRound)
    {
        score = ApplyFinalRoundBonus(score);
    }

    return score;
}



                                              39
4.7.     Coincidencia de Patrones
4.7.1.    Regla: patrón de tipo en lugar de as con comprobación de nulo
    Regla: Para comprobar el tipo de un valor y usarlo convertido se emplea el patrón is Tipo
nombre, o is not Tipo nombre cuando forma parte de una cláusula de guarda (Sección 4.2).
Prohibido usar as seguido de una comprobación de nulo o una conversión explícita después de
is. La variable que introduce el patrón sigue las reglas de nombrado de variables (Sección 2.1)
(Microsoft, 2026i).
    Descripción: El patrón comprueba el tipo y declara la variable en una sola expresión, y el
compilador solo la considera asignada en la rama donde el patrón se cumple, por lo que no puede
usarse por error cuando la comprobación falla.
    Código correcto:
public void ApplyEffect(Tile tile)
{
    if (tile is not TrapTile trapTile)
    {
        return;
    }

     trapTile.Trigger();
}

     Código incorrecto:
public void ApplyEffect(Tile tile)
{
    TrapTile trapTile = tile as TrapTile;

     if (trapTile == null)
     {
         return;
     }

     trapTile.Trigger();
}
```
