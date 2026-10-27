# 25. Puesto de Limonada

**Versión original en inglés:** [25 - Lemonade Stand.md](./25%20-%20Lemonade%20Stand.md)

**Curso:** C++
**Tema:** Índices de vectores
**Etiquetas:** `#cpp` `#vectors` `#index`

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

Los elementos de un vector son modificables: podemos actualizar elementos individuales. Pero antes
hay que saber cómo **acceder** a un elemento concreto.

Aquí entra el **índice**: la posición de un elemento dentro del vector.

C++ es **base 0**, es decir, los índices empiezan en `0`:

- El índice `0` es el primer elemento.
- El índice `1` es el segundo, y así sucesivamente.
- El último índice siempre es `size() - 1`.

Accede a un elemento con la sintaxis `nombre[indice]`.

```cpp
std::vector<int> limonada = {25, 28, 40, 85, 76};
std::cout << limonada[0]; // 25
std::cout << limonada[4]; // 76 — el último elemento
```

## Ejemplo

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<int> limonada = {25, 28, 40, 85, 76};
  std::vector<double> ventas = {75.50, 89.25, 60.00, 102.45, 95.10};

  std::cout << "Limones usados el último día: " << limonada[4] << "\n";
  std::cout << "Ventas del último día: $" << ventas[4] << "\n";

  double ganancia_por_limonada = ventas[4] / limonada[4];
  std::cout << "Ganancia por limonada: $" << ganancia_por_limonada << "\n";

  // Fuera de rango — lee memoria que no es nuestra. Comportamiento indefinido:
  // std::cout << limonada[9] << "\n";
}
```

> [!CAUTION]
> **Salirse del rango no avisa**
> `limonada[9]` en un vector de 5 elementos no lanza nada. Lee lo que haya en ese desplazamiento:
> basura, o datos de otra persona. En C++ esto es *comportamiento indefinido*: el compilador no te
> debe nada. Protege el índice o usa `.at()` si quieres una excepción real.

> [!TIP]
> El último elemento siempre es `v[v.size() - 1]`. Memoriza esa forma; aparece constantemente.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
