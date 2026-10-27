# 18. Trivial Quiz

**Versión original en inglés:** [18 - Trivia Quiz.md](./18%20-%20Trivia%20Quiz.md)

**Curso:** C++
**Tema:** Repaso del capítulo 3 y proyecto de quiz
**Etiquetas:** `#cpp` `#recap` `#project` `#control-flow`

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

## Repaso del capítulo 3

- **Flujo de control** es el orden en que se ejecuta el código.
- **`if`** comprueba una condición y ejecuta su bloque cuando es `true`.
- **`else if`** se añade entre `if` y `else` para comprobar más condiciones.
- **`else`** se ejecuta cuando ninguna de las anteriores coincidió.
- **Operadores relacionales** comparan dos valores: `==`, `!=`, `>`, `>=`, `<`, `<=`.
- **Operadores lógicos** combinan condiciones: `&&`, `||`, `!`.

## Proyecto: Trivial Quiz

```cpp
#include <iostream>
#include <string>

int main() {
  int puntuacion = 0;
  int resp1, resp2;
  std::string resp3;

  // Pregunta 1
  std::cout << "P1) ¿Cuál es el río más largo del mundo? 💧\n";
  std::cout << "1) Río Misuri\n";
  std::cout << "2) Nilo\n";
  std::cout << "3) Río Amazonas\n";
  std::cout << "4) Río Yangtsé\n\n";
  std::cin >> resp1;

  if (resp1 == 2) {
    puntuacion++;
  }

  // Pregunta 2
  std::cout << "\nP2) ¿Cuántos huesos tiene el cuerpo humano? 🦴\n";
  std::cout << "1) 92\n";
  std::cout << "2) 150\n";
  std::cout << "3) 206\n";
  std::cout << "4) 10\n\n";
  std::cin >> resp2;

  if (resp2 == 3) {
    puntuacion++;
  }

  // Pregunta 3 (texto libre)
  std::cout << "\nP3) ¿Qué alimento nunca caduca? 🍯\n";
  std::cout << "Escribe tu respuesta: ";
  std::cin >> resp3;

  if (resp3 == "Miel" || resp3 == "miel") {
    puntuacion++;
  }

  std::cout << "\nTu puntuación final es: " << puntuacion << "/3\n";
}
```

> [!NOTE]
> **`puntuacion++` es `puntuacion = puntuacion + 1`**
> El operador de incremento suma uno y guarda el resultado. Su espejo, `puntuacion--`, resta uno.
> Ambos vuelven al escenario en [[21 - Contando Ovejas]].

> [!TIP]
> Las respuestas de texto libre son frágiles: `std::cin >> resp3` se detiene en el primer espacio,
> así que "miel de abeja" solo compararía "miel". Normaliza la entrada (a minúsculas) antes de
> comparar.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
