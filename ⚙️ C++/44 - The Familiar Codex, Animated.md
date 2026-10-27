# 44. The Familiar Codex, Animated

**Spanish version:** [44 - El Códice, Animado](./44%20-%20El%20C%C3%B3dice%2C%20Animado.md)

**Course:** C++
**Chapter:** 7 — Entities
**Topic:** Separating declaration from definition across files
**Tags:** `#cpp` `#headers` `#translation-units`

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

The codex has grown: three hundred lines, used by the spawner, the UI and the save system. Every file
that includes it would recompile the whole thing. The fix is old and boring: declaration in a header,
definition in one `.cpp`.

`codex.hpp` — the promise:

```cpp
#ifndef CODEX_HPP
#define CODEX_HPP

#include <cstddef>
#include <string>
#include <vector>

class FamiliarCodex {
 public:
  void register_familiar(const std::string& name, int level);
  std::size_t count() const;
  int highest_level() const;
  std::string summary() const;

 private:
  std::vector<std::string> names_;
  std::vector<int> levels_;
};

#endif  // CODEX_HPP
```

`codex.cpp` — the delivery:

```cpp
#include "codex.hpp"

void FamiliarCodex::register_familiar(const std::string& name, int level) {
  names_.push_back(name);
  levels_.push_back(level);
}

std::size_t FamiliarCodex::count() const { return names_.size(); }

int FamiliarCodex::highest_level() const {
  int best = 0;
  for (int lvl : levels_) {
    best = lvl > best ? lvl : best;
  }
  return best;
}

std::string FamiliarCodex::summary() const {
  return std::to_string(count()) + " familiars, highest level " +
         std::to_string(highest_level());
}
```

`main.cpp` — the user:

```cpp
#include <iostream>

#include "codex.hpp"

int main() {
  FamiliarCodex codex;
  codex.register_familiar("cinder", 4);
  codex.register_familiar("drift", 9);

  std::cout << codex.summary() << "\n";
}
```

Build and run:

```bash
g++ -std=c++17 -Wall -Wextra main.cpp codex.cpp -o codex && ./codex
```

## Output

```text
2 familiars, highest level 9
```

## What lives where

| File | Contains | Included by |
| :--- | :--- | :--- |
| `codex.hpp` | class shape: members and signatures | anything that uses the codex |
| `codex.cpp` | method bodies | nothing |
| `main.cpp` | `#include "codex.hpp"` | — |

The header is compiled many times, once per including file. That is why it holds declarations only:
a function *definition* in a header included twice breaks the one-definition rule at link time.

## The include guard

`#ifndef CODEX_HPP / #define / #endif` makes the second inclusion in the same translation unit a
no-op. `#pragma once` does the same on every compiler you are likely to meet, in one line.

> [!CAUTION]
> Never `#include "codex.cpp"`. It compiles the bodies into every file that includes it, produces
> duplicate symbols, and hides the fact that your build command forgot `codex.cpp`.

> [!NOTE]
> The class declaration in a header must match the definition's signatures exactly. A missing `const`
> in one place produces a "no declaration matches" error that points at the `.cpp`, not at the
> header — read both before editing either.

---

**Next:** [[45 - Where Things Live]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
