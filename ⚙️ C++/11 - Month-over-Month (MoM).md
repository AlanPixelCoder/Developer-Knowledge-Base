# 11. Month-over-Month (MoM)

**Spanish version:** [11 - Mes a Mes (MoM).md](./11%20-%20Mes%20a%20Mes%20%28MoM%29.md)

**Course:** C++
**Topic:** User Input (`std::cin`)
**Tags:** `#cpp` `#input` `#cin`

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

To get input from the user, C++ uses the `std::cin` statement.

- `cin` stands for **c**haracter **in**put and refers to the standard input stream.
- It is followed by the `>>` operator and the input variable.

In the terminal the user types their response and hits `enter`. Whatever they typed gets stored
in the variable.

> [!IMPORTANT]
> You must **declare** a variable before you can use it to store input. `std::cin >> x;` on an
> undeclared `x` will not compile.

## `cin` vs `cout`

| | Operator | Direction | Target |
| :--- | :--- | :--- | :--- |
| `std::cout` | `<<` | Program → screen | A value |
| `std::cin` | `>>` | Keyboard → program | A variable |

The arrows always point **toward the destination**.

## Example

```cpp
#include <iostream>

int main() {
  double month1;
  double month2;

  std::cout << "Enter month 1: ";
  std::cin >> month1;

  std::cout << "Enter month 2: ";
  std::cin >> month2;

  double mom = ((month2 - month1) / month1) * 100;

  std::cout << "Month-over-month change: " << mom << "%";
}
```

> [!NOTE]
> The formula: $\text{MoM} = \dfrac{\text{month}_2 - \text{month}_1}{\text{month}_1} \times 100$.
> A positive result is growth, a negative one is a decline.

> [!WARNING]
> `std::cin` splits on whitespace. Typing `1,000` reads `1` and leaves `,000` in the buffer for
> the next read. Whole numbers, one per prompt.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
