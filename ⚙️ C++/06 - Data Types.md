# 06. Data Types

**Spanish version:** [06 - Tipos de Datos.md](./06%20-%20Tipos%20de%20Datos.md)

**Course:** C++
**Topic:** Variables and Data Types
**Tags:** `#cpp` `#variables` `#data-types`

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

In programming, variables are used for storing data values. Each variable has a **data type**, a **variable name**, and stores a **value** — think of it as a box in computer memory with a label on it.

## The Five Basic Data Types

| Type | Holds | Example |
| :--- | :--- | :--- |
| **`int`** | Whole numbers, positive or negative, no decimal point | `int year = 2024;` |
| **`double`** | Floating-point (decimal) numbers — fractions, precise measurements | `double pi = 3.14159;` |
| **`char`** | One single character, wrapped in **single** quotes | `char hashtag = '#';` |
| **`std::string`** | Text, a sequence of characters, wrapped in **double** quotes | `std::string message = "good nite";` |
| **`bool`** | Only `true` or `false`, always lowercase | `bool late_to_class = false;` |

`std::string` uses the `std::` prefix because it comes from the standard C++ library — which is
also why `#include <string>` is required.

> [!NOTE]
> **Single quotes vs double quotes is not cosmetic**
> `'a'` is a `char` (one byte). `"a"` is a `std::string` (a sequence, with a null terminator
> behind it). Mixing them up produces compiler errors that look cryptic until you spot the quote.

> [!TIP]
> **Sizing up the box**
> A `bool` is 1 byte, a `char` is 1 byte, an `int` is typically 4 bytes, a `double` is 8. This is
> why "just use `double` for everything" quietly doubles your memory bill in tight loops.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
