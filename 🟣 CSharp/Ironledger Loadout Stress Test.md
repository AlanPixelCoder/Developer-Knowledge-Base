# Ironledger Loadout Stress Test

**Spanish version:** [Prueba de Esfuerzo del Equipamiento de Ironledger](./Prueba%20de%20Esfuerzo%20del%20Equipamiento%20de%20Ironledger.md)

**Course:** C#
**Topic:** Capstone: a full console tool — input validation, loops, arrays, methods and decisions
**Tags:** `#csharp` `#capstone` `#console`

The studio's balance pass needs one number: the total weight a character carries, and whether it
crosses the encumbrance line. This note builds that tool end to end — input, loop, array, method,
decision — and shows what a testable console program looks like before it becomes a window.

## What it must do

| Requirement | Rule |
| :--- | :--- |
| Read a count | between 1 and 8 slots |
| Read each weight | positive whole numbers |
| Report | total, average, heaviest slot |
| Warn | total above the encumbrance limit |
| Repeat | until the operator answers `n` |

## The program

```csharp
using System;

class StressTest
{
    const int MaxSlots = 8;
    const int Encumbrance = 15;

    static int ReadInt(string prompt, int min, int max)
    {
        while (true)
        {
            Console.Write(prompt);
            string? line = Console.ReadLine();
            if (int.TryParse(line, out int value) && value >= min && value <= max)
            {
                return value;
            }
            Console.WriteLine("invalid entry");
        }
    }

    static int Total(int[] weights)
    {
        int sum = 0;
        foreach (int w in weights) sum += w;
        return sum;
    }

    static int Heaviest(int[] weights)
    {
        int best = weights[0];
        for (int i = 1; i < weights.Length; i++)
        {
            if (weights[i] > best) best = weights[i];
        }
        return best;
    }

    static void Main()
    {
        bool again = true;

        while (again)
        {
            int slots = ReadInt("slots: ", 1, MaxSlots);
            int[] weights = new int[slots];

            for (int i = 0; i < slots; i++)
            {
                weights[i] = ReadInt($"weight {i + 1}: ", 1, 99);
            }

            int total = Total(weights);
            double average = (double)total / slots;

            Console.WriteLine($"total {total}, average {average:F1}, heaviest {Heaviest(weights)}");

            if (total > Encumbrance)
            {
                Console.WriteLine($"over the limit by {total - Encumbrance}");
            }
            else
            {
                Console.WriteLine($"under the limit by {Encumbrance - total}");
            }

            Console.Write("another loadout? (y/n): ");
            again = Console.ReadLine() == "y";
        }
    }
}
```

## A sample session

Typed answers follow each prompt:

```text
slots: 3
weight 1: 6
weight 2: 7
weight 3: 4
total 17, average 5.7, heaviest 7
over the limit by 2
another loadout? (y/n): n
```

## Why it is split this way

| Piece | Reason |
| :--- | :--- |
| `ReadInt` | one place enforces parsing and range, so no call site repeats the loop |
| `Total`, `Heaviest` | pure functions over an array: same input, same answer, no console |
| `Main` | only orchestration and printing |
| constants | the limits are named once and read everywhere |

The pure methods are the part you can test without typing: call `Total(new[] { 6, 7, 4 })` and check
`17`. That separation is the whole reason the tool is not one long `Main`.

## What to test by hand

1. A single slot: average equals that weight.
2. Exactly at the limit: the message says "under the limit by 0".
3. Junk input (`abc`, blank, `0`, `99` where max is 8): `ReadInt` asks again, never crashes.
4. Eight slots: the maximum, then try nine.

## Stretch goals

- Print the slot index of the heaviest entry, not only its value.
- Track a running total while typing, so the operator sees the budget fall.
- Move the slots into a `List<int>` and allow removal by index.
- Return a small `record` with total, average and heaviest instead of printing three times.

> [!NOTE]
> `average` is computed with `(double)total / slots` on purpose: `total / slots` would be integer
> division and report `5` instead of `5.7`. The cast is the difference between a correct report and a
> plausible one.

> [!TIP]
> Run the tool with `dotnet run` from the project folder. Because the loop ends on `n`, you can test
> the whole path in one session without restarting the process.
