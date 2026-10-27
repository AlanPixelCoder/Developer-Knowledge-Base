# 06. Métodos de Herrería

**Versión original en inglés:** [06 - Toolsmith Methods](./06%20-%20Toolsmith%20Methods.md)

**Curso:** C#
**Tema:** Declarar y llamar métodos, parámetros y argumentos, valores de retorno, sobrecarga, out y ref
**Etiquetas:** `#csharp` `#methods` `#parameters`

Un herrero no rehace la hoja para probar su equilibrio: la forja recibe una hoja y devuelve un número.
Un método es eso: una operación con nombre, con entradas y una salida, escrita una vez y llamada en
todas partes.

## Declarar y llamar

```csharp
using System;

class Forja
{
    static int PesoTotal(int[] pesos)
    {
        int suma = 0;
        foreach (int p in pesos)
        {
            suma += p;
        }
        return suma;
    }

    static void Main()
    {
        int[] carga = { 3, 2, 1, 4 };
        Console.WriteLine($"total {PesoTotal(carga)}");
    }
}
```

## Salida

```text
total 10
```

| Término | Significado |
| :--- | :--- |
| método | el bloque con nombre |
| parámetro | la variable de la declaración (`pesos`) |
| argumento | el valor en la llamada (`carga`) |
| tipo de retorno | `int` aquí; `void` cuando no devuelve nada |
| `return` | entrega el valor y sale del método |

## `void` frente a devolver

```csharp
static void Informar(int peso)
{
    Console.WriteLine($"peso {peso}");
}

static double Media(int total, int cuenta)
{
    if (cuenta == 0) return 0;      // guarda: nunca dividas entre cero
    return (double)total / cuenta;
}
```

Un método `void` es para efectos —imprimir, escribir un archivo—. Un método que devuelve es para
valores. Mezclarlos (un `void` que además fija un campo, una función que imprime) es cómo un método
se vuelve imposible de probar.

## Miembros con cuerpo de expresión

```csharp
static int Doble(int n) => n * 2;
static bool EsPesado(int p) => p > 5;
```

El mismo método, más corto cuando el cuerpo es una sola expresión. El `=>` aquí no es una lambda: es
sintaxis para un miembro de una línea.

## Sobrecarga

```csharp
static string Etiqueta(int id) => $"unidad {id}";
static string Etiqueta(int id, string grado) => $"unidad {id} ({grado})";
```

Mismo nombre, listas de parámetros distintas, resueltas por los argumentos en la llamada. Sobrecarga
cuando la operación es la misma; usa otro nombre cuando el comportamiento difiere.

## `out` y `ref`

```csharp
static bool TrySplit(int total, out int cada)
{
    cada = 0;
    if (total < 2) return false;
    cada = total / 2;
    return true;
}

// llamada
if (TrySplit(9, out int mitad))
{
    Console.WriteLine(mitad);
}
```

| Modificador | Dirección | Debe asignarse dentro |
| :--- | :--- | :--- |
| `out` | devuelve un segundo valor | sí, en todos los caminos |
| `ref` | lee y escribe la variable del llamador | no |

`out` es el patrón detrás de `int.TryParse`: un `bool` para el éxito y el valor por el parámetro.

## Ámbito

Una variable declarada dentro de un método existe solo ahí. Los parámetros son locales, copiados en la
llamada; salvo en tipos por referencia, donde la copia es de la referencia, así que mutar un array
dentro de un método lo cambia también para el llamador.

> [!NOTE]
> `static` significa que el método pertenece a la clase, no a una instancia, así que `Main` puede
> llamarlo directamente. En el momento en que hay que conservar estado entre llamadas, el método deja
> de ser estático y pasa a un objeto.

> [!TIP]
> Escribe un método cuando las mismas cinco líneas aparezcan dos veces, o cuando un bloque necesite
> un nombre para poder probarlo. No antes: un método por línea es un laberinto con puertas extra.

---

**Siguiente:** [[Prueba de Esfuerzo del Equipamiento de Ironledger]]
