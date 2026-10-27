# 32. Conversions (Continuation)

**Spanish version:** [32 - Conversiones (Continuación).md](./32%20-%20Conversiones%20%28Continuaci%C3%B3n%29.md)

**Course:** C++
**Topic:** Returning Values and Calling Functions
**Tags:** `#cpp` `#functions` `#return` `#conversion`

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

When a function returns a value, we can use that value directly in an output statement or assign
it to a variable.

> [!NOTE]
> When a `return` statement is reached, C++ stops executing the current function and sends a value
> out to wherever the function was called.

## Example

```cpp
#include <iostream>

// Takes BPM, returns seconds per beat
double bpm_to_seconds(double bpm) {
  return 60.0 / bpm;
}

int main() {
  double track_bpm = 140.0;

  std::cout << "Analyzing track...\n";
  std::cout << "Tempo: " << track_bpm << " BPM\n";

  // Use the returned value directly in an output statement
  std::cout << "Time per beat: " << bpm_to_seconds(track_bpm) << " seconds\n";

  // Call it again with a different argument
  std::cout << "\nAnalyzing ambient track...\n";
  std::cout << "Tempo: 90 BPM\n";
  std::cout << "Time per beat: " << bpm_to_seconds(90.0) << " seconds\n";
}
```

## Output

```text
Analyzing track...
Tempo: 140 BPM
Time per beat: 0.428571 seconds

Analyzing ambient track...
Tempo: 90 BPM
Time per beat: 0.666667 seconds
```

> [!NOTE]
> The formula: $\text{seconds per beat} = \dfrac{60}{\text{BPM}}$. At 120 BPM one beat lasts
> half a second; double the tempo, halve the beat.

> [!TIP]
> `60.0` — not `60` — is what keeps the division floating-point. Write `60 / bpm` with two
> integers and you'd get `0`. Same trap as [[09 - Temperature]].

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
