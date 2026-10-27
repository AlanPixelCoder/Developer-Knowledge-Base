# 39. Puertas Selladas y Abiertas

**Versión original en inglés:** [39 - Sealed and Open Doors](./39%20-%20Sealed%20and%20Open%20Doors.md)

**Curso:** C++
**Capítulo:** 7 — Entidades
**Tema:** public y private: mantener los invariantes dentro del tipo
**Etiquetas:** `#cpp` `#class` `#encapsulation`

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

La puerta de una cámara tiene un asa pública y un mecanismo privado. Girar el asa está permitido;
meter la mano en el mecanismo y dejar el cerrojo a medio camino no, porque dejaría la cámara en un
estado que el diseñador nunca previó.

```cpp
#include <iostream>

struct PuertaCamara {
 public:
  bool esta_abierta() const { return abierta_; }

  void desbloquear() { bloqueada_ = false; }

  bool abrir() {
    if (bloqueada_) {
      return false;
    }
    abierta_ = true;
    return true;
  }

 private:
  bool bloqueada_ = true;
  bool abierta_ = false;
};

int main() {
  PuertaCamara puerta;

  std::cout << "abrir bloqueada: " << puerta.abrir() << "\n";
  puerta.desbloquear();
  std::cout << "abrir desbloqueada: " << puerta.abrir() << "\n";
  std::cout << "estado: " << (puerta.esta_abierta() ? "abierta" : "cerrada") << "\n";
}
```

## Salida

```text
abrir bloqueada: 0
abrir desbloqueada: 1
estado: abierta
```

## Dos etiquetas, una regla

| Etiqueta | Quién puede tocarlo | Qué poner |
| :--- | :--- | :--- |
| `public` | cualquier código con el objeto | lo que el tipo promete |
| `private` | solo los miembros del tipo | cómo se cumple la promesa |

`struct` es público por defecto, `class` es privado por defecto. La otra diferencia es solo el
defecto; una `class` con `public:` arriba es el mismo tipo que un `struct`.

## El invariante

`bloqueada_ == true` significa `abierta_ == false`. Nada de fuera puede romper esa regla, porque los
campos son privados y `abrir()` es el único que escribe. El invariante es local, así que se comprueba
leyendo veinte líneas y no todo el programa.

> [!IMPORTANT]
> `puerta.abrir()` con la puerta bloqueada devuelve `false` e imprime `0` en contexto `bool`. Es un
> contrato deliberado, no un error: un cerrojo que falla en silencio es peor que uno inalcanzable.

> [!TIP]
> Marca los métodos de solo lectura como `const` (`bool esta_abierta() const`). Así un
> `const PuertaCamara&` todavía puede preguntar su estado, y el compilador rechaza cualquier intento
> de modificar a través de esa referencia.

---

**Siguiente:** [[40 - La Caja Fuerte de Reliquias]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
