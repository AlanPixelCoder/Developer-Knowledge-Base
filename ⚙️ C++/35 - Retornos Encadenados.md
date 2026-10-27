# 35. Retornos Encadenados

**Versión original en inglés:** [35 - Chained Returns](./35%20-%20Chained%20Returns.md)

**Curso:** C++
**Capítulo:** 6 — Funciones
**Tema:** Componer funciones: piezas pequeñas que se llaman entre sí
**Etiquetas:** `#cpp` `#functions` `#composition`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Chapter-6-7C5CFF?style=for-the-badge" alt="Chapter 6">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

El daño final de una runa se construye por etapas: base, luego el multiplicador de afinidad, luego la
resta de armadura, luego el suelo de uno. Cada etapa es una función, y cada una se puede probar sola.

```cpp
#include <iostream>

double dano_base(int poder) {
  return poder * 2.5;
}

double afinidad(double valor, double multiplicador) {
  return valor * multiplicador;
}

int tras_armadura(double valor, int armadura) {
  double reducido = valor - armadura;
  return reducido < 1.0 ? 1 : static_cast<int>(reducido);
}

int dano_de_runa(int poder, double multiplicador, int armadura) {
  return tras_armadura(afinidad(dano_base(poder), multiplicador), armadura);
}

int main() {
  std::cout << dano_de_runa(10, 1.5, 4) << "\n";
  std::cout << dano_de_runa(2, 1.0, 30) << "\n";
}
```

## Salida

```text
33
1
```

## Lee la tubería de dentro hacia fuera

`dano_de_runa` se lee así: base desde el poder, luego afinidad, luego armadura, luego el recorte.

| Etapa | Entra | Sale |
| :--- | :--- | :--- |
| `dano_base(10)` | 10 | 25 |
| `afinidad(25, 1.5)` | 25 | 37.5 |
| `tras_armadura(37.5, 4)` | 37.5 | 33 |

Encadenar llamadas en una expresión está bien **cuando el orden coincide con la frase**. Cuando deja
de coincidir, nombra una variable intermedia.

## Por qué dividir

- Cada etapa se puede cambiar por un ajuste de balance sin tocar las otras.
- Cada etapa se comprueba con una llamada y un número esperado.
- La traza impresa de una corrida rota apunta a una etapa, no a "la fórmula entera".

> [!IMPORTANT]
> `static_cast<int>` trunca hacia cero, así que `tras_armadura(4.9, 0)` devuelve 4, no 5. Si el juego
> redondea el daño, decídelo explícitamente: convierte después de sumar `0.5`, o usa `std::lround`.

> [!TIP]
> Mantén una idea por función. Si un nombre necesita "y" dentro — `dano_y_armadura` — son dos
> funciones con un solo abrigo.

---

**Siguiente:** [[36 - El Impuesto del Portal]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
