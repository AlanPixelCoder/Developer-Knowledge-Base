# 44. El Códice, Animado

**Versión original en inglés:** [44 - The Familiar Codex, Animated](./44%20-%20The%20Familiar%20Codex%2C%20Animated.md)

**Curso:** C++
**Capítulo:** 7 — Entidades
**Tema:** Separar declaración de definición entre archivos
**Etiquetas:** `#cpp` `#headers` `#translation-units`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Chapter-7-7C5CFF?style=for-the-badge" alt="Chapter 7">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

El códice ha crecido: trescientas líneas, usadas por el invocador, la interfaz y el sistema de
guardado. Todo archivo que lo incluya recompilaría la cosa entera. La solución es vieja y aburrida:
declaración en una cabecera, definición en un solo `.cpp`.

`codice.hpp` — la promesa:

```cpp
#ifndef CODICE_HPP
#define CODICE_HPP

#include <cstddef>
#include <string>
#include <vector>

class CodiceFamiliares {
 public:
  void registrar(const std::string& nombre, int nivel);
  std::size_t cuenta() const;
  int nivel_maximo() const;
  std::string resumen() const;

 private:
  std::vector<std::string> nombres_;
  std::vector<int> niveles_;
};

#endif  // CODICE_HPP
```

`codice.cpp` — la entrega:

```cpp
#include "codice.hpp"

void CodiceFamiliares::registrar(const std::string& nombre, int nivel) {
  nombres_.push_back(nombre);
  niveles_.push_back(nivel);
}

std::size_t CodiceFamiliares::cuenta() const { return nombres_.size(); }

int CodiceFamiliares::nivel_maximo() const {
  int mejor = 0;
  for (int nivel : niveles_) {
    mejor = nivel > mejor ? nivel : mejor;
  }
  return mejor;
}

std::string CodiceFamiliares::resumen() const {
  return std::to_string(cuenta()) + " familiares, nivel máximo " +
         std::to_string(nivel_maximo());
}
```

`main.cpp` — quien lo usa:

```cpp
#include <iostream>

#include "codice.hpp"

int main() {
  CodiceFamiliares codigo;
  codigo.registrar("brasa", 4);
  codigo.registrar("deriva", 9);

  std::cout << codigo.resumen() << "\n";
}
```

Compilar y ejecutar:

```bash
g++ -std=c++17 -Wall -Wextra main.cpp codice.cpp -o codice && ./codice
```

## Salida

```text
2 familiares, nivel máximo 9
```

## Qué vive dónde

| Archivo | Contiene | Lo incluye |
| :--- | :--- | :--- |
| `codice.hpp` | la forma de la clase: miembros y firmas | cualquier cosa que use el códice |
| `codice.cpp` | los cuerpos de los métodos | nada |
| `main.cpp` | `#include "codice.hpp"` | — |

La cabecera se compila muchas veces, una por archivo que la incluye. Por eso guarda solo
declaraciones: una *definición* de función en una cabecera incluida dos veces rompe la regla de una
sola definición en el enlazado.

## La guarda de inclusión

`#ifndef CODICE_HPP / #define / #endif` convierte la segunda inclusión en el mismo archivo en un
no-op. `#pragma once` hace lo mismo en todos los compiladores que probablemente encuentres, en una
línea.

> [!CAUTION]
> Nunca hagas `#include "codice.cpp"`. Compila los cuerpos en cada archivo que lo incluye, produce
> símbolos duplicados y esconde el hecho de que tu comando de compilación olvidó `codice.cpp`.

> [!NOTE]
> La declaración en la cabecera debe coincidir exactamente con las firmas de la definición. Un
> `const` olvidado en un sitio produce un error de "ninguna declaración coincide" que apunta al
> `.cpp` y no a la cabecera: lee ambos antes de editar cualquiera.

---

**Siguiente:** [[45 - Dónde Viven las Cosas]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
