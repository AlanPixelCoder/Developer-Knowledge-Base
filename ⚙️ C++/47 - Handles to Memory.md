# 47. Handles to Memory

**Spanish version:** [47 - Asas a la Memoria](./47%20-%20Asas%20a%20la%20Memoria.md)

**Course:** C++
**Chapter:** 8 — Memory
**Topic:** new and delete, and why containers usually replace them
**Tags:** `#cpp` `#pointers` `#new-delete`

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

A spawner creates entities while the level is running. The number is not known when the code is
written, so the object cannot live on the stack of `main`. `new` asks the heap for exactly enough
room and hands back a handle.

```cpp
#include <iostream>
#include <string>

struct Entity {
  std::string name;
  int hp;
};

int main() {
  Entity* boss = new Entity{"warden", 250};

  std::cout << boss->name << " hp " << boss->hp << "\n";

  boss->hp -= 40;
  std::cout << "after a hit: " << (*boss).hp << "\n";

  delete boss;
  boss = nullptr;

  std::cout << "handle now: " << (boss == nullptr) << "\n";
}
```

## Output

```text
warden hp 250
after a hit: 210
handle now: 1
```

## `new`, `->`, `delete`

| Form | Means |
| :--- | :--- |
| `new Entity{...}` | allocate one object on the heap, return its address |
| `p->field` | shorthand for `(*p).field` |
| `delete p` | destroy the object and return the memory |
| `delete p; p = nullptr;` | also removes the dangling handle |

## The three rules that come with `new`

1. Every `new` needs exactly one `delete`.
2. `delete[]` for arrays, `delete` for single objects — mixing them is undefined behaviour.
3. After `delete`, the pointer still holds the old address. Drop it or set it to `nullptr`.

> [!CAUTION]
> Deleting twice corrupts the allocator, and the crash usually happens later, in unrelated code. The
> fix is not a second check — it is to not own raw memory by hand.

> [!TIP]
> `std::vector<Entity> entities;` allocates on the heap, grows, and frees itself at scope exit. Reach
> for `new` only when you are implementing a container or interoperating with an API that demands it.

---

**Next:** [[48 - Reaching Through the Handle]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
