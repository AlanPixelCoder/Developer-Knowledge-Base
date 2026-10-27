# 04. Wave Cadence

**Spanish version:** [04 - Cadencia de Oleadas](./04%20-%20Cadencia%20de%20Oleadas.md)

**Course:** C#
**Topic:** while, do-while and for; sentinel loops, accumulation, break and continue
**Tags:** `#csharp` `#loops` `#iteration`

A wave simulator spawns enemies until the wave budget is spent. The count is not known when the code
is written — it depends on the budget and the cost of each enemy — so the loop is driven by a
condition, not by a number.

## `while`: check first

```csharp
using System;

class Wave
{
    static void Main()
    {
        int budget = 7;
        int spawned = 0;

        while (budget >= 2)
        {
            budget -= 2;
            spawned++;
        }

        Console.WriteLine($"spawned {spawned}, leftover {budget}");
    }
}
```

## Output

```text
spawned 3, leftover 1
```

The body may run zero times: with `budget = 1` the condition is false immediately. That is the
difference between `while` and a `do ... while`, which always runs once.

## `do ... while`: at least once

```csharp
int key = 0;
do
{
    Console.WriteLine("press 1 to end the wave");
    key = 1;   // simulated input
} while (key != 1);
```

A prompt loop wants this shape: you cannot know the answer is wrong until you have asked.

## `for`: the count is known

```csharp
for (int wave = 1; wave <= 3; wave++)
{
    Console.WriteLine($"wave {wave} incoming");
}
```

| Clause | Runs | Here |
| :--- | :--- | :--- |
| Initialisation | once | `int wave = 1` |
| Condition | before every pass | `wave <= 3` |
| Increment | after every pass | `wave++` |

## Sentinel loops

A sentinel is a value that means "stop", not data. Reading until sentinel is the standard pattern for
input:

```csharp
int total = 0;
int value = 7;              // simulated reading; a real tool parses Console.ReadLine()

while (value != 0)
{
    total += value;
    value = 0;              // next reading: the sentinel that ends the loop
}

Console.WriteLine($"total {total}");
```

## Output

```text
total 7
```

> [!CAUTION]
> Delete the `value = 0;` line and that loop never ends, because nothing inside it can change the
> condition. Every sentinel loop needs a path that produces the sentinel; if the reading comes from
> `Console.ReadLine()`, that path is the user typing it, or a `break` on a keyword.

## `break` and `continue`

```csharp
for (int i = 1; i <= 6; i++)
{
    if (i == 2) continue;   // skip this pass
    if (i == 5) break;      // leave the loop entirely
    Console.Write(i + " ");
}
```

## Output

```text
1 3 4
```

`continue` returns to the increment; `break` leaves the loop. Both make a loop harder to reason about,
so prefer a well-written condition and use them for the exceptional case.

## Accumulate, do not just count

| Goal | Start | Update |
| :--- | :--- | :--- |
| Count | `0` | `count++` |
| Sum | `0` | `total += value` |
| Maximum | first value | `if (v > best) best = v` |
| Average | sum + count | divide after the loop |

> [!TIP]
> `for` is a `while` with the bookkeeping moved into the header. If the loop needs the counter after
> it ends, declare the counter before the header; inside, it goes out of scope at the closing brace.

---

**Next:** [[05 - Loadout Roster]]
