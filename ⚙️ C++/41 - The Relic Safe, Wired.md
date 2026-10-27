# 41. The Relic Safe, Wired

**Spanish version:** [41 - La Caja Fuerte, Conectada](./41%20-%20La%20Caja%20Fuerte%2C%20Conectada.md)

**Course:** C++
**Chapter:** 7 — Entities
**Topic:** Delegating constructors and default construction
**Tags:** `#cpp` `#class` `#delegating-constructor`

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

The vault now ships two variants: an archival safe with four dials and an expedition safe with two.
Both share the same rules, so the second constructor hands its work to the first instead of repeating
the validation.

```cpp
#include <iostream>
#include <string>

class RelicSafe {
 public:
  RelicSafe(std::string owner, int dials)
      : owner_(owner), dials_(dials < 3 ? 3 : dials), locked_(true) {}

  RelicSafe() : RelicSafe("unassigned", 3) {}          // default: delegate
  RelicSafe(std::string owner) : RelicSafe(owner, 3) {} // delegation with one argument

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
  RelicSafe a;
  RelicSafe b("courier");
  RelicSafe c("expedition", 2);   // clamped to 3

  std::cout << a.describe() << "\n";
  std::cout << b.describe() << "\n";
  std::cout << c.describe() << "\n";
}
```

## Output

```text
unassigned / 3 dials / locked
courier / 3 dials / locked
expedition / 3 dials / locked
```

## One constructor that knows the rules

| Constructor | Delegates to | Why |
| :--- | :--- | :--- |
| `RelicSafe(owner, dials)` | — | the one that validates |
| `RelicSafe()` | `RelicSafe("unassigned", 3)` | sensible empty state |
| `RelicSafe(owner)` | `RelicSafe(owner, 3)` | one-argument convenience |

Delegation runs the target constructor first and its body after. The rules live in exactly one place,
so a change to the minimum dial count changes every path at once.

## The rule `RelicSafe a;` depends on

Without `RelicSafe()`, `RelicSafe a;` does not compile — and that is usually the right outcome. A safe
that exists without an owner is only useful if "no owner" is a meaningful state; here it is spelled
out explicitly instead of arriving as uninitialised memory.

> [!WARNING]
> `RelicSafe a();` is not an object, it is a function declaration. The "most vexing parse" bites
> everyone once. Use `RelicSafe a;` or `RelicSafe a{};` when you mean an object.

> [!TIP]
> If two constructors would have identical bodies, delete one and give the other default arguments.
> Delegation is for the case where the bodies differ but must share the same guarantees.

---

**Next:** [[42 - Spawn With Stats]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
