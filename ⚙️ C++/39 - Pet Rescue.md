# 39. Pet Rescue

**Spanish version:** [39 - Rescate de Mascotas.md](./39%20-%20Rescate%20de%20Mascotas.md)

**Course:** C++
**Topic:** Chapter 7 Recap & OOP Project
**Tags:** `#cpp` `#recap` `#classes` `#oop` `#project`

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

## Chapter 7 Recap

We learned how to:

- Create a class and initialize it with attributes.
- Create objects from those classes and set their attribute values.
- Create classes with a **constructor** that does the initializing.
- Create **class methods** that use or update those attributes.

## Project: Pet Rescue

Suppose we are building a Pet Rescue app where users create and interact with pets. We build a
`Cat` class with attributes (`name`, `breed`, `age`, `rescued`, `mood`, `hunger`) and methods to
`feed()`, `play()`, and `status()`.

```cpp
#include <iostream>
#include <string>

class Cat {
  public:
    std::string name;
    std::string breed;
    int age;
    bool rescued;
    int mood;   // 0 = sad, 10 = very happy
    int hunger; // 0 = hungry, 10 = full

    Cat(std::string n, std::string b, int a, bool r, int m, int h) {
      name = n;
      breed = b;
      age = a;
      rescued = r;
      mood = m;
      hunger = h;
    }

    // feed(), play(), status() go here
};

int main() {
  Cat garfield("Garfield", "Persian", 5, true, 4, 9);
  Cat luna("Luna", "Sphynx", 2, false, 7, 3);

  // Interact through a text menu
}
```

## Data Flow

| Action | Effect on `hunger` | Effect on `mood` |
| :--- | :--- | :--- |
| `feed()` | +1, capped at 10 | — |
| `play()` | — | +1, capped at 10 |
| `status()` | reads only | reads only |

> [!NOTE]
> **The caps are the design**
> `if (hunger < 10) hunger++;` keeps the stat inside its 0–10 band. Without the guard, a few
> dozen feeds would push hunger to 40 and break every assumption the UI makes.

> [!TIP]
> Two objects, one class. `garfield.hunger` and `luna.hunger` are totally independent boxes —
> that is the entire point of instantiating a blueprint.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
