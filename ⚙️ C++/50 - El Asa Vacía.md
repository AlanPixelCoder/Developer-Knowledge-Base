# 50. El Asa Vacía

**Versión original en inglés:** [50 - The Empty Handle](./50%20-%20The%20Empty%20Handle.md)

**Curso:** C++
**Capítulo:** 8 — Memoria
**Tema:** Comprobaciones de nulo, punteros colgados y propiedad
**Etiquetas:** `#cpp` `#pointers` `#nullptr`

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

El invocador guarda un puntero al jefe actual. Antes de que aparezca es nulo; después de que muera la
memoria se ha ido pero el puntero no. Dos fallos distintos, un solo asa.

```cpp
#include <iostream>
#include <string>

struct Entidad {
  std::string nombre;
  int vida;
};

Entidad* buscar_jefe(bool invocado) {
  static Entidad guardian{"guardian", 300};
  return invocado ? &guardian : nullptr;
}

int main() {
  Entidad* jefe = buscar_jefe(false);

  if (jefe != nullptr) {
    std::cout << jefe->nombre << "\n";
  } else {
    std::cout << "aún no hay jefe\n";
  }

  jefe = buscar_jefe(true);
  std::cout << "encontrado: " << jefe->nombre << "\n";

  Entidad* propio = new Entidad{"eco", 40};
  delete propio;
  propio = nullptr;                // deja de usar la dirección vieja

  if (propio == nullptr) {
    std::cout << "asa limpiada\n";
  }
}
```

## Salida

```text
aún no hay jefe
encontrado: guardian
asa limpiada
```

## Dos formas en que un asa miente

| Fallo | Qué significa | Cómo evitarlo |
| :--- | :--- | :--- |
| Desreferencia nula | el asa no apunta a nada | comprobar antes de `->` |
| Puntero colgado | el objeto se fue, la dirección no | `delete` y luego `nullptr` |

Un puntero colgado es peor que uno nulo: la comprobación `p != nullptr` pasa, y la lectura llega a
memoria liberada.

## La propiedad decide las reglas

Quien llama a `new` debe llamar a `delete`. Si una función devuelve un puntero, quien llama tiene que
saber si posee el objeto o solo lo toma prestado, y esa es justo la pregunta que un puntero crudo no
puede responder.

> [!CAUTION]
> Devolver `&local` desde una función devuelve un puntero colgado en el instante del retorno. La
> dirección parece válida; el objeto ya no está. Es el error de punteros más común en código de
> principiante.

> [!TIP]
> `std::unique_ptr<Entidad>` dice "este asa posee el objeto" en el tipo, lo borra al salir del ámbito
> y no se puede copiar por accidente. Usa punteros crudos solo para *observar*, nunca para poseer.

---

**Siguiente:** [[51 - La Última Brasa]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
