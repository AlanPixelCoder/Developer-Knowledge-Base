# 19. Enter PIN

**Spanish version:** [19 - Introducir PIN.md](./19%20-%20Introducir%20PIN.md)

**Course:** C++
**Topic:** Introduction to Loops
**Tags:** `#cpp` `#loops` `#while` `#iteration`

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

In programming, a **loop** repeats a block of code until a specified condition is satisfied. It's
an incredibly powerful tool, and it's used constantly.

People often say **iterate** when referring to loops — iterate simply means "to repeat".

There are two types of loops we will learn:

- `while` loops
- `for` loops

## The `while` Loop

You can think of the `while` loop like a traffic circle: each lap is one **iteration**. A car will
go around and around until it can't do so anymore.

```cpp
while (condition) {
  // runs again and again while condition is true
}
```

> [!WARNING]
> **The infinite loop**
> If the condition never becomes `false`, the program never leaves the loop. Inside a `while`
> that depends on user input, make sure the input statement is *inside* the loop — otherwise the
> same answer is checked forever.

## Anatomy of a Loop That Terminates

| Piece | Purpose |
| :--- | :--- |
| A starting state | Something is `true` before the loop begins |
| A condition | Checked before every iteration |
| A body | The work, which must move the state toward `false` |
| A change | Usually inside the body — often a re-read of input |

> [!TIP]
> Say the loop out loud before writing it: *"while the PIN is wrong, ask again."* If you can't
> finish the sentence, you don't have the exit condition yet.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
