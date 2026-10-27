# 02. First Light

**Spanish version:** [02 - Primera Luz](./02%20-%20Primera%20Luz.md)

**Course:** C++
**Chapter:** 1 — First Boot
**Topic:** Printing to the console with std::cout
**Tags:** `#cpp` `#output` `#iostream`

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

The engine console is useless until it can talk. The first thing it does on every launch is print a
boot banner, and that banner is made of three instructions that all look the same:

```cpp
#include <iostream>

int main() {
  std::cout << "Emberfall engine console\n";
  std::cout << "build 0.1.0\n";
  std::cout << "status: ready\n";
}
```

## Reading the line from right to left

| Piece | Name | What it does |
| :--- | :--- | :--- |
| `std::cout` | character output stream | The console's outgoing pipe |
| `<<` | insertion operator | Pushes the value on its right into the stream on its left |
| `"..."` | string literal | Exactly the characters between the quotes |
| `;` | terminator | Ends the statement — the compiler will not guess |

`std::` means *standard library*: `cout` lives in a namespace, and the prefix says where to find it.

## Output

```text
Emberfall engine console
build 0.1.0
status: ready
```

Three separate statements, three lines, because each string ends with `\n`.

> [!TIP]
> `\n` inside the string and `std::endl` after it both break the line. Prefer `\n`: `endl` also
> flushes the buffer, which is a cost you rarely need in a log line.

> [!WARNING]
> A missing `;` is reported on the **next** line, because that is where the compiler gives up. When
> the error points at a line that looks perfectly fine, check the one above it.

---

**Next:** [[03 - The Skeleton File]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
