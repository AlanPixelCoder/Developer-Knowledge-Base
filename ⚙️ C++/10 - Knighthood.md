# 10. Knighthood

**Spanish version:** [10 - Caballería.md](./10%20-%20Caballer%C3%ADa.md)

**Course:** C++
**Topic:** Chaining Output
**Tags:** `#cpp` `#output` `#chaining`

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

In C++, we can use **chaining** to output text and a variable in a single line.

Chaining is helpful primarily because it allows for more concise and readable code. We do it by
using multiple `<<` operators in a single statement — each `<<` hands the stream to the next
piece.

```cpp
std::cout << "Arise, " << name << ", a knight of the Seven Kingdoms.\n";
```

Read it left to right: send `"Arise, "` to the screen, then send `name`, then send the rest.

## Example

```cpp
#include <iostream>

int main() {
  std::string name = "Brianne";

  std::cout << "In the name of the Warrior, I charge you to be brave.\n";
  std::cout << "In the name of the Father, I charge you to be just.\n";
  std::cout << "In the name of the Mother, I charge you to defend the innocent.\n";
  std::cout << "Arise, " << name << ", a knight of the Seven Kingdoms.\n";
}
```

> [!TIP]
> Chain spacing explicitly (`"Arise, "` with a trailing space) instead of relying on `std::cout`
> to add gaps. It never adds gaps — that is why chained output so often comes out as
> `Arise,Brianne,a knight`.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
