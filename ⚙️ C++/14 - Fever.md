# 14. Fever

**Spanish version:** [14 - Fiebre.md](./14%20-%20Fiebre.md)

**Course:** C++
**Topic:** `if` and `else` Statements
**Tags:** `#cpp` `#conditionals` `#if-else`

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

## The `if` Statement

An `if` statement tests a condition for truth:

- If the condition evaluates to `true`, the code in the `if` block runs.
- If it evaluates to `false`, the block is skipped.

The code "inside" the `if` should be indented (usually two spaces).

```cpp
if (temp >= 100) {
  std::cout << "You have a fever.\n";
}
```

## The `else` Clause

An `else` clause can optionally follow an `if`:

- Condition `true` → the `if` block runs.
- Condition `false` → the `else` block runs.

Exactly one of the two always executes. There is no path where both run, and no path where
neither runs.

```cpp
#include <iostream>

int main() {
  double temp = 98.6;

  if (temp >= 100) {
    std::cout << "You have a fever. 🤒\n";
  } else {
    std::cout << "You do not have a fever. 🌡️\n";
  }
}
```

> [!TIP]
> **Braces are not optional in practice**
> C++ lets you write a brace-less `if` for a single statement. Don't. The day you add a second
> line to that block, only the first one stays conditional — and the bug is invisible.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
