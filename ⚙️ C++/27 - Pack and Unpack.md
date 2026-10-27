# 27. Pack and Unpack

**Spanish version:** [27 - Cargar y Descargar](./27%20-%20Cargar%20y%20Descargar.md)

**Course:** C++
**Chapter:** 5 — Collections
**Topic:** push_back, pop_back, and the size that follows them
**Tags:** `#cpp` `#vector` `#push-back`

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

Loot arrives one item at a time and leaves one item at a time. The satchel has no fixed length, so
both ends move.

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<std::string> satchel;

  satchel.push_back("torch");
  satchel.push_back("rope");
  satchel.push_back("bread");

  std::cout << "after packing:  " << satchel.size() << "\n";
  std::cout << "top item:       " << satchel.back() << "\n";

  satchel.pop_back();

  std::cout << "after unpacking: " << satchel.size() << "\n";
  std::cout << "top item:       " << satchel.back() << "\n";
}
```

## Output

```text
after packing:  3
top item:       bread
after unpacking: 2
top item:       rope
```

## Growing and shrinking

| Call | Effect | Cost |
| :--- | :--- | :--- |
| `push_back(x)` | append `x` at the end, size + 1 | amortised constant |
| `pop_back()` | remove last element, size − 1 | constant |
| `back()` | read the last element | constant |
| `clear()` | remove everything, size 0 | linear |

The vector keeps a capacity larger than its size so that most `push_back` calls do not reallocate.
That is why the cost is "amortised" and not "free".

## The empty trap

`pop_back()` on an empty vector and `back()` on an empty vector are both undefined behaviour. The
guard costs one comparison:

```cpp
if (!satchel.empty()) {
  satchel.pop_back();
}
```

> [!CAUTION]
> `pop_back()` returns nothing. It removes the element and throws it away. To keep the value, read
> `satchel.back()` first, then pop.

> [!TIP]
> `push_back` is the natural way to build a collection of unknown length. Reserve a size only when
> you already know it and the reallocation shows up in a profile.

---

**Next:** [[28 - Walking the Satchel]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
