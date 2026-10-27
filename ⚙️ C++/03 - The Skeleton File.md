# 03. The Skeleton File

**Spanish version:** [03 - El Archivo Esqueleto](./03%20-%20El%20Archivo%20Esqueleto.md)

**Course:** C++
**Chapter:** 1 — First Boot
**Topic:** Includes, main, braces and escape sequences
**Tags:** `#cpp` `#structure` `#escape-sequences`

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

Almost every C++ program starts from the same skeleton. Learn it once and you stop reading it and
start reading what changed.

```cpp
#include <iostream>

int main() {
  std::cout << "slot\tname\tstate\n";
  std::cout << "01\tlantern\tlit\n";
  std::cout << "02\tgate\tsealed\n";
}
```

## The five pieces

| Line | Piece | What it contributes |
| :--- | :--- | :--- |
| `#include <iostream>` | preprocessor directive | Copies the declarations for input/output into this unit |
| `int main()` | entry point | Where execution begins; returns an `int` to the shell |
| `{` `}` | block | Everything between them is the body of `main` |
| `std::cout <<` | statement | One action: send text to the console |
| `\t`, `\n` | escape sequences | A tab and a newline, inside a plain string |

The include is not a library import at runtime. It is a **copy-paste performed before compilation**:
the header's declarations land at the top of your file.

## Output

```text
slot	name	state
01	lantern	lit
02	gate	sealed
```

The tabs line the columns up, which is exactly what a console table needs before you learn to
format properly.

> [!NOTE]
> C++ ignores indentation and line breaks. Braces decide structure. The formatting is for humans,
> and every style guide in the world has an opinion about it.

> [!WARNING]
> Two backslashes, quotes and control characters are where beginners lose an hour: `\n` is a
> newline, but `\\n` is a literal backslash followed by `n`. See [[05 - Escape Velocity]].

---

**Next:** [[04 - Notes in the Margin]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
