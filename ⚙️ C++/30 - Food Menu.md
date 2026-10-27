# 30. Food Menu

**Spanish version:** [30 - Menú de Comida.md](./30%20-%20Men%C3%BA%20de%20Comida.md)

**Course:** C++
**Topic:** Defining and Calling Functions
**Tags:** `#cpp` `#functions` `#void`

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

**User-defined functions** are functions we define ourselves to do a specific task. It's a
two-step process:

1. **Define** the function.
2. **Call** the function.

## Define a Function

A definition begins with the `void` keyword, followed by the function name and a set of
parentheses `()`. The code inside is the **body**, enclosed in curly braces and indented.

```cpp
void voicemail() {
  std::cout << "Hi, you've reached Bob's Burgers!\n";
}
```

`void` means "this function returns nothing" — it does the work and hands back no value.

> [!NOTE]
> The common naming convention for classic functions is `snake_case`, but modern `camelCase` is
> also fine. Pick one per project.

## Call a Function

Defining a function creates it, but C++ will not run it automatically. To execute the body we
**call** it: the function name followed by `()`, usually inside `main()`.

```cpp
#include <iostream>

void welcome() {
  std::cout << "Welcome to The Pixel Squire's Tavern!\n\n";
  std::cout << "Here's the menu:\n";
  std::cout << "1. 🍗 Roast Leg\n";
  std::cout << "2. 🍚 Jasmine Rice\n";
  std::cout << "3. 🧪 Health Potion\n";
  std::cout << "4. ☕ Triple Espresso\n";
  std::cout << "5. 🍪 Travel Cookie\n\n";
}

int main() {
  welcome(); // first call
  welcome(); // second call — same body, zero duplicated code
}
```

> [!IMPORTANT]
> **Order matters**
> A function must be *declared or defined* before the line that calls it. Put definitions above
> `main()`, or add a **prototype** (`void welcome();`) near the top and define the body later.

> [!TIP]
> This is DRY in its simplest form: two calls, one body. Change the menu once and both prints
> update.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
