# 38. Coches Clásicos

**Versión original en inglés:** [38 - Classic Cars.md](./38%20-%20Classic%20Cars.md)

**Curso:** C++
**Tema:** Constructores y valores por defecto
**Etiquetas:** `#cpp` `#classes` `#oop` `#constructors`

<p align="left">
  <img src="https://img.shields.io/badge/Lenguaje-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Estado-Completo-00C2A8?style=for-the-badge" alt="Completo">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Bóveda-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Cuando creamos un objeto, asignar un valor a cada atributo en una línea separada es tedioso.

Los **constructores** existen en C++ para inicializar objetos automáticamente al crearlos.

## Crear un constructor

- Tiene **exactamente el mismo nombre** que la clase.
- **No tiene tipo de retorno** — ni siquiera `void`.
- Se ejecuta automáticamente en el momento de la creación.
- Los argumentos se pasan con la misma sintaxis `Tipo nombre` que cualquier función.

```cpp
class Student {
  public:
    std::string name;
    int year;

    // Constructor
    Student(std::string n, int y) {
      name = n;
      year = y;
    }
};

Student ferris("Ferris Bueller", 12); // una línea en vez de tres
```

## Valores por defecto

Si un atributo no se proporciona, define un valor por defecto donde lo declaras en la clase. Ese
valor actúa como marcador de posición.

```cpp
class Car {
  public:
    int year = 2000;   // por defecto
    bool classic = false;
};
```

## Ejemplo

```cpp
#include <iostream>
#include <string>

class Car {
  public:
    std::string brand;
    std::string model;
    int year;
    bool classic;

    Car(std::string b, std::string m, int y, bool c) {
      brand = b;
      model = m;
      year = y;
      classic = c;
    }
};

int main() {
  Car mustang("Ford", "Mustang", 1965, true);
  Car jaguar("Jaguar", "E-Type", 1961, true);

  std::cout << "Coche 1: " << mustang.year << " " << mustang.brand << " " << mustang.model << "\n";
  std::cout << "Coche 2: " << jaguar.year << " " << jaguar.brand << " " << jaguar.model << "\n";
}
```

## Salida

```text
Coche 1: 1965 Ford Mustang
Coche 2: 1961 Jaguar E-Type
```

> [!TIP]
> **Constructor por defecto**
> Una clase **sin** ningún constructor recibe uno implícito gratis, así que `Car c;` compila. En el
> momento en que escribes *cualquier* constructor, ese gratis desaparece: una fuente clásica de
> errores repentinos de "no matching constructor".

> [!NOTE]
> En C++ moderno se prefiere la lista de inicialización (`Car(std::string b) : brand(b) {}`). La
> asignación en el cuerpo que ves aquí es la versión didáctica y hace el mismo trabajo.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
