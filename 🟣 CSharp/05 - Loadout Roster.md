# 05. Loadout Roster

**Spanish version:** [05 - Lista de Carga](./05%20-%20Lista%20de%20Carga.md)

**Course:** C#
**Topic:** Single-dimensional arrays: declaration, indexing, Length, iteration, and the parallel-array trap
**Tags:** `#csharp` `#arrays` `#collections`

A loadout is a fixed number of slots. That is what an array models: one type, one length, set when it
is created, and every slot reachable by position.

## Declare, create, fill

```csharp
using System;

class Roster
{
    static void Main()
    {
        string[] slots = new string[4];
        slots[0] = "blade";
        slots[1] = "buckler";
        slots[2] = "torch";
        slots[3] = "ration";

        Console.WriteLine($"{slots.Length} slots, first is {slots[0]}");
    }
}
```

## Output

```text
4 slots, first is blade
```

Three ways to give an array its content:

| Form | Length |
| :--- | :--- |
| `new int[3]` | 3, all `0` |
| `new int[] { 4, 8, 15 }` | 3, as listed |
| `new[] { "a", "b" }` | 2, element type inferred |
| `int[] c = { 1, 2 };` | 2, only at the declaration |

## Indexing is 0-based

| Position | `slots[position]` | In range |
| :--- | :--- | :--- |
| 0 | `blade` | yes |
| 3 | `ration` | yes |
| 4 | — | `IndexOutOfRangeException` |
| -1 | — | `IndexOutOfRangeException` |

The valid indexes of an array of length `n` are `0` to `n - 1`. `Length` is the count, never the last
index; `slots[slots.Length]` is always wrong.

## Iterate

```csharp
foreach (string item in slots)
{
    Console.WriteLine($"- {item}");
}

for (int i = 0; i < slots.Length; i++)
{
    Console.WriteLine($"{i}: {slots[i]}");
}
```

`foreach` when you only need the values; `for` when you need the position, or need to write back into
the slot.

## The parallel-array trap

Two arrays that must stay aligned by index are a bug waiting for a sort:

```csharp
string[] names   = { "blade", "buckler", "torch" };
int[]    weights = { 3, 2, 1 };
```

Nothing in the language keeps `names[i]` next to `weights[i]`. Sort one and the pairs break. The fix
is one array of a type that holds both — a `struct` or a class — which is exactly what the collections
notes build toward.

> [!WARNING]
> `int[] a = new int[3]; a[0] = 1;` mutates. `int[] b = a;` copies the reference, so writing `b[0]`
> changes `a[0]` too. Two names, one array; clone when you want a copy.

> [!TIP]
> Reach for `List<T>` when the count is not known in advance: it grows, keeps `[]` indexing, and
> exposes `Count` where an array has `Length`.

---

**Next:** [[06 - Toolsmith Methods]]
