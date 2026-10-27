# 25. The Satchel

**Spanish version:** [25 - La Alforja](./25%20-%20La%20Alforja.md)

**Course:** C++
**Chapter:** 5 — Collections
**Topic:** What a std::vector is and why it beats a fistful of variables
**Tags:** `#cpp` `#vector` `#collections`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-5-7C5CFF?style=for-the-badge" alt="Chapter 5">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Four ingredient stacks, four variables, four lines of printing. Then the recipe grows to six and the
code grows with it. A `std::vector` holds all of them under one name and knows its own size.

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<int> satchel{7, 3, 12, 1};  // four stacks, one container

  std::cout << "stacks: " << satchel.size() << "\n";
  std::cout << "first:  " << satchel[0] << "\n";
  std::cout << "last:   " << satchel[satchel.size() - 1] << "\n";
}
```

## Output

```text
stacks: 4
first:  7
last:   1
```

## One name, many slots

| Need | With variables | With a vector |
| :--- | :--- | :--- |
| Add a fifth stack | new variable + new print | `satchel.push_back(9)` |
| Report the count | keep a separate counter | `satchel.size()` |
| Loop over all | one line per variable | three-line `for` |

The container does not make individual values less accessible. `satchel[2]` is the same twelve you
would have stored in `stack3`.

## Include, declare, fill

1. `#include <vector>`
2. `std::vector<int> satchel;` — empty, grows later
3. `std::vector<int> satchel{7, 3, 12, 1};` — four values from the start
4. `std::vector<int> satchel(4);` — careful: four **zeroes**, not four empty slots

> [!CAUTION]
> `std::vector<int> satchel(4)` and `std::vector<int> satchel{4}` differ: the first is four
> zeroes, the second is one element holding 4. Braces versus parentheses is the whole difference.

> [!TIP]
> `size()` returns an unsigned type. When you subtract from it, as in `size() - 1`, make sure the
> vector is not empty first, or the subtraction wraps to a huge number.

---

**Next:** [[26 - Slot and Index]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
