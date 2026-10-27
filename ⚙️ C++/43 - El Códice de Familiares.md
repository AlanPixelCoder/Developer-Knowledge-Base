# 43. El Códice de Familiares

**Versión original en inglés:** [43 - The Familiar Codex](./43%20-%20The%20Familiar%20Codex.md)

**Curso:** C++
**Capítulo:** 7 — Entidades
**Tema:** Una clase que posee una colección, con métodos const y un contador static
**Etiquetas:** `#cpp` `#class` `#static`

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

El códice guarda una lista de familiares y responde preguntas sobre ellos. Es dueño de la lista, así
que nadie puede añadir un familiar sin que el códice lo sepa, y mantiene la cuenta de todos los
familiares que ha registrado alguna vez.

```cpp
#include <iostream>
#include <string>
#include <vector>

class CodiceFamiliares {
 public:
  void registrar(const std::string& nombre, int nivel) {
    nombres_.push_back(nombre);
    niveles_.push_back(nivel);
    ++total_registrados;
  }

  std::size_t cuenta() const { return nombres_.size(); }

  int nivel_maximo() const {
    int mejor = 0;
    for (int nivel : niveles_) {
      if (nivel > mejor) {
        mejor = nivel;
      }
    }
    return mejor;
  }

  std::string resumen() const {
    return std::to_string(cuenta()) + " familiares, nivel máximo " +
           std::to_string(nivel_maximo()) + ", " +
           std::to_string(total_registrados) + " en total";
  }

  static int total_registrados;

 private:
  std::vector<std::string> nombres_;
  std::vector<int> niveles_;
};

int CodiceFamiliares::total_registrados = 0;

int main() {
  CodiceFamiliares codigo;

  codigo.registrar("brasa", 4);
  codigo.registrar("deriva", 9);
  codigo.registrar("musgo", 2);

  std::cout << codigo.resumen() << "\n";

  CodiceFamiliares segundo;
  segundo.registrar("pluma", 1);
  std::cout << segundo.resumen() << "\n";
}
```

## Salida

```text
3 familiares, nivel máximo 9, 3 en total
1 familiares, nivel máximo 1, 4 en total
```

## Dos clases de estado

| Estado | Pertenece a | Se declara | Compartido |
| :--- | :--- | :--- | :--- |
| `nombres_`, `niveles_` | cada objeto | miembros normales | no |
| `total_registrados` | la clase | `static` + definición fuera | sí |

Un miembro `static` necesita una definición fuera de la clase
(`int CodiceFamiliares::total_registrados = 0;`) o el enlazador se queja de un símbolo ausente. Desde
C++17, `static inline int total_registrados = 0;` dentro de la clase hace lo mismo en una línea.

## Métodos `const` que devuelven un valor guardado

`cuenta()` y `nivel_maximo()` son `const`, así que se pueden llamar sobre un
`const CodiceFamiliares&`. `nivel_maximo()` recalcula cada vez; cachearlo exigiría un miembro
`mutable` o no `const` y un segundo lugar que mantener correcto.

> [!NOTE]
> Los vectores paralelos son simples y funcionan. Un `std::vector<Familiar>` — un struct por elemento
> — suele ser mejor cuando los campos pasan de tres, porque un `push_back` olvidado en uno de los
> vectores desincroniza el códice en silencio.

> [!TIP]
> Mantén el contenedor privado y expón lo que los llamadores necesitan de verdad (`cuenta`,
> `nivel_maximo`) en lugar de un getter del vector. Un getter entrega la capacidad de romper el
> invariante que acabas de construir.

---

**Siguiente:** [[44 - El Códice, Animado]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
