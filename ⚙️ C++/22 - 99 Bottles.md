# 22. 99 Bottles

**Spanish version:** [22 - 99 Botellas.md](./22%20-%2099%20Botellas.md)

**Course:** C++
**Topic:** Decrementing `for` Loops
**Tags:** `#cpp` `#loops` `#for` `#decrement`

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

You can write `for` loops where the counter goes **up** (incrementing) and also where it goes
**down** (decrementing).

To count down: start the initialization at a higher number, check that it is *greater* than a
value, and use `i--` as the change.

```cpp
for (int i = 99; i > 0; i--) {
  // body
}
```

## Up vs Down

| Direction | Init | Condition | Change |
| :--- | :--- | :--- | :--- |
| Up | `int i = 0` | `i < n` | `i++` |
| Down | `int i = n` | `i > 0` | `i--` |

## Example

```cpp
#include <iostream>

int main() {
  for (int i = 99; i > 0; i--) {
    std::cout << i << " bottles of beer on the wall\n";
    std::cout << i << " bottles of beer\n";
    std::cout << "Take one down, pass it around\n";
    std::cout << i - 1 << " bottles of beer on the wall\n\n";
  }
}
```

> [!NOTE]
> Note the `i - 1` in the last line: the loop counter is still on the current bottle, so the
> "after taking one down" count has to be computed. The final iteration prints `0 bottles on the
> wall` — canonically wrong grammar, canonically part of the song.

> [!TIP]
> Counting down is exactly what you need to walk a vector backwards:
> `for (int i = v.size() - 1; i >= 0; i--)`.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
