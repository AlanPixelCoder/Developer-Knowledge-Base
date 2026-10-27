# 39. Sealed and Open Doors

**Spanish version:** [39 - Puertas Selladas y Abiertas](./39%20-%20Puertas%20Selladas%20y%20Abiertas.md)

**Course:** C++
**Chapter:** 7 — Entities
**Topic:** public and private: keeping invariants inside the type
**Tags:** `#cpp` `#class` `#encapsulation`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Chapter-7-7C5CFF?style=for-the-badge" alt="Chapter 7">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

A vault door has a public handle and a private mechanism. Turning the handle is allowed; reaching into
the mechanism and setting the bolt halfway is not — it would leave the vault in a state the designer
never planned for.

```cpp
#include <iostream>

struct VaultDoor {
 public:
  bool is_open() const { return open_; }

  void unlock() { locked_ = false; }

  bool open() {
    if (locked_) {
      return false;
    }
    open_ = true;
    return true;
  }

 private:
  bool locked_ = true;
  bool open_ = false;
};

int main() {
  VaultDoor door;

  std::cout << "opened locked: " << door.open() << "\n";
  door.unlock();
  std::cout << "opened unlocked: " << door.open() << "\n";
  std::cout << "state: " << (door.is_open() ? "open" : "closed") << "\n";
}
```

## Output

```text
opened locked: 0
opened unlocked: 1
state: open
```

## Two labels, one rule

| Label | Who can touch it | Put here |
| :--- | :--- | :--- |
| `public` | any code with the object | what the type promises |
| `private` | only the type's own members | how the promise is kept |

`struct` defaults to public, `class` defaults to private. The only other difference is the default; a
`class` with `public:` at the top is the same type as a `struct`.

## The invariant

`locked_ == true` means `open_ == false`. Nothing outside can break that rule, because the fields are
private and `open()` is the only writer. The invariant is local, so it can be checked by reading
twenty lines instead of the whole program.

> [!IMPORTANT]
> `door.open()` on a locked door returns `false` and prints `0` in a `bool` context. That is a
> deliberate contract, not an error: a lock that fails silently is worse than one that cannot be
> reached.

> [!TIP]
> Mark read-only methods `const` (`bool is_open() const`). Then a `const VaultDoor&` can still be
> asked its state, and the compiler rejects any attempt to modify through that reference.

---

**Next:** [[40 - The Relic Safe]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
