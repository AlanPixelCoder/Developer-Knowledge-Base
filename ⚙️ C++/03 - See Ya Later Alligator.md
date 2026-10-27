# 03. See Ya Later Alligator

**Spanish version:** [03 - Nos Vemos Más Tarde, Cocodrilo.md](./03%20-%20Nos%20Vemos%20M%C3%A1s%20Tarde%2C%20Cocodrilo.md)

**Course:** C++
**Topic:** Structure, Code Blocks, and Escape Sequences
**Tags:** `#cpp` `#structure` `#escape-sequences`

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

## Program Structure

| Element | Role |
| :--- | :--- |
| **`#include <iostream>`** | Includes the library needed for input/output |
| **`int main()`** | The **function** where every program starts |
| **`{ }`** | The **code block**: everything inside runs as one unit |

C++ runs one line at a time, from top to bottom of the file. We can output multiple messages by using multiple `std::cout` statements.

## Escape Sequences

An **escape sequence** is a backslash followed by a character that the compiler interprets instead of printing literally.

| Sequence | Effect |
| :--- | :--- |
| `\n` | New line |
| `\t` | Horizontal tab |
| `\"` | A literal double quote |
| `\\` | A literal backslash |

The `\n` is the workhorse: it creates a new line in a text, so the output appears on a second line.

```cpp
#include <iostream>

int main() {
  std::cout << "Goodbye!\nAdiós!\nCiao!\nAu revoir!\nSee ya later!";
}
```

> [!TIP]
> One `std::cout` with four `\n` beats four separate statements — fewer lines, same output,
> and one less place for a typo to hide.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
