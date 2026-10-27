# 23. Countdown Protocol

**Spanish version:** [23 - Protocolo de Cuenta Atrás](./23%20-%20Protocolo%20de%20Cuenta%20Atr%C3%A1s.md)

**Course:** C++
**Chapter:** 4 — Iteration
**Topic:** Decrementing loops and the direction of a countdown
**Tags:** `#cpp` `#for` `#decrement`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-4-7C5CFF?style=for-the-badge" alt="Chapter 4">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

The console announces a shutdown and counts the ticks it has left. Counting down is the same loop
with the increment reversed — and one detail decides whether the last tick prints.

```cpp
#include <iostream>

int main() {
  for (int ticks_left = 5; ticks_left > 0; ticks_left--) {
    std::cout << ticks_left << " ticks until shutdown\n";
  }

  std::cout << "engine halted\n";
}
```

## Output

```text
5 ticks until shutdown
4 ticks until shutdown
3 ticks until shutdown
2 ticks until shutdown
1 ticks until shutdown
engine halted
```

## What changes when you count down

| Direction | Header | Stops when |
| :--- | :--- | :--- |
| Up | `for (int i = 0; i < n; i++)` | `i` reaches `n` |
| Down | `for (int i = n; i > 0; i--)` | `i` reaches `0` |

The comparison flips with the direction. Keeping `i <= n` while decrementing gives a loop that never
starts, which is at least easy to spot.

> [!CAUTION]
> If the counter is `unsigned`, `i--` at zero wraps to the largest possible value and the condition
> `i >= 0` is always true. Signed counters avoid the problem entirely; containers use unsigned
> indices, so count down with care there.

> [!NOTE]
> `i--` yields the value *before* decrementing; `--i` yields it after. Inside the loop body that
> difference is invisible; inside an expression or a condition it is the whole story.

> [!TIP]
> Count down with `> 0` rather than `>= 0` unless you actually want the zero pass. The shutdown
> message belongs after the loop, where it prints exactly once.

---

**Next:** [[24 - The Pattern Trial]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
