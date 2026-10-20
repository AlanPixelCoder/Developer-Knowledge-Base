# 🟨 JavaScript: El Lenguaje de la Web (MOC)

**English:** [README.md](./README.md)

<p align="left">
  <img src="https://img.shields.io/badge/Lenguaje-JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE_A_INTERMEDIO-6CC24A?style=for-the-badge" alt="De principiante a intermedio">
  <img src="https://img.shields.io/badge/Cap%C3%ADtulos-8-7C5CFF?style=for-the-badge" alt="8 capítulos">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
  <img src="https://img.shields.io/badge/Entorno-macOS-lightgrey?style=for-the-badge&logo=apple&logoColor=white" alt="macOS">
</p>

**Nota:**
Este módulo es el Mapa de Contenidos (MOC) de las notas de JavaScript de este vault de
Obsidian. JavaScript es el lenguaje que hace que las páginas web *hagan* cosas — desde
imprimir en la consola y guardar datos en variables, pasando por condicionales, bucles,
arreglos, funciones y objetos, hasta un DOM vivo que escucha al jugador. Todos los ejemplos
son mínimos y ejecutables tal cual: pégalos en la consola del navegador o en un archivo
`.js` y funcionan.

**Consejo:**
Empieza por [[01 - Inserta la Moneda]]. Aprende a imprimir y guardar valores antes de aprender
a buclar y a agruparlos — cuando las variables y los tipos sean memoria muscular, todo lo demás
de este módulo es composición.

**Requisito previo:** [MOC de 🌐 HTML](../%F0%9F%8C%90%20HTML/README-ES.md). El capítulo
[[08 - HUD Vivo]] reescribe páginas construidas con el curso de HTML, así que el vocabulario
de estructura ya debería serle familiar. El [MOC de 🎨 CSS](../%F0%9F%8E%A8%20CSS/README-ES.md)
ayuda pero no es obligatorio.

> [!NOTE]
> **La narrativa de Emberfall**
> Todos los ejercicios de este módulo pertenecen al mismo proyecto ficticio: *Emberfall*, un
> roguelike. El recibo de la tienda se vuelve un log de consola, el daño por caída se vuelve
> aritmética, el dado de mazmorra se vuelve `Math.random()`, el inventario se vuelve un
> arreglo, la ficha de personaje se vuelve un objeto y el HUD se vuelve el DOM. La sintaxis no
> cambia en absoluto — y ese es el punto: aprendes un solo vocabulario y lo reutilizas en
> todas partes.

---

## 🗺️ Mapa de Contenidos

### 📚 Referencia y Chuletas

* **Chuletas:**
  * [00b - Chuleta de JavaScript](./00b%20-%20Chuleta%20de%20JavaScript.md) — Consola, variables, tipos, operadores, condicionales, bucles, arreglos, funciones y objetos.
  * [00c - Chuleta de JavaScript II](./00c%20-%20Chuleta%20de%20JavaScript%20II.md) — `<script>`, el DOM, selección, escritura de contenido y estilos, eventos y `addEventListener`.

### 🖥️ 1. Inserta la Moneda (Capítulo 1)

* **Inserta la Moneda:** [01 - Inserta la Moneda](./01%20-%20Inserta%20la%20Moneda.md) — `console.log`, comentarios, tus primeros programas y el proyecto del recibo de tienda.

### 📦 2. Atributos del Jugador (Capítulo 2)

* **Atributos del Jugador:** [02 - Atributos del Jugador](./02%20-%20Atributos%20del%20Jugador.md) — `let` / `const`, los siete tipos, aritmética, exponentes y el calculador de daño por caída.

### 🎲 3. Tiradas de Botín (Capítulo 3)

* **Tiradas de Botín:** [03 - Tiradas de Botín](./03%20-%20Tiradas%20de%20Bot%C3%ADn.md) — Condicionales, comparaciones, operadores lógicos, `Math.random()` y el dado de mazmorra.

### 🌾 4. El Farmeo (Capítulo 4)

* **El Farmeo:** [04 - El Farmeo](./04%20-%20El%20Farmeo.md) — Bucles `while` y `for`, `break` / `continue`, bucles anidados, el pase de temporada y el año bisiesto.

### 🎒 5. Inventario (Capítulo 5)

* **Inventario:** [05 - Inventario](./05%20-%20Inventario.md) — Arreglos, índices, longitud, métodos de mutación, `indexOf` / `includes` y la semilla de mazmorra.

### ⚙️ 6. Funciones de Habilidad (Capítulo 6)

* **Funciones de Habilidad:** [06 - Funciones de Habilidad](./06%20-%20Funciones%20de%20Habilidad.md) — Funciones, parámetros, `return`, ámbito, funciones flecha, el analizador de registro de combate y el verificador de palíndromos.

### 🗂️ 7. Ficha de Personaje (Capítulo 7)

* **Ficha de Personaje:** [07 - Ficha de Personaje](./07%20-%20Ficha%20de%20Personaje.md) — Objetos, propiedades, notación con punto, métodos, `this` y el proyecto Pase de Gremio.

### 🖱️ 8. HUD Vivo (Capítulo 8)

* **HUD Vivo:** [08 - HUD Vivo](./08%20-%20HUD%20Vivo.md) — `<script>`, el DOM, métodos de selección, `innerText` / `src` / `.style`, eventos, `addEventListener()` y la Cápstone Generadora de Tarjetas de Botín.

---

## 🧭 Ruta de Aprendizaje

1. **Inserta la Moneda** → habla con la máquina: imprime valores y documenta tu código.
2. **Atributos del Jugador** → guarda datos: declara variables y reconoce cada tipo.
3. **Tiradas de Botín** → decide: condicionales, comparaciones y aleatoriedad.
4. **El Farmeo** → repite trabajo: las dos formas de bucle y cómo salir de ellas.
5. **Inventario** → guarda muchos: arreglos y los métodos que los remodelan.
6. **Funciones de Habilidad** → nombra el trabajo: parámetros, `return`, ámbito y el atajo flecha.
7. **Ficha de Personaje** → guarda significado: objetos, métodos y `this`.
8. **HUD Vivo** → encuentra al jugador: el DOM, los estilos y los event listeners.

---

## 🎯 Lo que serás capaz de hacer

- Imprimir en la consola y leer errores como un mapa.
- Declarar con `const` por defecto, `let` cuando los valores cambian, y nombrar tipos a la vista.
- Calcular con aritmética, comparación y lógica — incluidas tiradas con `Math.random()`.
- Dirigir decisiones con `if / else if / else`, el ternario y `switch`.
- Repetir con `while`, `for` y `for...of`, usando `break` y `continue` a propósito.
- Guardar datos ordenados en arreglos y remodelarlos con los métodos estándar.
- Escribir funciones con parámetros y `return`, y elegir la sintaxis flecha cuando encaje.
- Modelar cosas como objetos con propiedades y métodos, y leer `this` dentro de ellos.
- Seleccionar y reescribir la página viva con el DOM, y reaccionar a clics con `addEventListener`.

---

## 🧰 Herramientas

| Herramienta | Para qué |
| :--- | :--- |
| Cualquier editor de código (recomendado VS Code) | Escribir y guardar archivos `.js` y `.html` |
| Un navegador moderno con DevTools | Ejecutar scripts, abrir la consola, inspeccionar el DOM en vivo |
| Obsidian (este vault) | Guardar notas, chuletas y ejercicios en un solo sitio |

---

## 🗺️ Mapa del Curso

| # | Nota | Lecciones | Qué aprenderás |
| --- | --- | --- | --- |
| 00b | [00b - Chuleta de JavaScript](./00b%20-%20Chuleta%20de%20JavaScript.md) | — | Consola, tipos, operadores, control de flujo, arreglos, funciones, objetos |
| 00c | [00c - Chuleta de JavaScript II](./00c%20-%20Chuleta%20de%20JavaScript%20II.md) | — | `<script>`, DOM, estilos, eventos, `addEventListener` |
| 01 | [01 - Inserta la Moneda](./01%20-%20Inserta%20la%20Moneda.md) | 01–05 | `console.log`, comentarios, primeros programas, recibo de tienda |
| 02 | [02 - Atributos del Jugador](./02%20-%20Atributos%20del%20Jugador.md) | 06–11 | `let`/`const`, tipos, aritmética, exponentes, daño por caída |
| 03 | [03 - Tiradas de Botín](./03%20-%20Tiradas%20de%20Bot%C3%ADn.md) | 12–16 | Condicionales, comparaciones, lógica, `Math.random()`, dado de mazmorra |
| 04 | [04 - El Farmeo](./04%20-%20El%20Farmeo.md) | 17–22 | `while`, `for`, `break`/`continue`, bucles anidados, pase de temporada |
| 05 | [05 - Inventario](./05%20-%20Inventario.md) | 23–27 | Arreglos, índices, longitud, métodos, semilla de mazmorra |
| 06 | [06 - Funciones de Habilidad](./06%20-%20Funciones%20de%20Habilidad.md) | 28–33 | Funciones, parámetros, `return`, ámbito, funciones flecha |
| 07 | [07 - Ficha de Personaje](./07%20-%20Ficha%20de%20Personaje.md) | 34–38 | Objetos, propiedades, métodos, `this`, Pase de Gremio |
| 08 | [08 - HUD Vivo](./08%20-%20HUD%20Vivo.md) | 39–44 | `<script>`, DOM, `.style`, eventos, `addEventListener`, cápstone |

---

## 🎮 Filosofía de práctica

El código es una máquina que se construye escribiendo. Los ejercicios siguen ese principio:
cada fragmento corre tal cual — los comentarios indican la salida que deberías obtener
realmente. Si algo no se ve bien, abre las DevTools y compara el resultado real con el
esperado, línea a línea.

Cada capítulo termina con un proyecto que es el capítulo entero en un archivo — el recibo de
tienda, el dado de mazmorra, el pase de temporada, el analizador de registro de combate, el
Pase de Gremio, la generadora de tarjetas de botín — de modo que nada se quede como dato
aislado.

---

## 🔗 Ver también

- [MOC de 🌐 HTML](../%F0%9F%8C%90%20HTML/README-ES.md) — la estructura que este módulo da vida; requisito previo
- [MOC de 🎨 CSS](../%F0%9F%8E%A8%20CSS/README-ES.md) — la mitad de estilos de las mismas páginas
- [MOC de ⚛️ React](../%E2%9A%9B%EF%B8%8F%20React/README-ES.md) — la capa de componentes que se apoya en este módulo, HTML y CSS
- [MOC de 🟣 CSharp](../%F0%9F%9F%A3%20CSharp/README-ES.md) — el equivalente de tipado fuerte, con el mismo enfoque primero-juego

---
