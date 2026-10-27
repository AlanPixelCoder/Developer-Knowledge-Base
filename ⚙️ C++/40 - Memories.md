# 40. Memories

**Spanish version:** [40 - Recuerdos.md](./40%20-%20Recuerdos.md)

**Course:** C++
**Topic:** Memory Addresses
**Tags:** `#cpp` `#memory` `#pointers`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-ADVANCED-E74C3C?style=for-the-badge" alt="Advanced">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Welcome to the final chapter of the C++ course. Here we dive into one of the most classic concepts
in C++: **pointers**.

Before pointers, we need to talk about **memory addresses**.

A **memory address** is a unique sequence used to locate a specific byte (or group of bytes) in a
computer's memory.

Computer memory is organized as a long sequence of numbered storage cells (bytes). Each cell can
be accessed by its address — just like houses on a street.

```text
0x00  0x01  0x02  0x03  0x04  ...
```

## Why hexadecimal?

Addresses are printed in **hexadecimal** (base 16). It makes long binary numbers shorter and
easier to read: `0x7ffefb2a` instead of thirty-two bits of ones and zeros.

| Base | Digits | Example |
| :--- | :--- | :--- |
| Binary | `0`–`1` | `1111111111111110` |
| Decimal | `0`–`9` | `65534` |
| Hexadecimal | `0`–`9`, `a`–`f` | `0xfffe` |

## The stack picture

| Variable | Address | Value |
| :--- | :--- | :--- |
| `year` | `0x1000` | `2005` |
| `grade` | `0x1004` | `5.8` |

> [!NOTE]
> **A variable is two things at once**
> Its **address** (where it lives) and its **value** (what it holds). Normal code only ever sees
> the value. Pointers are the tool that lets you work with the address.

> [!TIP]
> Addresses on a modern 64-bit system are typically 8 bytes (64 bits) wide — which is why they
> look absurdly long in `std::cout`.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
