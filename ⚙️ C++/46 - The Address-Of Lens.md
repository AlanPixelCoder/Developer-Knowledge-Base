# 46. The Address-Of Lens

**Spanish version:** [46 - La Lente Dirección-De](./46%20-%20La%20Lente%20Direcci%C3%B3n-De.md)

**Course:** C++
**Chapter:** 8 — Memory
**Topic:** Pointers: taking an address, dereferencing, and null
**Tags:** `#cpp` `#pointers` `#memory`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Chapter-8-7C5CFF?style=for-the-badge" alt="Chapter 8">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

A pointer is a number that names a place. `&` asks for the place, `*` reads through it. Two operators,
one idea: the pointer is not the value, it is the label on the shelf.

```cpp
#include <iostream>

int main() {
  int hp = 30;
  int* handle = &hp;

  std::cout << "value:      " << hp << "\n";
  std::cout << "address:    " << handle << "\n";
  std::cout << "through it: " << *handle << "\n";

  *handle = 12;             // writes hp, not a copy
  std::cout << "hp now:     " << hp << "\n";

  int* nothing = nullptr;
  std::cout << "null?       " << (nothing == nullptr) << "\n";
  std::cout << "null print: " << nothing << "\n";
}
```

## Output

A sample run — your addresses will differ:

```text
value:      30
address:    0x7ff7b6f0a5ac
through it: 30
hp now:     12
null?       1
null print: 0
```

## The two operators

| Symbol | Name | Meaning |
| :--- | :--- | :--- |
| `&x` | address-of | a pointer to `x` |
| `*p` | dereference | the object `p` points at |
| `int*` | pointer type | "pointer to int" |

`*` in a declaration means "this is a pointer". `*` in an expression means "go there". Same glyph,
opposite direction, and one of C++'s few genuinely confusing inheritances.

## `nullptr` is a value, not an address

`nullptr` means "points at nothing". Dereferencing it is undefined behaviour — usually a crash,
sometimes worse. `std::cout << nullptr` is defined: it prints `0` through the `void*` overload.

> [!CAUTION]
> A pointer that has never been assigned holds garbage, not `nullptr`. `int* p;` then `*p = 5;` writes
> to a random address. Always initialise: `int* p = nullptr;` or straight to a real object.

> [!TIP]
> `const int* p` cannot change the value; `int* const p` cannot change the pointer. Read the
> declaration right-to-left: "p is a const pointer to int" versus "p is a pointer to const int".

---

**Next:** [[47 - Handles to Memory]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
