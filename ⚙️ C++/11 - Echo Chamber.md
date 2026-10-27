# 11. Echo Chamber

**Spanish version:** [11 - Cámara de Eco](./11%20-%20C%C3%A1mara%20de%20Eco.md)

**Course:** C++
**Chapter:** 2 — Raw Values
**Topic:** Chaining insertions into one output line
**Tags:** `#cpp` `#output` `#formatting`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-2-7C5CFF?style=for-the-badge" alt="Chapter 2">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

The engine log needs one line per event: a tag, an identifier, a message. One statement per line is
fine, but chaining does it in one, and it is how every log line you will read is written.

```cpp
#include <iostream>
#include <string>

int main() {
  std::string tag = "SPAWN";
  int entity_id = 42;
  double x = 118.5;

  std::cout << "[" << tag << "] id=" << entity_id << " x=" << x << "\n";
  std::cout << "[" << tag << "]" << " id=" << entity_id << "\n";
}
```

## Output

```text
[SPAWN] id=42 x=118.5
[SPAWN] id=42
```

Look at the first line closely: the spaces you see are the ones inside the literals. C++ inserts
nothing on its own.

## Why `<<` can repeat

`std::cout << value` returns the stream itself. That is what lets you write
`std::cout << a << b`: the first insertion hands the stream to the second. The operator is left
associative, so it reads left to right.

| Written | Reads as | Prints |
| :--- | :--- | :--- |
| `"a" << 1 << 2` | `(("a" << 1) << 2)` | `a12` |
| `"a" << " " << 1` | `(("a" << " ") << 1)` | `a 1` |

> [!TIP]
> Put the separators in the literal — `" id="` — rather than as their own `<< " "`. Fewer insertions,
> fewer chances to forget one, and the spacing is visible where you wrote it.

> [!NOTE]
> This same chaining is what makes `std::cout << a + b` different from `std::cout << a << b`. The
> first inserts a number, the second inserts two values glued together with no separator.

---

**Next:** [[12 - Speak to the Machine]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
