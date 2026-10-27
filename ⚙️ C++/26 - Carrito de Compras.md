# 26. Carrito de Compras

**Versión original en inglés:** [26 - Order Cart.md](./26%20-%20Order%20Cart.md)

**Curso:** C++
**Tema:** Métodos de vectores (`push_back`, `pop_back`, `size`)
**Etiquetas:** `#cpp` `#vectors` `#methods`

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

Los vectores incluyen funciones integradas que actúan como herramientas listas para usar.

## Añadir y quitar elementos

| Método | Efecto |
| :--- | :--- |
| `.push_back(x)` | Añade `x` al **final** del vector |
| `.pop_back()` | Elimina el elemento del **final** |
| `.size()` | Devuelve el número de elementos |

```cpp
std::vector<std::string> adn = {"AUG", "AUC", "UCG"};

adn.push_back("UAA"); // {"AUG", "AUC", "UCG", "UAA"}
adn.pop_back();       // {"AUG", "AUC", "UCG"}
```

## Tamaño

`.size()` devuelve el número de elementos del vector. Con docenas de elementos se vuelve
imprescindible — y es el límite canónico de cualquier bucle.

```cpp
std::cout << adn.size() << "\n"; // Salida: 3
```

## Ejemplo completo

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<std::string> carrito = {
    "🍕 Pizza de pepperoni",
    "🥗 Ensalada",
    "🥤 Refresco"
  };

  carrito.push_back("🥫 Salsa de tomate");
  carrito.pop_back();

  std::cout << carrito[0] << " ";
  std::cout << carrito[1] << " ";
  std::cout << carrito[2] << "\n";

  std::cout << carrito.size() << "\n";
}
```

> [!WARNING]
> **`pop_back()` en un vector vacío** es comportamiento indefinido: no hay nada que quitar. Comprueba
> `!carrito.empty()` primero. Igual que el índice fuera de rango, no te avisará.

> [!TIP]
> `.empty()` es la forma idiomática de comprobar si está vacío (`size() == 0` también funciona, pero
> dice menos).

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
