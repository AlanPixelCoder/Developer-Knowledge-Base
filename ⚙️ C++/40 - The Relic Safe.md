# 40. The Relic Safe

**Spanish version:** [40 - La Caja Fuerte de Reliquias](./40%20-%20La%20Caja%20Fuerte%20de%20Reliquias.md)

**Course:** C++
**Chapter:** 7 — Entities
**Topic:** Constructors: guaranteeing a valid object from the first line
**Tags:** `#cpp` `#class` `#constructors`

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

A safe that can exist with no combination is a bug waiting for the first night. The constructor runs
before anyone can touch the object, so it is the only honest place to establish the rules.

```cpp
#include <iostream>
#include <string>

class RelicSafe {
 public:
  RelicSafe(std::string owner, int dials)
      : owner_(owner), dials_(dials < 3 ? 3 : dials), locked_(true) {}

  bool try_code(int code) {
    if (!locked_) {
      return true;
    }
    if (code == expected()) {
      locked_ = false;
      return true;
    }
    return false;
  }

  int expected() const { return dials_ * 137; }

  std::string describe() const {
    return owner_ + " / " + std::to_string(dials_) + " dials / " +
           (locked_ ? "locked" : "open");
  }

 private:
  std::string owner_;
  int dials_;
  bool locked_;
};

int main() {
  RelicSafe safe("archivist", 4);

  std::cout << safe.describe() << "\n";
  std::cout << "wrong: " << safe.try_code(1) << "\n";
  std::cout << "right: " << safe.try_code(safe.expected()) << "\n";
  std::cout << safe.describe() << "\n";
}
```

## Output

```text
archivist / 4 dials / locked
wrong: 0
right: 1
archivist / 4 dials / open
```

## What the constructor guarantees

| Field | Rule | Enforced by |
| :--- | :--- | :--- |
| `owner_` | always set | required parameter |
| `dials_` | never below 3 | the ternary in the initialiser |
| `locked_` | true at birth | explicit initialiser |

Every `RelicSafe` that exists satisfies the rules, because there is no other way to create one.

## The member initialiser list

```cpp
RelicSafe(std::string owner, int dials)
    : owner_(owner), dials_(dials < 3 ? 3 : dials), locked_(true) {}
```

Everything after the colon runs **before** the body. Members are initialised in declaration order, not
in the order written here — a mismatch between the two orders is a real bug when one initialiser
reads another field.

> [!CAUTION]
> If the class has no user-declared constructor, the compiler generates a default one and fields of
> built-in types stay uninitialised. `RelicSafe safe;` would then hold garbage `dials_`. The
> constructor above removes that possibility entirely.

> [!TIP]
> Prefer initialiser lists to assignments in the body: `const` and reference members can only be
> initialised, never assigned, and the initialiser avoids a default-construct-then-overwrite cycle.

---

**Next:** [[41 - The Relic Safe, Wired]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
