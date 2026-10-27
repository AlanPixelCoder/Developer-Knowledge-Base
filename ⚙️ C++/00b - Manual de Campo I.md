# Manual de Campo I

**Versión original en inglés:** [00b - Field Manual I](./00b%20-%20Field%20Manual%20I.md)

**Curso:** C++
**Tema:** Referencia rápida
**Etiquetas:** `#cpp` `#cheatsheet` `#reference`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Reference-Field%20Manual-7C5CFF?style=for-the-badge" alt="Field Manual">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

<p align="center">
  <sub>1–4 · Del Primer Arranque a la Iteración</sub>
</p>

> [!TIP]
> Todo lo de los capítulos 1 a 4 en una página: la forma de un programa, los tipos de valor, los
> operadores que los combinan, las ramas que eligen y los bucles que repiten.

## El programa más pequeño

```cpp
#include <iostream>

int main() {
  std::cout << "arranque en frío\n";
  return 0;
}
```

```bash
g++ -std=c++17 -Wall -Wextra main.cpp -o console && ./console
```

## Imprimir y leer

```cpp
std::cout << "vida: " << vida << "\n";   // encadena valores y texto
std::cin >> vida;                        // lee un valor separado por espacios
std::string linea;
std::getline(std::cin, linea);           // lee una línea completa
```

## Tipos de valor

| Tipo | Contiene | Ejemplo |
| :--- | :--- | :--- |
| `int` | enteros, unos ±2.100 millones | `int vida = 100;` |
| `double` | decimales, 15 dígitos significativos | `double tasa = 0.75;` |
| `char` | un carácter | `char rango = 'B';` |
| `bool` | `true` / `false` | `bool vivo = true;` |
| `std::string` | texto, crece según necesidad | `std::string nombre = "guardian";` |

| Conversión | Sintaxis | Resultado |
| :--- | :--- | :--- |
| int → double | `static_cast<double>(n)` | exacta |
| double → int | `static_cast<int>(x)` | trunca hacia cero |
| número → cadena | `std::to_string(n)` | `"42"` |
| cadena → número | `std::stoi(s)` | `42`, lanza si hay basura |

## Operadores

| Grupo | Operadores | Nota |
| :--- | :--- | :--- |
| Aritmética | `+ - * / %` | `5 / 2` es `2`; convierte un lado a `double` |
| Comparación | `== != < <= > >=` | el resultado es `bool` |
| Lógica | `&&` `\|\|` `!` | cortocircuito: el lado derecho puede no ejecutarse |
| Asignación | `= += -= *= /=` | `x += 3` significa `x = x + 3` |
| Incremento | `++ --` | prefijo da el valor nuevo, postfijo el viejo |

## Decisiones

```cpp
if (vida <= 0) {
  std::cout << "caído\n";
} else if (vida < 20) {
  std::cout << "tambaleante\n";
} else {
  std::cout << "firme\n";
}
```

| Escrito | Coincide con |
| :--- | :--- |
| `x == 3` | igualdad |
| `x = 3` | asignación: siempre verdadera en una condición |
| `0 <= x && x < 10` | comprobación de rango |
| `x % 2 == 0` | par |

## Bucles

```cpp
for (int i = 0; i < 3; i++) { /* cuenta conocida */ }

while (combustible > 0.0) { combustible -= 0.5; }   // condición primero

do { preguntar(); } while (!respondido());          // cuerpo al menos una vez

for (const auto& objeto : alforja) { /* cada elemento */ }
```

| Bucle | Úsalo cuando |
| :--- | :--- |
| `for` | la cuenta es conocida, o necesitas el índice |
| `while` | el final depende de una condición |
| `do ... while` | el cuerpo debe correr al menos una vez |
| range-`for` | quieres cada elemento de una colección |

> [!CAUTION]
> Todo bucle necesita un camino hacia una condición falsa. Un paso de cambio dentro de un `if` que
> nunca se cumple es el bucle infinito más común en código principiante.

## Banderas del compilador que merecen memorizarse

```bash
g++ -std=c++17 -Wall -Wextra -Wshadow main.cpp -o console
```

| Bandera | Detecta |
| :--- | :--- |
| `-std=c++17` | fija la versión del lenguaje |
| `-Wall -Wextra` | variables sin usar, mezclas de signo, returns ausentes |
| `-Wshadow` | un local que oculta una variable externa |
| `-fsanitize=address,undefined` | fuera de rango y uso tras liberación, en ejecución |

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
