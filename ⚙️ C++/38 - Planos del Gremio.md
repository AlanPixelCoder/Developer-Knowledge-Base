# 38. Planos del Gremio

**Versión original en inglés:** [38 - Guild Blueprints](./38%20-%20Guild%20Blueprints.md)

**Curso:** C++
**Capítulo:** 7 — Entidades
**Tema:** Definir un struct: un tipo que tú inventas
**Etiquetas:** `#cpp` `#struct` `#types`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-7-7C5CFF?style=for-the-badge" alt="Chapter 7">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Un registro de gremio tiene nombre, rango, bolsa y reputación. Cuatro arrays paralelos funcionarían
hasta la primera inserción, cuando tres de ellos deben desplazarse a la vez. Un `struct` mantiene los
cuatro campos soldados.

```cpp
#include <iostream>
#include <string>

struct MiembroGremio {
  std::string nombre;
  std::string rango;
  int bolsa;
  double reputacion;
};

int main() {
  MiembroGremio exploradora{"Wren", "exploradora", 40, 3.5};
  MiembroGremio herrera{"Odo", "herrera", 120, 7.25};

  std::cout << exploradora.nombre << " (" << exploradora.rango << ") bolsa "
            << exploradora.bolsa << "\n";
  std::cout << herrera.nombre << " (" << herrera.rango << ") reputación "
            << herrera.reputacion << "\n";

  herrera.bolsa += 30;
  std::cout << "tras un encargo: " << herrera.bolsa << "\n";
  std::cout << "sizeof: " << sizeof(MiembroGremio) << " bytes\n";
}
```

## Salida

```text
Wren (exploradora) bolsa 40
Odo (herrera) reputación 7.25
tras un encargo: 150
sizeof: 64 bytes
```

## Un struct es un tipo

| Paso | Sintaxis | Efecto |
| :--- | :--- | :--- |
| Definir | `struct MiembroGremio { ... };` | un tipo nuevo, aún sin variable |
| Crear | `MiembroGremio exploradora{...};` | un objeto, campos rellenados en orden |
| Acceder | `exploradora.bolsa` | leer o escribir un campo |
| Asignar entero | `herrera = exploradora;` | copia todos los campos |

`sizeof` puede ser mayor que la suma de los campos: el compilador rellena por alineación. Aquí 64
bytes son un `std::string` (32) más otro (32) más `int` y `double` metidos en el relleno final.

## Definición frente a instanciación

La definición no reserva nada. Le dice al compilador el diseño, para que las líneas posteriores sepan
cuántos bytes necesita `MiembroGremio` y dónde va cada campo. Una definición, cualquier número de
objetos.

> [!NOTE]
> No olvides el punto y coma tras la llave de cierre. `struct X { ... }` sin `;` es uno de los pocos
> errores cuyo mensaje apunta a la línea *siguiente* en lugar de a la real.

> [!TIP]
> Nombra el struct por la cosa, en singular: `MiembroGremio`, no `MiembrosGremio`. El nombre de la
> variable lleva el plural (`miembros`), y leer `miembros[0].nombre` te da los dos datos a la vez.

---

**Siguiente:** [[39 - Puertas Selladas y Abiertas]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
