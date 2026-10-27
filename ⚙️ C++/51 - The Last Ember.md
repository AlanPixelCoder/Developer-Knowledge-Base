# 51. The Last Ember

**Spanish version:** [51 - La Última Brasa](./51%20-%20La%20%C3%9Altima%20Brasa.md)

**Course:** C++
**Chapter:** 8 — Memory
**Topic:** Chapter 8 and course recap: memory chosen deliberately
**Tags:** `#cpp` `#recap` `#memory`

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

The console's last service reads the log, keeps the run's entities, and reports what survived. Every
line is a decision about where a value lives — and each decision is one you can now name.

```cpp
#include <iostream>
#include <memory>
#include <string>
#include <vector>

struct Entity {
  std::string name;
  int hp;
  bool alive() const { return hp > 0; }
};

int main() {
  std::vector<Entity> roster;                        // heap buffer, stack object
  roster.push_back({"warden", 0});
  roster.push_back({"cinder", 45});
  roster.push_back({"moss", 12});

  int survivors = 0;
  for (const Entity& e : roster) {                   // reference: no copy
    if (e.alive()) {
      survivors++;
    }
  }

  auto note = std::make_unique<std::string>("run closed");  // owned heap value

  Entity* seen = &roster.front();                    // observing pointer, no ownership
  std::string tallest = roster.back().name;          // a copy, deliberately

  std::cout << "survivors: " << survivors << "\n";
  std::cout << "first:     " << seen->name << "\n";
  std::cout << "last copy: " << tallest << "\n";
  std::cout << "note:      " << *note << "\n";
  std::cout << "handles:   " << (seen != nullptr) << " " << (note != nullptr) << "\n";
}
```

## Output

```text
survivors: 2
first:     warden
last copy: moss
note:      run closed
handles:   1 1
```

## Every line, justified

| Line | Storage | Why |
| :--- | :--- | :--- |
| `std::vector<Entity> roster` | object on stack, elements on heap | count unknown up front |
| `const Entity& e` | no storage | read-only access, no copy |
| `std::make_unique<std::string>` | heap, owned | lifetime longer than a block, single owner |
| `Entity* seen` | a pointer | borrow, never delete |
| `std::string tallest` | stack, with heap buffer | a copy is wanted |

## The rules that survived the course

1. Prefer automatic storage; it cleans itself up.
2. When you need the heap, let a container or a smart pointer own it.
3. Use raw pointers to observe and references to require.
4. Mark read-only methods and parameters `const` so the compiler enforces your intent.

> [!IMPORTANT]
> `roster.front()` returns a reference to an element. Taking `&roster.front()` is safe while the
> vector lives and does not reallocate — a `push_back` after that point can invalidate every pointer
> into the buffer.

> [!TIP]
> Compile with `-Wall -Wextra -fsanitize=address,undefined` while learning. The sanitizers turn a
> silent out-of-bounds read or a use-after-free into a message with a line number, which is the
> fastest feedback loop in C++.

## Where to go next

You have the shape of the language: values and types, control flow, collections, functions, types you
define, and memory. The next steps worth taking are `std::string` in depth, the algorithms in
`<algorithm>`, error handling with exceptions, and reading other people's headers until the
declarations stop looking like noise.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
