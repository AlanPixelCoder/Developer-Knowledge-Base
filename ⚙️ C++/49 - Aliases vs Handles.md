# 49. Aliases vs Handles

**Spanish version:** [49 - Alias vs Asas](./49%20-%20Alias%20vs%20Asas.md)

**Course:** C++
**Chapter:** 8 — Memory
**Topic:** When a reference is better than a pointer
**Tags:** `#cpp` `#references` `#memory`

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

Two names for one entity. The difference between a reference and a pointer is not syntax — it is a
promise: a reference always names something that exists, and it cannot be made to name something else.

```cpp
#include <iostream>
#include <string>

struct Entity {
  std::string name;
  int hp;
};

int main() {
  Entity warden{"warden", 120};

  Entity& alias = warden;      // another name, same object
  Entity* handle = &warden;    // a value holding the address

  alias.hp -= 20;

  std::cout << "warden:      " << warden.hp << "\n";
  std::cout << "via alias:   " << alias.hp << "\n";
  std::cout << "via handle:  " << handle->hp << "\n";
  std::cout << "same?        " << (&alias == handle) << "\n";

  Entity shade{"shade", 60};
  handle = &shade;             // a pointer can be reassigned
  std::cout << "handle now:  " << handle->name << "\n";
}
```

## Output

```text
warden:      100
via alias:   100
via handle:  100
same?        1
handle now:  shade
```

## What each one promises

| Property | `Entity&` | `Entity*` |
| :--- | :--- | :--- |
| Can be null | no | yes |
| Can be reseated | no | yes |
| Needs `*` or `->` | no | yes |
| Address exists | guaranteed | only after a check |

A reference is bound once, at creation, and lives with that binding. `Entity& alias = warden;` then
`alias = shade;` does not point the alias at `shade` — it **assigns shade's fields into warden**.

## The reassignment trap

That last line is the reason references are not just "nicer pointers". If you need to walk a list,
change which object you are looking at, or represent "none", a pointer is the honest choice. A
reference that appears to be reassigned is almost always a bug that compiles cleanly.

> [!WARNING]
> `&alias == handle` is `true` here, and it is also how you can prove to yourself that an alias really
> is the same object rather than a copy. Do not build logic on address comparisons; do use them while
> learning.

> [!TIP]
> Prefer `const Entity&` for parameters you only read: no copy, no null check, and the compiler
> enforces "read only" for you. Reach for a pointer when the answer to "which object?" can change.

---

**Next:** [[50 - The Empty Handle]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
