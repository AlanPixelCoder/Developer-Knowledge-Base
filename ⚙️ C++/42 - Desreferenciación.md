# 42. Desreferenciación

**Versión original en inglés:** [42 - Dereference.md](./42%20-%20Dereference.md)

**Curso:** C++
**Tema:** Desreferenciar punteros
**Etiquetas:** `#cpp` `#pointers` `#dereference`

<p align="left">
  <img src="https://img.shields.io/badge/Lenguaje-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Dificultad-AVANZADO-E74C3C?style=for-the-badge" alt="Avanzado">
  <img src="https://img.shields.io/badge/Estado-Completo-00C2A8?style=for-the-badge" alt="Completo">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Bóveda-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Ya sabemos crear un puntero y obtener la dirección de la variable a la que apunta. Pero ¿cómo
accedemos al **valor** al que apunta?

**Desreferenciar** significa acceder al valor al que apunta un puntero. Se hace con `*`, el operador
de desreferenciación.

```cpp
int x = 420;
int* p = &x;

std::cout << p << "\n";  // la dirección de memoria (ej. 0x16f...)
std::cout << *p << "\n"; // el valor: 420
```

## Las dos caras de `*`

| Contexto | Significado | Ejemplo |
| :--- | :--- | :--- |
| En una **declaración** | Crea un puntero | `int* p = &x;` |
| **Fuera** de una declaración | Desreferencia: lee el valor | `std::cout << *p;` |

Mismo carácter, dos trabajos. La diferencia es la posición: `*` junto a un tipo es declaración; `*`
en una expresión es desreferencia.

## Escribir a través de un puntero

Desreferenciar también es cómo **cambias** el valor original:

```cpp
*p = 99;          // ahora x vale 99
std::cout << x;   // 99
```

```cpp
// Continuando la nota anterior
std::cout << *pConsejo1 << "\n";
std::cout << *pConsejo2 << "\n";
std::cout << *pConsejo3 << "\n";
std::cout << *pConsejo4 << "\n";
```

> [!TIP]
> **Lee `*` como "el valor en"**
> `*p` → "el valor en `p`". `&x` → "la dirección de `x`". Esas dos frases cubren casi cualquier línea
> de código con punteros que leas.

> [!WARNING]
> Desreferenciar un puntero sin inicializar o colgante es comportamiento indefinido. La dirección
> puede ser válida, puede apuntar a otra variable o puede provocar un fallo. Inicializa siempre: ver
> [[44 - Nullptr]].

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
