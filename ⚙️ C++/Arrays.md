# Arrays

**Spanish version:** [Arrays en C++.md](./Arrays%20en%20C%2B%2B.md)

**Course:** C++
**Topic:** C-style Arrays vs Vectors
**Tags:** `#cpp` `#arrays` `#data-structures` `#memory`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Classic arrays in C++ are known as **C-style arrays**.

The biggest difference between arrays and vectors is that an array is **fixed-size** — the size
has to stay the same. It cannot grow or shrink.

## Syntax

```cpp
int lottery[6];                          // array of 6 integers
int lottery[6] = {6, 7, 25, 46, 57, 12}; // initialized
```

## Arrays vs. Vectors

| Feature | Arrays | Vectors |
| :--- | :--- | :--- |
| **Size** | Fixed at compile time | Dynamic — grows and shrinks |
| **Syntax** | Basic C-style | Modern (`std::vector`) |
| **Memory** | Stack | Heap |
| **Speed** | Very fast | Very fast, slightly slower than arrays |
| **When to use** | You know the size ahead of time and it won't change. You want slightly faster performance. You're in low-level, hardware or robotics code where you want control over memory. | You need flexibility to add and remove elements |

> [!TIP]
> Working with modern C++? `std::array` gives you a fixed-size array with a `.size()` and safer
> semantics — it is the sane middle ground between `int arr[6]` and `std::vector`.

> [!NOTE]
> Arrays do not know their own size. There is no `arr.size()` — it does not exist. You pass the
> length around separately or use `std::size(arr)`. This is exactly the bookkeeping vectors do for
> you, and exactly why they replaced arrays in everyday code.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
