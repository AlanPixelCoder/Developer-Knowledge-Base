# 27. Roadtrip Playlist

**Spanish version:** [27 - Lista de Reproducción de Viaje.md](./27%20-%20Lista%20de%20Reproducci%C3%B3n%20de%20Viaje.md)

**Course:** C++
**Topic:** Iterating over Vectors
**Tags:** `#cpp` `#vectors` `#loops` `#iteration`

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

You can iterate over a vector using a `for` loop.

Use `.size()` in the loop condition so it runs exactly as many times as there are elements — and
the counter `i` doubles as the index for each element.

```cpp
for (int i = 0; i < playlist.size(); i++) {
  std::cout << playlist[i] << "\n";
}
```

## Reading the condition

| Part | Meaning |
| :--- | :--- |
| `int i = 0` | Start at the first index |
| `i < playlist.size()` | Stop *before* the first invalid index |
| `i++` | Move to the next element |

`<` — not `<=`. With `<=` the loop would try `playlist[size()]` on its last pass, which is one
past the end.

## Example

```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
  std::vector<std::string> playlist = {
    "Seven Lions - Days to Come",
    "Illenium - Crawl Outta Love",
    "Blackmill - Let It Be",
    "Zeds Dead - Eyes on Fire",
    "Nero - Promises"
  };

  for (int i = 0; i < playlist.size(); i++) {
    std::cout << i + 1 << ". " << playlist[i] << "\n";
  }
}
```

> [!NOTE]
> **The range-based alternative**
> Modern C++ offers `for (const auto& track : playlist)`, which walks every element without an
> index. It reads better, but it cannot give you the position — so the classic indexed loop still
> earns its place.

> [!TIP]
> `i + 1` is used for the human-readable numbering. Keep the index 0-based and add 1 only when
> printing — never change the index itself.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
