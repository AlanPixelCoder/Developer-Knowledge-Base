# 03. Triage Logic

**Spanish version:** [03 - Lógica de Triaje](./03%20-%20L%C3%B3gica%20de%20Triaje.md)

**Course:** C#
**Topic:** if / else if / else, comparison and logical operators, short-circuiting, and validating input
**Tags:** `#csharp` `#control-flow` `#logic`

The triage desk decides which report reaches a developer first. The rule has three conditions and one
of them can only be checked safely if an earlier one already passed — which is what short-circuiting
is for.

## The shape

```csharp
using System;

class Triage
{
    static void Main()
    {
        int armour = 4;
        int hp = 30;

        if (hp <= 0)
        {
            Console.WriteLine("unit lost");
        }
        else if (armour < hp / 3)
        {
            Console.WriteLine("armour critical");
        }
        else
        {
            Console.WriteLine("holding");
        }
    }
}
```

## Output

```text
armour critical
```

Exactly one branch runs, and only the first true condition counts. `armour < hp / 3` here is
`4 < 10`, so the second branch wins even though the third would also "fit".

## Comparison operators

| Operator | True when | Example |
| :--- | :--- | :--- |
| `==` | equal | `hp == 0` |
| `!=` | different | `rank != 'D'` |
| `<` `<=` | less than | `armour < 5` |
| `>` `>=` | greater than | `hp >= 1` |

`=` assigns; `==` compares. The compiler catches `if (hp = 0)` in C# — unlike C — because an `int`
is not a `bool`. That is one inheritance the studio does not miss.

## Logical operators and the order they run

| Operator | Meaning | Evaluates right side |
| :--- | :--- | :--- |
| `&&` | and | only if left is `true` |
| `\|\|` | or | only if left is `false` |
| `!` | not | unary |

```csharp
string? input = Console.ReadLine();
int parsed = 0;

if (input != null && int.TryParse(input, out parsed) && parsed > 0)
{
    Console.WriteLine($"queued priority {parsed}");
}
else
{
    Console.WriteLine("rejected");
}
```

The `input != null` test must come first: `int.TryParse(null, ...)` would throw. Short-circuiting is
not an optimisation here, it is the guard that makes the line legal.

## Guards beat nesting

Deep nesting is where triage rules rot. Invert the condition and return early:

```csharp
static void Report(int hp, int armour)
{
    if (hp <= 0) { Console.WriteLine("unit lost"); return; }
    if (armour <= 0) { Console.WriteLine("no armour"); return; }
    Console.WriteLine("combat ready");
}
```

Each guard states one precondition, and the happy path stays at the left margin.

> [!WARNING]
> `&&` and `&` are different operators: `&` evaluates both sides. On a null check that difference is
> a crash, not a style choice.

> [!TIP]
> When two conditions look interchangeable, check the order that matters. First-match-wins makes the
> sequence of `else if` blocks the algorithm, not the formatting.

---

**Next:** [[04 - Wave Cadence]]
