# 31. One Spell, Many Casts

**Spanish version:** [31 - Un Hechizo, Muchos Usos](./31%20-%20Un%20Hechizo%2C%20Muchos%20Usos.md)

**Course:** C++
**Chapter:** 6 — Functions
**Topic:** Why functions exist: one definition, many call sites
**Tags:** `#cpp` `#functions` `#basics`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-6-7C5CFF?style=for-the-badge" alt="Chapter 6">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

The same three-line damage calculation appears in six places: the melee branch, the spell branch, the
trap branch, the boss branch. Change the formula and you must find all six. A function makes it one
place.

```cpp
#include <iostream>

int damage(int power, int armor) {
  int raw = power * 3;
  int reduced = raw - armor;
  return reduced < 1 ? 1 : reduced;
}

int main() {
  std::cout << "goblin:   " << damage(4, 2) << "\n";
  std::cout << "skeleton: " << damage(4, 11) << "\n";
  std::cout << "ogre:     " << damage(9, 6) << "\n";
}
```

## Output

```text
goblin:   10
skeleton: 1
ogre:     21
```

## Anatomy

| Part | Here | Meaning |
| :--- | :--- | :--- |
| Return type | `int` | the type of the value handed back |
| Name | `damage` | what you call it |
| Parameters | `int power, int armor` | the inputs, typed |
| Body | the three lines | the work |
| `return` | `return ...;` | the value and the exit |

## Three reasons, not one

1. **One place to change.** Balance patches touch the formula, not six call sites.
2. **A name for the idea.** `damage(4, 2)` reads better than `4 * 3 - 2`.
3. **A place to test.** You can call `damage` with edge cases before the game exists.

> [!NOTE]
> The function must be declared or defined *before* the first call. Defining it above `main` is the
> simplest way; a prototype above `main` and the body below is the other.

> [!TIP]
> If you copy three lines twice, write a function. If you copy them six times, you already have a
> bug — the copies have started to drift.

---

**Next:** [[32 - The Tavern Board]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
