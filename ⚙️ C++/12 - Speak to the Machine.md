# 12. Speak to the Machine

**Spanish version:** [12 - Hablar con la Máquina](./12%20-%20Hablar%20con%20la%20M%C3%A1quina.md)

**Course:** C++
**Chapter:** 2 — Raw Values
**Topic:** Reading input from the console with std::cin
**Tags:** `#cpp` `#input` `#iostream`

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

Output makes a program a report. Input makes it a tool. The engine console asks for a build name and
a frame cap, then confirms what it received.

```cpp
#include <iostream>
#include <string>

int main() {
  std::string build_name;
  int frame_cap;

  std::cout << "build name: ";
  std::cin >> build_name;

  std::cout << "frame cap: ";
  std::cin >> frame_cap;

  std::cout << "building " << build_name << " at " << frame_cap << " fps\n";
}
```

## Arrows point the way data moves

| Operator | Direction | Meaning |
| :--- | :--- | :--- |
| `<<` | out of the program | insert into an output stream |
| `>>` | into the program | extract from an input stream |

`std::cin >> name` reads one whitespace-separated token. That is why a build name with a space in it
stops at the space.

## A sample session

```text
build name: ember-rc1
frame cap: 120
building ember-rc1 at 120 fps
```

> [!WARNING]
> `std::cin >> x` when `x` is an `int` and the user types `abc` leaves the stream in a failed state;
> every later read returns immediately. Check with `if (std::cin >> x)` before trusting the value.

> [!NOTE]
> For a whole line, spaces included, use `std::getline(std::cin, line)`. Mixing `>>` and `getline`
> needs care: the `>>` leaves the newline in the buffer, and `getline` consumes it as an empty line.

---

**Next:** [[13 - Level Scaling]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
