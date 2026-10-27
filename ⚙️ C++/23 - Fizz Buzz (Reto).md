# 23. Fizz Buzz (Reto)

**Versión original en inglés:** [23 - Fizz Buzz.md](./23%20-%20Fizz%20Buzz.md)

**Curso:** C++
**Tema:** Repaso del capítulo 4 y desafío Fizz Buzz
**Etiquetas:** `#cpp` `#recap` `#loops` `#challenge`

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

## Repaso del capítulo 4

- El bucle `while` itera una y otra vez mientras la condición sea `true`.
- El bucle `for` itera un número determinado de veces.
- `i++` incrementa, `i--` decrementa.
- Ambos bucles pueden ejecutarse cero veces si la condición empieza en `false`.

## Fizz Buzz

Fizz Buzz es un juego infantil de palabras que enseña divisiones — y una pregunta clásica de
entrevista técnica.

Las reglas:

- Muestra los números del 1 al 100.
- Para múltiplos de 3, imprime `Fizz` en lugar del número.
- Para múltiplos de 5, imprime `Buzz` en lugar del número.
- Para múltiplos de **ambos**, imprime `FizzBuzz`.

## Ejemplo

```cpp
#include <iostream>

int main() {
  for (int i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      std::cout << "FizzBuzz\n";
    } else if (i % 3 == 0) {
      std::cout << "Fizz\n";
    } else if (i % 5 == 0) {
      std::cout << "Buzz\n";
    } else {
      std::cout << i << "\n";
    }
  }
}
```

> [!IMPORTANT]
> **El orden es todo el truco**
> El caso combinado `i % 15 == 0` debe comprobarse **primero**. Si `i % 3` fuera antes, el 15
> imprimiría `Fizz` y nunca llegaría a `FizzBuzz`. Como `else if` se detiene en la primera
> coincidencia, lo específico debe ir antes que lo general — la misma lección que en
> [[15 - Niveles y Rangos]].

> [!TIP]
> `%` es el motor aquí: un número es divisible por `n` exactamente cuando `x % n == 0`.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
