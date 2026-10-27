# ⚙️ C++: Programación de Sistemas y Fundamentos de Motores de Juego (MOC)

**English:** [README.md](./README.md)

<p align="left">
  <img src="https://img.shields.io/badge/Lenguaje-C%2B%2B20-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++20">
  <img src="https://img.shields.io/badge/Cadena_de_herramientas-g%2B%2B%20%7C%20Clang-7C5CFF?style=for-the-badge&logo=llvm&logoColor=white" alt="Cadena de herramientas">
  <img src="https://img.shields.io/badge/Paradigma-Procedural%20y%20POO-FF6B35?style=for-the-badge" alt="Procedural y POO">
  <img src="https://img.shields.io/badge/Dificultad-Principiante_a_Avanzado-6CC24A?style=for-the-badge" alt="Principiante a avanzado">
  <img src="https://img.shields.io/badge/Capítulos-8-7C5CFF?style=for-the-badge" alt="8 capítulos">
  <img src="https://img.shields.io/badge/Notas-53-00C2A8?style=for-the-badge" alt="53 notas">
  <img src="https://img.shields.io/badge/Estado-Completo-00C2A8?style=for-the-badge" alt="Completo">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Bóveda-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
  <img src="https://img.shields.io/badge/Entorno-macOS-lightgrey?style=for-the-badge&logo=apple&logoColor=white" alt="macOS">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="Onda C++" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

**Nota:**
Este módulo es el Mapa de Contenido (MOC) de las notas de C++ en este vault de Obsidian. C++ es el
lenguaje detrás de los motores de juego, los sistemas operativos, los navegadores y todo aquello que
no puede permitirse ser lento. Te entrega la memoria real de la máquina como algo a lo que puedes
apuntar: por eso es rápido y por eso es implacable. Todos los ejemplos son mínimos y ejecutables tal
como están escritos.

**Consejo:**
Empieza en [[01 - El Programa]]. Compila y ejecuta algo antes de estudiar otra cosa: el ciclo
*escribir → `g++` → `./a.out`* es el hábito del que depende todo el módulo. Después sigue el orden de
los capítulos; cada uno asume el anterior.

**Requisito previo:** ninguno. Una terminal, un compilador (`g++` o `clang++`) y un editor de texto.
Ver [[Compilar y Ejecutar]] si todavía no tienes `g++`.

> [!NOTE]
> **La narrativa Emberfall**
> Cada ejercicio pertenece al mismo proyecto ficticio: *Emberfall*, un roguelike. Las galletas de la
> fortuna se vuelven rumores de misión, los lanzamientos de moneda se vuelven tiradas de botín, las
> cuentas bancarias se vuelven cámaras del gremio y los menús de terminal se vuelven tabernas. La
> sintaxis nunca cambia: ese es el punto. Aprendes un vocabulario y lo reutilizas en cada programa
> que llegues a publicar.

---

## 🗺️ Mapa de Contenido

### 📚 Referencia y Chuletas

* **Chuletas:**
  * [00b - Chuleta de C++](./00b%20-%20Chuleta%20de%20C%2B%2B.md) — Entrada/salida, tipos, operadores, flujo, bucles, vectores, funciones, clases y punteros.
  * [00c - Chuleta de C++ II](./00c%20-%20Chuleta%20de%20C%2B%2B%20II.md) — Ámbito, modificadores de acceso, constructores, paso por referencia, tabla puntero vs referencia y cabeceras.

### ⚡ 1. Hola, Sistemas (Capítulo 1)

* **[01 - El Programa](./01%20-%20El%20Programa.md)** — Stroustrup, 1979, "C with Classes", dónde corre C++ hoy y el archivo `.cpp`.
* **[02 - ¡Howdy!](./02%20-%20%C2%A1Howdy%21.md)** — `std::cout`, las cuatro piezas de una sentencia de salida, el punto y coma.
* **[03 - Nos Vemos Más Tarde, Cocodrilo](./03%20-%20Nos%20Vemos%20M%C3%A1s%20Tarde%2C%20Cocodrilo.md)** — `#include`, `int main()`, bloques de código y secuencias de escape (`\n`, `\t`).
* **[04 - Tabla Ouija](./04%20-%20Tabla%20Ouija.md)** — `//` y `/* */`, y por qué el código comentado es un olor.
* **[05 - Conejito de Señalización](./05%20-%20Conejito%20de%20Se%C3%B1alizaci%C3%B3n.md)** — Repaso del capítulo 1 y arte ASCII que sobrevive al escapado.
* **[Compilar y Ejecutar](./Compilar%20y%20Ejecutar.md)** — Código fuente vs código máquina, `g++`, `-o`, `./a.out`.

### 🔢 2. Variables, Tipos y Matemáticas (Capítulo 2)

* **[06 - Tipos de Datos](./06%20-%20Tipos%20de%20Datos.md)** — `int`, `double`, `char`, `std::string`, `bool` — y cuántos bytes cuesta cada uno.
* **[07 - Declaración de Independencia](./07%20-%20Declaraci%C3%B3n%20de%20Independencia.md)** — Declarar, reglas de nombres, `snake_case` vs `PascalCase`.
* **[08 - IPO (Entrada, Proceso, Salida)](./08%20-%20IPO%20%28Entrada%2C%20Proceso%2C%20Salida%29.md)** — Asignación vs igualdad, actualizar e imprimir variables.
* **[09 - Temperatura](./09%20-%20Temperatura.md)** — Operadores aritméticos, precedencia y la trampa de la división entera.
* **[10 - Caballería](./10%20-%20Caballer%C3%ADa.md)** — Encadenar salida con varios `<<`.
* **[11 - Mes a Mes (MoM)](./11%20-%20Mes%20a%20Mes%20%28MoM%29.md)** — `std::cin`, hacia dónde apuntan las flechas y la fórmula del porcentaje.
* **[12 - Años Gato](./12%20-%20A%C3%B1os%20Gato.md)** — Repaso del capítulo 2 aplicado a una fórmula con caso límite.

### 🧠 3. Lógica y Flujo de Control (Capítulo 3)

* **[13 - Lanzamiento de Moneda](./13%20-%20Lanzamiento%20de%20Moneda.md)** — Flujo de control, `srand` y un error real que vale la pena detectar.
* **[14 - Fiebre](./14%20-%20Fiebre.md)** — `if` / `else`, y por qué las llaves no son opcionales en la práctica.
* **[15 - Niveles y Rangos](./15%20-%20Niveles%20y%20Rangos.md)** — Seis operadores relacionales, `else if`, orden de primera coincidencia.
* **[16 - Galleta de la Fortuna](./16%20-%20Galleta%20de%20la%20Fortuna.md)** — `std::rand()`, rangos con `%` y siembra con `time(NULL)`.
* **[17 - Votación](./17%20-%20Votaci%C3%B3n.md)** — `&&`, `||`, `!`, tablas de verdad y evaluación de cortocircuito.
* **[18 - Trivial Quiz](./18%20-%20Trivial%20Quiz.md)** — Repaso del capítulo 3 como proyecto de quiz con puntuación.

### 🔁 4. Bucles e Iteración (Capítulo 4)

* **[19 - Introducir PIN](./19%20-%20Introducir%20PIN.md)** — Qué es iterar y las cuatro piezas de un bucle que termina.
* **[20 - Adivina el Número](./20%20-%20Adivina%20el%20Número.md)** — `while`: el bucle que puede ejecutarse cero veces.
* **[21 - Contando Ovejas](./21%20-%20Contando%20Ovejas.md)** — `for`: inicialización, condición, cambio — y el off-by-one.
* **[22 - 99 Botellas](./22%20-%2099%20Botellas.md)** — Contar hacia abajo con `i--`.
* **[23 - Fizz Buzz (Reto)](./23%20-%20Fizz%20Buzz%20%28Reto%29.md)** — Repaso del capítulo 4 y el clásico de entrevistas, donde el orden lo es todo.

### 📦 5. Vectores y Colecciones (Capítulo 5)

* **[24 - Equipo de Supervivencia](./24%20-%20Equipo%20de%20Supervivencia.md)** — `std::vector`, cabeceras y por qué los vectores reemplazaron a los arrays.
* **[25 - Puesto de Limonada](./25%20-%20Puesto%20de%20Limonada.md)** — Índices desde 0, `v[size() - 1]` y comportamiento indefinido al pasarse.
* **[26 - Carrito de Compras](./26%20-%20Carrito%20de%20Compras.md)** — `.push_back()`, `.pop_back()`, `.size()`.
* **[27 - Lista de Reproducción de Viaje](./27%20-%20Lista%20de%20Reproducción%20de%20Viaje.md)** — Iterar con `for` y `.size()` como límite.
* **[28 - Suma de Pares - Producto de Impares](./28%20-%20Suma%20de%20Pares%20-%20Producto%20de%20Impares.md)** — Repaso del capítulo 5 y los valores identidad (`0` para sumas, `1` para productos).
* **[Arrays en C++](./Arrays%20en%20C%2B%2B.md)** — Arrays estilo C vs `std::vector`: fijo vs dinámico, pila vs montículo.

### 🧩 6. Funciones y Ámbito (Capítulo 6)

* **[29 - D.R.Y. (No te repitas)](./29%20-%20D.R.Y.%20%28No%20te%20repitas%29.md)** — Qué compra realmente una función.
* **[30 - Menú de Comida](./30%20-%20Menú%20de%20Comida.md)** — Definir y llamar funciones `void`; declarar antes de llamar.
* **[31 - Fuera de Oficina](./31%20-%20Fuera%20de%20Oficina.md)** — Los parámetros son marcadores, los argumentos son valores reales.
* **[32 - Conversiones](./32%20-%20Conversiones.md)** — `return` y la diferencia entre `void` y un tipo de retorno.
* **[32 - Conversiones (Continuación)](./32%20-%20Conversiones%20%28Continuación%29.md)** — Usar un valor retornado dentro de una expresión.
* **[33 - Calculadora de Propinas](./33%20-%20Calculadora%20de%20Propinas.md)** — Repaso del capítulo 6: recoger, calcular, informar.
* **[Ámbito en C++](./Ámbito%20en%20C%2B%2B.md)** — Local vs global, tiempo de vida y sombreado.

### 🏛️ 7. Clases y POO (Capítulo 7)

* **[34 - Restaurantes](./34%20-%20Restaurantes.md)** — `class` como plano; el punto y coma que todos olvidan.
* **[35 - Público vs Privado](./35%20-%20Público%20vs%20Privado.md)** — Modificadores de acceso y encapsulación.
* **[36 - Cuentas Bancarias](./36%20-%20Cuentas%20Bancarias.md)** — Atributos vs métodos; `this`.
* **[37 - Cuentas Bancarias (Continuación)](./37%20-%20Cuentas%20Bancarias%20%28Continuación%29.md)** — Un sistema funcional de depósito, retiro y consulta.
* **[38 - Coches Clásicos](./38%20-%20Coches%20Clásicos.md)** — Constructores, valores por defecto y el constructor implícito que desaparece.
* **[39 - Rescate de Mascotas](./39%20-%20Rescate%20de%20Mascotas.md)** — Repaso del capítulo 7 como esqueleto de proyecto POO.
* **[39 - Rescate de Mascotas (Continuación)](./39%20-%20Rescate%20de%20Mascotas%20%28Continuación%29.md)** — Los métodos, los topes de estadísticas y el menú interactivo.

### 🧠 8. Punteros y Memoria (Capítulo 8)

* **[40 - Recuerdos](./40%20-%20Recuerdos.md)** — Direcciones de memoria, hexadecimal y el mapa de la pila.
* **[40 - Recuerdos (Continuación)](./40%20-%20Recuerdos%20%28Continuación%29.md)** — El operador `&` y el cast a `(void*)`.
* **[41 - Unos Punteros](./41%20-%20Unos%20Punteros.md)** — `int*`, coincidencia de tipos y las cuatro razones por las que existen los punteros.
* **[42 - Desreferenciación](./42%20-%20Desreferenciación.md)** — `*` como declaración vs `*` como operador.
* **[43 - Referencias vs Punteros](./43%20-%20Referencias%20vs%20Punteros.md)** — Alias, tabla comparativa y paso por referencia.
* **[44 - Puntero Nulo](./44%20-%20Puntero%20Nulo.md)** — El puntero que no apunta a nada, y por qué es mejor que `NULL`.
* **[45 - El Fin](./45%20-%20El%20Fin.md)** — Repaso del capítulo 8 y todo el curso en una tabla.

---

## 🎯 Ruta de Aprendizaje

1. **Hola, sistemas** → compilar, ejecutar, imprimir, comentar, escapar.
2. **Variables y matemáticas** → tipos, declaraciones, `cin`, aritmética.
3. **Lógica** → `if` / `else if` / `else`, operadores relacionales y lógicos, aleatoriedad.
4. **Bucles** → `while` y `for`, incremento y decremento, límites de iteración.
5. **Vectores** → colecciones dinámicas, índices, métodos, iteración.
6. **Funciones** → DRY, parámetros y argumentos, retornos, ámbito.
7. **Clases** → planos, encapsulación, constructores, métodos.
8. **Punteros** → direcciones, desreferencia, referencias, `nullptr`.

---

## 🎯 Lo Que Podrás Hacer

- Escribir, compilar y ejecutar programas C++ desde la terminal con `g++`.
- Elegir el tipo de dato correcto y saber cuánto cuesta en memoria.
- Imprimir salida con formato y leer entrada del usuario con `std::cin`.
- Controlar el flujo con condicionales y ambos tipos de bucle, sin errores de off-by-one.
- Guardar y recorrer colecciones con `std::vector` en lugar de variables paralelas.
- Dividir un programa en funciones con entradas, salidas y ámbito claros.
- Modelar entidades con clases, constructores y métodos: la forma del código de juego.
- Explicar qué es un puntero, cuándo usar una referencia y por qué `nullptr` importa.

---

## 🧰 Herramientas

| Herramienta | Por qué |
| :--- | :--- |
| `g++` o `clang++` | Compila `.cpp` en un ejecutable |
| Una terminal | Donde compilas y donde aparece la salida del programa |
| Cualquier editor de código (se recomienda VS Code) | Escribir, guardar y ejecutar archivos `.cpp` |
| Obsidian (este vault) | Mantener notas, chuletas y ejercicios juntos |

```bash
# el ciclo que repetirás el resto del módulo
g++ -Wall -Wextra -std=c++17 main.cpp -o main
./main
```

---

## 🗺️ Mapa del Curso

| # | Notas | Qué aprendes |
| :--- | :--- | :--- |
| 00b / 00c | Chuletas I y II | Todo a la vista, para consultar |
| 1 | 01 – 05 + Compilar y Ejecutar | Salida, estructura, comentarios, escapado, ciclo de compilación |
| 2 | 06 – 12 | Tipos, declaración, asignación, aritmética, entrada |
| 3 | 13 – 18 | `if` / `else`, comparaciones, operadores lógicos, `rand()` |
| 4 | 19 – 23 | `while`, `for`, incremento/decremento, Fizz Buzz |
| 5 | 24 – 28 + Arrays | Vectores, índices, métodos, iteración, arrays vs vectores |
| 6 | 29 – 33 + Ámbito | Funciones, parámetros, retornos, DRY, local vs global |
| 7 | 34 – 39 | Clases, acceso, métodos, constructores, proyecto POO |
| 8 | 40 – 45 | Direcciones, punteros, desreferencia, referencias, `nullptr` |

---

## 🎮 Filosofía de Práctica

C++ no te da red de seguridad: un índice fuera de rango no lanza nada, un puntero sin inicializar no
se detecta y un bucle infinito simplemente sigue. Por eso cada nota empareja un concepto con la
**trampa concreta** que esconde —comportamiento indefinido, división entera, orden de primera
coincidencia, memoria sin inicializar.

Compila después de cada cambio pequeño. Un programa C++ que da un error es un programa que te dijo
algo; el que compila y falla en silencio es el que te cuesta una noche.

---

## 🔗 Ver También

- [🐍 Python MOC](../%F0%9F%90%8D%20Python/README.md) — la rampa más suave a la lógica de programación antes de la memoria manual.
- [🟣 C# MOC](../%F0%9F%9F%A3%20CSharp/README.md) — las mismas ideas de POO, con recolector de basura y Unity.
- [🖥️ Línea de Comandos MOC](../%F0%9F%96%A5%EF%B8%8F%20Command%20Line/README.md) — navegar la carpeta, ejecutar `g++`, lanzar binarios.
- [🧮 Estructuras de Datos y Algoritmos MOC](../%F0%9F%A7%AE%20Data%20Structures%20%26%20Algorithms/README.md) — qué hacer cuando los vectores y punteros ya son familiares.
- [🌐 HTML MOC](../%F0%9F%8C%90%20HTML/README.md) · [🎨 CSS MOC](../%F0%9F%8E%A8%20CSS/README.md) · [🟨 JavaScript MOC](../%F0%9F%9F%A8%20JavaScript/README.md) · [⚛️ React MOC](../%E2%9A%9B%EF%B8%8F%20React/README.md) — la pista web, como contraste con la programación de sistemas.

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="Pie C++" />
</p>
