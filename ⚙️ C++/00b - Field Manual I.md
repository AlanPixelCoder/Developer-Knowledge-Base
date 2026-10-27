# Field Manual I

**Spanish version:** [00b - Manual de Campo I](./00b%20-%20Manual%20de%20Campo%20I.md)

**Course:** C++
**Topic:** Quick reference
**Tags:** `#cpp` `#cheatsheet` `#reference`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Reference-Field%20Manual-7C5CFF?style=for-the-badge" alt="Field Manual">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

<p align="center">
  <sub>1–4 · First Boot to Iteration</sub>
</p>

> [!TIP]
> Everything in chapters 1 to 4, on one page: the shape of a program, the value types, the operators
> that combine them, the branches that choose, and the loops that repeat.

## The smallest program

```cpp
#include <iostream>

int main() {
  std::cout << "cold start\n";
  return 0;
}
```

```bash
g++ -std=c++17 -Wall -Wextra main.cpp -o console && ./console
```

## Printing and reading

```cpp
std::cout << "hp: " << hp << "\n";   // chain values and text
std::cin >> hp;                      // read one value, whitespace-separated
std::string line;
std::getline(std::cin, line);        // read a whole line
```

## Value types

| Type | Holds | Example |
| :--- | :--- | :--- |
| `int` | whole numbers, about ±2.1 billion | `int hp = 100;` |
| `double` | decimals, 15 significant digits | `double rate = 0.75;` |
| `char` | one character | `char rank = 'B';` |
| `bool` | `true` / `false` | `bool alive = true;` |
| `std::string` | text, grows as needed | `std::string name = "warden";` |

| Conversion | Syntax | Result |
| :--- | :--- | :--- |
| int → double | `static_cast<double>(n)` | exact |
| double → int | `static_cast<int>(x)` | truncates toward zero |
| number → string | `std::to_string(n)` | `"42"` |
| string → number | `std::stoi(s)` | `42`, throws on junk |

## Operators

| Group | Operators | Note |
| :--- | :--- | :--- |
| Arithmetic | `+ - * / %` | `5 / 2` is `2`; make one side `double` |
| Comparison | `== != < <= > >=` | result is `bool` |
| Logical | `&&` `\|\|` `!` | short-circuit: right side may not run |
| Assignment | `= += -= *= /=` | `x += 3` means `x = x + 3` |
| Increment | `++ --` | prefix yields the new value, postfix the old |

## Decisions

```cpp
if (hp <= 0) {
  std::cout << "down\n";
} else if (hp < 20) {
  std::cout << "staggering\n";
} else {
  std::cout << "steady\n";
}
```

| Written | Matches |
| :--- | :--- |
| `x == 3` | equality |
| `x = 3` | assignment — always true in a condition |
| `0 <= x && x < 10` | range check |
| `x % 2 == 0` | even |

## Loops

```cpp
for (int i = 0; i < 3; i++) { /* known count */ }

while (fuel > 0.0) { fuel -= 0.5; }          // condition first

do { ask(); } while (!answered());           // body at least once

for (const auto& item : satchel) { /* every element */ }
```

| Loop | Use when |
| :--- | :--- |
| `for` | the count is known, or you need the index |
| `while` | the end depends on a condition |
| `do ... while` | the body must run at least once |
| range-`for` | you want every element of a collection |

> [!CAUTION]
> Every loop needs a path to a false condition. A change step inside an `if` that never fires is the
> most common infinite loop in beginner code.

## Compiler flags worth memorising

```bash
g++ -std=c++17 -Wall -Wextra -Wshadow main.cpp -o console
```

| Flag | Catches |
| :--- | :--- |
| `-std=c++17` | pins the language version |
| `-Wall -Wextra` | unused variables, sign mismatches, missing returns |
| `-Wshadow` | a local hiding an outer variable |
| `-fsanitize=address,undefined` | out-of-bounds and use-after-free, at runtime |

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
