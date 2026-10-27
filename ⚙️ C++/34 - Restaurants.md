# 34. Restaurants

**Spanish version:** [34 - Restaurantes.md](./34%20-%20Restaurantes.md)

**Course:** C++
**Topic:** Introduction to Classes
**Tags:** `#cpp` `#classes` `#oop` `#data-types`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

With **classes** we can create our own data types and use them to model everyday objects with
unique characteristics and behaviors.

Classes serve as a template for the objects created using them. Simply put, a class is a
**blueprint** — a car manufacturer uses one blueprint to build hundreds of cars, each with its own
paint and mileage.

## Defining a Class

The `class` keyword followed by a class name creates the class. By convention the class name is
**capitalized**.

```cpp
class Student {
  std::string name;
  int year;
  double gpa;
};
```

> [!IMPORTANT]
> **Do not forget the semicolon**
> There is a `;` after the closing `}` of a class. Omit it and the compiler reports an error that
> points at the *next* line, which makes it feel like the problem is somewhere else entirely.

## Class vs Object

| Term | Meaning |
| :--- | :--- |
| **Class** | The blueprint — the definition, no data |
| **Object** | One concrete instance built from that blueprint |

> [!NOTE]
> **Default access is `private`**
> Members of a `class` are private unless marked `public`. That is why the next note,
> [[35 - Public vs. Private]], exists — right now nothing outside the class can even read
> `name`, `year` or `gpa`.

> [!TIP]
> Everything in this chapter is the runway for Unity-style game code: `class Enemy`, `class
> Inventory`, `class Weapon` are the same construct you are learning here.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
