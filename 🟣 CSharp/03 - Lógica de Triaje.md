# 03. Lógica de Triaje

**Versión original en inglés:** [03 - Triage Logic](./03%20-%20Triage%20Logic.md)

**Curso:** C#
**Tema:** if / else if / else, operadores de comparación y lógicos, cortocircuito y validación de entrada
**Etiquetas:** `#csharp` `#control-flow` `#logic`

El mostrador de triaje decide qué informe llega antes a un desarrollador. La regla tiene tres
condiciones y una de ellas solo se puede comprobar con seguridad si otra ya pasó: para eso existe el
cortocircuito.

## La forma

```csharp
using System;

class Triaje
{
    static void Main()
    {
        int armadura = 4;
        int vida = 30;

        if (vida <= 0)
        {
            Console.WriteLine("unidad perdida");
        }
        else if (armadura < vida / 3)
        {
            Console.WriteLine("armadura crítica");
        }
        else
        {
            Console.WriteLine("aguantando");
        }
    }
}
```

## Salida

```text
armadura crítica
```

Se ejecuta exactamente una rama, y solo cuenta la primera condición verdadera. Aquí
`armadura < vida / 3` es `4 < 10`, así que gana la segunda rama aunque la tercera también "encajaría".

## Operadores de comparación

| Operador | Verdadero cuando | Ejemplo |
| :--- | :--- | :--- |
| `==` | igual | `vida == 0` |
| `!=` | distinto | `rango != 'D'` |
| `<` `<=` | menor que | `armadura < 5` |
| `>` `>=` | mayor que | `vida >= 1` |

`=` asigna; `==` compara. El compilador atrapa `if (vida = 0)` en C# —a diferencia de C— porque un
`int` no es un `bool`. Esa herencia no la echa de menos el estudio.

## Operadores lógicos y el orden en que corren

| Operador | Significado | Evalúa el lado derecho |
| :--- | :--- | :--- |
| `&&` | y | solo si el izquierdo es `true` |
| `\|\|` | o | solo si el izquierdo es `false` |
| `!` | no | unario |

```csharp
string? entrada = Console.ReadLine();
int analizado = 0;

if (entrada != null && int.TryParse(entrada, out analizado) && analizado > 0)
{
    Console.WriteLine($"prioridad {analizado} en cola");
}
else
{
    Console.WriteLine("rechazado");
}
```

La prueba `entrada != null` debe ir primero: `int.TryParse(null, ...)` lanzaría. El cortocircuito no es
una optimización aquí, es la guarda que hace legal la línea.

## Guardas antes que anidamiento

El anidamiento profundo es donde se pudren las reglas de triaje. Invierte la condición y sal temprano:

```csharp
static void Informar(int vida, int armadura)
{
    if (vida <= 0) { Console.WriteLine("unidad perdida"); return; }
    if (armadura <= 0) { Console.WriteLine("sin armadura"); return; }
    Console.WriteLine("lista para combate");
}
```

Cada guarda declara una precondición, y el camino feliz se queda en el margen izquierdo.

> [!WARNING]
> `&&` y `&` son operadores distintos: `&` evalúa ambos lados. En una comprobación de nulo esa
> diferencia es una caída, no una elección de estilo.

> [!TIP]
> Cuando dos condiciones parezcan intercambiables, revisa el orden que importa. Que gane la primera
> coincidencia hace de la secuencia de `else if` el algoritmo, no el formato.

---

**Siguiente:** [[04 - Cadencia de Oleadas]]
