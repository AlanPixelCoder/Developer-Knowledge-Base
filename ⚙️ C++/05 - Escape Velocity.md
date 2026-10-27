# 05. Escape Velocity

**Spanish version:** [05 - Velocidad de Escape](./05%20-%20Velocidad%20de%20Escape.md)

**Course:** C++
**Chapter:** 1 — First Boot
**Topic:** Escaping backslashes and quotes, and drawing with text
**Tags:** `#cpp` `#strings` `#ascii-art`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-1-7C5CFF?style=for-the-badge" alt="Chapter 1">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

The console banner needs a frame. Frames are built from characters that mean something else inside a string literal, so before you can
frame a banner you have to learn to neutralise them. Only two characters need the treatment: the
backslash and the double quote.

```cpp
#include <iostream>

int main() {
  std::cout << "************************\n";
  std::cout << "*  EMBERFALL  ENGINE   *\n";
  std::cout << "*  \"it compiles!\"      *\n";
  std::cout << "*  path: C:\\ember      *\n";
  std::cout << "************************\n";
}
```

## The escape table

| You want to print | You must write | Because |
| :--- | :--- | :--- |
| `\` | `\\` | A single backslash starts an escape sequence |
| `"` | `\"` | A bare quote ends the string early |
| new line | `\n` | The escape for a line break |
| tab | `\t` | The escape for a tab |

## Output

```text
************************
*  EMBERFALL  ENGINE   *
*  "it compiles!"      *
*  path: C:\ember      *
************************
```

> [!WARNING]
> An escape C++ does not recognise — `\d`, for instance — usually still compiles: the compiler warns
> and then prints the bare character. Compile with `-Wall` and read the warning instead of blaming
> the terminal.

> [!TIP]
> For heavy art, use a raw string: `R"(...)"` keeps every backslash literal, so a whole banner can
> be pasted without touching it. The parentheses are part of the syntax.

> [!NOTE]
> Every `\n` in this lesson sits **inside** the quotes. Outside them it is not an escape, it is a
> syntax error waiting for a compiler message.

---

**Next:** [[06 - From Source to Switch]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
