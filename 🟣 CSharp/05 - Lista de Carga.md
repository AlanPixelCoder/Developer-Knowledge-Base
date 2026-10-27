# 05. Lista de Carga

**Versión original en inglés:** [05 - Loadout Roster](./05%20-%20Loadout%20Roster.md)

**Curso:** C#
**Tema:** Matrices unidimensionales: declaración, indexación, Length, iteración y la trampa de las matrices paralelas
**Etiquetas:** `#csharp` `#arrays` `#collections`

Una lista de carga es un número fijo de ranuras. Eso modela un array: un tipo, una longitud fijada al
crearlo, y cada ranura accesible por posición.

## Declarar, crear, rellenar

```csharp
using System;

class Lista
{
    static void Main()
    {
        string[] ranuras = new string[4];
        ranuras[0] = "hoja";
        ranuras[1] = "rodela";
        ranuras[2] = "antorcha";
        ranuras[3] = "ración";

        Console.WriteLine($"{ranuras.Length} ranuras, la primera es {ranuras[0]}");
    }
}
```

## Salida

```text
4 ranuras, la primera es hoja
```

Tres formas de dar contenido a un array:

| Forma | Longitud |
| :--- | :--- |
| `new int[3]` | 3, todo `0` |
| `new int[] { 4, 8, 15 }` | 3, tal como se lista |
| `new[] { "a", "b" }` | 2, tipo de elemento inferido |
| `int[] c = { 1, 2 };` | 2, solo en la declaración |

## La indexación empieza en 0

| Posición | `ranuras[posición]` | En rango |
| :--- | :--- | :--- |
| 0 | `hoja` | sí |
| 3 | `ración` | sí |
| 4 | — | `IndexOutOfRangeException` |
| -1 | — | `IndexOutOfRangeException` |

Los índices válidos de un array de longitud `n` van de `0` a `n - 1`. `Length` es la cuenta, nunca el
último índice; `ranuras[ranuras.Length]` siempre está mal.

## Iterar

```csharp
foreach (string objeto in ranuras)
{
    Console.WriteLine($"- {objeto}");
}

for (int i = 0; i < ranuras.Length; i++)
{
    Console.WriteLine($"{i}: {ranuras[i]}");
}
```

`foreach` cuando solo necesitas los valores; `for` cuando necesitas la posición o escribir de vuelta
en la ranura.

## La trampa de las matrices paralelas

Dos arrays que deben quedar alineados por índice son un error esperando a un ordenamiento:

```csharp
string[] nombres = { "hoja", "rodela", "antorcha" };
int[]    pesos   = { 3, 2, 1 };
```

Nada en el lenguaje mantiene `nombres[i]` junto a `pesos[i]`. Ordena uno y los pares se rompen. La
solución es un array de un tipo que contenga ambos —un `struct` o una clase—, que es justo lo que
construyen las notas de colecciones.

> [!WARNING]
> `int[] a = new int[3]; a[0] = 1;` muta. `int[] b = a;` copia la referencia, así que escribir
> `b[0]` cambia también `a[0]`. Dos nombres, un array; clona cuando quieras una copia.

> [!TIP]
> Recurre a `List<T>` cuando la cuenta no se conoce de antemano: crece, mantiene indexación `[]` y
> expone `Count` donde el array tiene `Length`.

---

**Siguiente:** [[06 - Métodos de Herrería]]
