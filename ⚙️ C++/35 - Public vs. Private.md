# 35. Public vs. Private

**Spanish version:** [35 - Público vs Privado.md](./35%20-%20P%C3%BAblico%20vs%20Privado.md)

**Course:** C++
**Topic:** Access Modifiers & Encapsulation
**Tags:** `#cpp` `#classes` `#oop` `#encapsulation`

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

A class is a blueprint — but a blueprint nobody can read is useless. **Access modifiers** decide
who may touch each member.

| Modifier | Who can access it |
| :--- | :--- |
| `public` | Anyone — code inside and outside the class |
| `private` | Only the class's own code |
| `protected` | The class and classes that inherit from it |

```cpp
class Player {
  public:
    std::string name;  // anyone can read/write
    int level;
  private:
    double wallet;     // only Player's own methods
};
```

Outside code can set `player.name`, but `player.wallet = 999;` is a compile error.

## Encapsulation

**Encapsulation** means hiding internal data behind a controlled interface. The class decides
what the outside world may see and how it may change it.

> [!NOTE]
> **Why bother?** Because an invariant is only worth something if nothing can break it. If
> `wallet` could be set directly, every line of code would be allowed to invent money. Private
> members plus a public method that validates means only one place can break the rule — and only
> one place needs to enforce it.

## Example

```cpp
#include <iostream>

class Player {
  public:
    std::string name;

    void show_wallet() {
      std::cout << name << " has $" << wallet << "\n";
    }

    void spend(double amount) {
      if (amount > 0 && amount <= wallet) {
        wallet -= amount;
      }
    }

  private:
    double wallet = 100.0;
};

int main() {
  Player hero;
  hero.name = "Aldric";
  hero.spend(30);
  hero.show_wallet(); // Aldric has $70
}
```

> [!TIP]
> Start everything `private`. Open a member to `public` only when you have a reason — the default
> in a well-designed class is closed.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
