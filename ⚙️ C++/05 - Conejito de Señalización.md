# 05. Conejito de Señalización

**Versión original en inglés:** [05 - Sign Bunny.md](./05%20-%20Sign%20Bunny.md)

**Curso:** C++
**Tema:** Repaso del capítulo 1 y arte ASCII
**Etiquetas:** `#cpp` `#recap` `#ascii`

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

## Repaso del capítulo 1

- La sentencia `std::cout` muestra mensajes en la terminal.
- El código C++ se ejecuta línea a línea, de arriba hacia abajo.
- Los comentarios de una línea se crean con `//`.
- Los comentarios multilínea empiezan con `/*` y cierran con `*/`.
- `\n` rompe la línea; `\t` inserta una tabulación.

## Arte ASCII

El arte de terminal se construye con caracteres normales. La dificultad no es el código: es
escapar los caracteres que significan algo para C++ (`\`, `"`). Cada barra invertida que quieras
*imprimir* se escribe `\\`, y cada comilla `\"`.

```cpp
// Conejito de señalización 🐰
// Tablón de anuncios de la taberna

#include <iostream>

int main() {
  std::cout << "  (\\_/)" << "  +------------------+\n";
  std::cout << "  (o.o )" << "  | GRACIAS          |\n";
  std::cout << "  ( > <)" << "  | POR VENIR        |\n";
  std::cout << "          +------------------+\n";
}
```

> [!TIP]
> Dibuja el arte ASCII primero en un archivo de texto plano y después escápalo. Intentar dibujar y
> escapar al mismo tiempo es cómo el conejito termina con tres orejas.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
