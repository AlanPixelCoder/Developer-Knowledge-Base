# 06. From Source to Switch

**Spanish version:** [06 - De Fuente a Interruptor](./06%20-%20De%20Fuente%20a%20Interruptor.md)

**Course:** C++
**Chapter:** 1 — First Boot
**Topic:** Compiling and running: source, object, executable
**Tags:** `#cpp` `#toolchain` `#gcc`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-1-7C5CFF?style=for-the-badge" alt="Chapter 1">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

The engine cannot boot from a `.cpp` file. The machine only understands instructions, so something
has to translate. That something is the toolchain, and it has three stages.

| Stage | What happens | Output |
| :--- | :--- | :--- |
| Preprocess | Headers are copied in, macros expand | One big translation unit |
| Compile | That unit becomes assembly, then machine code | `main.o` |
| Link | Object files and libraries are joined, `main` becomes the entry point | `ember` |

The driver does all three when you ask for an executable:

```bash
g++ -std=c++17 -Wall -Wextra -O2 main.cpp -o ember
./ember
```

## Reading the command

| Flag | Meaning |
| :--- | :--- |
| `-std=c++17` | Use the C++17 standard, so the compiler stops guessing |
| `-Wall -Wextra` | Turn on the warnings that catch real mistakes |
| `-O2` | Optimise; the engine will not be fast by accident |
| `-o ember` | Name the output `ember` instead of `a.out` |
| `./ember` | Run the file in the current folder — the `./` is not decoration |

> [!WARNING]
> `-o` takes the next word as the output name. `g++ -o main.cpp ember` builds a program called
> `main.cpp` from a file called `ember`, and the error message will be baffling.

> [!CAUTION]
> After a failed build, the old executable is still there. Running `./ember` and seeing the previous
> behaviour is the classic sign that the compile never succeeded and nobody read the output.

> [!TIP]
> Chain the two steps so a failed build never runs: `g++ main.cpp -o ember && ./ember`. The `&&`
> runs the second command only if the first returned success.

---

**Next:** [[07 - Raw Materials]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
