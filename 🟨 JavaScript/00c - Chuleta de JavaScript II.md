# 00c. Chuleta de JavaScript II

**Versión original en inglés:** [00c - JavaScript Cheatsheet II.md](00c%20-%20JavaScript%20Cheatsheet%20II.md)

**Curso:** JavaScript
**Tema:** Referencia rápida de la mitad de navegador: `<script>`, el DOM, selección, escritura de contenido y estilos, eventos y `addEventListener`
**Tags:** `#javascript` `#dom` `#events` `#cheatsheet` `#reference` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-E67E22?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Cubre-Cap%C3%ADtulo_08-7C5CFF?style=for-the-badge" alt="Capítulo 08">
  <img src="https://img.shields.io/badge/Tipo-Chuleta-00C2A8?style=for-the-badge" alt="Chuleta">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

La mitad de navegador del módulo en una página. Todo lo de aquí se introdujo en
[[08 - HUD Vivo]] — nada de esta chuleta es nuevo. El lenguaje base — variables, tipos,
operadores, bucles, arreglos, funciones y objetos — vive en
[[00b - Chuleta de JavaScript]].

> [!TIP]
> El DOM nunca es más complicado de lo que sugiere esta chuleta: **seleccionar, leer,
> escribir, escuchar**. Los proyectos reales solo multiplican el número de elementos, no el
> número de ideas.

**El hilo conductor de este módulo: Emberfall**, un roguelike de mazmorra. Esta chuleta es
la instalación eléctrica detrás de su compañera web: la barra de vida, la piedra de ánimo, el
botón de poción, la generadora de tarjetas de botín.

---

## 🔌 Cargar JavaScript

```html
<!-- Al final de <body> — después del marcado que toca -->
<script src="script.js"></script>
```

| Ubicación | Nota |
| :--- | :--- |
| Final de `<body>` | El por defecto — los elementos existen antes de que corra el script |
| En `<head>` | Solo con `defer`, o aún no existen los elementos |
| `<script>...</script>` en línea | Vale para demos pequeñas; guarda el código real en archivos `.js` |

---

## 🌳 El DOM en Una Tabla

El **DOM** (Document Object Model) es la página renderizada como un árbol de objetos. El
`document` global es su raíz; cada etiqueta es un objeto bajo ella.

| Método | Devuelve | Recúrrelo cuando |
| :--- | :--- | :--- |
| `document.querySelector("css")` | Primer elemento coincidente | Conoces un selector CSS |
| `document.getElementById("id")` | Un elemento por id | El elemento tiene un `id` único |
| `document.getElementsByClassName("cls")` | Colección de coincidencias | Necesitas **todos** los elementos con una clase |
| `document.body` | El elemento `<body>` | Para estilizar o agregar a toda la página |

`querySelector` acepta cualquier selector CSS del curso de estilo: `"p"`, `".card"`,
`"#health-bar"`.

---

## ✍️ Escribir en la Página

| Propiedad | Escribe | Nota |
| :--- | :--- | :--- |
| `.innerText` | Texto renderizado | La opción segura por defecto — no interpreta marcado |
| `.innerHTML` | HTML crudo | Potente, y un agujero si la entrada es texto de usuario |
| `.src` | Fuente de la imagen | El truco del cambio de sprite: `img.src = "lit.png"` |
| `.disabled` | Estado del botón | `true` silencia el botón — pantallas de fin de partida |
| `.className` | Reemplaza todas las clases | Sobrescribe todas las clases del elemento |
| `.classList.add("x")` | Agrega una clase | Conserva las demás — el hábito moderno |

```js
const hpBar = document.querySelector("#health-bar");
hpBar.innerText = "HP: 85 / 100";
document.querySelector("img").src = "smiley2.png";
```

---

## 🎨 Escribir Estilos

Cada elemento seleccionado lleva `.style` para su CSS en línea. Dos reglas:

- Las propiedades de varias palabras se convierten en **camelCase**: `background-color` →
  `backgroundColor`, `font-size` → `fontSize`, `text-align` → `textAlign`.
- Los valores son **strings** — comillas obligatorias.

```js
element.style.backgroundColor = "red";
element.style.fontSize = "24px";
element.style.textAlign = "center";
```

---

## 🖱️ Eventos

Un **evento** es cualquier cosa que el jugador hace: clic, hover, tecla, envío.
`addEventListener` adjunta una función y **espera** — corre una vez por disparo.

```js
button.addEventListener("click", function () {
  // runs on every click
});
```

| Evento | Se dispara cuando |
| :--- | :--- |
| `"click"` | Se hace clic en el elemento — botones, tarjetas, la propia página |
| `"mouseover"` | El puntero entra al elemento |
| `"keydown"` | Se pulsa una tecla — el manejador de entrada clásico |
| `"submit"` | Se envía un formulario |

```js
let hp = 100;
const useButton = document.getElementById("use-button");

useButton.addEventListener("click", function () {
  hp = hp + 25;
  if (hp > 100) {
    hp = 100;
  }
  document.querySelector("#hp-display").innerText = "HP: " + hp + " / 100";
});
```

---

## ⚠️ Trampas que Conviene Memorizar

| Trampa | Qué pasa de verdad |
| :--- | :--- |
| Script en `<head>` sin `defer` | El script corre antes de que existan los elementos; `querySelector` devuelve `null` |
| `.style.background` con guion | Error de sintaxis — las propiedades del DOM son camelCase |
| Olvidar comillas en valores de estilo | `style.fontSize = 24px` lanza error; debe ser `"24px"` |
| `.innerHTML` con entrada de usuario | Inyecta marcado — incluido lo-hostil; prefiere `.innerText` |
| Listener dentro de un bucle con `var` | Todas las iteraciones comparten una variable; `let` da una por vuelta |
| Esperar que `.style` lea reglas CSS | Solo refleja estilos **en línea** — los computados necesitan `getComputedStyle` |
| Seleccionar antes de que exista el DOM | `null` — el elemento aún no está en el árbol; revisa la ubicación de tu script |

---

## 🎮 La Versión de Una Página

Todo lo de esta chuleta en un solo archivo — un widget de campamento de Emberfall:

```html
<!DOCTYPE html>
<html>
  <body>
    <h1 id="status">HP: 100 / 100</h1>
    <button id="use-button">Use Potion 🧪</button>

    <script>
      let hp = 100;
      const useButton = document.getElementById("use-button");
      const status = document.getElementById("status");

      useButton.addEventListener("click", function () {
        hp = hp + 25;
        if (hp > 100) {
          hp = 100;
          status.style.backgroundColor = "green";
        }
        status.innerText = "HP: " + hp + " / 100";
      });
    </script>
  </body>
</html>
```

---

## 🔗 Ver También

- [[00b - Chuleta de JavaScript]] — la mitad de lenguaje base: variables, bucles, arreglos, funciones, objetos
- [[08 - HUD Vivo]] — donde se introduce cada sentencia de esta chuleta, con misiones
- [[01 - Inserta la Moneda]] — el marcado que el DOM renderiza
- [[12 - Flexbox]] — maquetando la página que este script manipula

---
