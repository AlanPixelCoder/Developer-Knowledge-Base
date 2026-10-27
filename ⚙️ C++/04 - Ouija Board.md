# 04. Ouija Board

**Spanish version:** [04 - Tabla Ouija.md](./04%20-%20Tabla%20Ouija.md)

**Course:** C++
**Topic:** Single Line and Multi-line Comments
**Tags:** `#cpp` `#comments` `#documentation`

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

In programming, comments are important because they are used to document what our code does, for ourselves and other developers. They can also be used to disable parts of a program. When the program is run, comments are completely **ignored** by the compiler.

## Single Line Comments

Create a single line comment using `//`. Everything to the right of the `//` on the same line is ignored.

```cpp
int hp = 100; // the hero's starting health
```

## Multi-line Comments

Start with `/*` and end with `*/`. Everything in between is commented out, so a multi-line comment can be as long as you want.

```cpp
/*
  Emberfall combat prototype
  Phase 1: turn order
  Phase 2: damage resolution
*/
```

## Example

```cpp
// Ouija Board 👻
// Emberfall scrying table

#include <iostream>

int main() {
  std::cout << "------------------------------\n";
  std::cout << "|       x YES   NO x         |\n";
  std::cout << "|                            |\n";
  std::cout << "|       ABCDEFGHIJKLM        |\n";
  std::cout << "|       NOPQRSTUVWXYZ        |\n";
  std::cout << "|                            |\n";
  std::cout << "|       1234567890           |\n";
  std::cout << "------------------------------\n";
}
```

> [!NOTE]
> **Commented-out code is a smell, not a strategy**
> Keep a dead line commented for a minute if you're comparing two approaches. If it survives
> the commit, delete it — version control already remembers it for you.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
