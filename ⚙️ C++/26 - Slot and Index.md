# 26. Slot and Index

**Spanish version:** [26 - Ranura e Índice](./26%20-%20Ranura%20e%20%C3%8Dndice.md)

**Course:** C++
**Chapter:** 5 — Collections
**Topic:** Reading and writing elements, and what operator[] does not check
**Tags:** `#cpp` `#vector` `#indexing`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-5-7C5CFF?style=for-the-badge" alt="Chapter 5">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

The satchel has eight slots. Reading slot 3 is one line; writing slot 3 is the same line on the left
of an equals sign. Reading slot 8 is undefined behaviour, and the compiler will not say a word.

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<std::string> slots(3, "empty");

  slots[1] = "torch";
  slots[2] = "rope";

  std::cout << "slot 0: " << slots[0] << "\n";
  std::cout << "slot 1: " << slots[1] << "\n";
  std::cout << "slot 2: " << slots[2] << "\n";
  std::cout << "count:  " << slots.size() << "\n";
}
```

## Output

```text
slot 0: empty
slot 1: torch
slot 2: rope
count:  3
```

## Index rules

| Fact | Value |
| :--- | :--- |
| First index | `0` |
| Last index | `size() - 1` |
| Valid for size 3 | `0`, `1`, `2` |
| Checked by `[]` | nothing |

`slots.at(5)` throws `std::out_of_range`. `slots[5]` reads whatever memory happens to be there. Use
`[]` when the index is provably in range, `at()` when it comes from input.

## A slot is a variable

Anything you can do with an `int` variable you can do with `slots[0]`: assign it, print it, compare
it, pass it to a function. The index is just the address arithmetic in disguise.

> [!WARNING]
> Out-of-range `[]` is undefined behaviour, not an error message. The program may print garbage,
> crash later, or appear to work until the demo. `at()` costs a bounds check and buys a diagnosis.

> [!TIP]
> Negative indices do not wrap around in a vector the way they do in Python. `slots[-1]` is
> out-of-range, and with an unsigned conversion it is very out-of-range.

---

**Next:** [[27 - Pack and Unpack]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
