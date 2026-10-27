# 43. Referencias vs Punteros

**Versión original en inglés:** [43 - References vs. Pointers.md](./43%20-%20References%20vs.%20Pointers.md)

**Curso:** C++
**Tema:** Referencias y paso por referencia
**Etiquetas:** `#cpp` `#pointers` `#references` `#memory`

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

Los punteros existen desde C (y el C++ temprano); las **referencias** llegaron a C++ más tarde —
sobre todo para facilitar el paso de parámetros y los alias. Una referencia es una alternativa más
segura y cómoda a un puntero cuando no necesitas aritmética de punteros ni reasignar la dirección.

A diferencia de los punteros, las referencias:

- deben **inicializarse** al declararse,
- no pueden ser **nulas** (no puedes ponerte un apodo si no existes),
- no pueden **reasignarse** a otra variable.

```cpp
// Referencia
int valor = 42;
int& referencia = valor;

// Puntero
int x = 10;
int* p = &x;
```

> [!NOTE]
> Aquí `&` significa **tipo referencia**, no "dirección-de". El contexto decide: `int& r = valor;`
> declara una referencia; `&valor` toma una dirección.

## Comparación

| Característica | Puntero | Referencia |
| :--- | :--- | :--- |
| Sintaxis | `int* p = &x;` | `int& r = x;` |
| Puede ser nulo | Sí (`nullptr`) | No |
| Reasignable | Sí | No |
| Desreferencia | Sí (`*p`) | No: *es* la variable |
| Aritmética | Sí | No |
| Inicialización | Opcional | Obligatoria |

## Paso por valor vs paso por referencia

- **Paso por valor** — la función recibe una **copia**. Los cambios internos no tocan el original.
- **Paso por referencia** — la función recibe un **alias**. Los cambios internos *sí* afectan al
  original.

```cpp
#include <iostream>

// int& pasa la salud por referencia
void curarJugador(int& salud) {
  salud += 20;
}

int main() {
  int saludJugador = 50;

  curarJugador(saludJugador); // altera saludJugador de forma permanente

  std::cout << saludJugador << "\n"; // 70
}
```

> [!IMPORTANT]
> **La pregunta clásica de examen**
> Quita el `&` y `saludJugador` se queda en `50`: la función curó una copia. Ese `&` es toda la
> diferencia entre "curar al héroe" y "curar un holograma".

> [!TIP]
> Prefiere referencias para parámetros; recurre a punteros solo cuando "no hay objeto" sea un estado
> legítimo (`nullptr`) o cuando necesites re-apuntar.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
