# 42. Spawn With Stats

**Spanish version:** [42 - Nacer con Atributos](./42%20-%20Nacer%20con%20Atributos.md)

**Course:** C++
**Chapter:** 7 — Entities
**Topic:** Member functions, the implicit this, and mutating state
**Tags:** `#cpp` `#class` `#methods`

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

A spawned creature has stats, and stats change. Damage arrives from outside, so the object needs
methods that read and write its own fields — and a way to name those fields when a parameter has the
same name.

```cpp
#include <iostream>
#include <string>

class Creature {
 public:
  Creature(std::string name, int hp) : name_(name), hp_(hp), max_hp_(hp) {}

  void take_damage(int amount) {
    hp_ -= amount;
    if (hp_ < 0) {
      hp_ = 0;
    }
  }

  void heal(int amount) {
    hp_ += amount;
    if (hp_ > max_hp_) {
      hp_ = max_hp_;
    }
  }

  bool is_alive() const { return hp_ > 0; }

  std::string status() const {
    return name_ + ": " + std::to_string(hp_) + "/" + std::to_string(max_hp_);
  }

  Creature& rename(const std::string& name) {
    this->name_ = name;
    return *this;
  }

 private:
  std::string name_;
  int hp_;
  int max_hp_;
};

int main() {
  Creature c("ashling", 12);

  std::cout << c.status() << "\n";
  c.take_damage(20);
  std::cout << c.status() << " alive=" << c.is_alive() << "\n";
  c.heal(5);
  std::cout << c.rename("emberling").status() << "\n";
}
```

## Output

```text
ashling: 12/12
ashling: 0/12 alive=0
emberling: 5/12
```

## What `this` is

Inside `rename`, `name_` and `name` are two different things. `name_` is the member; `name` is the
parameter that shadows the member's plain name. `this->name_` says "the member of the object I was
called on", which is what you want when names collide.

| Expression | Means |
| :--- | :--- |
| `name_` | the member of this object |
| `name` | the parameter |
| `this` | pointer to this object |
| `*this` | the object itself |

## Chaining by returning `*this`

`rename` returns `Creature&`, so `c.rename("emberling").status()` works: the reference is the same
object, and the next call operates on it. Returning `*this` by value would chain and then copy, which
is a different thing.

> [!IMPORTANT]
> A method that does not modify the object should be marked `const`. `is_alive() const` can be called
> on a `const Creature`, and the compiler then guarantees it does not change the object.

> [!TIP]
> Clamp inside the method, as `heal` does with `max_hp_`, rather than trusting every caller. The
> object is the only place that knows all its rules, and it is called from everywhere.

---

**Next:** [[43 - The Familiar Codex]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
