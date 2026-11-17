---
tipo: estandar-texto
seccion: 6
verificado: 2026-11-13 (copia literal de pdftotext del PDF v2.4; ver [[estandar-v2.4]])
---
# 6. Estructura de Archivos

```text
6.     Estructura de Archivos
6.1.    Regla: un tipo de nivel superior por archivo
    Regla: Cada archivo contiene exactamente un tipo de nivel superior: clase, interfaz, record,
struct, enum o delegate. El nombre del archivo coincide con el del tipo; en un tipo genérico
se omiten los parámetros de tipo, de modo que ServiceChannel<TContract> se guarda en
ServiceChannel.cs (McConnell, 2004).
    Tipos anidados: Prohibido declarar un tipo anidado visible fuera de la clase que lo contiene
(public, internal o protected); un tipo que otras clases usan se declara en su propio archivo.
Se permite un tipo anidado private que solo sirve a la clase que lo contiene. El analizador CA1034
detecta los tipos anidados visibles (Microsoft, s. f.-a).
    Código generado: Los archivos que produce una herramienta, como Strings.Designer.cs
a partir de un archivo .resx, quedan exentos de esta sección porque se regeneran en cada cambio
y cualquier corrección manual se pierde.
    Código correcto (archivo TurnManager.cs):
namespace BoardGame.Logic;

public sealed class TurnManager
{
}

     Código incorrecto (archivo GameLogic.cs):
namespace BoardGame.Logic;

public sealed class TurnManager
{
    public sealed class TurnSnapshot
    {
    }
}

public sealed class ScoreBoard
{
}


6.2.    Regla: orden de los elementos dentro de la clase
   Regla: Orden fijo dentro de una clase: constantes, campos estáticos, campos de instancia,
constructores, propiedades estáticas, propiedades de instancia, eventos, métodos y, al final, tipos
anidados privados (McConnell, 2004).
   Código correcto:
public sealed class DiceRoller
{
    private const int MinimumFaceValue = 1;

     private static readonly Random _random = Random.Shared;

     private readonly int _maximumFaceValue;

     public DiceRoller(int maximumFaceValue)
     {
         _maximumFaceValue = maximumFaceValue;
     }


                                                44
    public static int StandardFaceCount { get; } = 6;

    public int LastRoll { get; private set; }

    public event EventHandler? DiceRolled;

    public int Roll()
    {
        LastRoll = _random.Next(MinimumFaceValue, _maximumFaceValue + 1);
        DiceRolled?.Invoke(this, EventArgs.Empty);
        return LastRoll;
    }
}

    Código incorrecto:
public sealed class DiceRoller
{
    public event EventHandler? DiceRolled;

    public int Roll()
    {
        LastRoll = _random.Next(MinimumFaceValue, _maximumFaceValue + 1);
        DiceRolled?.Invoke(this, EventArgs.Empty);
        return LastRoll;
    }

    private readonly int _maximumFaceValue;

    public int LastRoll { get; private set; }

    public DiceRoller(int maximumFaceValue)
    {
        _maximumFaceValue = maximumFaceValue;
    }

    public static int StandardFaceCount { get; } = 6;

    private const int MinimumFaceValue = 1;
    private static readonly Random _random = Random.Shared;
}


6.3.    Regla: orden y continuidad de directivas using
    Regla: Las directivas using se colocan fuera del espacio de nombres en un único bloque sin
líneas en blanco. Primero van los espacios de nombres de System, en orden alfabético; después,
todos los demás en un solo grupo alfabético, sin separar bibliotecas de terceros y espacios de
nombres propios del proyecto (Microsoft, 2022a; Microsoft, 2022b). El orden alfabético no distingue
mayúsculas de minúsculas, por lo que log4net va después de CoreWCF y antes de Microsoft.
    Descripción: Es el orden que produce el comando de ordenar using del editor con la
configuración siguiente, de modo que no requiere revisión manual:

       csharp_using_directive_placement = outside_namespace
       dotnet_sort_system_directives_first = true
       dotnet_separate_import_directive_groups = false

                                                45
     Código correcto:
using System;
using System.Collections.Generic;
using BoardGame.Core;
using log4net;
using Microsoft.Extensions.DependencyInjection;

namespace BoardGame.Services;

     Código incorrecto:
using log4net;

using System.Collections.Generic;
using Microsoft.Extensions.DependencyInjection;
using BoardGame.Core;
using System;

namespace BoardGame.Services;


6.4.    Regla: agrupación mediante espacios de nombres
     Regla: Todo tipo pertenece a un espacio de nombres que coincide con la carpeta en la que está
el archivo, a partir de la carpeta raíz del proyecto, y que refleja la responsabilidad del archivo. Se
usa la declaración de ámbito de archivo y un solo espacio de nombres por archivo; por ejemplo, los
servicios de guardado en la carpeta Services/Saves se agrupan bajo BoardGame.Services.Saves
(Microsoft, 2026d).
     Descripción: La compilación verifica ambas condiciones: IDE0161 exige la declaración de
ámbito de archivo y IDE0130 exige que el espacio de nombres coincida con la carpeta (Microsoft,
s. f.-b; Microsoft, s. f.-c). La configuración equivalente es:

       csharp_style_namespace_declarations = file_scoped

       dotnet_style_namespace_match_folder = true

     Código correcto (archivo Services/Saves/SaveGameService.cs):
namespace BoardGame.Services.Saves;

public sealed class SaveGameService
{
}

     Código incorrecto (archivo Services/Saves/SaveGameService.cs):
namespace BoardGame
{
    public sealed class SaveGameService
    {
    }
}
```
