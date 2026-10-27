# 05. Sign Bunny

**Spanish version:** [05 - Conejito de Señalización.md](./05%20-%20Conejito%20de%20Se%C3%B1alizaci%C3%B3n.md)

**Course:** C++
**Topic:** Chapter 1 Recap & ASCII Art
**Tags:** `#cpp` `#recap` `#ascii`

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

## Chapter 1 Recap

- The `std::cout` statement outputs messages to the terminal.
- C++ code runs one line at a time, from top to bottom.
- Single line comments are created using `//`.
- Multi-line comments are started by `/*` and closed with `*/`.
- `\n` breaks the line; `\t` inserts a tab.

## ASCII Art

Terminal art is built from plain characters. The difficulty is not the code — it's escaping the
characters that mean something to C++ (`\`, `"`). Each backslash you want to *print* must be
written as `\\`, and each quote as `\"`.

```cpp
// Sign Bunny 🐰
// Emberfall tavern notice board

#include <iostream>

int main() {
  std::cout << "  (\\_/)" << "  +------------------+\n";
  std::cout << "  (o.o )" << "  | THANK YOU        |\n";
  std::cout << "  ( > <)" << "  | 4 BEING HERE     |\n";
  std::cout << "          +------------------+\n";
}
```

> [!TIP]
> Build ASCII art in a plain text file first, then escape it. Trying to draw and escape at the
> same time is how the bunny ends up with three ears.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
