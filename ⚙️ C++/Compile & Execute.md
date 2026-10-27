# Compile & Execute

**Spanish version:** [Compilar y Ejecutar.md](./Compilar%20y%20Ejecutar.md)

**Course:** C++
**Topic:** Compilers, Source Code, and Terminal Execution
**Tags:** `#cpp` `#compiler` `#terminal` `#execution`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

## What is compilation?

C++ is a **compiled language**. To get a program to run, you must first translate it from a
human-readable form (**source code**) into something the machine understands (**machine code** or
an **executable**). That translation is done by a **compiler**.

The whole process looks like this:

1. Write some code.
2. Save the program.
3. Compile & execute.
4. Repeat.

| File | Extension | Readable by |
| :--- | :--- | :--- |
| Source code | `.cpp` | Humans |
| Machine code | `.out` (or no extension) | The CPU |

## Running in the terminal

### Compile

```bash
g++ hello.cpp
```

This creates a machine code file usually called `a.out`.

### Execute

```bash
./a.out
```

### Naming your executable

```bash
g++ hello.cpp -o hello
./hello
```

> [!TIP]
> In Emberfall terms: writing `.cpp` is forging your spellbook, compiling is enchanting it, and
> executing is casting it in the terminal arena.

> [!NOTE]
> **See the warnings**
> `g++ -Wall -Wextra -std=c++17 file.cpp -o file` surfaces suspicious comparisons, unused variables
> and silent mistakes like `=` where you meant `==`. The default compiler flags tell you almost
> nothing on purpose.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
