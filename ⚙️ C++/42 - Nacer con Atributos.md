# 42. Nacer con Atributos

**Versión original en inglés:** [42 - Spawn With Stats](./42%20-%20Spawn%20With%20Stats.md)

**Curso:** C++
**Capítulo:** 7 — Entidades
**Tema:** Funciones miembro, el this implícito y estado mutable
**Etiquetas:** `#cpp` `#class` `#methods`

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

Una criatura invocada tiene atributos, y los atributos cambian. El daño llega de fuera, así que el
objeto necesita métodos que lean y escriban sus propios campos, y una forma de nombrarlos cuando un
parámetro se llama igual.

```cpp
#include <iostream>
#include <string>

class Criatura {
 public:
  Criatura(std::string nombre, int vida) : nombre_(nombre), vida_(vida), vida_max_(vida) {}

  void recibir_dano(int cantidad) {
    vida_ -= cantidad;
    if (vida_ < 0) {
      vida_ = 0;
    }
  }

  void curar(int cantidad) {
    vida_ += cantidad;
    if (vida_ > vida_max_) {
      vida_ = vida_max_;
    }
  }

  bool esta_viva() const { return vida_ > 0; }

  std::string estado() const {
    return nombre_ + ": " + std::to_string(vida_) + "/" + std::to_string(vida_max_);
  }

  Criatura& renombrar(const std::string& nombre) {
    this->nombre_ = nombre;
    return *this;
  }

 private:
  std::string nombre_;
  int vida_;
  int vida_max_;
};

int main() {
  Criatura c("brasita", 12);

  std::cout << c.estado() << "\n";
  c.recibir_dano(20);
  std::cout << c.estado() << " viva=" << c.esta_viva() << "\n";
  c.curar(5);
  std::cout << c.renombrar("lumita").estado() << "\n";
}
```

## Salida

```text
brasita: 12/12
brasita: 0/12 viva=0
lumita: 5/12
```

## Qué es `this`

Dentro de `renombrar`, `nombre_` y `nombre` son dos cosas distintas. `nombre_` es el miembro;
`nombre` es el parámetro que oculta el nombre simple del miembro. `this->nombre_` dice "el miembro del
objeto sobre el que me llamaron", que es lo que quieres cuando los nombres chocan.

| Expresión | Significa |
| :--- | :--- |
| `nombre_` | el miembro de este objeto |
| `nombre` | el parámetro |
| `this` | puntero a este objeto |
| `*this` | el objeto mismo |

## Encadenar devolviendo `*this`

`renombrar` devuelve `Criatura&`, así que `c.renombrar("lumita").estado()` funciona: la referencia es
el mismo objeto y la llamada siguiente opera sobre él. Devolver `*this` por valor también encadenaría,
pero copiando, que es otra cosa.

> [!IMPORTANT]
> Un método que no modifica el objeto debe marcarse `const`. `esta_viva() const` se puede llamar sobre
> un `const Criatura`, y entonces el compilador garantiza que no cambia el objeto.

> [!TIP]
> Recorta dentro del método, como hace `curar` con `vida_max_`, en lugar de confiar en cada llamador.
> El objeto es el único que conoce todas sus reglas, y se llama desde todas partes.

---

**Siguiente:** [[43 - El Códice de Familiares]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
