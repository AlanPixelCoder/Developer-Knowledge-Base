# 04. Notes in the Margin

**Spanish version:** [04 - Notas al Margen](./04%20-%20Notas%20al%20Margen.md)

**Course:** C++
**Chapter:** 1 — First Boot
**Topic:** Comments: line, block, and what they are for
**Tags:** `#cpp` `#comments` `#readability`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-1-7C5CFF?style=for-the-badge" alt="Chapter 1">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

A comment is text the compiler throws away. Used well, it records the *why* that the code cannot
say on its own; used badly, it records what the code already says, in a version that stops being
true.

```cpp
#include <iostream>

int main() {
  // Tick rate is capped at 60: the physics step was tuned against it.
  const int TICKS_PER_SECOND = 60;

  std::cout << "tick rate: " << TICKS_PER_SECOND << "\n";

  /* The render budget below is deliberately generous.
     The engine draws the lantern glow in two passes, and the
     second pass has no upper bound on light sources yet. */
  const double RENDER_BUDGET_MS = 12.5;

  std::cout << "render budget: " << RENDER_BUDGET_MS << " ms\n";
}
```

## The two forms

| Form | Syntax | When it is the right tool |
| :--- | :--- | :--- |
| Line comment | `// until end of line` | Most of the time: one reason, one line |
| Block comment | `/* ... */` | A paragraph of context above a declaration |

## Output

```text
tick rate: 60
render budget: 12.5 ms
```

> [!CAUTION]
> Block comments do **not** nest. `/* outer /* inner */ still comment */` closes at the first `*/`,
> and everything after it becomes code the compiler will try to read.

> [!WARNING]
> Commented-out code is not documentation, it is sediment. Version control already remembers the old
> version; delete it and let the history do its job.

> [!TIP]
> If a comment explains *what* the next line does, rename the variable instead. If it explains *why*
> the line exists at all, keep it forever.

---

**Next:** [[05 - Escape Velocity]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
