# 43. The Familiar Codex

**Spanish version:** [43 - El Códice de Familiares](./43%20-%20El%20C%C3%B3dice%20de%20Familiares.md)

**Course:** C++
**Chapter:** 7 — Entities
**Topic:** A class that owns a collection, with const methods and a static counter
**Tags:** `#cpp` `#class` `#static`

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

The codex holds a list of familiars and answers questions about them. It owns the list, so nobody
else can add a familiar without the codex knowing — and the codex keeps a running total of every
familiar it has ever registered.

```cpp
#include <iostream>
#include <string>
#include <vector>

class FamiliarCodex {
 public:
  void register_familiar(const std::string& name, int level) {
    names_.push_back(name);
    levels_.push_back(level);
    ++total_registered;
  }

  std::size_t count() const { return names_.size(); }

  int highest_level() const {
    int best = 0;
    for (int lvl : levels_) {
      if (lvl > best) {
        best = lvl;
      }
    }
    return best;
  }

  std::string summary() const {
    return std::to_string(count()) + " familiars, highest level " +
           std::to_string(highest_level()) + ", " +
           std::to_string(total_registered) + " ever";
  }

  static int total_registered;

 private:
  std::vector<std::string> names_;
  std::vector<int> levels_;
};

int FamiliarCodex::total_registered = 0;

int main() {
  FamiliarCodex codex;

  codex.register_familiar("cinder", 4);
  codex.register_familiar("drift", 9);
  codex.register_familiar("moss", 2);

  std::cout << codex.summary() << "\n";

  FamiliarCodex second;
  second.register_familiar("quill", 1);
  std::cout << second.summary() << "\n";
}
```

## Output

```text
3 familiars, highest level 9, 3 ever
1 familiars, highest level 1, 4 ever
```

## Two kinds of state

| State | Belongs to | Declared | Shared |
| :--- | :--- | :--- | :--- |
| `names_`, `levels_` | each object | normal members | no |
| `total_registered` | the class | `static` + definition outside | yes |

A `static` member needs a definition outside the class (`int FamiliarCodex::total_registered = 0;`)
or the linker complains about a missing symbol. Since C++17, `static inline int total_registered = 0;`
inside the class does the same in one line.

## `const` methods returning a stored value

`count()` and `highest_level()` are `const`, so they can be called on a `const FamiliarCodex&`.
`highest_level()` recomputes each time; caching it would mean a non-`const` or `mutable` member and a
second place to keep correct.

> [!NOTE]
> Parallel vectors are simple and work. A `std::vector<Familiar>` — one struct per element — is
> usually better once the fields pass three, because a forgotten `push_back` on one vector desyncs the
> codex silently.

> [!TIP]
> Keep the container private and expose what callers actually need (`count`, `highest_level`) instead
> of a getter for the vector. A getter hands out the ability to break the invariant you just built.

---

**Next:** [[44 - The Familiar Codex, Animated]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
