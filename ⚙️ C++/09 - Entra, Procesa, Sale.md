# 09. Entra, Procesa, Sale

**Versión original en inglés:** [09 - In, Through, Out](./09%20-%20In%2C%20Through%2C%20Out.md)

**Curso:** C++
**Capítulo:** 2 — Valores en Bruto
**Tema:** Asignación frente a igualdad, y los tres tiempos de un cálculo
**Etiquetas:** `#cpp` `#variables` `#assignment`

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

Todo programa útil de este curso sigue el mismo ritmo: un valor **entra**, le pasa algo y un resultado
**sale**. Si el ritmo está bien, la sintaxis deja de ser el problema.

```cpp
#include <iostream>

int main() {
  double aceite_linterna = 6.0;      // entra: con lo que empieza el jugador
  double consumo_por_minuto = 0.75;  // entra: gasto

  double minutos_restantes = aceite_linterna / consumo_por_minuto;  // procesa

  std::cout << "minutos de luz: " << minutos_restantes << "\n";  // sale
}
```

## `=` no es `==`

| Operador | Significado | Ejemplo | Resultado |
| :--- | :--- | :--- | :--- |
| `=` | guarda la derecha en la izquierda | `combustible = 10;` | `combustible` pasa a 10 |
| `==` | pregunta si ambos lados son iguales | `combustible == 10` | `true` o `false` |

Usar `=` donde querías `==` dentro de una condición es C++ legal y silenciosamente incorrecto: la
asignación ocurre y el *valor guardado* se convierte en la condición. El compilador avisa — una de
las razones por las que existe `-Wall`.

## Dos formas de cambiar una variable

```cpp
#include <iostream>

int main() {
  int brasas = 4;

  brasas = brasas + 3;  // forma larga
  brasas += 2;          // asignación compuesta
  brasas++;             // incremento en uno

  std::cout << "brasas: " << brasas << "\n";
}
```

## Salida

```text
brasas: 10
```

> [!NOTE]
> El primer ejemplo imprime `8` minutos de luz: 6 / 0.75. La división solo se vuelve entera cuando
> **ambos** operandos son enteros; esa trampa está a una lección de distancia, en
> [[10 - Números que Mienten]].

> [!TIP]
> Escribe los tres tiempos como tres sentencias separadas antes de comprimir nada. Quien lea debe
> poder señalar una línea y decir "aquí entra la entrada".

---

**Siguiente:** [[10 - Números que Mienten]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
