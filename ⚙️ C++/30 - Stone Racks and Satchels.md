# 30. Stone Racks and Satchels

**Spanish version:** [30 - Estantes de Piedra y Alforjas](./30%20-%20Estantes%20de%20Piedra%20y%20Alforjas.md)

**Course:** C++
**Chapter:** 5 — Collections
**Topic:** C-style arrays next to vectors: when each one is the right tool
**Tags:** `#cpp` `#array` `#vector`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Chapter-5-7C5CFF?style=for-the-badge" alt="Chapter 5">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

The forge has a fixed rack of six stone slots carved into the wall, and a satchel that stretches. One
cannot change size, the other can — and that single difference decides most of your choices.

```cpp
#include <iostream>
#include <vector>

int main() {
  int rack[6] = {40, 12, 0, 7, 33, 8};  // fixed: six stones, forever

  int total = 0;
  for (int i = 0; i < 6; i++) {
    total += rack[i];
  }

  std::vector<int> satchel{total};      // grows when the forge yields more
  satchel.push_back(95);

  std::cout << "rack stones:    " << sizeof(rack) / sizeof(rack[0]) << "\n";
  std::cout << "rack total:     " << total << "\n";
  std::cout << "satchel stones: " << satchel.size() << "\n";
  std::cout << "satchel last:   " << satchel.back() << "\n";
}
```

## Output

```text
rack stones:    6
rack total:     100
satchel stones: 2
satchel last:   95
```

## Two containers, two promises

| Question | `int rack[6]` | `std::vector<int>` |
| :--- | :--- | :--- |
| Size known at compile time | yes | optional |
| Can grow | no | yes |
| Knows its own size | no (`sizeof` trick) | `size()` |
| Copies with `=` | no (decays to a pointer) | yes |
| Passes to a function safely | only as a pointer, size lost | by value or reference |

## The `sizeof` trick

`sizeof(rack)` is the whole array in bytes; `sizeof(rack[0])` is one element. Divide and you get the
count — but only where the array type is still visible. Inside a function that received `rack`, it
has already decayed to a pointer and the division returns nonsense.

> [!CAUTION]
> Passing an array to a function loses its size. `void f(int rack[6])` declares `void f(int* rack)`.
> The `6` is documentation, not a promise. Prefer `std::array<int, 6>` or a vector.

> [!TIP]
> Use a fixed array when the count really is a compile-time constant and you never pass it across a
> function boundary. Otherwise a vector costs one pointer and saves a class of bugs.

---

**Next:** [[31 - One Spell, Many Casts]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
