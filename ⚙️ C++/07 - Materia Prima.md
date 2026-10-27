# 07. Materia Prima

**Versión original en inglés:** [07 - Raw Materials](./07%20-%20Raw%20Materials.md)

**Curso:** C++
**Capítulo:** 2 — Valores en Bruto
**Tema:** Los cinco tipos básicos en los que se apoya el motor, y cuánto cuestan
**Etiquetas:** `#cpp` `#types` `#memory`

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

La pantalla de configuración del motor muestra cinco campos: el tope de fotogramas, un multiplicador
de gravedad, la inicial de calidad, el nombre del build y una bandera para la capa de depuración.
Cinco valores, y cada uno necesita un tipo lo bastante ancho para contenerlo — ni más ancho, porque
esta es la capa donde se cuentan los bytes.

| Tipo | Guarda | Tamaño típico | Ejemplo en el motor |
| :--- | :--- | :--- | :--- |
| `int` | números enteros | 4 bytes | tope de fotogramas |
| `double` | decimales | 8 bytes | multiplicador de gravedad |
| `char` | un carácter | 1 byte | inicial de calidad |
| `std::string` | texto | variable (24+ bytes) | nombre del build |
| `bool` | verdadero / falso | 1 byte | capa de depuración |

## Pregúntale al compilador en vez de confiar en una tabla

```cpp
#include <iostream>
#include <string>

int main() {
  int tope_fps = 60;
  double escala_gravedad = 1.35;
  char calidad = 'B';
  std::string nombre_build = "ember-0.2.1";
  bool ver_depuracion = true;

  std::cout << "int     " << sizeof(tope_fps) << " bytes\n";
  std::cout << "double  " << sizeof(escala_gravedad) << " bytes\n";
  std::cout << "char    " << sizeof(calidad) << " bytes\n";
  std::cout << "string  " << sizeof(nombre_build) << " bytes\n";
  std::cout << "bool    " << sizeof(ver_depuracion) << " bytes\n";
}
```

## Salida

```text
int     4 bytes
double  8 bytes
char    1 bytes
string  24 bytes
bool    1 bytes
```

`sizeof` se evalúa en tiempo de compilación: no cuesta nada y nunca adivina.

> [!NOTE]
> El estándar fija tamaños mínimos, no exactos. `int` tiene al menos 16 bits; en cualquier escritorio
> son 32. `sizeof` es la forma de escribir código al que eso le da igual.

> [!WARNING]
> `double` guarda los decimales de forma **aproximada**. `0.1 + 0.2` no es exactamente `0.3`. Para
> dinero usa enteros de céntimos; para física, acepta la deriva y compara con una tolerancia.

---

**Siguiente:** [[08 - Nombrar las Piezas]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
