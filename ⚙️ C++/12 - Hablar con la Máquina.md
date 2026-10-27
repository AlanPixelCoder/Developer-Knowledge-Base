# 12. Hablar con la Máquina

**Versión original en inglés:** [12 - Speak to the Machine](./12%20-%20Speak%20to%20the%20Machine.md)

**Curso:** C++
**Capítulo:** 2 — Valores en Bruto
**Tema:** Leer entrada de la consola con std::cin
**Etiquetas:** `#cpp` `#input` `#iostream`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-2-7C5CFF?style=for-the-badge" alt="Chapter 2">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

La salida convierte un programa en un informe. La entrada lo convierte en una herramienta. La consola
del motor pide un nombre de build y un tope de fotogramas, y luego confirma lo que recibió.

```cpp
#include <iostream>
#include <string>

int main() {
  std::string nombre_build;
  int tope_fps;

  std::cout << "nombre del build: ";
  std::cin >> nombre_build;

  std::cout << "tope de fotogramas: ";
  std::cin >> tope_fps;

  std::cout << "compilando " << nombre_build << " a " << tope_fps << " fps\n";
}
```

## Las flechas apuntan hacia donde van los datos

| Operador | Dirección | Significado |
| :--- | :--- | :--- |
| `<<` | hacia fuera del programa | insertar en un flujo de salida |
| `>>` | hacia dentro del programa | extraer de un flujo de entrada |

`std::cin >> nombre` lee un solo token separado por espacios. Por eso un nombre de build con espacio
se corta en el espacio.

## Una sesión de ejemplo

```text
nombre del build: ember-rc1
tope de fotogramas: 120
compilando ember-rc1 a 120 fps
```

> [!WARNING]
> `std::cin >> x` con `x` de tipo `int` y el usuario escribiendo `abc` deja el flujo en estado de
> fallo; toda lectura posterior vuelve al instante. Comprueba con `if (std::cin >> x)` antes de
> confiar en el valor.

> [!NOTE]
> Para una línea completa, con espacios incluidos, usa `std::getline(std::cin, linea)`. Mezclar `>>`
> y `getline` exige cuidado: el `>>` deja el salto de línea en el búfer y `getline` lo consume como
> línea vacía.

---

**Siguiente:** [[13 - Escalado de Niveles]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
