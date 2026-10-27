# 08. IPO

**Spanish version:** [08 - IPO (Entrada, Proceso, Salida).md](./08%20-%20IPO%20%28Entrada%2C%20Proceso%2C%20Salida%29.md)

**Course:** C++
**Topic:** Initializing and Updating Variables
**Tags:** `#cpp` `#variables` `#initialization`

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

**I**nput → **P**rocess → **O**utput. Every program you will write in this module follows that
shape, and variables are where the middle step happens.

After we declare a variable, we can give it a value to store. This is called **initialization**.

```cpp
int score;
score = 0;
```

- `score` is the variable name.
- `=` means **assignment**, not "equals". In C++, an equal sign means *put this value in this
  box*, not *these two things are the same*.
- `;` ends the statement.

You can update the value as many times as you want later in the program:

```cpp
score = 10;
score = 8;
```

## Printing Variables

Print a variable's value by putting the variable name after the `<<` **without** double quotes.

```cpp
std::cout << score; // Output: 8
```

> [!WARNING]
> `std::cout << "score";` prints the literal word `score`. `std::cout << score;` prints `8`.
> The quotes are the entire difference, and it is one of the most common beginner bugs.

> [!TIP]
> **Declare-and-initialize in one line**
> `int score = 0;` is the same as the two lines above, and it removes the window where the
> variable exists but holds garbage.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
