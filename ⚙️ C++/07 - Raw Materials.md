# 07. Raw Materials

**Spanish version:** [07 - Materia Prima](./07%20-%20Materia%20Prima.md)

**Course:** C++
**Chapter:** 2 — Raw Values
**Topic:** The five built-in types the engine leans on, and what they cost
**Tags:** `#cpp` `#types` `#memory`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-2-7C5CFF?style=for-the-badge" alt="Chapter 2">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

The engine config screen shows five fields: the frame cap, a gravity multiplier, the quality
initial, a build name and a flag for the debug overlay. Five values, and each one needs a type wide
enough to hold it — no wider, because this is the layer where bytes are counted.

| Type | Holds | Typical size | Engine example |
| :--- | :--- | :--- | :--- |
| `int` | whole numbers | 4 bytes | frame cap |
| `double` | decimals | 8 bytes | gravity multiplier |
| `char` | one character | 1 byte | quality initial |
| `std::string` | text | variable (24+ bytes) | build name |
| `bool` | true / false | 1 byte | debug overlay |

## Ask the compiler instead of trusting a table

```cpp
#include <iostream>
#include <string>

int main() {
  int frame_cap = 60;
  double gravity_scale = 1.35;
  char quality = 'B';
  std::string build_name = "ember-0.2.1";
  bool show_debug = true;

  std::cout << "int     " << sizeof(frame_cap) << " bytes\n";
  std::cout << "double  " << sizeof(gravity_scale) << " bytes\n";
  std::cout << "char    " << sizeof(quality) << " bytes\n";
  std::cout << "string  " << sizeof(build_name) << " bytes\n";
  std::cout << "bool    " << sizeof(show_debug) << " bytes\n";
}
```

## Output

```text
int     4 bytes
double  8 bytes
char    1 bytes
string  24 bytes
bool    1 bytes
```

`sizeof` is evaluated at compile time: it costs nothing and it never guesses.

> [!NOTE]
> The standard fixes minimum sizes, not exact ones. `int` is at least 16 bits; on every desktop
> target it is 32. `sizeof` is how you write code that does not care.

> [!WARNING]
> `double` holds decimals **approximately**. `0.1 + 0.2` is not exactly `0.3`. For money, use
> integers of cents; for physics, accept the drift and compare with a tolerance.

---

**Next:** [[08 - Naming the Parts]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
