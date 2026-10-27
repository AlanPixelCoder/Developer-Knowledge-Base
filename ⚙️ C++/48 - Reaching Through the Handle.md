# 48. Reaching Through the Handle

**Spanish version:** [48 - Alcanzar a Través del Asa](./48%20-%20Alcanzar%20a%20Trav%C3%A9s%20del%20Asa.md)

**Course:** C++
**Chapter:** 8 — Memory
**Topic:** Pointers as parameters: the object, not a copy
**Tags:** `#cpp` `#pointers` `#functions`

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

The spawner must fill in an entity that already exists. Passing the struct by value hands over a copy
and the original stays untouched — which is exactly what happened to the first version of this
system.

```cpp
#include <iostream>
#include <string>

struct Entity {
  std::string name;
  int hp;
};

void damage_by_value(Entity e) {
  e.hp -= 30;
}

void damage_by_pointer(Entity* e) {
  if (e == nullptr) {
    return;
  }
  e->hp -= 30;
}

void damage_by_reference(Entity& e) {
  e.hp -= 30;
}

int main() {
  Entity target{"warden", 100};

  damage_by_value(target);
  std::cout << "after value:     " << target.hp << "\n";

  damage_by_pointer(&target);
  std::cout << "after pointer:   " << target.hp << "\n";

  damage_by_reference(target);
  std::cout << "after reference: " << target.hp << "\n";
}
```

## Output

```text
after value:     100
after pointer:   70
after reference: 40
```

## Three ways to pass an entity

| Signature | Call site | Modifies caller? | Can be "nothing"? |
| :--- | :--- | :--- | :--- |
| `Entity e` | `f(target)` | no | no |
| `Entity* e` | `f(&target)` | yes | yes, `nullptr` |
| `Entity& e` | `f(target)` | yes | no |

A reference is a pointer that cannot be null and needs no `&` at the call site. A pointer is for when
"absent" is a real possibility — an optional target, a not-yet-spawned boss.

## The null check is the price

`damage_by_pointer` opens with `if (e == nullptr) return;`. A reference version cannot be called with
nothing, so it does not need the check. That is the whole trade: a null check in exchange for
expressiveness at the call site.

> [!IMPORTANT]
> `&target` in the call is the address-of operator; `Entity*` in the signature is the pointer type.
> Both use `&` and `*`, and neither is the same glyph usage as inside the function body.

> [!TIP]
> Default to references (`Entity&`) for "must exist" and pointers (`Entity*`) for "may be missing".
> Passing by value is right only for small types you intend to copy.

---

**Next:** [[49 - Aliases vs Handles]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
