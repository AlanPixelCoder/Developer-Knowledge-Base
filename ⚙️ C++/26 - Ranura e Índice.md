# 26. Ranura e Índice

**Versión original en inglés:** [26 - Slot and Index](./26%20-%20Slot%20and%20Index.md)

**Curso:** C++
**Capítulo:** 5 — Colecciones
**Tema:** Leer y escribir elementos, y lo que operator[] no comprueba
**Etiquetas:** `#cpp` `#vector` `#indexing`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-5-7C5CFF?style=for-the-badge" alt="Chapter 5">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

La alforja tiene ocho ranuras. Leer la ranura 3 es una línea; escribir la ranura 3 es la misma línea
a la izquierda de un igual. Leer la ranura 8 es comportamiento indefinido, y el compilador no dirá
nada.

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<std::string> ranuras(3, "vacía");

  ranuras[1] = "antorcha";
  ranuras[2] = "cuerda";

  std::cout << "ranura 0: " << ranuras[0] << "\n";
  std::cout << "ranura 1: " << ranuras[1] << "\n";
  std::cout << "ranura 2: " << ranuras[2] << "\n";
  std::cout << "cuenta:   " << ranuras.size() << "\n";
}
```

## Salida

```text
ranura 0: vacía
ranura 1: antorcha
ranura 2: cuerda
cuenta:   3
```

## Reglas del índice

| Dato | Valor |
| :--- | :--- |
| Primer índice | `0` |
| Último índice | `size() - 1` |
| Válidos para tamaño 3 | `0`, `1`, `2` |
| Comprobados por `[]` | ninguno |

`ranuras.at(5)` lanza `std::out_of_range`. `ranuras[5]` lee la memoria que haya ahí. Usa `[]` cuando
el índice está demostradamente en rango, `at()` cuando viene de una entrada.

## Una ranura es una variable

Todo lo que puedes hacer con una variable `int` lo puedes hacer con `ranuras[0]`: asignarla,
imprimirla, compararla, pasarla a una función. El índice es aritmética de direcciones disfrazada.

> [!WARNING]
> Un `[]` fuera de rango es comportamiento indefinido, no un mensaje de error. El programa puede
> imprimir basura, caerse más tarde o parecer correcto hasta la demo. `at()` cuesta una comprobación
> y compra un diagnóstico.

> [!TIP]
> Los índices negativos no dan la vuelta en un vector como en Python. `ranuras[-1]` está fuera de
> rango, y con una conversión sin signo está muy fuera de rango.

---

**Siguiente:** [[27 - Cargar y Descargar]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
