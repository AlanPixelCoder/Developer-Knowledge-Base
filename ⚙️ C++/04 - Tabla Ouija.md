# 04. Tabla Ouija

**Versión original en inglés:** [04 - Ouija Board.md](./04%20-%20Ouija%20Board.md)

**Curso:** C++
**Tema:** Comentarios de una línea y multilínea
**Etiquetas:** `#cpp` `#comments` `#documentation`

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

En programación los comentarios son importantes: documentan lo que hace nuestro código, para
nosotros y para otros desarrolladores. También sirven para desactivar partes de un programa.
Cuando el programa se ejecuta, los comentarios se **ignoran** por completo.

## Comentarios de una línea

Se crean con `//`. Todo lo que está a la derecha de `//` en esa línea se ignora.

```cpp
int vida = 100; // salud inicial del héroe
```

## Comentarios multilínea

Empiezan con `/*` y terminan con `*/`. Todo lo que está entre ambos se comenta, así que pueden ser
tan largos como quieras.

```cpp
/*
  Prototipo de combate de Emberfall
  Fase 1: orden de turnos
  Fase 2: resolución del daño
*/
```

## Ejemplo

```cpp
// Tabla Ouija 👻
// Mesa de adivinación de Emberfall

#include <iostream>

int main() {
  std::cout << "------------------------------\n";
  std::cout << "|       x SÍ    NO x         |\n";
  std::cout << "|                            |\n";
  std::cout << "|       ABCDEFGHIJKLM        |\n";
  std::cout << "|       NOPQRSTUVWXYZ        |\n";
  std::cout << "|                            |\n";
  std::cout << "|       1234567890           |\n";
  std::cout << "------------------------------\n";
}
```

> [!NOTE]
> **El código comentado es un olor, no una estrategia**
> Deja una línea muerta comentada un minuto si estás comparando dos enfoques. Si sobrevive al
> commit, bórrala: el control de versiones ya la recuerda por ti.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
