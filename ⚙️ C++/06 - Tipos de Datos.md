# 06. Tipos de Datos

**Versión original en inglés:** [06 - Data Types.md](./06%20-%20Data%20Types.md)

**Curso:** C++
**Tema:** Variables y tipos de datos
**Etiquetas:** `#cpp` `#variables` `#data-types`

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

En programación las variables sirven para almacenar valores. Cada variable tiene un **tipo de
dato**, un **nombre** y guarda un **valor**: piensa en una caja en la memoria con una etiqueta.

## Los cinco tipos básicos

| Tipo | Guarda | Ejemplo |
| :--- | :--- | :--- |
| **`int`** | Números enteros, positivos o negativos, sin decimales | `int anio = 2024;` |
| **`double`** | Números con decimales: fracciones, medidas precisas | `double pi = 3.14159;` |
| **`char`** | Un único carácter, entre **comillas simples** | `char numeral = '#';` |
| **`std::string`** | Texto, una secuencia de caracteres, entre **comillas dobles** | `std::string mensaje = "buenas noches";` |
| **`bool`** | Solo `true` o `false`, siempre en minúsculas | `bool llego_tarde = false;` |

`std::string` usa el prefijo `std::` porque viene de la biblioteca estándar de C++ — y por eso
necesita `#include <string>`.

> [!NOTE]
> **Comillas simples vs dobles no es cosmético**
> `'a'` es un `char` (un byte). `"a"` es un `std::string` (una secuencia, con terminador nulo
> detrás). Confundirlos produce errores de compilación que parecen crípticos hasta que ves la
> comilla.

> [!TIP]
> **El tamaño de la caja**
> Un `bool` ocupa 1 byte, un `char` 1 byte, un `int` normalmente 4 y un `double` 8. Por eso "usa
> `double` para todo" duplica la factura de memoria en bucles ajustados.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
