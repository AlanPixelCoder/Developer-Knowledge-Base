# 11. Cámara de Eco

**Versión original en inglés:** [11 - Echo Chamber](./11%20-%20Echo%20Chamber.md)

**Curso:** C++
**Capítulo:** 2 — Valores en Bruto
**Tema:** Encadenar inserciones en una sola línea de salida
**Etiquetas:** `#cpp` `#output` `#formatting`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-2-7C5CFF?style=for-the-badge" alt="Chapter 2">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

El registro del motor necesita una línea por evento: una etiqueta, un identificador, un mensaje. Una
sentencia por línea está bien, pero encadenar lo hace en una sola, y así están escritas todas las
líneas de registro que vas a leer.

```cpp
#include <iostream>
#include <string>

int main() {
  std::string etiqueta = "APARICION";
  int id_entidad = 42;
  double x = 118.5;

  std::cout << "[" << etiqueta << "] id=" << id_entidad << " x=" << x << "\n";
  std::cout << "[" << etiqueta << "]" << " id=" << id_entidad << "\n";
}
```

## Salida

```text
[APARICION] id=42 x=118.5
[APARICION] id=42
```

Mira la primera línea con atención: los espacios que ves son los que están dentro de los literales.
C++ no inserta nada por su cuenta.

## Por qué `<<` puede repetirse

`std::cout << valor` devuelve el propio flujo. Eso es lo que permite escribir `std::cout << a << b`:
la primera inserción le entrega el flujo a la segunda. El operador es asociativo por la izquierda,
así que se lee de izquierda a derecha.

| Escrito | Se lee como | Imprime |
| :--- | :--- | :--- |
| `"a" << 1 << 2` | `(("a" << 1) << 2)` | `a12` |
| `"a" << " " << 1` | `(("a" << " ") << 1)` | `a 1` |

> [!TIP]
> Pon los separadores dentro del literal — `" id="` — en lugar de como un `<< " "` aparte. Menos
> inserciones, menos ocasiones de olvidar una, y el espaciado se ve donde lo escribiste.

> [!NOTE]
> Ese mismo encadenado es lo que hace que `std::cout << a + b` sea distinto de
> `std::cout << a << b`. El primero inserta un número; el segundo, dos valores pegados sin separador.

---

**Siguiente:** [[12 - Hablar con la Máquina]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
