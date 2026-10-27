# 24. Equipo de Supervivencia

**Versión original en inglés:** [24 - Survival Gear.md](./24%20-%20Survival%20Gear.md)

**Curso:** C++
**Tema:** Vectores
**Etiquetas:** `#cpp` `#vectors` `#data-structures`

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

Los **vectores** almacenan varios elementos en una sola variable. Es una forma limpia de guardar
muchos datos en lugar de crear un montón de variables separadas, algo tedioso y propenso a errores.

`std::vector` vive en la cabecera `<vector>`, así que añade `#include <vector>` al inicio del
programa.

## Crear un vector

- La palabra clave `std::vector` y el tipo de elemento entre paréntesis angulares `< >`.
- Luego el nombre del vector.
- Los elementos van entre llaves, separados por comas.

```cpp
std::vector<tipo> nombre = {1, 2, 3, 4};
```

## Datos sobre los vectores

| Propiedad | Detalle |
| :--- | :--- |
| Duplicados | Permitidos: el mismo valor puede repetirse |
| Tipos de elemento | Todos comparten **un** tipo de dato |
| Tamaño | Puede crecer y encogerse en tiempo de ejecución |

> [!NOTE]
> **Por qué los vectores reemplazaron a los arrays**
> Antes se usaban los "arrays" del lenguaje C. Los arrays tienen tamaño **fijo**: se decide una vez y
> para siempre. Los vectores crecen y se encogen a demanda, que es como se comporta un inventario de
> verdad. La comparación completa está en [[Arrays en C++]].

## Ejemplo

```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
  std::vector<std::string> equipo = {
    "Abrigo de invierno",
    "Hacha para leña",
    "Pedernal y acero",
    "Purificador de agua",
    "Generador solar",
    "Portátil",
    "Licuadora",
    "Arroz jazmín",
    "Pociones de vida",
    "Espada ancha"
  };
}
```

> [!TIP]
> Los paréntesis angulares pueden anidarse. Un vector de vectores —un inventario con ranuras— se
> escribe `std::vector<std::vector<std::string>>`. En C++11 y posteriores el `>>` final está bien;
> los compiladores antiguos exigían un espacio entre ellos.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
