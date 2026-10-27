# 00b. Emberforge Field Manual

**Spanish version:** [00b - Manual de Campo de Emberforge](./00b%20-%20Manual%20de%20Campo%20de%20Emberforge.md)

**Course:** C#
**Topic:** One-page syntax reference for the whole module
**Tags:** `#csharp` `#reference` `#cheatsheet`

One page for the syntax this module uses, in the order the lessons introduce it. When a note and this
page disagree, the note is right — this page is the index, not the explanation.

## Types

| Type | Use | Default | Note |
| :--- | :--- | :--- | :--- |
| `int` | counts, hp | `0` | 32-bit |
| `long` | big counts | `0` | 64-bit |
| `double` | physics, ratios | `0` | binary floating point |
| `decimal` | currency | `0` | exact, slower |
| `char` | one character | `'\0'` | single quotes |
| `bool` | flags | `false` | `true` / `false` |
| `string` | text | `null` | immutable, double quotes |

## Declaration

```csharp
int hp = 30;
double ratio = 0.5;
string name = "riveted cuirass";
var slots = new List<string>();
const int MaxSlots = 8;
```

## Conversions

| From | To | Code |
| :--- | :--- | :--- |
| `int` | `double` | `double d = i;` |
| `double` | `int` | `int i = (int)d;` truncates |
| `string` | `int` | `int.TryParse(s, out int v)` |
| any | `string` | `v.ToString()` or `$"{v}"` |

## Operators

| Group | Symbols |
| :--- | :--- |
| Arithmetic | `+ - * / %` |
| Comparison | `== != < <= > >=` |
| Logical | `&& \|\| !` short-circuit |
| Assignment | `= += -= *= /=` |
| Increment | `++ --` |

## Control flow

```csharp
if (cond) { }
else if (cond) { }
else { }

switch (value)
{
    case 1: break;
    default: break;
}
```

## Loops

| Loop | Use |
| :--- | :--- |
| `while (cond)` | unknown count, check first |
| `do { } while (cond);` | at least one pass |
| `for (int i = 0; i < n; i++)` | known count |
| `foreach (var x in items)` | read every element |

`break` leaves, `continue` skips to the next pass.

## Arrays

```csharp
int[] a = new int[3];
int[] b = { 4, 8, 15 };
Console.WriteLine(b.Length);     // 3
Console.WriteLine(b[0]);         // 4
```

Valid indexes: `0` to `Length - 1`.

## Methods

```csharp
static int Total(int[] values)
{
    int sum = 0;
    foreach (int v in values) sum += v;
    return sum;
}

static void Report(int total) => Console.WriteLine(total);

if (int.TryParse(text, out int n)) { }
```

| Modifier | Direction |
| :--- | :--- |
| `out` | must be assigned inside |
| `ref` | read and write the caller's variable |

## Console

```csharp
Console.WriteLine("line");
Console.Write("prompt: ");
string? input = Console.ReadLine();
```

## Compile and run

```bash
dotnet new console -o tool
dotnet run
dotnet build
```

## Gotchas

| Trap | Fix |
| :--- | :--- |
| `3 / 2` is `1` | cast one side: `(double)3 / 2` |
| `array.Length` as index | last index is `Length - 1` |
| `a = b` with arrays | shares the array; clone for a copy |
| `int.Parse("abc")` | throws; prefer `TryParse` |
| `&&` versus `&` | `&` evaluates both sides |
| string `+=` in a loop | builds a new string each time; use `StringBuilder` |
---

**Start here:** [[01 - Blueprint to Binary]]
