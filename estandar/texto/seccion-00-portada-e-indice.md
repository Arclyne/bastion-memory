---
tipo: estandar-texto
seccion: 0
verificado: 2026-11-13 (copia literal de pdftotext del PDF v2.4; ver [[estandar-v2.4]])
---
# Portada e índice

```text
    Estándar de Codificación C# para Desarrollo de Videojuegos
                                  Versión 2.4 — Juego de Mesa 3D

             Angel Gabriel Aguilar Hernández               José Eduardo Prior Hernández




Índice
1         Introducción                                                                                  4
    1.1         Problemática . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    4
    1.2         Propósito . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   5
    1.3         Idioma del código . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     5
            1.3.1      Regla: todo el contenido del programa en inglés . . . . . . . . . . . . .        5

2       Reglas de Nombrado                                                                               5
    2.1      Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       6
         2.1.1       Regla: camelCase y nombres descriptivos . . . . . . . . . . . . . . . .             6
         2.1.2       Regla: nombres de colecciones en plural . . . . . . . . . . . . . . . . .           6
         2.1.3       Regla: una declaración por línea . . . . . . . . . . . . . . . . . . . . .          7
         2.1.4       Regla: prefijos interrogativos para variables booleanas . . . . . . . . .           7
    2.2      Métodos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       7
         2.2.1       Regla: PascalCase y verbo descriptivo . . . . . . . . . . . . . . . . . .           7
         2.2.2       Regla: máximo de parámetros . . . . . . . . . . . . . . . . . . . . . .             8
         2.2.3       Regla: métodos booleanos como pregunta . . . . . . . . . . . . . . . .              9
    2.3      Constantes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        9
         2.3.1       Regla: PascalCase para constantes . . . . . . . . . . . . . . . . . . . .           9
         2.3.2       Regla: const frente a static readonly . . . . . . . . . . . . . . . . .             9
    2.4      Clases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     10
         2.4.1       Regla: PascalCase y sustantivo singular . . . . . . . . . . . . . . . . .          10
         2.4.2       Regla: sin prefijos ni abreviaturas poco claras . . . . . . . . . . . . . .        11
    2.5      Interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     11
         2.5.1       Regla: prefijo I . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     11
         2.5.2       Regla: correspondencia entre interfaz e implementación estándar . . .              12
    2.6      Campos Privados . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        12
         2.6.1       Regla: prefijo de guion bajo . . . . . . . . . . . . . . . . . . . . . . . .       12
         2.6.2       Regla: misma convención para campos estáticos . . . . . . . . . . . .              13
         2.6.3       Regla: momento de inicialización de un campo . . . . . . . . . . . . .             13
    2.7      Variables No Utilizadas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        14
         2.7.1       Regla: excepción sin nombre en catch . . . . . . . . . . . . . . . . . .           14
         2.7.2       Regla: descarte _ en expresiones lambda . . . . . . . . . . . . . . . . .          15
    2.8      Estructuras de Datos: class frente a record . . . . . . . . . . . . . . . . . .            15
         2.8.1       Regla: mutabilidad como criterio de elección . . . . . . . . . . . . . .           15
    2.9      Identidad de los Objetos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       16
         2.9.1       Regla: identidad mediante clave de negocio . . . . . . . . . . . . . . .           16
    2.10     Valores Mágicos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        18
         2.10.1      Regla: enumeradores y constantes en lugar de literales . . . . . . . . .           18
    2.11     Propiedades . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      19

                                                     1
         2.11.1      Regla: PascalCase y acceso mínimo necesario . . . . . . . . . . . . . .         19
         2.11.2      Regla: modificación controlada con private set . . . . . . . . . . . .          20
         2.11.3      Regla: propiedad totalmente mutable en objetos de datos . . . . . . .           20
         2.11.4      Regla: cuerpo de expresión solo en catálogos de diccionario . . . . . .         21
    2.12     Eventos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   23
         2.12.1      Regla: verbo y tiempo verbal . . . . . . . . . . . . . . . . . . . . . . .      23
         2.12.2      Regla: EventHandler y EventArgs . . . . . . . . . . . . . . . . . . . .         24
    2.13     Parámetros de Tipo Genérico . . . . . . . . . . . . . . . . . . . . . . . . . . .       25
         2.13.1      Regla: prefijo T y nombre descriptivo . . . . . . . . . . . . . . . . . . .     25
    2.14     Sufijos por Responsabilidad . . . . . . . . . . . . . . . . . . . . . . . . . . . .     25
         2.14.1      Regla: sufijos definidos por .NET . . . . . . . . . . . . . . . . . . . . .     25
         2.14.2      Regla: sufijos arquitectónicos del proyecto . . . . . . . . . . . . . . . .     26
         2.14.3      Regla: nombre de la clase base al final de la clase derivada . . . . . .        26
    2.15     Enumeraciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     27
         2.15.1      Regla: singular, o plural con [Flags] . . . . . . . . . . . . . . . . . .       27
         2.15.2      Regla: valor None en las enumeraciones de indicadores . . . . . . . . .         27

3       Estilo de Codificación                                                                       28
    3.1      Indentación . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   28
         3.1.1       Regla: cuatro espacios por nivel . . . . . . . . . . . . . . . . . . . . .      28
    3.2      Espaciado . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   28
         3.2.1       Regla: espacio entre palabra reservada y paréntesis, y línea en blanco
                     entre miembros . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    28
    3.3      Posición de las Llaves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    29
         3.3.1       Regla: estilo Allman . . . . . . . . . . . . . . . . . . . . . . . . . . . .    29
    3.4      Uso de var . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    30
         3.4.1       Regla: solo cuando el tipo es evidente . . . . . . . . . . . . . . . . . .      30
    3.5      División de Líneas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    30
         3.5.1       Regla: cómo continuar una instrucción en varias líneas . . . . . . . . .        30
    3.6      Atributos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   31
         3.6.1       Regla: un atributo por línea, encima del elemento . . . . . . . . . . .         31
    3.7      Controles de Gum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      32
         3.7.1       Regla: inicializador de objeto al crear un control de Gum . . . . . . .         32

4       Complejidad                                                                                  33
    4.1      Profundidad de Anidamiento . . . . . . . . . . . . . . . . . . . . . . . . . . .        33
         4.1.1       Regla: máximo tres niveles de anidamiento . . . . . . . . . . . . . . .         33
    4.2      Salida Anticipada (Early Exit) . . . . . . . . . . . . . . . . . . . . . . . . . .      34
         4.2.1       Regla: cláusula de guarda con retorno anticipado . . . . . . . . . . . .        34
    4.3      Estructuras de Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    34
         4.3.1       Regla: llaves obligatorias en todo bloque . . . . . . . . . . . . . . . . .     34
         4.3.2       Regla: rama default obligatoria en switch . . . . . . . . . . . . . . .         35
    4.4      Reutilización de Código . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     36
         4.4.1       Regla: principio DRY . . . . . . . . . . . . . . . . . . . . . . . . . . .      36
         4.4.2       Regla: una sola definición para cada dato . . . . . . . . . . . . . . . .       37
    4.5      Operador Ternario . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     38
         4.5.1       Regla: solo para seleccionar un valor simple . . . . . . . . . . . . . . .      38
    4.6      Complejidad Ciclomática . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       38
         4.6.1       Regla: máximo de 10 por método . . . . . . . . . . . . . . . . . . . . .        38
    4.7      Coincidencia de Patrones . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      40
         4.7.1       Regla: patrón de tipo en lugar de as con comprobación de nulo . . . .           40



                                                   2
5       Prácticas de Programación Funcional                                                           40
    5.1      Expresiones Lambda . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       40
         5.1.1      Regla: solo para operaciones concisas de una línea . . . . . . . . . . .          40
         5.1.2      Regla: contextos en los que se prohíbe una expresión lambda . . . . .             41
    5.2      Referencias a Métodos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      42
         5.2.1      Regla: grupo de método sobre lambda de reenvío . . . . . . . . . . . .            42
    5.3      Consultas LINQ a Objetos . . . . . . . . . . . . . . . . . . . . . . . . . . . .         43
         5.3.1      Regla: un operador por línea y materialización aparte . . . . . . . . .           43

6         Estructura de Archivos                                                                      44
    6.1        Regla: un tipo de nivel superior por archivo . . . . . . . . . . . . . . . . . . .     44
    6.2        Regla: orden de los elementos dentro de la clase . . . . . . . . . . . . . . . . .     44
    6.3        Regla: orden y continuidad de directivas using . . . . . . . . . . . . . . . . .       45
    6.4        Regla: agrupación mediante espacios de nombres . . . . . . . . . . . . . . . .         46

7       Documentación XML                                                                             46
    7.1      A Nivel de Tipo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      47
         7.1.1       Regla: etiqueta summary en la interfaz del servicio . . . . . . . . . . .        47
         7.1.2       Regla: inheritdoc en la implementación . . . . . . . . . . . . . . . .           47
    7.2      A Nivel de Miembro . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       47
         7.2.1       Regla: orden de las etiquetas param, returns y exception . . . . . .             47
         7.2.2       Regla: qué excepciones se documentan . . . . . . . . . . . . . . . . . .         47
    7.3      Verificación . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   48
         7.3.1       Regla: el compilador exige la documentación de los servicios . . . . . .         48

8       Comentarios Internos                                                                          48
    8.1      Intención e Idioma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     48
         8.1.1       Regla: explicar el porqué en inglés . . . . . . . . . . . . . . . . . . . .      48
         8.1.2       Regla: referencias a reglas y requisitos . . . . . . . . . . . . . . . . . .     48
    8.2      Comentarios de Línea y de Bloque . . . . . . . . . . . . . . . . . . . . . . . .         49
         8.2.1       Regla: preferir comentarios de línea breves . . . . . . . . . . . . . . .        49
         8.2.2       Regla: comentarios en scripts SQL . . . . . . . . . . . . . . . . . . . .        49
    8.3      Comentarios Especiales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       49
         8.3.1       Regla: TODO y FIXME solo en ramas de trabajo . . . . . . . . . . . . .           49

9       Manejo de Errores y Excepciones                                                               50
    9.1      Convenciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     50
         9.1.1       Regla: variable de excepción nombrada ex . . . . . . . . . . . . . . . .         50
         9.1.2       Regla: orden de las cláusulas catch . . . . . . . . . . . . . . . . . . .        50
    9.2      Excepciones Encadenadas . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        51
         9.2.1       Regla: preservar la excepción original como causa . . . . . . . . . . .          51
         9.2.2       Regla: throw; en lugar de throw ex; . . . . . . . . . . . . . . . . . .          52
    9.3      Restricciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    53
         9.3.1       Regla: prohibido capturar o lanzar Exception genérica . . . . . . . .            53
         9.3.2       Regla: preferir excepciones predefinidas . . . . . . . . . . . . . . . . .       53
    9.4      Comprobación de Nulos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        54
         9.4.1       Regla: referencias anulables y validación de argumentos . . . . . . . .          54
         9.4.2       Regla: valor alternativo con ?? cuando una expresión puede ser nula .            55
    9.5      Liberación de Recursos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       56
         9.5.1       Regla: la clase dueña de un recurso lo libera . . . . . . . . . . . . . .        56
         9.5.2       Regla: cerrar un canal WCF con Close y Abort . . . . . . . . . . . .             56
    9.6      Diseño de Excepciones Propias . . . . . . . . . . . . . . . . . . . . . . . . . .        57


                                                    3
            9.6.1     Regla: constructores de una excepción propia . . . . . . . . . . . . . .        57
     9.7        Manejadores async void . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      58
            9.7.1     Regla: un manejador async void no deja escapar excepciones . . . . .            58

10      Inyección de Dependencias                                                                     58
     10.1     Inyección por Constructor . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     58
          10.1.1      Regla: inyección por constructor y dependencia de abstracciones . . .           58
     10.2     Raíz de Composición . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     59
          10.2.1      Regla: los servicios se construyen solo en la raíz de composición . . . .       59
     10.3     Localizador de Servicios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    60
          10.3.1      Regla: prohibido pedir servicios al contenedor . . . . . . . . . . . . . .      60
     10.4     Proveedor de Tiempo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       61
          10.4.1      Regla: el tiempo se obtiene de un TimeProvider inyectado . . . . . .            61

11      Bitácoras                                                                                     62
     11.1     Niveles de Registro . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   62
          11.1.1      Regla: elección del nivel según la severidad del evento . . . . . . . . .       62
     11.2     Restricciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   63
          11.2.1      Regla: prohibido Console.WriteLine como bitácora . . . . . . . . . .            63
     11.3     Formato de Mensajes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       63
          11.3.1      Regla: acción, contexto y excepción separada . . . . . . . . . . . . . .        63

12      Pruebas Unitarias                                                                             64
     12.1     Nomenclatura de las Clases de Prueba . . . . . . . . . . . . . . . . . . . . . .        64
          12.1.1     Regla: prefijo Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    64
     12.2     Nomenclatura de Métodos de Prueba . . . . . . . . . . . . . . . . . . . . . . .         64
          12.2.1     Regla: patrón método-estado-comportamiento esperado . . . . . . . .              64
     12.3     Estructura Interna (Patrón AAA) . . . . . . . . . . . . . . . . . . . . . . . .         65
          12.3.1     Regla: separar Arrange, Act y Assert con líneas en blanco . . . . . . .          65
          12.3.2     Regla: una única aserción por prueba . . . . . . . . . . . . . . . . . .         65

13         Declaración de Uso de Inteligencia Artificial                                              66

14         Referencias                                                                                66
```
