# Chuleta de C++ II

**Versión original en inglés:** [00c - C++ Cheatsheet II.md](./00c%20-%20C%2B%2B%20Cheatsheet%20II.md)

**Curso:** C++
**Tema:** Referencia rápida avanzada
**Etiquetas:** `#cpp` `#cheatsheet` `#reference` `#memory`

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

## Ámbito

| Ámbito | Dónde | Accesible |
| :--- | :--- | :--- |
| **Local** | Dentro de una función o bloque `{}` | Solo ahí dentro |
| **Global** | Fuera de toda función | En todo el archivo |

## Modificadores de acceso

| Modificador | Acceso |
| :--- | :--- |
| `public` | Cualquiera |
| `private` | Solo la propia clase (por defecto en `class`) |
| `protected` | La clase y sus clases derivadas |

## Constructores

```cpp
class Car {
  public:
    std::string brand;
    Car(std::string b) { brand = b; } // constructor
};

Car c("Ford"); // inicializado en una línea
```

## Paso por valor vs paso por referencia

```cpp
// Paso por valor (copia)
void damage(int hp) { hp -= 10; }     // el original no cambia

// Paso por referencia (alias)
void damageRef(int& hp) { hp -= 10; } // el original cambia
```

## Punteros vs referencias

| Característica | Puntero | Referencia |
| :--- | :--- | :--- |
| Sintaxis | `int* p = &x;` | `int& ref = x;` |
| Puede ser nulo | Sí (`nullptr`) | No |
| Reasignable | Sí | No |
| Desreferencia | Sí (`*p`) | Se usa el nombre directo |
| Inicialización | Opcional | Obligatoria |

## Seguridad con `nullptr`

```cpp
void greet(const std::string* name) {
  if (name != nullptr) {
    std::cout << *name;
  } else {
    std::cout << "Invitado";
  }
}
```

## Cabeceras habituales

| Cabecera | Propósito |
| :--- | :--- |
| `<iostream>` | Entrada/salida (`std::cout`, `std::cin`) |
| `<string>` | `std::string` |
| `<vector>` | `std::vector` |
| `<cstdlib>` | `std::rand()` |
| `<ctime>` | `time(NULL)`, `srand()` |

## Hábitos que vale la pena mantener

- Inicializa siempre los punteros: con una dirección real o con `nullptr`.
- Prefiere referencias en parámetros cuando la función deba modificar el original.
- Marca punteros y referencias como `const` cuando solo lees a través de ellos.
- Compila con `g++ -Wall -Wextra -std=c++17 main.cpp -o main`.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
