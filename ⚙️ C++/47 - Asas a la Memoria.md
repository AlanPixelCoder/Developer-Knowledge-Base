# 47. Asas a la Memoria

**Versión original en inglés:** [47 - Handles to Memory](./47%20-%20Handles%20to%20Memory.md)

**Curso:** C++
**Capítulo:** 8 — Memoria
**Tema:** new y delete, y por qué los contenedores suelen reemplazarlos
**Etiquetas:** `#cpp` `#pointers` `#new-delete`

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

Un invocador crea entidades mientras corre el nivel. El número no se conoce cuando se escribe el
código, así que el objeto no puede vivir en la pila de `main`. `new` pide al montón exactamente el
espacio necesario y devuelve un asa.

```cpp
#include <iostream>
#include <string>

struct Entidad {
  std::string nombre;
  int vida;
};

int main() {
  Entidad* jefe = new Entidad{"guardian", 250};

  std::cout << jefe->nombre << " vida " << jefe->vida << "\n";

  jefe->vida -= 40;
  std::cout << "tras un golpe: " << (*jefe).vida << "\n";

  delete jefe;
  jefe = nullptr;

  std::cout << "asa ahora: " << (jefe == nullptr) << "\n";
}
```

## Salida

```text
guardian vida 250
tras un golpe: 210
asa ahora: 1
```

## `new`, `->`, `delete`

| Forma | Significa |
| :--- | :--- |
| `new Entidad{...}` | reserva un objeto en el montón y devuelve su dirección |
| `p->campo` | abreviatura de `(*p).campo` |
| `delete p` | destruye el objeto y devuelve la memoria |
| `delete p; p = nullptr;` | además elimina el asa colgada |

## Las tres reglas que trae `new`

1. Cada `new` necesita exactamente un `delete`.
2. `delete[]` para arrays, `delete` para objetos sueltos: mezclarlos es comportamiento indefinido.
3. Tras `delete`, el puntero conserva la dirección vieja. Suéltalo o ponlo a `nullptr`.

> [!CAUTION]
> Borrar dos veces corrompe el asignador, y la caída suele ocurrir después, en código no relacionado.
> La solución no es una segunda comprobación, es no poseer memoria cruda a mano.

> [!TIP]
> `std::vector<Entidad> entidades;` reserva en el montón, crece y se libera sola al salir del ámbito.
> Recurre a `new` solo si implementas un contenedor o hablas con una API que lo exige.

---

**Siguiente:** [[48 - Alcanzar a Través del Asa]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
