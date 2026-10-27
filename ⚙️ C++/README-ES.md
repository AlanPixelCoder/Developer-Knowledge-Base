# ⚙️ C++: Fundamentos de Motor (MOC)

**English:** [README.md](./README.md)

<p align="left">
  <img src="https://img.shields.io/badge/Lenguaje-C%2B%2B17-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++17">
  <img src="https://img.shields.io/badge/Herramientas-g%2B%2B%20%7C%20Clang-7C5CFF?style=for-the-badge&logo=llvm&logoColor=white" alt="Herramientas">
  <img src="https://img.shields.io/badge/Paradigma-Procedural%20y%20Objetos-FF6B35?style=for-the-badge" alt="Procedural y objetos">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE_A_INTERMEDIO-6CC24A?style=for-the-badge" alt="Principiante a intermedio">
  <img src="https://img.shields.io/badge/Capítulos-8-7C5CFF?style=for-the-badge" alt="8 capítulos">
  <img src="https://img.shields.io/badge/Notas-53-00C2A8?style=for-the-badge" alt="53 notas">
  <img src="https://img.shields.io/badge/Estado-Completo-00C2A8?style=for-the-badge" alt="Completo">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
  <img src="https://img.shields.io/badge/Entorno-macOS-lightgrey?style=for-the-badge&logo=apple&logoColor=white" alt="macOS">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="Ola C++" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

> [!NOTE]
> Este módulo es el mapa de contenido de las notas de C++ del vault: 51 lecciones en ocho capítulos,
> más dos manuales de campo. Cada programa está completo, compila con `-Wall -Wextra` y la salida
> documentada es la que imprime de verdad.

> [!TIP]
> Empieza en [[01 - Arranque en Frío]] y sigue los números. Compila y ejecuta cada ejemplo antes de
> pasar al siguiente: el hábito de *escribir → `g++` → ejecutar → leer la salida* es lo que entrena
> todo el módulo.

**Requisito:** un terminal, `g++` (o `clang++`) y cualquier editor de texto. Nada más: el capítulo 1
construye el ciclo de compilación desde cero.

> [!NOTE]
> **El hilo de Emberfall**
> Cada ejemplo pertenece a un mismo proyecto interno: la consola y las herramientas de *Emberfall*, un
> pequeño motor de juego. Registros de arranque, valores de configuración, tablas de invocación,
> alforjas, planos de entidades y asas de memoria dan a los ejemplos un vocabulario compartido. El
> lenguaje es exactamente el estándar: el decorado solo evita que los programas sean `foo` y `bar`.

---

## 🗺️ Mapa de Contenido

### 📚 Referencia

* **[00b - Manual de Campo I](./00b%20-%20Manual%20de%20Campo%20I.md)** — E/S, tipos, operadores, flujo de control, bucles, banderas del compilador.
* **[00c - Manual de Campo II](./00c%20-%20Manual%20de%20Campo%20II.md)** — Contenedores, funciones, clases, archivos y memoria.

### ⚡ 1. Primer Arranque

Compilar, imprimir y la forma de un programa.

* **[01 - Arranque en Frío](./01%20-%20Arranque%20en%20Fr%C3%ADo.md)** — Qué es C++, dónde corre y la forma de un archivo `.cpp`.
* **[02 - Primera Luz](./02%20-%20Primera%20Luz.md)** — `std::cout`, `#include <iostream>`, las cuatro partes de una sentencia de salida.
* **[03 - El Archivo Esqueleto](./03%20-%20El%20Archivo%20Esqueleto.md)** — `int main()`, llaves, `return 0` y secuencias de escape.
* **[04 - Notas al Margen](./04%20-%20Notas%20al%20Margen.md)** — `//` y `/* */`, y cuándo un comentario esconde un error.
* **[05 - Velocidad de Escape](./05%20-%20Velocidad%20de%20Escape.md)** — Repaso del capítulo 1: arte ASCII que sobrevive al escapado.
* **[06 - De Fuente a Interruptor](./06%20-%20De%20Fuente%20a%20Interruptor.md)** — Fuente, objeto, ejecutable: qué le hace `g++` de verdad a tu archivo.

### 🔢 2. Valores en Bruto

Tipos, declaraciones, aritmética y entrada.

* **[07 - Materia Prima](./07%20-%20Materia%20Prima.md)** — `int`, `double`, `char`, `bool`, `std::string`, y cuánto cuesta cada uno.
* **[08 - Nombrar las Piezas](./08%20-%20Nombrar%20las%20Piezas.md)** — Declarar, inicializar, reglas de nombres y las constantes que no deben moverse.
* **[09 - Entra, Procesa, Sale](./09%20-%20Entra%2C%20Procesa%2C%20Sale.md)** — Entrada, proceso, salida, y asignación frente a comparación.
* **[10 - Números que Mienten](./10%20-%20N%C3%BAmeros%20que%20Mienten.md)** — Aritmética, precedencia, división entera y `%`.
* **[11 - Cámara de Eco](./11%20-%20C%C3%A1mara%20de%20Eco.md)** — Encadenar `<<`, `std::cin` y la dirección de las flechas.
* **[12 - Hablar con la Máquina](./12%20-%20Hablar%20con%20la%20M%C3%A1quina.md)** — `std::getline`, salida con formato y texto que contiene espacios.
* **[13 - Escalado de Niveles](./13%20-%20Escalado%20de%20Niveles.md)** — Repaso del capítulo 2: una fórmula, varios tipos numéricos, una decisión de redondeo.

### 🧠 3. Decisiones

Ramas, comparaciones, aleatoriedad y lógica.

* **[14 - Caminos Bifurcados](./14%20-%20Caminos%20Bifurcados.md)** — `srand` / `rand`, y el error de semilla que hace idénticas todas las ejecuciones.
* **[15 - Puertas y Llaves](./15%20-%20Puertas%20y%20Llaves.md)** — `if` / `else`, llaves que no son opcionales y condiciones booleanas.
* **[16 - Rangos y Umbrales](./16%20-%20Rangos%20y%20Umbrales.md)** — Seis operadores relacionales, `else if` y el orden donde gana la primera coincidencia.
* **[17 - Dados Cargados](./17%20-%20Dados%20Cargados.md)** — Rangos con `rand()`, sesgo del módulo y `%` como herramienta de rango.
* **[18 - Guardias y Portones](./18%20-%20Guardias%20y%20Portones.md)** — `&&`, `||`, `!`, tablas de verdad y evaluación de cortocircuito.
* **[19 - Prueba de Preguntas](./19%20-%20Prueba%20de%20Preguntas.md)** — Repaso del capítulo 3 como un cuestionario puntuado que ramifica por totales.

### 🔁 4. Iteración

`while`, `for`, contar hacia atrás y repetir sin repetirte.

* **[20 - El Bucle que Espera](./20%20-%20El%20Bucle%20que%20Espera.md)** — Qué es iterar, `do ... while` y las cuatro partes de un bucle que termina.
* **[21 - Patrones de Espera](./21%20-%20Patrones%20de%20Espera.md)** — `while`, condiciones que cambian y recortar un valor al bajar.
* **[22 - Tic a Tic](./22%20-%20Tic%20a%20Tic.md)** — `for`: inicialización, condición, incremento y el off-by-one que le sigue.
* **[23 - Protocolo de Cuenta Atrás](./23%20-%20Protocolo%20de%20Cuenta%20Atr%C3%A1s.md)** — Contar hacia atrás, bucles decrementales y contadores con signo frente a sin signo.
* **[24 - La Prueba del Patrón](./24%20-%20La%20Prueba%20del%20Patr%C3%B3n.md)** — Repaso del capítulo 4: reglas que se solapan y se evalúan en orden.

### 📦 5. Colecciones

Vectores, índices, crecimiento, recorrido y arrays.

* **[25 - La Alforja](./25%20-%20La%20Alforja.md)** — `std::vector`, `#include <vector>` y por qué el contenedor gana a las variables paralelas.
* **[26 - Ranura e Índice](./26%20-%20Ranura%20e%20%C3%8Dndice.md)** — Índices desde cero, `v[i]`, `at()` y comportamiento indefinido pasado el final.
* **[27 - Cargar y Descargar](./27%20-%20Cargar%20y%20Descargar.md)** — `push_back`, `pop_back`, `back` y la trampa del contenedor vacío.
* **[28 - Recorrer la Alforja](./28%20-%20Recorrer%20la%20Alforja.md)** — Range-`for` frente a bucles con índice, y qué te ahorra `&`.
* **[29 - El Cómputo del Alquimista](./29%20-%20El%20C%C3%B3mputo%20del%20Alquimista.md)** — Repaso del capítulo 5: suma, cuenta, máximo, media, y la división entera.
* **[30 - Estantes de Piedra y Alforjas](./30%20-%20Estantes%20de%20Piedra%20y%20Alforjas.md)** — Arrays al estilo C junto a vectores: tamaño fijo, decaimiento y el truco de `sizeof`.

### 🧩 6. Funciones

Parámetros, retornos, composición y ámbito.

* **[31 - Un Hechizo, Muchos Usos](./31%20-%20Un%20Hechizo%2C%20Muchos%20Usos.md)** — Por qué existen las funciones: una definición, muchas llamadas, un sitio que cambiar.
* **[32 - El Tablón de la Taberna](./32%20-%20El%20Tabl%C3%B3n%20de%20la%20Taberna.md)** — Parámetros frente a argumentos, `return` y salidas tempranas.
* **[33 - Llenar las Ranuras](./33%20-%20Llenar%20las%20Ranuras.md)** — Argumentos por defecto, valores al final y dónde va el valor por defecto.
* **[34 - Devolver el Botín](./34%20-%20Devolver%20el%20Bot%C3%ADn.md)** — `void`, retornos por valor, referencias y devolver un struct.
* **[35 - Retornos Encadenados](./35%20-%20Retornos%20Encadenados.md)** — Componer funciones y leer una cadena de llamadas de dentro hacia fuera.
* **[36 - El Impuesto del Portal](./36%20-%20El%20Impuesto%20del%20Portal.md)** — Paso por valor frente a paso por referencia, y el coste de una copia.
* **[37 - Dónde Viven los Nombres](./37%20-%20D%C3%B3nde%20Viven%20los%20Nombres.md)** — Ámbito local, global, de bloque, tiempo de vida y ocultamiento.

### 🏛️ 7. Entidades

Structs, clases, constructores, métodos y cabeceras.

* **[38 - Planos del Gremio](./38%20-%20Planos%20del%20Gremio.md)** — Definir un `struct`: un tipo que inventas, y qué dice `sizeof` de él.
* **[39 - Puertas Selladas y Abiertas](./39%20-%20Puertas%20Selladas%20y%20Abiertas.md)** — `public`, `private` y un invariante mantenido dentro del tipo.
* **[40 - La Caja Fuerte de Reliquias](./40%20-%20La%20Caja%20Fuerte%20de%20Reliquias.md)** — Los constructores garantizan un objeto válido desde la primera línea.
* **[41 - La Caja Fuerte, Conectada](./41%20-%20La%20Caja%20Fuerte%2C%20Conectada.md)** — Constructores delegados y el constructor por defecto que debe existir.
* **[42 - Nacer con Atributos](./42%20-%20Nacer%20con%20Atributos.md)** — Funciones miembro, el `this` implícito y encadenar con `*this`.
* **[43 - El Códice de Familiares](./43%20-%20El%20C%C3%B3dice%20de%20Familiares.md)** — Una clase dueña de una colección, con métodos `const` y un contador `static`.
* **[44 - El Códice, Animado](./44%20-%20El%20C%C3%B3dice%2C%20Animado.md)** — Cabecera, implementación y el comando de compilación que las enlaza.

### 🧠 8. Memoria

Pila, montón, punteros, referencias y propiedad.

* **[45 - Dónde Viven las Cosas](./45%20-%20D%C3%B3nde%20Viven%20las%20Cosas.md)** — Pila, montón, almacenamiento estático, y cuál usa tu variable.
* **[46 - La Lente Dirección-De](./46%20-%20La%20Lente%20Direcci%C3%B3n-De.md)** — Punteros: `&`, `*`, `nullptr` y los dos significados de `*`.
* **[47 - Asas a la Memoria](./47%20-%20Asas%20a%20la%20Memoria.md)** — `new`, `delete`, `->` y las tres reglas que traen consigo.
* **[48 - Alcanzar a Través del Asa](./48%20-%20Alcanzar%20a%20Trav%C3%A9s%20del%20Asa.md)** — Punteros como parámetros: el objeto, no una copia, y la comprobación de nulo.
* **[49 - Alias vs Asas](./49%20-%20Alias%20vs%20Asas.md)** — Cuándo una referencia es mejor que un puntero, y la trampa de la reasignación.
* **[50 - El Asa Vacía](./50%20-%20El%20Asa%20Vac%C3%ADa.md)** — Comprobaciones de nulo, punteros colgados y quién posee el objeto.
* **[51 - La Última Brasa](./51%20-%20La%20%C3%9Altima%20Brasa.md)** — Repaso del capítulo 8 y del curso: memoria elegida a propósito.

---

## 🎯 Ruta de Aprendizaje

1. **Primer arranque** → compilar, ejecutar, imprimir, comentar, leer el mensaje de error.
2. **Valores en bruto** → tipos, declaraciones, aritmética, `std::cin`, `getline`.
3. **Decisiones** → `if` / `else if` / `else`, comparaciones, `rand()`, operadores lógicos.
4. **Iteración** → `do ... while`, `while`, `for`, contar hacia atrás, reglas de patrón.
5. **Colecciones** → vectores, índices, crecimiento, recorrido, arrays para tamaños fijos.
6. **Funciones** → parámetros, retornos, valores por defecto, composición, ámbito.
7. **Entidades** → structs, clases, constructores, métodos, cabeceras.
8. **Memoria** → pila y montón, punteros, referencias, propiedad.

---

## 🎯 Qué Sabrás Hacer

- Escribir, compilar y ejecutar programas de C++ desde el terminal, y leer los diagnósticos de `g++`.
- Elegir un tipo a propósito y explicar cuánto cuesta.
- Ramificar e iterar sin errores de off-by-one, y saber por qué un bucle termina.
- Guardar una colección de longitud desconocida en un `std::vector` y recorrerla bien.
- Dividir un programa en funciones con entradas, salidas y tiempos de vida explícitos.
- Modelar una entidad con una clase que sostiene sus propios invariantes.
- Explicar dónde vive un valor y elegir puntero, referencia o valor en consecuencia.

---

## 🧰 Herramientas

| Herramienta | Para qué |
| :--- | :--- |
| `g++` (o `clang++`) | Compila `.cpp` en un binario ejecutable |
| Un terminal | Donde compilas y donde aparece la salida |
| Cualquier editor (se recomienda VS Code) | Escribir, guardar, compilar |
| Obsidian (este vault) | Notas, manuales de campo y ejercicios en un sitio |

```bash
# el ciclo que repite cada lección
g++ -std=c++17 -Wall -Wextra main.cpp -o console
./console
```

---

## 🗺️ Mapa del Curso

| # | Lecciones | Qué aprendes |
| :--- | :--- | :--- |
| 00b / 00c | Manuales de Campo I y II | Todo de un vistazo, para consulta |
| 1 | 01 – 06 | Salida, forma del programa, comentarios, escapado, ciclo de compilación |
| 2 | 07 – 13 | Tipos, declaraciones, aritmética, entrada, texto |
| 3 | 14 – 19 | Ramas, comparaciones, `rand()`, lógica, un cuestionario puntuado |
| 4 | 20 – 24 | `do ... while`, `while`, `for`, cuenta atrás, reglas ordenadas |
| 5 | 25 – 30 | Vectores, indexado, crecimiento, recorrido, arrays |
| 6 | 31 – 37 | Funciones, parámetros, retornos, composición, ámbito |
| 7 | 38 – 44 | Structs, clases, constructores, métodos, archivos de cabecera |
| 8 | 45 – 51 | Pila y montón, punteros, referencias, propiedad |

---

## 🎮 Filosofía de Práctica

C++ no trae red de seguridad: un índice fuera de rango no lanza, un puntero sin inicializar no se
detecta y un bucle infinito simplemente sigue corriendo. Por eso cada lección empareja un concepto con
la trampa concreta que esconde: comportamiento indefinido, división entera, orden de primera
coincidencia, referencias colgadas.

Compila tras cada cambio pequeño y enciende los avisos. Un programa que no compila te dijo algo; uno
que compila y se porta mal en silencio es el que cuesta una tarde.

---

## 🔗 Ver También

- [🐍 MOC de Python](../%F0%9F%90%8D%20Python/README-ES.md) — la rampa más suave hacia la misma lógica.
- [🟣 MOC de C#](../%F0%9F%9F%A3%20CSharp/README-ES.md) — las mismas ideas de objetos con recolección de basura.
- [🖥️ MOC de Línea de Comandos](../%F0%9F%96%A5%EF%B8%8F%20Command%20Line/README-ES.md) — moverse y ejecutar `g++`.
- [🧮 MOC de Estructuras de Datos y Algoritmos](../%F0%9F%A7%AE%20Data%20Structures%20%26%20Algorithms/README-ES.md) — qué estudiar cuando vectores y punteros sean familiares.
- [🌐 MOC de HTML](../%F0%9F%8C%90%20HTML/README-ES.md) · [🎨 MOC de CSS](../%F0%9F%8E%A8%20CSS/README-ES.md) · [🟨 MOC de JavaScript](../%F0%9F%9F%A8%20JavaScript/README-ES.md) · [⚛️ MOC de React](../%E2%9A%9B%EF%B8%8F%20React/README-ES.md) — la pista web, para contrastar.

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="Ola de cierre C++" />
</p>
