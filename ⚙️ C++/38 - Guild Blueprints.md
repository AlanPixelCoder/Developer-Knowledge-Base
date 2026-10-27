# 38. Guild Blueprints

**Spanish version:** [38 - Planos del Gremio](./38%20-%20Planos%20del%20Gremio.md)

**Course:** C++
**Chapter:** 7 — Entities
**Topic:** Defining a struct: a type you invent
**Tags:** `#cpp` `#struct` `#types`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-7-7C5CFF?style=for-the-badge" alt="Chapter 7">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

A guild record has a name, a rank, a purse and a reputation. Four parallel arrays would work until the
first insertion, when three of them must shift in step. One `struct` keeps the four fields welded
together.

```cpp
#include <iostream>
#include <string>

struct GuildMember {
  std::string name;
  std::string rank;
  int purse;
  double reputation;
};

int main() {
  GuildMember scout{"Wren", "scout", 40, 3.5};
  GuildMember smith{"Odo", "smith", 120, 7.25};

  std::cout << scout.name << " (" << scout.rank << ") purse " << scout.purse << "\n";
  std::cout << smith.name << " (" << smith.rank << ") reputation " << smith.reputation << "\n";

  smith.purse += 30;
  std::cout << "after a job: " << smith.purse << "\n";
  std::cout << "sizeof: " << sizeof(GuildMember) << " bytes\n";
}
```

## Output

```text
Wren (scout) purse 40
Odo (smith) reputation 7.25
after a job: 150
sizeof: 64 bytes
```

## A struct is a type

| Step | Syntax | Effect |
| :--- | :--- | :--- |
| Define | `struct GuildMember { ... };` | a new type, no variable yet |
| Create | `GuildMember scout{...};` | one object, fields filled in order |
| Access | `scout.purse` | read or write one field |
| Assign whole | `smith = scout;` | copies every field |

`sizeof` may be larger than the sum of the fields: the compiler pads for alignment. 64 bytes here is
a `std::string` (32) plus another (32) plus `int` and `double` squeezed into the tail padding.

## Definition versus instantiation

The definition allocates nothing. It tells the compiler the layout, so that later lines know how many
bytes `GuildMember` needs and where each field sits. One definition, any number of objects.

> [!NOTE]
> Do not forget the semicolon after the closing brace. `struct X { ... }` with no `;` is one of the
> few errors whose message points at the *next* line rather than the real one.

> [!TIP]
> Name a struct after the thing, singular: `GuildMember`, not `GuildMembers`. The variable name
> carries the plural (`members`), and reading `members[0].name` tells you both facts at once.

---

**Next:** [[39 - Sealed and Open Doors]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
