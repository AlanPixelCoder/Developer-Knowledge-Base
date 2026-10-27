# 01. Del Plano al Binario

**Versión original en inglés:** [01 - Blueprint to Binary](./01%20-%20Blueprint%20to%20Binary.md)

**Curso:** C#
**Tema:** Linaje de C#, .NET y el CLR, la canalización de compilación y la forma de un programa de consola
**Etiquetas:** `#csharp` `#dotnet` `#clr`

Atelier Emberforge mantiene sus herramientas en C# porque el runtime del estudio es C#: las utilidades
de consola que equilibran *Ironledger* usan el mismo lenguaje que el juego, así que un número validado
en un script es un número que el runtime puede usar sin cambios.

## De 1999 hasta hoy

C# apareció en 2000 como parte de la iniciativa .NET de Microsoft, diseñado por el equipo de Anders
Hejlsberg. Su primer nombre interno fue **COOL** (*C-like Object Oriented Language*), descartado por
problemas de marca. El objetivo de diseño era explícito: la comodidad sintáctica de C++ con la
seguridad de memoria de un runtime gestionado.

| Año | Hito |
| :--- | :--- |
| 2000 | C# 1.0 con .NET Framework 1.0 |
| 2002 | Llegan los genéricos en C# 2.0 |
| 2007 | LINQ y `var` en C# 3.0 |
| 2016 | .NET Core: multiplataforma y de código abierto |
| 2020 | .NET 5 unifica el runtime; después, versiones anuales (8, 9, 10) |

Hoy el lenguaje corre en Windows, macOS y Linux a través de .NET, y dentro de Unity y Godot para
juegos. Por eso lo eligió el estudio: un solo lenguaje para herramientas y runtime.

## Dos compilaciones, no una

Un archivo `.cs` no se ejecuta: se compila dos veces.

| Etapa | Produce | La hace |
| :--- | :--- | :--- |
| Fuente → IL | Common Intermediate Language, en un `.dll` | el compilador de C# (`Roslyn`) |
| IL → nativo | código máquina para la CPU actual | el JIT, en tiempo de ejecución |

El paso intermedio es la razón por la que el mismo `.dll` corre en otro procesador: el JIT lo traduce
para esa máquina al arrancar, y el **CLR** (Common Language Runtime) aporta el recolector de basura,
el sistema de tipos y el mecanismo de excepciones alrededor.

```csharp
using System;

class ForgeBoot
{
    static void Main()
    {
        Console.WriteLine("Atelier Emberforge - herramientas en línea");
        Console.WriteLine("compilación de balance de Ironledger 0.1");
    }
}
```

## Salida

```text
Atelier Emberforge - herramientas en línea
compilación de balance de Ironledger 0.1
```

## Leer el programa

| Pieza | Significado |
| :--- | :--- |
| `using System;` | hace visible `Console` sin el prefijo del espacio de nombres |
| `class ForgeBoot` | toda sentencia vive dentro de un tipo |
| `static void Main()` | el punto de entrada que busca el CLR |
| `Console.WriteLine(...)` | escribe una línea y pasa a la siguiente |
| `;` | termina una sentencia |

`Main` puede devolver `int` cuando el código de salida le importa a un script de compilación, y puede
recibir `string[] args` para leer argumentos de línea de comandos. Empieza por la forma `void`; añade
el resto cuando una herramienta lo necesite.

## Ejecutarlo

```bash
dotnet new console -o forgeboot
cd forgeboot
dotnet run
```

`dotnet run` compila y ejecuta en un paso. Para un script sobre el que iteras, ese ciclo —editar,
ejecutar, leer— es todo el flujo de trabajo.

> [!NOTE]
> El C# moderno también admite **sentencias de nivel superior**: el cuerpo de `Main` escrito
> directamente en `Program.cs`, sin clase. Va bien para un script desechable y confunde en un
> proyecto donde varios archivos definen métodos. Las notas de este módulo usan la forma explícita
> con clase para que cada ejemplo muestre dónde vive el código.

> [!TIP]
> En una aplicación de consola el nombre del archivo no tiene que coincidir con el de la clase, pero
> mantenerlos alineados (`ForgeBoot.cs` con `ForgeBoot`) hace que el archivo que buscas sea el que
> imaginaste.

## Lo que esta nota no es

No es una lección de historia. La canalización importa porque explica tres cosas que verás
constantemente: por qué un error de compilación y uno de ejecución se ven distintos, por qué
`dotnet run` es más lento la primera vez, y por qué una traza de pila nombra una línea de un archivo
que puedes abrir.

---

**Siguiente:** [[02 - Planos Tipados]]
