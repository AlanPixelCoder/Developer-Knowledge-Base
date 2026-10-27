# 32. El Tablón de la Taberna

**Versión original en inglés:** [32 - The Tavern Board](./32%20-%20The%20Tavern%20Board.md)

**Curso:** C++
**Capítulo:** 6 — Funciones
**Tema:** Parámetros frente a argumentos, y devolver un valor calculado
**Etiquetas:** `#cpp` `#functions` `#return`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-6-7C5CFF?style=for-the-badge" alt="Chapter 6">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Un tablón a la puerta de la taberna lista precios de recompensa: tanto por piel de lobo, un extra por
una pieza limpia, una penalización por mercancía dañada. El precio depende de las entradas, y el
tablón nunca cambia.

```cpp
#include <iostream>

double recompensa(int pieles, bool limpia, int danadas) {
  double total = pieles * 12.5;
  if (limpia) {
    total += 20.0;
  }
  total -= danadas * 4.0;
  return total;
}

int main() {
  std::cout << recompensa(3, true, 0) << "\n";
  std::cout << recompensa(3, false, 1) << "\n";
  std::cout << recompensa(0, true, 0) << "\n";
}
```

## Salida

```text
57.5
33.5
20
```

## Parámetro y argumento

| Palabra | Dónde vive | Ejemplo |
| :--- | :--- | :--- |
| Parámetro | en la definición | `int pieles` |
| Argumento | en la llamada | `3` |

El parámetro es una variable local creada de nuevo en cada llamada. Asignarle dentro de la función
nunca toca la variable de quien llama.

## `return` termina la llamada

`return` devuelve el valor y se detiene. Nada de lo que venga después en esa llamada se ejecuta.

```cpp
if (pieles < 0) {
  return 0.0;   // salida temprana: se salta el resto del cuerpo
}
```

Una salida temprana para un caso imposible mantiene plano el camino principal, que se lee mejor que
un nido de `if`.

> [!IMPORTANT]
> Una función con tipo de retorno distinto de `void` debe devolver en todos los caminos. Caerse por
> el final es comportamiento indefinido, y g++ solo avisa cuando el camino que falta es evidente.

> [!TIP]
> Fíjate en que `recompensa(0, true, 0)` devuelve `20`, no `0`: el extra por pieza limpia se aplica
> antes de contar pieles. Si una cacería de cero debe pagar nada, compruébalo primero y deja la regla
> visible.

---

**Siguiente:** [[33 - Llenar las Ranuras]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
