# 33. Llenar las Ranuras

**Versión original en inglés:** [33 - Filling the Slots](./33%20-%20Filling%20the%20Slots.md)

**Curso:** C++
**Capítulo:** 6 — Funciones
**Tema:** Argumentos por defecto y sobrecargas con distinta aridad
**Etiquetas:** `#cpp` `#functions` `#default-arguments`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-6-7C5CFF?style=for-the-badge" alt="Chapter 6">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

La mayoría de las pociones se preparan con agua y una hierba. Algunas añaden un catalizador. Otras,
dos. En lugar de tres funciones con nombres casi iguales, las ranuras reciben valores por defecto.

```cpp
#include <iostream>
#include <string>

std::string preparar(const std::string& hierba,
                     const std::string& base = "agua",
                     int potencia = 1) {
  return hierba + " en " + base + " x" + std::to_string(potencia);
}

int main() {
  std::cout << preparar("raizbrasa") << "\n";
  std::cout << preparar("raizbrasa", "aceite") << "\n";
  std::cout << preparar("raizbrasa", "aceite", 3) << "\n";
}
```

## Salida

```text
raizbrasa en agua x1
raizbrasa en aceite x1
raizbrasa en aceite x3
```

## Cómo se eligen los valores por defecto

Quien llama pasa argumentos **de izquierda a derecha**. Todo parámetro sin argumento debe tener un
valor por defecto, y los valores por defecto deben ser los últimos:

| Llamada | hierba | base | potencia |
| :--- | :--- | :--- | :--- |
| `preparar("raizbrasa")` | raizbrasa | agua | 1 |
| `preparar("raizbrasa", "aceite")` | raizbrasa | aceite | 1 |
| `preparar("raizbrasa", "aceite", 3)` | raizbrasa | aceite | 3 |

No puedes saltarte `base` y pasar solo `potencia`. Por eso el parámetro con más probabilidad de
cambiar va al final.

## Los valores por defecto viven en la declaración

Si la función se declara y se define por separado, el valor por defecto va en la declaración — la
cabecera, donde quien llama puede verlo. Repetirlo en la definición es un error de redefinición.

> [!WARNING]
> Los argumentos por defecto se evalúan en el sitio de la llamada, no en la definición. Un valor por
> defecto como `time(nullptr)` o `rand()` se calcula en cada llamada; uno que nombre un global puede
> sorprenderte cuando ese global cambie.

> [!TIP]
> La sobrecarga y los valores por defecto resuelven el mismo problema de dos formas. Los valores por
> defecto mantienen una implementación; una segunda sobrecarga mantiene dos. Prefiere valores por
> defecto cuando los parámetros extra solo ajustan el mismo algoritmo.

---

**Siguiente:** [[34 - Devolver el Botín]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
