# 40. Memories (Continuation)

**Spanish version:** [40 - Recuerdos (Continuación).md](./40%20-%20Recuerdos%20%28Continuaci%C3%B3n%29.md)

**Course:** C++
**Topic:** Memory Addresses and the `&` Operator
**Tags:** `#cpp` `#memory` `#address`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-ADVANCED-E74C3C?style=for-the-badge" alt="Advanced">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

When we create variables, each one is stored at a different memory address (e.g., `0x1000`,
`0x1004`).

We can access that memory with `&` — the **address-of** operator. In simple terms, `&x` means
"give me the memory address of `x`". That address is where in RAM the variable lives.

## Example

```cpp
#include <iostream>
#include <string>

int main() {
  std::string favorite_game = "Destroy All Humans!";
  int year_first_played = 2005;
  double worst_school_grade = 5.8;
  char homeroom_section = 'B';

  std::cout << "--- Core Memory Addresses ---\n";
  std::cout << "Game location: " << &favorite_game << "\n";
  std::cout << "Year location: " << &year_first_played << "\n";
  std::cout << "Grade location: " << &worst_school_grade << "\n";

  // Cast to (void*) so the address prints cleanly instead of as a character
  std::cout << "Section location: " << (void*)&homeroom_section << "\n";
}
```

## Sample Output

```text
--- Core Memory Addresses ---
Game location: 0x16da47718
Year location: 0x16da47714
Grade location: 0x16da47708
Section location: 0x16da47707
```

> [!IMPORTANT]
> **Why the `(void*)` cast**
> A `char*` is treated as a C-string when streamed, so `&homeroom_section` would print the
> *characters* at that address until it hit a null byte — usually nothing, occasionally garbage.
> Casting to `void*` tells `std::cout` "this is a pointer, print the number".

> [!NOTE]
> The exact addresses change on every run. That is normal: the operating system decides where
> your program's stack goes. The **relative** order is stable, though. Walking down the sample:
> `&homeroom_section` is one byte below `&worst_school_grade` because a `char` is one byte; the
> `double` then spans its full 8 bytes; and the `int` lands 4 bytes after that, because 8-byte
> alignment leaves a hole. Read the gaps and you are reading type sizes and padding.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
