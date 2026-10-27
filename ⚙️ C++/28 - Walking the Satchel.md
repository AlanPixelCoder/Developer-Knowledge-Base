# 28. Walking the Satchel

**Spanish version:** [28 - Recorrer la Alforja](./28%20-%20Recorrer%20la%20Alforja.md)

**Course:** C++
**Chapter:** 5 — Collections
**Topic:** Range-for and index loops over a vector
**Tags:** `#cpp` `#vector` `#range-for`

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

Printing every stack means visiting every index. Two loops do it; they differ in what they give you
inside the body.

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<std::string> satchel{"torch", "rope", "bread"};
  std::vector<int> stacks{2, 5, 1};

  std::cout << "index loop:\n";
  for (std::size_t i = 0; i < satchel.size(); i++) {
    std::cout << "  " << i << ": " << satchel[i] << "\n";
  }

  std::cout << "range loop:\n";
  for (const std::string& item : satchel) {
    std::cout << "  " << item << "\n";
  }

  int total = 0;
  for (int n : stacks) {
    total += n;
  }
  std::cout << "total stacks: " << total << "\n";
}
```

## Output

```text
index loop:
  0: torch
  1: rope
  2: bread
range loop:
  torch
  rope
  bread
total stacks: 8
```

## Which loop to reach for

| You need | Loop |
| :--- | :--- |
| Every element, no index | `for (const auto& x : v)` |
| The index too | `for (std::size_t i = 0; i < v.size(); i++)` |
| To modify each element | `for (auto& x : v)` |
| To stop early on a condition | index loop with `break` |

`std::size_t` is the type `size()` returns. Using `int` triggers a signed/unsigned comparison warning
under `-Wextra`.

## `&` is not decoration

`for (const std::string& item : satchel)` binds a reference: no copy per pass. Without the `&`, a
fresh string is copied for every element, which is invisible in a three-item example and expensive
in a thousand-item one.

> [!IMPORTANT]
> Drop `const` and add `&` to modify in place: `for (auto& x : v) { x *= 2; }`. Without the `&` you
> modify a copy and the vector never changes.

> [!TIP]
> Range-for cannot give you the index. If the output needs numbering, use the index loop; do not
> invent a manual counter next to a range-for.

---

**Next:** [[29 - The Alchemist's Tally]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
