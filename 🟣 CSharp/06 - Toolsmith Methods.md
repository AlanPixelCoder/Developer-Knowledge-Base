# 06. Toolsmith Methods

**Spanish version:** [06 - Métodos de Herrería](./06%20-%20M%C3%A9todos%20de%20Herrer%C3%ADa.md)

**Course:** C#
**Topic:** Declaring and calling methods, parameters and arguments, return values, overloading, out and ref
**Tags:** `#csharp` `#methods` `#parameters`

A toolsmith does not reforge a blade to test its balance; the forge takes a blade and returns a
number. A method is that: a named operation with inputs and one output, written once, called
everywhere.

## Declare and call

```csharp
using System;

class Forge
{
    static int TotalWeight(int[] weights)
    {
        int sum = 0;
        foreach (int w in weights)
        {
            sum += w;
        }
        return sum;
    }

    static void Main()
    {
        int[] loadout = { 3, 2, 1, 4 };
        Console.WriteLine($"total {TotalWeight(loadout)}");
    }
}
```

## Output

```text
total 10
```

| Term | Meaning |
| :--- | :--- |
| method | the named block |
| parameter | the variable in the declaration (`weights`) |
| argument | the value at the call (`loadout`) |
| return type | `int` here; `void` when nothing comes back |
| `return` | hands the value back and leaves the method |

## `void` versus returning

```csharp
static void Report(int weight)
{
    Console.WriteLine($"weight {weight}");
}

static double Average(int total, int count)
{
    if (count == 0) return 0;      // guard: never divide by zero
    return (double)total / count;
}
```

A `void` method is for effects — printing, writing a file. A returning method is for values. Mixing
them (a `void` that also sets a field, a function that prints) is how a method becomes untestable.

## Expression-bodied members

```csharp
static int Double(int n) => n * 2;
static bool IsHeavy(int w) => w > 5;
```

Same method, shorter when the body is a single expression. The `=>` form is not a lambda here; it is
syntax for a one-line member.

## Overloading

```csharp
static string Label(int id) => $"unit {id}";
static string Label(int id, string grade) => $"unit {id} ({grade})";
```

Same name, different parameter lists, resolved by the arguments at the call. Overload when the
operation is the same; use a new name when the behaviour differs.

## `out` and `ref`

```csharp
static bool TrySplit(int total, out int each)
{
    each = 0;
    if (total < 2) return false;
    each = total / 2;
    return true;
}

// call
if (TrySplit(9, out int half))
{
    Console.WriteLine(half);
}
```

| Modifier | Direction | Must be set inside |
| :--- | :--- | :--- |
| `out` | returns a second value | yes, on every path |
| `ref` | reads and writes the caller's variable | no |

`out` is the pattern behind `int.TryParse`: a `bool` for success, the value through the parameter.

## Scope

A variable declared inside a method exists only there. Parameters are locals, copied at the call —
except for reference types, where the copy is of the reference, so mutating an array inside a method
is visible to the caller.

> [!NOTE]
> `static` means the method belongs to the class, not to an instance, so `Main` can call it directly.
> The moment state has to be kept between calls, the method stops being static and moves into an
> object.

> [!TIP]
> Write a method when the same five lines appear twice, or when a block needs a name to be tested.
> Not before: a method per line is a maze with extra doors.

---

**Next:** [[Ironledger Loadout Stress Test]]
