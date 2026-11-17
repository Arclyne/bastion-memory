---
tipo: estandar-texto
seccion: 12
verificado: 2026-11-13 (copia literal de pdftotext del PDF v2.4; ver [[estandar-v2.4]])
---
# 12. Pruebas Unitarias

```text
12.       Pruebas Unitarias
    Las pruebas unitarias deben ser independientes entre sí y autoexplicativas, de manera que
sirvan como documentación viva del comportamiento esperado de cada clase.

12.1.     Nomenclatura de las Clases de Prueba
12.1.1.    Regla: prefijo Test
    Regla: Una clase de prueba se nombra igual que la clase examinada, con el prefijo Test
(Osherove, 2013). Esta es una excepción explícita a la regla general de nombres de clase en
singular.
    Código correcto:
public sealed class TestDiceRoller
{
}

   Código incorrecto:
public sealed class DiceRollerTest
{
}


12.2.     Nomenclatura de Métodos de Prueba
12.2.1.    Regla: patrón método-estado-comportamiento esperado
    Regla: Nombre en tres partes, en PascalCase separadas por guion bajo: método bajo prueba,
estado evaluado, comportamiento esperado (Osherove, 2013). Esta es una excepción explícita a la
regla general de nombres de método sin separadores. Los ejemplos omiten el atributo de prueba
porque la regla de nombrado aplica al margen de él.
    Código correcto:
public void Roll_FaceValueSix_GrantsExtraTurn()
{
}

   Código incorrecto:
public void TestRollExtraTurn()
{
}




                                              64
12.3.     Estructura Interna (Patrón AAA)
12.3.1.    Regla: separar Arrange, Act y Assert con líneas en blanco
   Regla: Tres bloques consecutivos — preparación, ejecución, verificación — separados solo
por una línea en blanco, sin comentarios que los etiqueten (Osherove, 2013).
   Descripción: ExpectEqual representa la llamada de aserción del bloque de verificación.
   Código correcto:
public void Roll_FaceValueSix_GrantsExtraTurn()
{
    DiceRoller diceRoller = new(new FixedRandomProvider(6));

    int faceValue = diceRoller.Roll();

    ExpectEqual(6, faceValue);
}

    Código incorrecto:
public void Roll_FaceValueSix_GrantsExtraTurn()
{
    DiceRoller diceRoller = new(new FixedRandomProvider(6));
    int faceValue = diceRoller.Roll();
    ExpectEqual(6, faceValue);
}


12.3.2.    Regla: una única aserción por prueba
    Regla: El bloque de verificación contiene una única llamada de aserción, como ExpectEqual
(Osherove, 2013). Para comparar varios atributos de un mismo objeto, se prefiere una sola
aserción sobre el propio Equals de la clase (Sección 2.9) en lugar de una aserción por atributo.
Un caso puntual que en verdad necesite más de una aserción se admite solo con un comentario,
inmediatamente antes de las aserciones, que explique el motivo de esa decisión.
    Código correcto:
public void MoveTo_ValidDestination_UpdatesCurrentTile()
{
    Player player = new(startingTile: new BoardTile(0, 0));

    player.MoveTo(new BoardTile(2, 3));

    ExpectEqual(new BoardTile(2, 3), player.CurrentTile);
}

    Código incorrecto:
public void MoveTo_ValidDestination_UpdatesCurrentTile()
{
    Player player = new(startingTile: new BoardTile(0, 0));

    player.MoveTo(new BoardTile(2, 3));

    ExpectEqual(2, player.CurrentTile.Row);
    ExpectEqual(3, player.CurrentTile.Column);
}




                                              65
```
