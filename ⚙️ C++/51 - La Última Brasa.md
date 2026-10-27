# 51. La Última Brasa

**Versión original en inglés:** [51 - The Last Ember](./51%20-%20The%20Last%20Ember.md)

**Curso:** C++
**Capítulo:** 8 — Memoria
**Tema:** Repaso del capítulo 8 y del curso: memoria elegida a propósito
**Etiquetas:** `#cpp` `#recap` `#memory`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Chapter-8-7C5CFF?style=for-the-badge" alt="Chapter 8">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

El último servicio de la consola lee el registro, guarda las entidades de la corrida e informa qué
sobrevivió. Cada línea es una decisión sobre dónde vive un valor, y cada decisión es una que ya sabes
nombrar.

```cpp
#include <iostream>
#include <memory>
#include <string>
#include <vector>

struct Entidad {
  std::string nombre;
  int vida;
  bool viva() const { return vida > 0; }
};

int main() {
  std::vector<Entidad> plantilla;                    // búfer en montón, objeto en pila
  plantilla.push_back({"guardian", 0});
  plantilla.push_back({"brasa", 45});
  plantilla.push_back({"musgo", 12});

  int sobrevivientes = 0;
  for (const Entidad& e : plantilla) {               // referencia: sin copia
    if (e.viva()) {
      sobrevivientes++;
    }
  }

  auto nota = std::make_unique<std::string>("corrida cerrada");  // valor en montón, con dueño

  Entidad* visto = &plantilla.front();               // puntero observador, sin propiedad
  std::string ultimo = plantilla.back().nombre;      // una copia, a propósito

  std::cout << "sobrevivientes: " << sobrevivientes << "\n";
  std::cout << "primera:        " << visto->nombre << "\n";
  std::cout << "copia última:   " << ultimo << "\n";
  std::cout << "nota:           " << *nota << "\n";
  std::cout << "asas:           " << (visto != nullptr) << " " << (nota != nullptr) << "\n";
}
```

## Salida

```text
sobrevivientes: 2
primera:        guardian
copia última:   musgo
nota:           corrida cerrada
asas:           1 1
```

## Cada línea, justificada

| Línea | Almacenamiento | Por qué |
| :--- | :--- | :--- |
| `std::vector<Entidad> plantilla` | objeto en pila, elementos en montón | cuenta desconocida de antemano |
| `const Entidad& e` | ninguno | acceso de solo lectura, sin copia |
| `std::make_unique<std::string>` | montón, con dueño | vida más larga que un bloque, dueño único |
| `Entidad* visto` | un puntero | préstamo, nunca `delete` |
| `std::string ultimo` | pila, con búfer en montón | la copia es deseada |

## Las reglas que sobrevivieron al curso

1. Prefiere el almacenamiento automático; se limpia solo.
2. Cuando necesites el montón, deja que lo posea un contenedor o un puntero inteligente.
3. Usa punteros crudos para observar y referencias para exigir.
4. Marca como `const` los métodos y parámetros de solo lectura para que el compilador imponga tu
   intención.

> [!IMPORTANT]
> `plantilla.front()` devuelve una referencia a un elemento. Tomar `&plantilla.front()` es seguro
> mientras el vector viva y no se reubique: un `push_back` posterior puede invalidar todos los
> punteros al búfer.

> [!TIP]
> Compila con `-Wall -Wextra -fsanitize=address,undefined` mientras aprendes. Los sanitizadores
> convierten una lectura fuera de rango o un uso tras liberación en un mensaje con número de línea,
> que es el bucle de retroalimentación más rápido en C++.

## Hacia dónde seguir

Ya tienes la forma del lenguaje: valores y tipos, flujo de control, colecciones, funciones, tipos que
defines tú y memoria. Los siguientes pasos que valen la pena son `std::string` en profundidad, los
algoritmos de `<algorithm>`, el manejo de errores con excepciones, y leer cabeceras ajenas hasta que
las declaraciones dejen de parecer ruido.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
