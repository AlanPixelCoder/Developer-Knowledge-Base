# 50. The Empty Handle

**Spanish version:** [50 - El Asa Vacía](./50%20-%20El%20Asa%20Vac%C3%ADa.md)

**Course:** C++
**Chapter:** 8 — Memory
**Topic:** Null checks, dangling pointers, and ownership
**Tags:** `#cpp` `#pointers` `#nullptr`

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

The spawner keeps a pointer to the current boss. Before the boss appears that pointer is null; after
the boss dies the memory is gone but the pointer is not. Two different failures, one handle.

```cpp
#include <iostream>
#include <string>

struct Entity {
  std::string name;
  int hp;
};

Entity* find_boss(bool spawned) {
  static Entity warden{"warden", 300};
  return spawned ? &warden : nullptr;
}

int main() {
  Entity* boss = find_boss(false);

  if (boss != nullptr) {
    std::cout << boss->name << "\n";
  } else {
    std::cout << "no boss yet\n";
  }

  boss = find_boss(true);
  std::cout << "found: " << boss->name << "\n";

  Entity* owned = new Entity{"echo", 40};
  delete owned;
  owned = nullptr;                 // stop using the old address

  if (owned == nullptr) {
    std::cout << "handle cleared\n";
  }
}
```

## Output

```text
no boss yet
found: warden
handle cleared
```

## Two ways a handle lies

| Failure | What it means | How to avoid |
| :--- | :--- | :--- |
| Null dereference | the handle points at nothing | check before `->` |
| Dangling pointer | the object is gone, the address is not | `delete` then set `nullptr` |

A dangling pointer is worse than a null one: the check `p != nullptr` passes, and the read reaches
freed memory.

## Ownership decides the rules

Whoever calls `new` must call `delete`. If a function returns a pointer, the caller has to know
whether it owns the object or is merely borrowing it — and that is exactly the question a raw pointer
cannot answer.

> [!CAUTION]
> Returning `&local` from a function returns a dangling pointer the moment it returns. The address
> looks valid; the object is gone. This is the single most common pointer bug in beginner code.

> [!TIP]
> `std::unique_ptr<Entity>` states "this handle owns the object" in the type, deletes it at scope
> exit, and cannot be copied by accident. Use raw pointers only to *observe*, never to own.

---

**Next:** [[51 - The Last Ember]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
