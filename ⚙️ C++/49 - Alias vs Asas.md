# 49. Alias vs Asas

**Versión original en inglés:** [49 - Aliases vs Handles](./49%20-%20Aliases%20vs%20Handles.md)

**Curso:** C++
**Capítulo:** 8 — Memoria
**Tema:** Cuándo una referencia es mejor que un puntero
**Etiquetas:** `#cpp` `#references` `#memory`

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

Dos nombres para una entidad. La diferencia entre una referencia y un puntero no es de sintaxis, es
una promesa: una referencia siempre nombra algo que existe y no se puede hacer que nombre otra cosa.

```cpp
#include <iostream>
#include <string>

struct Entidad {
  std::string nombre;
  int vida;
};

int main() {
  Entidad guardian{"guardian", 120};

  Entidad& alias = guardian;      // otro nombre, el mismo objeto
  Entidad* asa = &guardian;       // un valor que guarda la dirección

  alias.vida -= 20;

  std::cout << "guardian:    " << guardian.vida << "\n";
  std::cout << "vía alias:   " << alias.vida << "\n";
  std::cout << "vía asa:     " << asa->vida << "\n";
  std::cout << "¿iguales?    " << (&alias == asa) << "\n";

  Entidad sombra{"sombra", 60};
  asa = &sombra;                  // un puntero se puede reasignar
  std::cout << "asa ahora:   " << asa->nombre << "\n";
}
```

## Salida

```text
guardian:    100
vía alias:   100
vía asa:     100
¿iguales?    1
asa ahora:   sombra
```

## Qué promete cada uno

| Propiedad | `Entidad&` | `Entidad*` |
| :--- | :--- | :--- |
| Puede ser nula | no | sí |
| Se puede reasignar | no | sí |
| Necesita `*` o `->` | no | sí |
| La dirección existe | garantizado | solo tras comprobar |

Una referencia se enlaza una vez, al crearse, y vive con ese enlace. `Entidad& alias = guardian;` y
luego `alias = sombra;` no apunta el alias a `sombra`: **copia los campos de sombra en guardian**.

## La trampa de la reasignación

Esa última línea es la razón por la que las referencias no son solo "punteros más agradables". Si
necesitas recorrer una lista, cambiar a qué objeto miras, o representar "ninguno", el puntero es la
elección honesta. Una referencia que parece reasignarse es casi siempre un error que compila limpio.

> [!WARNING]
> Aquí `&alias == asa` es `true`, y también es la forma de comprobar que un alias es de verdad el
> mismo objeto y no una copia. No construyas lógica sobre comparaciones de direcciones; úsalas
> mientras aprendes.

> [!TIP]
> Prefiere `const Entidad&` para parámetros que solo lees: sin copia, sin comprobación de nulo, y el
> compilador impone "solo lectura" por ti. Recurre a un puntero cuando la respuesta a "¿qué objeto?"
> puede cambiar.

---

**Siguiente:** [[50 - El Asa Vacía]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
