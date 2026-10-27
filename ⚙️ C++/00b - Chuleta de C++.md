# Chuleta de C++

**Versión original en inglés:** [00b - C++ Cheatsheet.md](./00b%20-%20C%2B%2B%20Cheatsheet.md)

**Curso:** C++
**Tema:** Referencia rápida
**Etiquetas:** `#cpp` `#cheatsheet` `#reference`

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

> [!TIP]
> Tenla abierta mientras trabajas en la terminal. Consulta más rápida, menos pestañas y más
> mazmorras superadas.

## Entrada / salida

```cpp
#include <iostream>

std::cout << "¡Hola!";       // salida
std::cin >> variable;        // entrada
std::cout << "Valor: " << x; // encadenado
```

## Tipos de datos

| Tipo | Uso | Ejemplo |
| :--- | :--- | :--- |
| `int` | Números enteros | `int vida = 100;` |
| `double` | Decimales | `double oro = 24.99;` |
| `char` | Un carácter | `char rango = 'S';` |
| `std::string` | Texto | `std::string nombre = "Caballero";` |
| `bool` | Verdadero / Falso | `bool vivo = true;` |

## Operadores

| Operador | Propósito |
| :--- | :--- |
| `+ - * / %` | Aritmética (`%` = resto) |
| `== != > < >= <=` | Relacionales |
| `&&` `||` `!` | Lógicos (y, o, no) |
| `=` | Asignación |

## Flujo de control

```cpp
if (condicion) { /* ... */ }
else if (condicion) { /* ... */ }
else { /* ... */ }
```

## Bucles

```cpp
while (condicion) { /* ... */ }

for (int i = 0; i < n; i++) { /* ... */ }
```

## Vectores

```cpp
#include <vector>

std::vector<std::string> inventario = {"Poción", "Mapa"};
inventario.push_back("Espada");
inventario.pop_back();
inventario.size();
inventario[0]; // acceder
```

## Funciones

```cpp
void saludar() { std::cout << "Hola\n"; }

int sumar(int x, int y) { return x + y; }

saludar();
int total = sumar(2, 3);
```

## Clases

```cpp
class Hero {
  public:
    std::string name;
    int hp;

    Hero(std::string n, int h) {
      name = n;
      hp = h;
    }

    void heal() { hp += 10; }
};

Hero knight("Aldric", 100);
knight.heal();
```

## Punteros y referencias

```cpp
int x = 10;
int* p = &x;      // puntero a la dirección
std::cout << *p;  // desreferencia

int& ref = x;     // referencia (alias)
ref = 20;         // cambia x

int* nullp = nullptr;
```

## Compilar y ejecutar

```bash
g++ main.cpp -o main
./main
```

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
