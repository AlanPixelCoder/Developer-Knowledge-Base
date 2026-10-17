# 08. HUD Vivo

**Versión original en inglés:** [08 - Living HUD.md](08%20-%20Living%20HUD.md)

**Curso:** JavaScript
**Tema:** El elemento `<script>`, el DOM, métodos de selección, `innerText` / `src` / `.style`, eventos, `addEventListener()` y la Cápstone Generadora de Tarjetas de Botín
**Tags:** `#javascript` `#dom` `#events` `#browser` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-E67E22?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-39_--_44_%2B_Capstone-7C5CFF?style=for-the-badge" alt="Lecciones 39 a 44 más cápstone">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

Todo hasta ahora corrió en la consola — invisible para los jugadores. Este capítulo conecta
el motor a la página. El **DOM** convierte el HTML de [[01 - Inserta la Moneda]] en un árbol
de objetos vivo que JavaScript puede leer y reescribir, y los **eventos** permiten al jugador
tirar de las palancas. Al final construirás la cápstone del módulo: una **Generadora de
Tarjetas de Botín** que acuña una tarjeta aleatoria en cada clic. Referencia:
[[00c - Chuleta de JavaScript II]].

> [!NOTE]
> **Todo el capítulo en una frase**
> El DOM es la página renderizada como un árbol de objetos bajo el `document` global; selecciona
> elementos con `querySelector` / `getElementById`, cámbialos con `innerText`, `src` y
> `.style`, y reacciona al jugador con `addEventListener`.

---

## 01. Luz Verde

### El elemento `<script>`

HTML construye la página, CSS la estiliza — **`<script>`** es la forma en que JavaScript
llega a la página. Puede vivir en `<head>` o cerca del final de `<body>`:

```html
<script src="script.js"></script>
```

Para algo mayor que un fragmento, mantén los scripts en un archivo `.js` separado y enlázalo
con el atributo `src` — exactamente la separación limpia que predica HTML. El navegador carga
el HTML, luego obtiene y ejecuta el script.

---

## 02. El Árbol de Escena

### ¿Qué es el DOM?

El **Document Object Model (DOM)** representa la página como un árbol familiar de nodos y
objetos. La raíz es `<html>`, que se ramifica en `<head>` y `<body>`, cada uno con atributos,
elementos hijos y nodos de texto.

Cada etiqueta que escribiste en el curso de HTML es ahora un **objeto** en memoria — con
propiedades que JavaScript puede leer y escribir. El puente entre los dos lenguajes es el
objeto global `document`.

### Seleccionar Elementos

| Método | Devuelve | Úsalo para |
| :--- | :--- | :--- |
| `document.querySelector("css")` | Primer coincidente | Un elemento, cualquier selector |
| `document.getElementById("id")` | Un elemento | Un id único conocido |
| `document.getElementsByClassName("cls")` | Colección | Cada elemento con una clase |

`querySelector` acepta cualquier selector CSS del curso de estilo — etiqueta, `.class` o
`#id`:

```js
document.querySelector("p");
document.querySelector(".card");
document.querySelector("#health-bar");
```

### Leer y Escribir Texto

La propiedad `.innerText` lee o reemplaza el **texto renderizado** dentro de un elemento:

```js
document.querySelector("#health-bar").innerText = "HP: 85 / 100";
```

`.innerHTML` hace lo mismo con el HTML crudo de adentro — útil cuando el reemplazo es marcado,
peligroso cuando la entrada es texto de usuario. `.src` cambia la fuente de un `<img>`, el
truco clásico de cambio de sprite:

```js
document.querySelector("img").src = "smiley2.png";
```

---

## 03. Anillo de Ánimo

### Cambiar Estilos con `.style`

Cada elemento seleccionado lleva una propiedad `.style` para su CSS en línea. Dos reglas:

- Las propiedades CSS de varias palabras se convierten en **camelCase** en el DOM:
  `background-color` → `backgroundColor`, `font-size` → `fontSize`, `text-align` → `textAlign`.
- Los valores son **strings** — comillas obligatorias.

### Misión: Ánimo de la Hoguera

Una piedra que cambia de color con el ánimo del motor — el anillo de ánimo de un campamento
de mazmorra:

```js
let stone = document.getElementById("stone");
let randomNumber = Math.floor(Math.random() * 9) + 1;

if (randomNumber === 1) {
  stone.style.backgroundColor = "red";
} else if (randomNumber === 2) {
  stone.style.backgroundColor = "orange";
} else {
  stone.style.backgroundColor = "black";
}
```

Cada pieza del capítulo hasta aquí, junto: una selección de DOM, `Math.random()` de
[[03 - Tiradas de Botín]] y una cadena `else if` escribiendo una propiedad de estilo en camelCase.

---

## 04. El Jugador Tira de la Palanca

### Eventos y Event Listeners

Un **evento** es cualquier cosa que el jugador hace en la página: un clic, un hover, un envío
de formulario, una tecla. `addEventListener()` adjunta una función a un elemento y **espera** —
nada corre hasta que la acción realmente ocurre:

```js
element.addEventListener("click", function () {
  // runs on every click
});
```

### Misión: Botón de Poción de Vida

La interacción más honesta del HUD — una poción que cura, una pulsación a la vez:

```js
let useButton = document.getElementById("use-button");
let hpDisplay = document.getElementById("hp-display");

let currentHP = 100;

useButton.addEventListener("click", function () {
  currentHP = currentHP + 25;
  if (currentHP > 100) {
    currentHP = 100;
  }
  hpDisplay.innerText = "HP: " + currentHP + " / 100";
});
```

Mira el flujo: la función se **define** al cargar y se **llama** después, una vez por clic —
una función de [[06 - Funciones de Habilidad]] viviendo dentro de un evento de este capítulo.

---

## 05. La Cápstone

### Checkpoint: Resumen del capítulo

- `<script src="script.js">` enlaza JavaScript con HTML — usualmente al final de `<body>`.
- El DOM es la página como árbol de objetos; `document` es su raíz global.
- `querySelector` (cualquier selector CSS), `getElementById`, `getElementsByClassName` seleccionan.
- `.innerText`, `.innerHTML` y `.src` reescriben contenido; `.style.camelCase` reescribe la apariencia.
- `addEventListener("click", fn)` espera al jugador y ejecuta `fn` en cada disparo.

### Proyecto: Generadora de Tarjetas de Botín

El jefe final del módulo. Dos arreglos de [[05 - Inventario]] — arte y texto de sabor — un
índice aleatorio a cada uno y un manejador de clic que acuña una tarjeta fresca en cada
pulsación. El truco de fiesta más antiguo de Internet, con ropaje de juego:

```js
const cardArt = [
  "https://placehold.co/300x200/ff6b35/white?text=Ember+Shard",
  "https://placehold.co/300x200/7c5cff/white?text=Lantern+Oil",
  "https://placehold.co/300x200/00c2a8/white?text=Ash+Blade",
  "https://placehold.co/300x200/f7df1e/black?text=Ember+Key"
];

const cardFlavor = [
  "When your damage formula compiles on the first try with zero null references",
  "Me explaining 2D pixel RPG tactical damage formulas at 2 AM",
  "When the boss has 1 HP left and your 95% hit-rate attack misses",
  "Fixing one bug in the engine only to spawn three new boss fights in the console",
  "When the melodic boss theme drops right as you enter flow state"
];

let cardImage = document.getElementById("card-image");
let cardText = document.getElementById("card-text");
let forgeButton = document.getElementById("forge-button");

forgeButton.addEventListener("click", function () {
  let artIndex = Math.floor(Math.random() * cardArt.length);
  let textIndex = Math.floor(Math.random() * cardFlavor.length);

  cardImage.src = cardArt[artIndex];
  cardText.innerText = cardFlavor[textIndex];
});
```

El lado HTML es un `<img>`, un `<p>` y un `<button>` — estructura del curso de HTML, estilo
del curso de CSS, y todo lo que lo mantiene **vivo** de este módulo. Tres lenguajes, una
página, un botón.

> [!TIP]
> **Hacia dónde va esto**
> Toda interfaz de juego real es este archivo ampliado: una barra de vida que escucha, una
> rejilla de inventario que se vuelve a dibujar al cambiar, un menú de ajustes de deslizadores.
> El vocabulario nunca crece más allá de seleccionar, leer, escribir, escuchar — solo crece el
> número de elementos.

---

## ⚡ XP Ganados: Ideas Clave

- 🔌 `<script src="...">` es el puente de HTML a JavaScript.
- 🌳 El DOM es la página como árbol de objetos; `document` es la raíz.
- 🎯 Selecciona: `querySelector` (cualquier selector CSS), `getElementById`, `getElementsByClassName`.
- ✍️ Escribe: `.innerText` para texto, `.src` para imágenes, `.style.backgroundColor` para CSS (¡camelCase!).
- 🖱️ `addEventListener("click", fn)` espera al jugador; `fn` corre en cada disparo.
- 🃏 La cápstone: arreglos + aleatoriedad + selección + eventos = una generadora funcional.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- ❤️ HUDs en vivo: vida, maná, enfriamientos, contadores de puntuación
- 🎰 Tiradas gacha, generadores de tarjetas, aleatorizadores de todo tipo
- 🧪 Demostraciones con clic y tutoriales interactivos
- 🌗 Cambiadores de tema — un cambio de clase y toda la página cambia
- 📱 La web móvil entera: taps adentro, DOM afuera

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Conecta un botón que cambie el texto de un `<h1>` al título de tu juego al hacer clic.
2. Haz un segundo botón que cambie `document.body.style.backgroundColor`.
3. Construye una antorcha de dos estados: un botón alterna `src` entre imágenes de prendida y apagada.
4. Imprime un nombre de NPC aleatorio de un arreglo en un párrafo en cada clic.
5. **Pelea de jefe:** un *simulador de daño* — un botón "Hit", una variable `currentHP`, una
   tirada de daño aleatoria por clic y un estado de `game over` que desactiva el botón a
   `0` de vida (`button.disabled = true`).

---

## 🔗 Ver También

- [[00c - Chuleta de JavaScript II]] — DOM, estilos y eventos en una página
- [[07 - Ficha de Personaje]] — capítulo anterior: objetos — el DOM es uno gigante
- [[01 - Inserta la Moneda]] — el marcado que este capítulo da vida
- [[12 - Flexbox]] — maquetando la página que este script manipula

---
