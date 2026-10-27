# 33. Calculadora de Propinas

**Versión original en inglés:** [33 - Tips Calculator.md](./33%20-%20Tips%20Calculator.md)

**Curso:** C++
**Tema:** Repaso del capítulo 6 y múltiples funciones
**Etiquetas:** `#cpp` `#recap` `#functions` `#calculator`

<p align="left">
  <img src="https://img.shields.io/badge/Lenguaje-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Estado-Completo-00C2A8?style=for-the-badge" alt="Completo">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Bóveda-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

## Repaso del capítulo 6

- La metodología "Don't Repeat Yourself" (DRY).
- Hemos estado usando funciones integradas desde el principio.
- Cómo **definir** y **llamar** una función `void`: el proceso de dos pasos.
- Entradas con **parámetros** y **argumentos**.
- Salidas con la palabra clave `return`.

## Proyecto

Tres funciones, tres responsabilidades: una recoge la entrada, una calcula, una informa.

```cpp
#include <iostream>

// 1. Pedir el porcentaje de propina
double menu_propina() {
  double porcentaje;
  std::cout << "--- ¿Dejar propina? ---\n";
  std::cout << "[ 15% ]  [ 20% ]  [ 25% ]\n\n";
  std::cout << "Ingresa el porcentaje (ej. 20): ";
  std::cin >> porcentaje;
  return porcentaje;
}

// 2. Calcular el monto de la propina
double calcular_propina(double subtotal, double porcentaje) {
  return subtotal * (porcentaje / 100.0);
}

// 3. Dividir la cuenta entre los comensales
void dividir_cuenta(double total, int comensales) {
  if (comensales > 0) {
    double por_persona = total / comensales;
    std::cout << "\n--- Cuenta compartida ---\n";
    std::cout << "Comensales: " << comensales << "\n";
    std::cout << "Cada uno debe: $" << por_persona << "\n";
  }
}

int main() {
  double costo_comida = 85.50;
  int comensales = 3;

  std::cout << "Subtotal: $" << costo_comida << "\n\n";

  double propina_elegida = menu_propina();
  double monto_propina = calcular_propina(costo_comida, propina_elegida);
  double total_final = costo_comida + monto_propina;

  std::cout << "\nPropina: $" << monto_propina << "\n";
  std::cout << "Total: $" << total_final << "\n";

  dividir_cuenta(total_final, comensales);
}
```

> [!NOTE]
> **El patrón de composición**
> `main()` se lee como un índice: recoger, calcular, informar. Cada función es lo bastante pequeña
> para probarla por separado. Eso es lo que compra DRY cuando el programa crece más allá de una
> pantalla.

> [!WARNING]
> La comprobación `comensales > 0` evita dividir entre cero. Dividir un `double` entre cero da `inf`
> en lugar de fallar — lo cual es peor, porque se propaga en silencio.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
