# 07. Declaration of Independence

**Spanish version:** [07 - Declaración de Independencia.md](./07%20-%20Declaraci%C3%B3n%20de%20Independencia.md)

**Course:** C++
**Topic:** Declaring Variables and Naming Rules
**Tags:** `#cpp` `#variables` `#declaration`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Every variable in C++ must be **declared** (created) before it is used.

To declare a variable we need two things:

1. A **data type**.
2. A **variable name**.

```cpp
int score;
```

- `int` is the data type.
- `score` is the variable name.
- `;` ends the statement.

## Rules for Variable Names

| Rule | Detail |
| :--- | :--- |
| Allowed characters | Letters, digits, and underscores `_` |
| Case sensitivity | `Shirt_Size` and `shirt_size` are **different** variables |
| No whitespace | `my score` is invalid |
| No special characters | `!`, `#`, `%`, `-` are rejected |
| Must start with a letter | `2fast` is invalid; `fast2` is fine |
| Reserved words | You cannot name a variable `int`, `return`, `class`… |

> [!NOTE]
> **Naming style**
> C++ has no single enforced convention, but the community converges on `snake_case` for
> variables and functions (`player_health`) and `PascalCase` for classes (`BankAccount`).
> Pick one and hold the line — consistency is worth more than the "right" choice.

> [!TIP]
> A declared-but-uninitialized `int` holds **garbage** — whatever happened to be in that memory
> cell. Always initialize. See [[08 - IPO]].

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
