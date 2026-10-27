# 03. Nos Vemos Más Tarde, Cocodrilo

**Versión original en inglés:** [03 - See Ya Later Alligator.md](./03%20-%20See%20Ya%20Later%20Alligator.md)

**Curso:** C++
**Tema:** Estructura, bloques de código y secuencias de escape
**Etiquetas:** `#cpp` `#structure` `#escape-sequences`

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

## Estructura del programa

| Elemento | Función |
| :--- | :--- |
| **`#include <iostream>`** | Incluye la biblioteca necesaria para entrada/salida |
| **`int main()`** | La **función** donde arranca todo programa |
| **`{ }`** | El **bloque de código**: todo lo que está dentro se ejecuta como una unidad |

C++ se ejecuta línea a línea, de arriba hacia abajo del archivo. Podemos mostrar varios mensajes
con varias sentencias `std::cout`.

## Secuencias de escape

Una **secuencia de escape** es una barra invertida seguida de un carácter que el compilador
interpreta en lugar de imprimir literalmente.

| Secuencia | Efecto |
| :--- | :--- |
| `\n` | Nueva línea |
| `\t` | Tabulación |
| `\"` | Comilla doble literal |
| `\\` | Barra invertida literal |

`\n` es la más usada: crea una línea nueva para que la salida aparezca abajo.

```cpp
#include <iostream>

int main() {
  std::cout << "¡Adiós!\nCiao!\nAu revoir!\n¡Nos vemos!";
}
```

> [!TIP]
> Un solo `std::cout` con cuatro `\n` supera a cuatro sentencias: menos líneas, misma salida y un
> lugar menos donde esconderse un error.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
