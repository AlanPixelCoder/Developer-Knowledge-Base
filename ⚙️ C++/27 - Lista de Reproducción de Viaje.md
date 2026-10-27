# 27. Lista de Reproducción de Viaje

**Versión original en inglés:** [27 - Roadtrip Playlist.md](./27%20-%20Roadtrip%20Playlist.md)

**Curso:** C++
**Tema:** Iterar sobre vectores
**Etiquetas:** `#cpp` `#vectors` `#loops` `#iteration`

<p align="left">
  <img src="https://img.shields.io/badge/Lenguaje-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Estado-Completo-00C2A8?style=for-the-badge" alt="Completo">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Bóveda-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Puedes iterar sobre un vector con un bucle `for`.

Usa `.size()` en la condición del bucle para que se ejecute exactamente tantas veces como elementos
haya — y el contador `i` sirve a la vez como índice de cada elemento.

```cpp
for (int i = 0; i < playlist.size(); i++) {
  std::cout << playlist[i] << "\n";
}
```

## Cómo leer la condición

| Parte | Significado |
| :--- | :--- |
| `int i = 0` | Empieza en el primer índice |
| `i < playlist.size()` | Detente *antes* del primer índice inválido |
| `i++` | Pasa al siguiente elemento |

`<` — no `<=`. Con `<=` el bucle intentaría `playlist[size()]` en su última pasada, que está uno más
allá del final.

## Ejemplo

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
> **La alternativa basada en rango**
> El C++ moderno ofrece `for (const auto& cancion : playlist)`, que recorre cada elemento sin índice.
> Se lee mejor, pero no te da la posición, así que el bucle indexado clásico sigue ganándose su
> lugar.

> [!TIP]
> `i + 1` se usa para la numeración humana. Mantén el índice en base 0 y suma 1 solo al imprimir:
> nunca cambies el índice en sí.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
