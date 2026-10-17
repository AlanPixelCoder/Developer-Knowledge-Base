# 01. Inserta la Moneda

**Versión original en inglés:** [01 - Insert Coin.md](01%20-%20Insert%20Coin.md)

**Curso:** JavaScript
**Tema:** Qué es JavaScript, la consola Web, `console.log()`, ejecución línea por línea, comentarios y el proyecto Recibo del Mercader
**Tags:** `#javascript` `#web-development` `#basics` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Lecciones-01_--_05_%2B_Proyecto-7C5CFF?style=for-the-badge" alt="Lecciones 01 a 05 más proyecto">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

El primer capítulo del lenguaje que impulsa aproximadamente el **97.5% de los sitios web
de Internet** — incluida cada página del sitio companion de Emberfall. Al terminarlo sabrás
cómo ejecutar JavaScript en la consola del navegador, imprimir mensajes y dejar comentarios,
y habrás construido tu primer programa: el **recibo de un mercader** impreso línea por línea
en la terminal. La referencia rápida de todo el capítulo está en
[[00b - Chuleta de JavaScript]].

> [!NOTE]
> **Todo el capítulo en una frase**
> HTML etiqueta contenido y CSS lo estiliza; JavaScript es el primer lenguaje de esta vault
> que de verdad **se ejecuta** — escribes instrucciones, el motor las ejecuta en orden, y
> lo que hagan depende de ti.

---

## 01. La Sala del Motor

> [!NOTE]
> **Información clave**
> **JavaScript** fue creado por **Brendan Eich** en Netscape en **1995** — legendariamente,
> en unos diez días, al amanecer de la era punto com. Hoy es el único lenguaje que se ejecuta
> de forma nativa en todos los navegadores, y alimenta alrededor del 97.5% de todos los sitios web.

JavaScript es un **lenguaje de programación**: a diferencia de HTML, no etiqueta contenido —
**instruye** a la máquina. Esas instrucciones pueden imprimir mensajes, reaccionar a clics,
tirar dados de daño o mover un bucle de juego completo.

### Las tres tecnologías principales de la web

| Tecnología | Rol | En el sitio de Emberfall |
| :--- | :--- | :--- |
| **HTML** | Crea la **estructura** de una página web | El esqueleto: qué paneles tiene el HUD |
| **CSS** | Da **estilo** a la página | La piel: colores, tipografías, maquetación |
| **JavaScript** | La hace **interactiva** | El motor: barras de vida que se actualizan |

Este curso se centra en JavaScript. Los archivos que crearemos usan la extensión **`.js`** —
pero durante los primeros capítulos ni siquiera necesitaremos un archivo: todo se ejecuta en
la consola del navegador.

### Misión: Primer Arranque

Toda consola de juego arranca con una prueba. Abre la Consola Web (más abajo) y ejecuta:

```js
console.log("Emberfall engine v1.0 online");
```

La consola imprime `Emberfall engine v1.0 online`. Acabas de ejecutar tu primera línea de
JavaScript — el motor está vivo.

---

## 02. La Consola

### ¿Qué es la Consola Web?

La **Consola Web** es una función integrada del navegador para ejecutar código JavaScript y
ver los mensajes de salida. Es la terminal del mundo web, y viene pegada a cada página que
visitas.

### Abrir la consola

| Navegador | Ruta | Atajo de Teclado |
| :--- | :--- | :--- |
| **Google Chrome** | Ver > Desarrollador > Consola de JavaScript | `cmd` + `option` + `c` (macOS) |
| **Apple Safari** | Desarrollar > Mostrar Consola de JavaScript | `option` + `cmd` + `c` |
| **Mozilla Firefox** | Herramientas > Herramientas del desarrollador > Web Developer Tools | `ctrl` + `shift` + `i` (Windows/Linux) |

> [!TIP]
> En Chrome la pestaña Consola está entre **Elements** y **Sources**; en Firefox, entre
> **Inspector** y **Debugger**. El atajo `cmd` + `option` + `c` funciona en los tres y
> vale la pena memorizarlo — abrirás la consola decenas de veces al día.

### `console.log()`

`console.log()` le pide a la consola imprimir un mensaje. El mensaje va entre paréntesis
`()` y entre comillas — dobles `"..."` o simples `'...'`, siempre que la comilla de apertura
y la de cierre **coincidan**:

```js
console.log("Lantern oil: low");
console.log('Ember Shard in inventory');
```

Ambas líneas imprimen su texto tal cual.

> [!NOTE]
> Un punto y coma `;` al final de una sentencia en JavaScript es **opcional**. Esta vault
> los escribe, porque la mayoría de las guías de estilo lo hacen — pero el motor no se
> quejará si los omites.

> [!WARNING]
> **El error que todos cometen una vez**
> Las comillas deben coincidir. `"Emberfall'` es un **SyntaxError**: el motor lee la cadena
> desde la primera `"` y sigue buscando la `"` de cierre hasta rendirse. Lo mismo vale para
> paréntesis y llaves — una llave sin cerrar se traga todo lo que hay después.

---

## 03. Línea por Línea

### Ejecución secuencial

JavaScript ejecuta código **secuencialmente**: una línea a la vez, de arriba abajo. No hay
misterio ni saltos — la línea 2 espera a la línea 1, la línea 3 espera a la línea 2.

Varias llamadas a `console.log()` se imprimen en el orden en que aparecen:

```js
console.log("Entering the Deep Halls...");
console.log("Torch equipped");
console.log("Something moves in the dark...");
// Output:
// Entering the Deep Halls...
// Torch equipped
// Something moves in the dark...
```

### Misión: Bandera de Señal

El arte ASCII solo funciona si cada línea se imprime exactamente donde debe. Recrea este
banner con un `console.log()` por línea:

```js
console.log("    a");
console.log("  b c");
console.log(" d e f");
console.log("g h i j");
console.log("   k");
```

Sustituye las letras por la primera letra del título de tu propio juego y comprueba que la
forma se mantiene. Si una línea falla, el motor imprimió algo distinto de lo que esperabas —
así empieza exactamente el depurado.

---

## 04. Receta Secreta

### Comentarios

Los **comentarios** son notas escritas para humanos. El motor los **ignora por completo** —
nunca se ejecutan, nunca imprimen, nunca rompen nada. Documentan qué hace el código, o
aparcan código con el que aún no quieres despedirte.

### Comentarios de una línea

Dos barras inclinadas `//` comentan el resto de la línea:

```js
// console.log("This never runs");
console.log("Only this prints"); // esta nota final también se ignora
```

### Comentarios de varias líneas

`/*` abre un comentario y `*/` lo cierra. Todo lo que hay entre ellos está muerto para el
motor, sin importar cuántas líneas dure:

```js
/*
  Emberfall crafting notes:
  1 Ember Shard + 2 Ash Mushrooms = one Lantern Charge.
  Drop rates documented in the design doc, section 4.
*/
console.log("Recipe loaded");
```

> [!TIP]
> Los comentarios son el lugar más fácil para dejar atrás una mentira. `// fix before
> launch` sobrevive años. Escribe comentarios que sigan siendo ciertos, o bórralos.

---

## 05. Recibo del Mercader

### Checkpoint: Resumen del capítulo

- `console.log()` imprime mensajes en la consola.
- JavaScript ejecuta **línea por línea**, de arriba abajo.
- Los comentarios de una línea usan `//`; los de varias líneas usan `/* ... */`.
- Las cadenas necesitan comillas que **coincidan**; los punto y coma son opcionales pero recomendados.

### Proyecto: Recibo del Mercader

Llega el primer programa. Usando nada más que `console.log()`, imprime el recibo de una
compra de suministros en el puesto de Emberfall — nombre de la tienda, un bloque de
**Order Details** con las columnas **Item**, **Quantity** y **Price**, al menos dos artículos
y un total:

```js
console.log("================================");
console.log("    EMBERFALL OUTPOST SUPPLY    ");
console.log("================================");
console.log("          Order Details         ");
console.log("--------------------------------");
console.log("Item        Quantity    Price");
console.log("--------------------------------");
console.log("Torch         2        4.50");
console.log("Rope          1        3.25");
console.log("Lantern Oil   1        6.00");
console.log("--------------------------------");
console.log("Total                  18.25");
console.log("================================");
```

Cuenta las líneas: el recibo no es más que una secuencia de impresiones, pero la alineación
la haces **tú** espaciando las cadenas a mano. Esa es toda la habilidad de este capítulo:
precisión en lo que recibe el motor.

> [!TIP]
> **Versión para game dev**
> Esta es la forma de cualquier superposición de depuración jamás escrita. La lectura de la
> barra de vida en el HUD de desarrollo de un motor, el volcado de la tabla de botín, el log
> del servidor — todo es `console.log()` disfrazado. El capítulo [[03 - Tiradas de Botín]]
> enseña al motor a calcular los números que ahora estás tecleando a mano.

---

## 💎 Bonus Loot: la Consola es un Intérprete Completo

La consola no es solo una ventana de salida — es un intérprete JavaScript completo. Algunos
poderes que conviene conocer ya:

### Evalúa lo que sea

La aritmética y la concatenación de cadenas funcionan directamente en la consola:

```js
console.log(42 * 3);              // 126
console.log("Ember " + "Fall");   // Ember Fall
```

### Guarda valores en variables

Los resultados pueden guardarse en variables con `let` o `const` — el tratamiento completo
está en [[02 - Atributos del Jugador]]:

```js
let followers = 1000000;
```

### Autocompletado

Escribir `document` seguido de un punto `.` abre una lista de todos los métodos y propiedades
disponibles. La consola te enseña la API mientras escribes — úsala.

### Modo multilínea

Todos los navegadores modernos admiten escribir programas multilínea completos: pega un bloque
entero, o usa la entrada multilínea de la consola, y ejecútalo como un solo programa.

---

## ⚡ XP Ganados: Ideas Clave

- 🟨 **JavaScript se ejecuta.** Es el primer lenguaje de la vault que la máquina ejecuta de verdad.
- 🖥️ La **Consola Web** es la terminal del navegador; `cmd` + `option` + `c` la abre.
- 📢 `console.log("message")` imprime — las comillas deben **coincidir**, los punto y coma son opcionales.
- 📜 La ejecución es **línea por línea**, de arriba abajo. Sin excepciones a este nivel.
- 💬 `//` comenta una línea; `/* ... */` comenta un bloque.
- 🧾 Un recibo no es más que muchos `console.log()`, alineados a mano.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🐛 Depuración: imprime el valor de lo que sea, en cualquier punto, mientras se ejecuta
- 🧪 Probar fragmentos antes de llevarlos a un archivo
- 📊 Logs del lado del servidor — `console.log()` también se ejecuta en Node.js
- 🎮 Superposiciones de depuración, volcados de botín y lecturas de stats en herramientas de juego
- 📝 Cálculos rápidos sin salir del navegador

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Imprime el título de tu juego como banner ASCII, un `console.log()` por línea.
2. Imprime el recibo de un pedido al herrero del juego con al menos tres artículos.
3. Imprime una lista de "patch notes" de cinco líneas usando solo `console.log()`.
4. Escribe un comentario que desactive un `console.log()`, ejecuta el archivo y confirma que guarda silencio.
5. **Pelea de jefe:** imprime un recibo a todo el ancho de la pantalla — nombre, línea de
   dirección, tres artículos, línea de impuestos, total — con cada columna alineada usando
   solo espacios dentro de las cadenas.

---

## 🔗 Ver También

- [[00b - Chuleta de JavaScript]] — todas las sentencias de este capítulo en una página
- [[02 - Atributos del Jugador]] — siguiente capítulo: variables, tipos de datos y matemáticas de daño
- [[03 - Tiradas de Botín]] — condicionales: enseñar al motor a tomar decisiones
- [[08 - HUD Vivo]] — donde `console.log` crece y se convierte en una interfaz real

---
