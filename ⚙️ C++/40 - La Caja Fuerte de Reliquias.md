# 40. La Caja Fuerte de Reliquias

**Versión original en inglés:** [40 - The Relic Safe](./40%20-%20The%20Relic%20Safe.md)

**Curso:** C++
**Capítulo:** 7 — Entidades
**Tema:** Constructores: garantizar un objeto válido desde la primera línea
**Etiquetas:** `#cpp` `#class` `#constructors`

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

Una caja fuerte que puede existir sin combinación es un error esperando la primera noche. El
constructor corre antes de que nadie pueda tocar el objeto, así que es el único sitio honesto para
establecer las reglas.

```cpp
#include <iostream>
#include <string>

class CajaReliquias {
 public:
  CajaReliquias(std::string duenio, int discos)
      : duenio_(duenio), discos_(discos < 3 ? 3 : discos), cerrada_(true) {}

  bool probar_codigo(int codigo) {
    if (!cerrada_) {
      return true;
    }
    if (codigo == esperado()) {
      cerrada_ = false;
      return true;
    }
    return false;
  }

  int esperado() const { return discos_ * 137; }

  std::string describir() const {
    return duenio_ + " / " + std::to_string(discos_) + " discos / " +
           (cerrada_ ? "cerrada" : "abierta");
  }

 private:
  std::string duenio_;
  int discos_;
  bool cerrada_;
};

int main() {
  CajaReliquias caja("archivista", 4);

  std::cout << caja.describir() << "\n";
  std::cout << "malo:   " << caja.probar_codigo(1) << "\n";
  std::cout << "bueno:  " << caja.probar_codigo(caja.esperado()) << "\n";
  std::cout << caja.describir() << "\n";
}
```

## Salida

```text
archivista / 4 discos / cerrada
malo:   0
bueno:  1
archivista / 4 discos / abierta
```

## Qué garantiza el constructor

| Campo | Regla | La impone |
| :--- | :--- | :--- |
| `duenio_` | siempre asignado | parámetro obligatorio |
| `discos_` | nunca por debajo de 3 | el ternario del inicializador |
| `cerrada_` | verdadera al nacer | inicializador explícito |

Toda `CajaReliquias` que existe cumple las reglas, porque no hay otra forma de crearla.

## La lista de inicialización de miembros

```cpp
CajaReliquias(std::string duenio, int discos)
    : duenio_(duenio), discos_(discos < 3 ? 3 : discos), cerrada_(true) {}
```

Todo lo que va tras los dos puntos corre **antes** del cuerpo. Los miembros se inicializan en orden de
declaración, no en el orden escrito aquí: una discrepancia entre los dos órdenes es un error real
cuando un inicializador lee otro campo.

> [!CAUTION]
> Si la clase no tiene constructor declarado por el usuario, el compilador genera uno por defecto y
> los campos de tipos básicos quedan sin inicializar. `CajaReliquias caja;` guardaría `discos_` con
> basura. El constructor de arriba elimina esa posibilidad por completo.

> [!TIP]
> Prefiere las listas de inicialización a las asignaciones en el cuerpo: los miembros `const` y las
> referencias solo se pueden inicializar, nunca asignar, y el inicializador evita el ciclo de
> construir por defecto y sobrescribir.

---

**Siguiente:** [[41 - La Caja Fuerte, Conectada]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
