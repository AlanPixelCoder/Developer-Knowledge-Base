# 00b. Chuleta de React

**Versión original en inglés:** [00b - React Cheatsheet.md](00b%20-%20React%20Cheatsheet.md)

**Curso:** React
**Tema:** Referencia rápida del kit central: JSX, componentes, composición, props, estado y eventos
**Tags:** `#react` `#cheatsheet` `#reference` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE_A_INTERMEDIO-6CC24A?style=for-the-badge" alt="Principiante a intermedio">
  <img src="https://img.shields.io/badge/Cubre-Capítulos_01_--_09-7C5CFF?style=for-the-badge" alt="Capítulos 01 a 09">
  <img src="https://img.shields.io/badge/Tipo-Chuleta-00C2A8?style=for-the-badge" alt="Chuleta">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

Una página para todo el kit central — JSX, componentes, composición, props, estado y
eventos. Cada sentencia de aquí se introdujo en [[01 - El Renacimiento]] a
[[09 - El Mando]] — nada en esta chuleta es nuevo. Formularios, hooks, context, obtención
de datos y enrutado viven en [[00c - Chuleta de React II]].

> [!TIP]
> Imprímela, o tenla en un panel dividido junto a tu editor. Una página escrita sin
> consultar esta chuleta es como se hace sopa de props: datos que nadie recibe, porque
> nada en la chuleta parecía estar mal.

**La trama en curso de este módulo: Emberfall**, el sitio companion de un roguelike del
mismo nombre. Cada ejercicio construye parte de él: el HUD del gremio, la publicación
social, el catálogo de reliquias, la búsqueda del bestiario, el test de clase. El código
es el mismo código que un estudio real envía — solo cambian las palabras.

---

## ⚛️ React en 30 Segundos

**React** es una **librería** de JavaScript de código abierto, presentada en **2013** por
un pequeño equipo de **Facebook** (Jordan Walke) para impulsar el Newsfeed. Es
**declarativa** (describes cómo debe verse la UI para un estado dado) y **basada en
componentes** (la UI es un árbol de funciones reutilizables).

```js
// El montaje raíz — uno por app, desde react-dom/client
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
  </StrictMode>
);
```

```text
mi-app/
├── index.html      ← aloja <div id="root"></div>
├── package.json    ← aquí viven "react" y "react-dom"
├── vite.config.js
└── src/
    ├── App.jsx
    └── index.css
```

| Concepto | Regla |
| :--- | :--- |
| Declarativa | Describe el resultado para un estado; React maneja el diff del DOM |
| Basada en componentes | UI = una jerarquía de pequeñas funciones que devuelven marcado |
| `react` | El motor: componentes, hooks, el DOM virtual |
| `react-dom` | El adaptador del DOM: `createRoot`, el puente al navegador |

---

## 🧬 JSX de un Vistazo

**JSX** (JavaScript Syntax Extension) es azúcar sobre llamadas a `React.createElement`.
Los navegadores no pueden ejecutarlo directamente — un transpilador (**Babel**, **SWC**,
**esbuild**) lo convierte antes.

| JSX | Se transpila a |
| :--- | :--- |
| `<h1 id="welcome">¡Bienvenido!</h1>` | `React.createElement("h1", { id: "welcome" }, "¡Bienvenido!")` |
| `<EmberBanner title="Temporada 4" />` | `React.createElement(EmberBanner, { title: "Temporada 4" })` |

```js
export default function App() {
  return (
    <div>
      <h1>¡Hola, Emberfall!</h1>
    </div>
  );
}
```

- Vive en archivos `.js` o `.jsx` (`.jsx` avisa de JSX al compilador y al lector).
- Envuelve el JSX multilínea en paréntesis `( )` para que la inserción automática de punto y coma no seque el `return`.

---

## 🏷️ Marcado Vivo

### Expresiones

Cualquier cosa entre llaves `{ }` — cualquier expresión JS que resuelva a un solo valor:

```js
const relicName = "Ember Shard";
const dropRate = 0.05;
<h2>{relicName}</h2>
<p>Tasa de drop: {dropRate * 100}%</p>
```

### Renderizado Condicional

| Forma | Úsala cuando |
| :--- | :--- |
| `if / else` en una variable, renderizar `{page}` | Las ramas son grandes |
| `{signedIn ? <Dashboard /> : <SignIn />}` | Dos alternativas excluyentes |
| `{signedIn && <Dashboard />}` | Mostrar algo, o no mostrar nada |

### Atributos

Cadenas estáticas como en HTML (`src`, `alt`, `href`, `id`); valores dinámicos en llaves.
Y como `class` es una palabra reservada de JS, JSX usa **`className`**:

```js
const avatarUrl = "/avatar.png";
<img src={avatarUrl} alt="Avatar del gremio" />
<button className="forge-button">Calentar el metal</button>
```

---

## 🧩 Componentes y Composición

```js
import React from "react";

export default function Greetings() {
  return (
    <div>
      <h1>¡Bienvenido de nuevo, Guardián!</h1>
    </div>
  );
}
```

| Regla | Por qué |
| :--- | :--- |
| Nombres en **PascalCase** | React distingue tus componentes de las etiquetas HTML |
| **Un solo elemento raíz** | Envuelve hermanos en un `<div>` o en un Fragment `<>...</>` |
| **`export default`** | Hace el componente importable desde otros archivos |
| Úsalo como `<Greetings />` | Auto-cerrada; la instanciación ocurre donde se renderiza |
| Comentarios JSX `{/* ... */}` | La única sintaxis de comentario dentro del marcado |

**Composición** = anidar componentes pequeños en una jerarquía — los datos fluyen
**padre → hijo**, en un solo sentido, desde una raíz única:

```text
App (raíz)
 └── Post (tarjeta)
      ├── FollowButton
      └── LikeButton
```

---

## 📦 Props

Las **props** son fragmentos de datos entregados a los componentes — el mecanismo del flujo
de un solo sentido padre → hijo. Cualquier tipo JS: cadenas, booleanos, objetos, funciones.

```js
// Pasar — comillas para cadenas, llaves para todo lo demás
<Notification message="¡El festín de GuildMasterVex es hoy!" isRead={true} />

// Recibir — un paréntesis, convencionalmente props
function Notification(props) {
  return <p>{props.message}</p>;
}
```

### Listas con `.map()`

```js
{relicList.map(function(relic) {
  return (
    <div key={relic.name}>
      <h2>{relic.name}</h2>
      <h3>Rareza: {relic.rarity}</h3>
    </div>
  );
})}
```

| Patrón | Forma |
| :--- | :--- |
| Estado como props | El padre guarda `scores`; los hijos reciben `<Player score={scores[0]} />` |
| Listas de componentes | El padre mapea datos → `<Relic name rarity imageUrl />`; el hijo renderiza `props.name` etc. |
| `key` | Un id estable por item — permite a React emparejar filas viejas y nuevas |

---

## 🧮 Estado

El **estado** son datos internos que se esperan que cambien (HP, pociones, entradas de
formulario). `useState` devuelve `[valor, setter]`; **cualquier llamada al setter re-renderiza**
el componente.

```js
import React, { useState } from "react";

function HealthBar() {
  const [hp, setHp] = useState(80);
  return <h1>HP: {hp}</h1>;
}
```

| Regla | Mal | Bien |
| :--- | :--- | :--- |
| Nunca mutar el estado | `hp = 50;` | `setHp(50);` |
| Valor nuevo a partir del viejo | `setHp(hp - 10);` | `setHp((prevHp) => prevHp - 10);` |
| Arrays/objetos | `items.push(x)` | `setItems([...items, x])` |

La forma funcional `(prev) => ...` siempre lee el estado más fresco — obligatoria dentro
de temporizadores y actualizaciones por lotes. El valor inicial puede ser de cualquier tipo
JS; se establece **una vez**, al montar.

---

## 🖱️ Eventos

React envuelve los eventos nativos en un **sistema de eventos sintéticos** para
consistencia entre navegadores. Los handlers van en **camelCase** y reciben la función en
sí — **sin paréntesis**, o se ejecutarán al renderizar.

```js
function handleClick(e) {
  console.log(e.target); // el elemento del DOM que lo disparó
}
return <h1 onClick={handleClick}>¡Haz clic!</h1>;
```

| Evento | Se dispara cuando | Uso típico |
| :--- | :--- | :--- |
| `onClick` | Clic | Botones, conmutadores |
| `onMouseOver` / `onMouseLeave` | El puntero entra / sale | Tooltips |
| `onFocus` / `onBlur` | El elemento gana / pierde foco | Validación, resaltados |
| `onKeyDown` / `onKeyUp` | Tecla pulsada / soltada | Atajos, teclas de volumen |

- Los elementos no enfocables (`<div>`, `<img>`) necesitan **`tabIndex={0}`** antes de poder disparar eventos de foco.
- Los estilos inline son objetos con propiedades en **camelCase**: `e.target.style.backgroundColor = "yellow"`.
- La identidad de la tecla vive en **`e.key`**: `e.key === "ArrowUp"`, `e.key === "Enter"`, `e.key === " "`.

```js
// Teclado y accesibilidad en un solo widget
<button
  tabIndex="0"
  onClick={handleGoing}
  onKeyDown={function(e) { if (e.key === "Enter") handleGoing(); }}
>
  Asistir a la noche de la arena ({goingCount})
</button>
```

---

## ⚠️ Trampas que Vale la Memoria

| Trampa | Qué pasa de verdad |
| :--- | :--- |
| `class=` en JSX | Se ignora en silencio — usa `className=` |
| `onClick={handle()}` | Se llama al renderizar; pasa `onClick={handle}` |
| Mutar el estado directamente | La UI se enfría — el setter es lo que re-renderiza |
| `key` ausente en `.map()` | React avisa; las actualizaciones de la lista se portan mal |
| Componente en minúsculas `<relic />` | Se trata como etiqueta HTML, no como tu función |
| Devolver hermanos adyacentes | Error de sintaxis — envuelve en una raíz o `<>...</>` |
| Errores de tecleo en nombres de props | Sin error — la prop simplemente es `undefined` |

---

## 🔗 Ver También

- [[00c - Chuleta de React II]] — formularios, hooks, context, fetch y enrutado
- [[01 - El Renacimiento]] — qué es React, donde empieza esta chuleta
- [[06 - El Árbol de Habilidades]] — composición y la jerarquía de componentes
- [[09 - El Mando]] — eventos, la última parada de esta chuleta

---
