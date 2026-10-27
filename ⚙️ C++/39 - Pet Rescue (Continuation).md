# 39. Pet Rescue (Continuation)

**Spanish version:** [39 - Rescate de Mascotas (Continuación).md](./39%20-%20Rescate%20de%20Mascotas%20%28Continuaci%C3%B3n%29.md)

**Course:** C++
**Topic:** Class Methods Implementation
**Tags:** `#cpp` `#classes` `#oop` `#methods` `#project`

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

Here is how the `Cat` methods are implemented so the objects can actually be interacted with.

```cpp
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

    void feed() {
      if (hunger < 10) {
        hunger++;
      }
      std::cout << "\n🍲 You fed " << name << ". Hunger is now " << hunger << "/10.\n";
    }

    void play() {
      if (mood < 10) {
        mood++;
      }
      std::cout << "\n🧶 You played with " << name << ". Mood is now " << mood << "/10.\n";
    }

    void status() {
      std::cout << "\n=== " << name << "'s Status ===\n";
      std::cout << "Breed: " << breed << " | Age: " << age << "\n";
      std::cout << "Mood: " << mood << "/10  | Hunger: " << hunger << "/10\n";
      std::cout << "Rescued: " << (rescued ? "Yes" : "No") << "\n";
    }
};
```

## The Interactive Menu

Using a `while` loop, we can build a terminal menu that keeps asking until the user chooses to
leave. Drop `#include <iostream>`, the `Cat` class from the previous block and this `main` into
one file and it runs as written.

```cpp
int main() {
  Cat garfield("Garfield", "Persian", 5, true, 4, 9);
  int choice = 0;

  while (choice != 4) {
    garfield.status();
    std::cout << "\n1) Feed  2) Play  3) Status  4) Leave\n> ";
    std::cin >> choice;

    if (choice == 1) garfield.feed();
    else if (choice == 2) garfield.play();
  }

  std::cout << "\nGoodbye! 🐾\n";
}
```

> [!NOTE]
> **`rescued ? "Yes" : "No"` — the ternary operator**
> A one-line `if/else` that produces a value instead of running statements:
> `condition ? value_if_true : value_if_false`. Perfect for printing, useless for control flow.

> [!WARNING]
> The loop only exits on `4`. Type `9` and it silently reprints the menu — which is *fine* here,
> but a real menu should say "unknown option" so the user knows their input registered.

> [!TIP]
> Note that `status()` takes no parameters and still prints everything it needs. That is the
> payoff of encapsulation: the object already holds its own state.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
