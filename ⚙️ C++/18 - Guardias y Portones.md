# 18. Guardias y Portones

**Versión original en inglés:** [18 - Guards and Gates](./18%20-%20Guards%20and%20Gates.md)

**Curso:** C++
**Capítulo:** 3 — Decisiones
**Tema:** Operadores lógicos y evaluación de cortocircuito
**Etiquetas:** `#cpp` `#logic` `#booleans`

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

Un portón que se abre solo si el jugador lleva luz **y** no está agotado necesita una condición
compuesta: dos hechos, una decisión.

```cpp
#include <iostream>

int main() {
  bool tiene_linterna = true;
  bool esta_agotado = false;
  int profundidad = 12;

  std::cout << std::boolalpha;

  std::cout << "linterna y no agotado:  "
            << (tiene_linterna && !esta_agotado) << "\n";
  std::cout << "linterna o cuerda:      "
            << (tiene_linterna || false) << "\n";
  std::cout << "puede descender:        "
            << (tiene_linterna && !esta_agotado && profundidad < 20) << "\n";
}
```

## Salida

```text
linterna y no agotado:  true
linterna o cuerda:      true
puede descender:        true
```

`std::boolalpha` hace que `bool` se imprima como `true` / `false` en vez de `1` / `0`; queda activo
para el resto del flujo.

## Los tres operadores

| Operador | Nombre | Verdadero cuando |
| :--- | :--- | :--- |
| `&&` | y | **ambos** lados son verdaderos |
| `\|\|` | o | **al menos un** lado es verdadero |
| `!` | no | el único operando es falso |

## Cortocircuito: la parte que sorprende

`a && b` evalúa `b` solo si `a` es verdadero. `a || b` evalúa `b` solo si `a` es falso. Es a la vez un
truco de velocidad y un mecanismo de seguridad, y una fuente de errores cuando `b` tiene efectos.

> [!WARNING]
> `std::cout << tiene_linterna && esta_agotado` **no** imprime un booleano. `<<` se une más fuerte
> que `&&`, así que se lee como `(std::cout << tiene_linterna) && ...`. Encierra la condición entre
> paréntesis.

> [!TIP]
> Usa el cortocircuito a propósito: `if (indice < tam && items[indice] > 0)` es seguro porque la
> segunda prueba nunca corre cuando falla la primera. Cambia el orden y la misma línea lee fuera de
> límites.

---

**Siguiente:** [[19 - Prueba de Preguntas]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
