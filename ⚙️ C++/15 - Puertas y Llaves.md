# 15. Puertas y Llaves

**Versión original en inglés:** [15 - Doors and Keys](./15%20-%20Doors%20and%20Keys.md)

**Curso:** C++
**Capítulo:** 3 — Decisiones
**Tema:** if / else, llaves y la bifurcación de dos caminos
**Etiquetas:** `#cpp` `#if` `#control-flow`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-3-7C5CFF?style=for-the-badge" alt="Chapter 3">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Una puerta cerrada tiene exactamente dos desenlaces, y la bifurcación de dos caminos es la decisión
más pequeña que puede tomar C++.

```cpp
#include <iostream>

int main() {
  int llave_requerida = 7;
  int llave_en_mano = 7;

  if (llave_en_mano == llave_requerida) {
    std::cout << "la puerta se abre\n";
  } else {
    std::cout << "la cerradura rechaza la llave\n";
  }
}
```

Cambia `llave_en_mano` a `3` y se imprime la otra línea. Nada más del programa cambia.

## La forma

| Pieza | Significado |
| :--- | :--- |
| `if (condición)` | Ejecuta el bloque siguiente solo si la condición es verdadera |
| `else` | Ejecuta el otro bloque cuando no lo es |
| `{ }` | El bloque; obligatorio en cuanto hay más de una sentencia |

`else` es opcional. Sin él, una condición falsa simplemente significa *no hacer nada y continuar*.

> [!WARNING]
> Sin llaves, **solo la sentencia siguiente** pertenece al `if`. Añade una segunda línea y se
> ejecutará siempre, sea cual sea la condición, mientras la indentación insiste en que forma parte
> de la rama.

> [!TIP]
> Prefiere la condición en positivo. `if (tiene_llave)` se lee mejor que `if (!sin_llave)` y le
> ahorra al lector una negación mental.

---

**Siguiente:** [[16 - Rangos y Umbrales]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
