# 48. Alcanzar a Través del Asa

**Versión original en inglés:** [48 - Reaching Through the Handle](./48%20-%20Reaching%20Through%20the%20Handle.md)

**Curso:** C++
**Capítulo:** 8 — Memoria
**Tema:** Punteros como parámetros: el objeto, no una copia
**Etiquetas:** `#cpp` `#pointers` `#functions`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Chapter-8-7C5CFF?style=for-the-badge" alt="Chapter 8">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

El invocador debe rellenar una entidad que ya existe. Pasar el struct por valor entrega una copia y el
original queda intacto, que es justo lo que le pasó a la primera versión de este sistema.

```cpp
#include <iostream>
#include <string>

struct Entidad {
  std::string nombre;
  int vida;
};

void danar_por_valor(Entidad e) {
  e.vida -= 30;
}

void danar_por_puntero(Entidad* e) {
  if (e == nullptr) {
    return;
  }
  e->vida -= 30;
}

void danar_por_referencia(Entidad& e) {
  e.vida -= 30;
}

int main() {
  Entidad objetivo{"guardian", 100};

  danar_por_valor(objetivo);
  std::cout << "tras valor:     " << objetivo.vida << "\n";

  danar_por_puntero(&objetivo);
  std::cout << "tras puntero:   " << objetivo.vida << "\n";

  danar_por_referencia(objetivo);
  std::cout << "tras referencia: " << objetivo.vida << "\n";
}
```

## Salida

```text
tras valor:     100
tras puntero:   70
tras referencia: 40
```

## Tres formas de pasar una entidad

| Firma | Llamada | ¿Modifica a quien llama? | ¿Puede ser "nada"? |
| :--- | :--- | :--- | :--- |
| `Entidad e` | `f(objetivo)` | no | no |
| `Entidad* e` | `f(&objetivo)` | sí | sí, `nullptr` |
| `Entidad& e` | `f(objetivo)` | sí | no |

Una referencia es un puntero que no puede ser nulo y no necesita `&` en la llamada. Un puntero es
para cuando "ausente" es una posibilidad real: un objetivo opcional, un jefe aún sin invocar.

## La comprobación de nulo es el precio

`danar_por_puntero` empieza con `if (e == nullptr) return;`. Una versión con referencia no se puede
llamar con nada, así que no necesita la comprobación. Ese es todo el intercambio: una comprobación de
nulo a cambio de expresividad en la llamada.

> [!IMPORTANT]
> `&objetivo` en la llamada es el operador dirección-de; `Entidad*` en la firma es el tipo puntero.
> Ambos usan `&` y `*`, y ninguno es el mismo uso del glifo que dentro del cuerpo de la función.

> [!TIP]
> Usa referencias (`Entidad&`) por defecto para "debe existir" y punteros (`Entidad*`) para "puede
> faltar". Pasar por valor solo es correcto para tipos pequeños que pretendes copiar.

---

**Siguiente:** [[49 - Alias vs Asas]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
