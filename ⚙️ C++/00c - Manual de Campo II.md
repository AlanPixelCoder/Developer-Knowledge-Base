# Manual de Campo II

**Versión original en inglés:** [00c - Field Manual II](./00c%20-%20Field%20Manual%20II.md)

**Curso:** C++
**Tema:** Referencia rápida
**Etiquetas:** `#cpp` `#cheatsheet` `#reference`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Reference-Field%20Manual-7C5CFF?style=for-the-badge" alt="Field Manual">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

<p align="center">
  <sub>5–8 · De Colecciones a Memoria</sub>
</p>

> [!TIP]
> Todo lo de los capítulos 5 a 8: contenedores, funciones, tipos que defines tú y dónde viven de
> verdad los valores. La página que quieres abierta mientras escribes el invocador.

## Contenedores

```cpp
#include <vector>

std::vector<int> montones{2, 5, 1};   // desde una lista
std::vector<int> vacio;               // crece después
std::vector<int> ceros(4);            // cuatro ceros
```

| Llamada | Efecto |
| :--- | :--- |
| `v.push_back(x)` | añade al final, tamaño + 1 |
| `v.pop_back()` | quita el último, tamaño − 1 |
| `v[i]` | elemento i, **sin comprobar** |
| `v.at(i)` | elemento i, lanza si está fuera de rango |
| `v.size()` | número de elementos |
| `v.empty()` | `size() == 0` |
| `v.front()` / `v.back()` | primer / último elemento |
| `v.clear()` | quita todos |

| Bucle | Te da |
| :--- | :--- |
| `for (auto& x : v)` | cada elemento, modificable |
| `for (const auto& x : v)` | cada elemento, solo lectura, sin copia |
| `for (std::size_t i = 0; i < v.size(); i++)` | también el índice |

## Funciones

```cpp
int dano(int poder, int armadura = 0);          // declaración con valor por defecto
int dano(int poder, int armadura) { return poder * 2 - armadura; }  // definición
```

| Forma del parámetro | ¿Copia? | ¿Quien llama ve el cambio? |
| :--- | :--- | :--- |
| `int x` | sí | no |
| `const std::string& s` | no | no |
| `std::vector<int>& v` | no | sí |
| `Entidad* e` | solo el puntero | sí, si se desreferencia |

## Tipos que defines

```cpp
class Entidad {
 public:
  Entidad(std::string nombre, int vida) : nombre_(std::move(nombre)), vida_(vida) {}

  void golpear(int cantidad) { vida_ -= cantidad; }
  bool viva() const { return vida_ > 0; }

 private:
  std::string nombre_;
  int vida_;
};
```

| Palabra | Significado |
| :--- | :--- |
| `public:` | usable por cualquier código con el objeto |
| `private:` | usable solo dentro de la clase |
| `const` tras un método | promete no modificar el objeto |
| miembro `static` | una copia compartida por la clase |
| `this` | puntero al objeto que se está usando |

## Archivos

| Archivo | Contiene | Lo incluye |
| :--- | :--- | :--- |
| `entidad.hpp` | forma de la clase, declaraciones | cualquier cosa que la use |
| `entidad.cpp` | cuerpos de los métodos | nada |
| `main.cpp` | `#include "entidad.hpp"` y `main` | — |

```bash
g++ -std=c++17 -Wall -Wextra main.cpp entidad.cpp -o console
```

## Memoria

| Dónde | Lo crea | Lo libera | Tiempo de vida |
| :--- | :--- | :--- | :--- |
| Pila | el compilador | el compilador | el bloque que lo contiene |
| Montón | `new`, contenedores, punteros inteligentes | `delete`, el dueño | hasta liberarse |
| Estática | el cargador | la salida del programa | toda la ejecución |

| Símbolo | Significa |
| :--- | :--- |
| `&x` | dirección de `x` |
| `*p` | objeto al que apunta `p` |
| `p->campo` | `(*p).campo` |
| `nullptr` | no apunta a nada |
| `new T{...}` | reserva en el montón |
| `delete p` | libera un objeto |
| `std::make_unique<T>(...)` | valor en montón con dueño, se libera solo |

> [!CAUTION]
> Un puntero a un local (`&local` devuelto por una función), un `delete` doble y un `nullptr`
> desreferenciado son las tres formas de perder este capítulo. Comprueba antes de `->`, y nunca
> devuelvas la dirección de un local.

## Los tres hábitos

1. Deja que el compilador lo atrape: `-Wall -Wextra -Wshadow -fsanitize=address,undefined`.
2. Deja que los contenedores y punteros inteligentes posean la memoria del montón; usa punteros
   crudos solo para observar.
3. Haz que el tipo sostenga sus propias reglas: validación en el constructor, recorte en el método.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
