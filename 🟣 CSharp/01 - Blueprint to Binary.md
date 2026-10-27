# 01. Blueprint to Binary

**Spanish version:** [01 - Del Plano al Binario](./01%20-%20Del%20Plano%20al%20Binario.md)

**Course:** C#
**Topic:** C# lineage, .NET and the CLR, the compilation pipeline, and the shape of a console program
**Tags:** `#csharp` `#dotnet` `#clr`

Emberforge Atelier keeps its tools in C# because the studio's game runtime is C#: the console utilities
that balance *Ironledger* use the same language as the game, so a number validated in a script is a
number the runtime can use unchanged.

## From 1999 to now

C# appeared in 2000 as part of Microsoft's .NET initiative, designed by Anders Hejlsberg's team. Its
first internal name was **COOL** (*C-like Object Oriented Language*), dropped for trademark reasons.
The design goal was explicit: the syntax comfort of C++ with the memory safety of a managed runtime.

| Year | Milestone |
| :--- | :--- |
| 2000 | C# 1.0 with .NET Framework 1.0 |
| 2002 | Generics arrive in C# 2.0 |
| 2007 | LINQ and `var` in C# 3.0 |
| 2016 | .NET Core: cross-platform, open source |
| 2020 | .NET 5 unifies the runtime; later yearly releases (8, 9, 10) |

Today the language runs on Windows, macOS and Linux through .NET, and inside Unity and Godot for
games. That is why the studio picked it: one language for tools and runtime.

## Two compilations, not one

A `.cs` file is not executed. It is compiled twice:

| Stage | Produces | Done by |
| :--- | :--- | :--- |
| Source → IL | Common Intermediate Language, in a `.dll` | the C# compiler (`Roslyn`) |
| IL → native | machine code for the current CPU | the JIT, at run time |

The intermediate step is the reason the same `.dll` runs on a different processor: the JIT translates
it for that machine as the program starts, and the **CLR** (Common Language Runtime) supplies the
garbage collector, the type system and the exception machinery around it.

```csharp
using System;

class ForgeBoot
{
    static void Main()
    {
        Console.WriteLine("Emberforge Atelier - toolchain online");
        Console.WriteLine("Ironledger balance build 0.1");
    }
}
```

## Output

```text
Emberforge Atelier - toolchain online
Ironledger balance build 0.1
```

## Reading the program

| Piece | Meaning |
| :--- | :--- |
| `using System;` | makes `Console` visible without its namespace prefix |
| `class ForgeBoot` | every statement lives inside a type |
| `static void Main()` | the entry point the CLR looks for |
| `Console.WriteLine(...)` | writes one line and moves to the next |
| `;` | ends a statement |

`Main` can return `int` when the exit code matters to a build script, and it can take
`string[] args` to read command-line arguments. Start with the `void` form; add the rest when a tool
needs it.

## Running it

```bash
dotnet new console -o forgeboot
cd forgeboot
dotnet run
```

`dotnet run` compiles and executes in one step. For a script you are iterating on, that loop —
edit, run, read — is the whole workflow.

> [!NOTE]
> Modern C# also allows **top-level statements**: the body of `Main` written directly in
> `Program.cs`, with no class. It is fine for a throwaway script and confusing in a project where
> several files define methods. The notes in this module use the explicit class form so that every
> example shows where the code lives.

> [!TIP]
> The file name does not have to match the class name in a console app, but keeping them aligned
> (`ForgeBoot.cs` holding `ForgeBoot`) means the file you are looking for is the file you guessed.

## What this note is not

It is not a history lesson. The pipeline matters because it explains three things you will meet
constantly: why a build error and a runtime error look different, why `dotnet run` is slower the first
time, and why a stack trace names a line in a file you can open.

---

**Next:** [[02 - Typed Blueprints]]
