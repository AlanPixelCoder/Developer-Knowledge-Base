# 38. Classic Cars

**Spanish version:** [38 - Coches Clásicos.md](./38%20-%20Coches%20Cl%C3%A1sicos.md)

**Course:** C++
**Topic:** Constructors and Default Values
**Tags:** `#cpp` `#classes` `#oop` `#constructors`

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

When we create an object, assigning a value to each attribute on a separate line is tedious.

**Constructors** exist in C++ to automatically initialize objects when they are created.

## Creating a Constructor

- It has the **exact same name** as the class.
- It has **no return type** — not even `void`.
- It runs automatically at the moment of creation.
- Arguments are passed in the same `Type name` syntax as any function.

```cpp
class Student {
  public:
    std::string name;
    int year;

    // Constructor
    Student(std::string n, int y) {
      name = n;
      year = y;
    }
};

Student ferris("Ferris Bueller", 12); // one line instead of three
```

## Default Values

If an attribute is not supplied, set a default where you declare it in the class. That value acts
as a placeholder.

```cpp
class Car {
  public:
    int year = 2000;   // default
    bool classic = false;
};
```

## Example

```cpp
#include <iostream>
#include <string>

class Car {
  public:
    std::string brand;
    std::string model;
    int year;
    bool classic;

    Car(std::string b, std::string m, int y, bool c) {
      brand = b;
      model = m;
      year = y;
      classic = c;
    }
};

int main() {
  Car mustang("Ford", "Mustang", 1965, true);
  Car jaguar("Jaguar", "E-Type", 1961, true);

  std::cout << "Car 1: " << mustang.year << " " << mustang.brand << " " << mustang.model << "\n";
  std::cout << "Car 2: " << jaguar.year << " " << jaguar.brand << " " << jaguar.model << "\n";
}
```

## Output

```text
Car 1: 1965 Ford Mustang
Car 2: 1961 Jaguar E-Type
```

> [!TIP]
> **Default constructor**
> A class with **no** constructor at all gets a free implicit one, so `Car c;` compiles. The moment
> you write *any* constructor, that free one disappears — a classic source of sudden
> "no matching constructor" errors.

> [!NOTE]
> In modern C++, the initializer list (`Car(std::string b) : brand(b) {}`) is the preferred form.
> The in-body assignment you see here is the friendlier teaching version and does the same job.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
