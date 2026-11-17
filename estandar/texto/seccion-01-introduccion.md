---
tipo: estandar-texto
seccion: 1
verificado: 2026-11-13 (copia literal de pdftotext del PDF v2.4; ver [[estandar-v2.4]])
---
# 1. Introducción

```text
1.     Introducción
1.1.       Problemática
    Cuando varias personas desarrollan simultáneamente un mismo videojuego, cada integrante
tiende a resolver problemas equivalentes — nombrar una variable, estructurar una clase, registrar
un error, escribir una prueba — de una manera distinta. En ausencia de un criterio compartido,
el código de un mismo proyecto termina mezclando convenciones de nombrado incompatibles,
niveles de anidamiento excesivos, manejo inconsistente de excepciones y bitácoras improvisadas
con Console.WriteLine. Esta heterogeneidad incrementa el tiempo que cualquier integrante
necesita para comprender un módulo escrito por alguien más, dificulta la revisión de código y
facilita la introducción de errores al modificar lógica que no se entiende por completo.
    El problema se agrava en un proyecto como un juego de mesa digital en 3D, donde la lógica
de turnos, movimientos, validación de reglas y estado del tablero se reparte entre varias clases
que deben interactuar de forma predecible. Sin reglas explícitas de nombrado, manejo de errores,
complejidad y pruebas unitarias, el equipo no cuenta con un criterio objetivo para decidir si una
porción de código está lista para integrarse al resto del proyecto.


                                                    4
1.2.     Propósito
    Este documento define el estándar de codificación en C# para el desarrollo de un videojuego
de mesa en tres dimensiones. Su propósito es establecer un conjunto único de reglas de nombrado,
estilo, complejidad, manejo de errores, documentación, bitácoras y pruebas unitarias que todo
el equipo debe seguir, de manera que el código resultante sea consistente, legible y mantenible
independientemente de quién lo haya escrito.
    El alcance del estándar es el lenguaje C# y las bibliotecas oficiales de .NET: no define
convenciones de un motor de videojuegos, una tecnología de interfaz gráfica o de conexión de red
en particular. Cada regla incluye, además, la justificación técnica o académica en la que se apoya,
para que el equipo comprenda no solo qué debe hacer, sino por qué conviene hacerlo así.

1.3.     Idioma del código
1.3.1.    Regla: todo el contenido del programa en inglés
    Regla: Todo elemento que forme parte del programa se escribe en inglés: clases, interfaces,
métodos, propiedades, eventos, variables, constantes, parámetros genéricos, espacios de nombres,
comentarios, documentación XML, mensajes de excepción, mensajes de bitácora, elementos de la
base de datos (tablas, columnas, restricciones, procedimientos almacenados) y cualquier cadena
visible para la persona usuaria. El estándar se redacta en español, pero el código y sus textos
permanecen íntegramente en inglés (Microsoft, 2025c).
    Código correcto:
public int CalculatePlayerScore(Player player)
{
    if (!player.IsActive)
    {
        throw new InvalidOperationException("The player is not active.");
    }

     return player.BaseScore + player.BonusScore;
}

     Código incorrecto:
public int calcularPlayerScore(Player jugador)
{
    if (!jugador.IsActive)
    {
        throw new InvalidOperationException("El jugador no esta activo.");
    }

     return jugador.BaseScore + jugador.BonusScore;
}
```
