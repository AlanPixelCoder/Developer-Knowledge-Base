# 20. El Bucle que Espera

**Versión original en inglés:** [20 - The Loop That Waits](./20%20-%20The%20Loop%20That%20Waits.md)

**Curso:** C++
**Capítulo:** 4 — Iteración
**Tema:** Qué es iterar, y las cuatro partes de un bucle que termina
**Etiquetas:** `#cpp` `#loops` `#do-while`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-4-7C5CFF?style=for-the-badge" alt="Chapter 4">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

El motor pide un código de desbloqueo de cuatro dígitos. El jugador tiene tres intentos, y cada
código equivocado tiene que devolver el programa al aviso: ese "volver al aviso" es iteración.

```cpp
#include <iostream>

int main() {
  const int CODIGO = 4821;
  int intentos = 0;
  int intento = 0;

  do {
    intentos++;
    intento = CODIGO + (intentos == 2 ? -111 : 0);  // entrada simulada
    std::cout << "intento " << intentos << ": " << intento << "\n";
  } while (intento != CODIGO && intentos < 3);

  if (intento == CODIGO) {
    std::cout << "consola desbloqueada tras " << intentos << " intentos\n";
  } else {
    std::cout << "consola bloqueada\n";
  }
}
```

## Salida

```text
intento 1: 4821
consola desbloqueada tras 1 intentos
```

## Las cuatro partes

| Parte | En este programa | Si falta |
| :--- | :--- | :--- |
| Estado inicial | `intentos = 0` | El contador arranca con basura |
| Condición | `intento != CODIGO && intentos < 3` | El bucle nunca termina |
| Cuerpo | pedir, comparar, imprimir | No ocurre nada útil |
| Cambio | `intentos++` | La condición nunca se hace falsa |

## `do` se ejecuta al menos una vez

Un `while` comprueba primero y puede ejecutarse cero veces. Un `do ... while` ejecuta el cuerpo y
luego comprueba. Los avisos quieren lo segundo: siempre muestras el aviso antes de que te digan que
la respuesta está mal.

> [!CAUTION]
> Todo bucle necesita un camino hacia una condición falsa. Si el paso de cambio está dentro de un
> `if` que nunca se cumple, el bucle corre para siempre y el único síntoma es un programa que no
> vuelve a imprimir.

> [!TIP]
> Traza las dos primeras iteraciones en papel antes de ejecutar. Los bucles son fáciles de escribir
> y difíciles de releer; dos líneas de traza atrapan casi todos los errores de off-by-one.

---

**Siguiente:** [[21 - Patrones de Espera]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
