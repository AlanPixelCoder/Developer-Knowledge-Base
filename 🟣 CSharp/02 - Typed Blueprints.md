# 02. Typed Blueprints

**Spanish version:** [02 - Planos Tipados](./02%20-%20Planos%20Tipados.md)

**Course:** C#
**Topic:** Static typing, value vs reference types, conversions, string immutability, var and const
**Tags:** `#csharp` `#types` `#casting`

Every field in the Ironledger loadout table declares what it holds. The compiler reads that
declaration and refuses the file if the code contradicts it — before the tool ever runs.

## Static typing means the compiler checks

```csharp
int armour = 12;
double weight = 3.75;
char grade = 'B';
bool equipped = true;
string name = "riveted cuirass";
```

| Type | Holds | Size | Default |
| :--- | :--- | :--- | :--- |
| `int` | whole numbers, ±2.1 billion | 4 bytes | `0` |
| `long` | whole numbers, ±9.2 quintillion | 8 bytes | `0` |
| `double` | decimals, 15–17 significant digits | 8 bytes | `0` |
| `decimal` | decimals, exact, for money | 16 bytes | `0` |
| `char` | one UTF-16 character | 2 bytes | `'\0'` |
| `bool` | `true` / `false` | 1 byte | `false` |
| `string` | text, immutable | reference | `null` |

`decimal` exists for currency because `0.1 + 0.2` in `double` is not exactly `0.3`. A shop total
computed in `double` will disagree with the receipt; a shop total in `decimal` will not.

## Value and reference types

| Kind | Examples | Assignment copies |
| :--- | :--- | :--- |
| Value type | `int`, `double`, `bool`, `char`, `struct` | the value itself |
| Reference type | `string`, arrays, classes, `List<T>` | the reference |

```csharp
int a = 5;
int b = a;      // b is a separate 5
b = 9;
Console.WriteLine(a);   // 5

int[] first = { 1, 2, 3 };
int[] second = first;   // same array, second name
second[0] = 99;
Console.WriteLine(first[0]);   // 99
```

The second block is the one that bites: two names, one array. Copying an array needs
`(int[])first.Clone()` or `Array.Copy`.

## Conversions

| From → To | Kind | Syntax |
| :--- | :--- | :--- |
| `int` → `double` | implicit, widening | `double d = n;` |
| `double` → `int` | explicit, truncates | `int i = (int)d;` |
| `string` → `int` | parse, can fail | `int.Parse(s)` / `int.TryParse(s, out i)` |
| anything → `string` | formatting | `value.ToString()` |

```csharp
double weight = 3.79;
int whole = (int)weight;          // 3, truncated toward zero

int parsed;
bool ok = int.TryParse("42", out parsed);
Console.WriteLine($"{whole} {ok} {parsed}");
```

## Output

```text
3 True 42
```

`(int)` never rounds and never throws; it truncates. `int.Parse` throws `FormatException` on junk, so
`TryParse` — which returns a `bool` and writes the result through `out` — is the version you want for
anything typed by a person.

## Strings are immutable

```csharp
string tag = "iron";
tag += "ledger";        // a NEW string; the old one is garbage
Console.WriteLine(tag);
```

Every apparent edit builds a new string. In a loop that concatenates a thousand lines this is
quadratic; `StringBuilder` is the tool for that, and this note is where you learn why it exists.

## `var` and `const`

```csharp
var roster = new List<string>();   // type inferred at compile time: List<string>
const int MaxSlots = 8;            // compile-time constant, cannot change
```

`var` is not "no type": the type is fixed at the declaration, inferred from the right-hand side.
`const` must be a literal known at compile time; `readonly` covers the case where the value is
computed once per object instead.

> [!WARNING]
> `var` with a literal is a guessing game: `var ratio = 3 / 2;` is an `int` holding `1`, not a
> `double` holding `1.5`. Write the type when the right-hand side does not make it obvious.

> [!TIP]
> Prefer `double` for physics and `decimal` for money. Mixing them forces a cast and a rounding
> decision at every boundary, and that decision is easier to make once, in the type, than in ten
> expressions.

---

**Next:** [[03 - Triage Logic]]
