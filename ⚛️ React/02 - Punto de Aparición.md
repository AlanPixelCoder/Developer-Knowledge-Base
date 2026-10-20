# 02. Punto de Aparición

**Versión original en inglés:** [02 - Spawn Point.md](02%20-%20Spawn%20Point.md)

**Curso:** React
**Tema:** Node.js y npm, creación del proyecto con Vite, el servidor de desarrollo, recarga en caliente, estructura del proyecto y el contenedor raíz con `createRoot`
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Lecciones-01_--_07-7C5CFF?style=for-the-badge" alt="Lecciones 01 a 07">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

El capítulo 01 te vendió la librería. Este capítulo la **instala**. Al terminar tendrás
Node.js y npm verificados, un proyecto React creado con **Vite**, el servidor de desarrollo
en marcha en `http://localhost:5173/` y un mapa claro de cada archivo del proyecto —
incluida la única línea sagrada que ancla toda la app a la página. La referencia rápida de
todo el capítulo está en [[00b - Chuleta de React]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Una app React es un montón de archivos JavaScript hasta que `npm run dev` les da un
> servidor — así que este capítulo prepara el toolchain, recorre los archivos del proyecto y
> aterriza en el único `<div id="root">` donde vivirá todo lo que construyas.

---

## 01. Antes de Aparecer

> [!NOTE]
> **Información clave**
> **Node.js** es un entorno de ejecución de JavaScript que ejecuta el lenguaje **fuera del
> navegador**. **npm** (Node Package Manager) es la herramienta que descarga y gestiona las
> librerías de las que depende tu proyecto. Los dos vienen juntos cuando instalas Node.

El desarrollo con React ocurre en tu máquina, no en una pestaña del navegador: tu editor
escribe el código, Node.js ejecuta las herramientas que lo procesan y npm descarga las
librerías que esas herramientas necesitan. Instala Node.js desde nodejs.org (la versión LTS
es la elección segura) y luego verifica los requisitos del spawn:

```bash
# Comprueba que Node.js está instalado — se recomienda v18 o superior
node -v
```

El terminal responde con una versión como `v20.11.0`. Si responde con *command not found*,
la instalación no cuadró — vuelve a nodejs.org antes de continuar.

> [!TIP]
> npm no es una descarga aparte: viene incluido con Node. Que `node -v` responda verde
> significa que `npm` ya está en tu sistema, listo a invocar paquetes del registro.

### Misión: Comprobación de Equipo

Ejecuta `node -v` y anota la versión. Cualquier cosa desde la **v18** en adelante sirve para
este módulo. Si estás en una versión antigua (v12, v14), actualízate a la LTS ahora — Vite
moderno se niega a aparecer en entornos de ejecución tan viejos.

---

## 02. El Glifo Vite

### ¿Qué es Vite?

**Vite** (se pronuncia /veet/, del francés «rápido») es una herramienta de build ligera para
el frontend. Empaqueta tu código, arranca un servidor de desarrollo en milisegundos y
refresca la página mientras escribes. Es la forma estándar en que nacen los proyectos React
nuevos.

### Crear el Proyecto

Un solo hechizo convoca el proyecto. Vite hace tres preguntas interactivas — nombre del
proyecto, framework y variante:

```bash
# Crea una app React nueva. Las preguntas piden:
#   nombre del proyecto -> my-first-app
#   framework           -> React
#   variante            -> JavaScript (o JavaScript + SWC, el Speedy Web Compiler basado en Rust)
npm create vite@latest
```

Responde a las preguntas así:

| Pregunta | Tu respuesta | Notas |
| :--- | :--- | :--- |
| **Nombre del proyecto** | `my-first-app` | Se convierte en el nombre de la carpeta |
| **Framework** | `React` | La librería que cubre este curso |
| **Variante** | `JavaScript` | `JavaScript + SWC` es lo mismo, compilado por el **S**peedy **W**eb **C**ompiler basado en **R**ust — más rápido, mismo resultado |

Después entra en la carpeta, descarga las dependencias y arranca:

```bash
# Entra en la carpeta del proyecto y descarga sus dependencias en node_modules
cd my-first-app
npm install

# Arranca el servidor de desarrollo — la página aparece en http://localhost:5173/
npm run dev
```

- `npm install` lee `package.json` y descarga cada dependencia en una carpeta llamada
  `node_modules`. Se ejecuta una vez por proyecto (y otra vez cuando cambian las dependencias).
- `npm run dev` arranca el servidor de desarrollo. Abre `http://localhost:5173/` y la app
  por defecto te saluda — tu primera app React, en marcha.

> [!WARNING]
> **El error que todos cometen una vez**
> Ejecutar `npm run dev` en la carpeta equivocada — o antes de `npm install` — y recibir
> `Cannot find module` o un listado vacío. El servidor se ejecuta **dentro** de la carpeta
> del proyecto: haz `cd my-first-app` primero y ejecuta `npm install` una vez antes del
> primer arranque.

### Misión: Primer Arranque

Crea `my-first-app`, ejecuta la instalación, arranca el servidor de desarrollo y abre
`http://localhost:5173/`. Edita el texto dentro de `src/App.jsx`, guarda y observa cómo el
navegador se actualiza **antes de que termines de llegar al ratón**. Ya estás ejecutando
React.

---

## 03. Anatomía del Punto de Aparición

Todo proyecto React con Vite tiene el mismo esqueleto:

```text
my-first-app/
├── index.html          ← entrada raíz: aloja el punto de montaje <div id="root">
├── package.json        ← scripts y lista de dependencias
├── vite.config.js      ← configuración de Vite
└── src/
    ├── App.jsx         ← el componente raíz (el marcado JSX vive aquí)
    └── index.css       ← estilos globales
```

| Archivo | Rol |
| :--- | :--- |
| `index.html` | La única página real que carga el navegador; aloja `<div id="root">` |
| `package.json` | Declara las dependencias y los scripts `dev` / `build` |
| `vite.config.js` | Configuración del bundler y del servidor de desarrollo |
| `src/App.jsx` | El componente raíz — la cima de todo lo que renderizarás |
| `src/index.css` | Estilos globales aplicados en toda la app |

> [!NOTE]
> Fíjate en la extensión `.jsx` de `App.jsx`. Vite acepta tanto `.js` como `.jsx`, pero la
> `x` extra anuncia «este archivo contiene marcado JSX» al compilador y a tu editor — los
> dos lo leen y cambian al modo correcto.

### Misión: Lee los Runes

Sin buscar en internet, escribe una frase para cada archivo de arriba explicando qué se
rompería si se borrara. `index.html` y `App.jsx` son los dos que tocarás más; los otros tres
sobre todo se configuran y se olvidan.

---

## 04. Los Dos Motores

Mira dentro de `package.json`: dos dependencias importan más que el resto:

```json
{
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0"
  }
}
```

| Paquete | Rol |
| :--- | :--- |
| `react` | El **motor central**: componentes, hooks y el DOM virtual — las ideas del capítulo [[01 - El Renacimiento]] |
| `react-dom` | El **renderizador específico del DOM**: todo lo que coloca la salida de React en una página web real, incluido `createRoot` |

Reparten responsabilidades a propósito. `react` sabe lo que *es* un componente; `react-dom`
sabe cómo mostrar uno en una página de navegador. Un renderizador futuro (React Native, para
teléfonos) cambia `react-dom` y conserva `react` — mismo motor, otra pantalla.

---

## 05. La Recarga Viva

Arranca el servidor con `npm run dev` y déjalo correr. Vite observa tus archivos: la salida
renderizada se actualiza **en tiempo real mientras escribes**, sin recarga manual y sin paso
de compilación. Guarda un archivo y el navegador refleja la edición casi al instante — eso
es la **recarga en caliente** (*hot reloading*).

El servidor de desarrollo es también tu primer depurador:

- Un **error de compilación** (etiqueta sin cerrar, llave suelta) aparece como una
  superposición en el navegador, con el nombre del archivo y el mensaje.
- Un **error en tiempo real** aparece igual, con el archivo y la **traza de pila** — la
  cadena de llamadas que llevó al fallo.

> [!TIP]
> Lee la superposición en vez de refrescarla para deshacerte de ella. La primera línea nombra
> el archivo; la traza de pila nombra la línea. Nueve de cada diez veces el bug está en el
> primer archivo de esa lista.

### Misión: Rómpelo a Propósito

Abre `src/App.jsx` y borra una etiqueta `</div>` de cierre. Guarda. Lee la superposición de
error en voz alta — nombre del archivo, mensaje. Deshaz el cambio, guarda y observa cómo la
app se cura. Repite con un error en tiempo real (escribe `{undefinedThing.map(...)}` dentro
del marcado). El miedo a la superposición roja es la forma más rápida de dejar de aprender;
leerla es la forma más rápida de empezar.

---

## 06. El Diseño Clásico

Vite es el punto de aparición moderno, pero encontrarás proyectos React antiguos — y muchísimos
tutoriales — organizados a la manera clásica (la convención de Create React App):

```text
classic-project/
├── public/
│   └── index.html      ← página de entrada estática, copia tal cual al build
├── src/
│   ├── index.js        ← script de entrada: renderiza <App /> dentro del raíz
│   ├── App.js          ← componente raíz
│   └── styles.css      ← estilos globales
└── package.json
```

| Archivo | Rol |
| :--- | :--- |
| `public/index.html` | El shell HTML estático que se sirve al navegador |
| `src/index.js` | El punto de entrada JavaScript: importa React y monta la app |
| `src/App.js` | El componente raíz — el mismo trabajo que `App.jsx` de Vite |
| `package.json` | Dependencias y scripts, como siempre |
| `styles.css` | Hoja de estilos global — el mismo trabajo que `index.css` de Vite |

El mismo castillo, otro plano: un shell HTML estático, un script de entrada que monta la app,
un componente raíz y una hoja de estilos. Ya veas `App.js` o `App.jsx`, y `index.js` o
`main.jsx`, el cableado es idéntico — un script de entrada encuentra el elemento raíz y
renderiza dentro el componente raíz.

---

## 07. El Ancla Raíz

### El contenedor de montaje

Toda app React necesita **un lugar** en la página real del que hacerse cargo. El shell HTML
clásico lo deja en el `<body>`:

```html
<body>
  <div id="root"></div>
</body>
```

Un `<div>` vacío con un `id` de `"root"`. A React no le importa qué más haya en la página —
tratará ese div como su territorio.

### `createRoot` y `render`

El script de entrada reclama el contenedor con `createRoot` (importado de `react-dom/client`)
y pinta la app dentro:

```javascript
import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";

const root = createRoot(document.getElementById("root"));
root.render(<App />);
```

Línea a línea: importa React, importa `createRoot`, importa el componente raíz `App`;
toma el `<div id="root">` del documento con `document.getElementById("root")`; pásaselo a
`createRoot`; llama a `root.render(<App />)` para dibujar el árbol de componentes en la
página. Desde esa llamada en adelante, todo lo que hay dentro de `<App />` es mantenido por
React.

> [!WARNING]
> **El caos clásico**
> Borra el atributo `id="root"` (o apunta `getElementById` a otro id) y la app muere al
> arrancar con el error en tiempo real `Target container is not a DOM element`. React no
> encuentra su ancla y se niega a renderizar nada. Un solo atributo sosteniendo todo el
> sitio companion.

### Misión: Vuelve a Cablear el Ancla

En `index.html`, renombra el contenedor a `id="app"` y luego arregla el script de entrada
para que la app vuelva a arrancar. Rómpelo primero a propósito, lee la superposición
`Target container is not a DOM element` y solo entonces aplica la corrección. Acabas de
recorrer la ruta completa del spawn: contenedor HTML → `createRoot` → `render`.

---

## ⚡ XP Ganados: Ideas Clave

- 🛠️ **Node.js** ejecuta JavaScript fuera del navegador; **npm** descarga librerías. Verifica
  con `node -v` (se recomienda v18+).
- ⚡ **Vite** (/veet/, francés para «rápido») crea el proyecto: `npm create vite@latest`, y
  luego `cd`, `npm install`, `npm run dev` → `http://localhost:5173/`.
- 🗂️ Anatomía de Vite: `index.html` (aloja el div raíz), `package.json`, `vite.config.js`,
  `src/App.jsx`, `src/index.css`. El diseño clásico añade `public/`, `index.js` y `App.js`.
- 📦 `react` es el motor central; `react-dom` es el renderizador del DOM que aporta `createRoot`.
- 🔥 La **recarga en caliente** repinta mientras escribes; los errores de compilación y en
  tiempo real muestran una superposición con el archivo y la traza de pila.
- 🎯 Todo se monta a través de un ancla: `<div id="root">` → `createRoot(...)` →
  `root.render(<App />)`. Pierde el id y pierdes la app: `Target container is not a DOM
  element`.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🏗️ `npm create vite@latest` es como empieza casi todo proyecto React moderno, prototipo y
  app de hackatón
- 🧪 Un servidor de desarrollo local con recarga en caliente es el bucle de feedback estándar
  del trabajo frontend
- 📦 Entender `package.json` se traslada a cada herramienta JS del planeta
- 🔍 La superposición de errores te enseña a leer trazas de pila — una habilidad que
  sobrevive a React
- 🧩 Conocer tanto Vite como el diseño clásico te deja contribuir en codebases viejas y nuevas

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Crea un segundo proyecto llamado `guild-dashboard` y bórralo después — memoria muscular
   para las tres preguntas.
2. Lista el contenido de `node_modules` y encuentra la carpeta `react` dentro.
3. Añade un `<p>` a `index.html` **fuera** del div raíz y observa que React nunca lo toca.
4. Cambia `src/index.css`, guarda y cronometra cuánto tarda el navegador en mostrarlo.
5. **Pelea de jefe:** reproduce desde cero el error `Target container is not a DOM element` —
   renombra el id, ejecuta la app, lee la superposición — y luego corrígelo con un cambio de
   una línea y anota la ruta exacta desde `index.html` hasta `root.render`.

---

## 🔗 Ver También

- [[01 - El Renacimiento]] — el capítulo anterior: qué es React y por qué existe este toolchain
- [[03 - Taller de Glifos]] — siguiente capítulo: JSX, la sintaxis en la que se escribe `App.jsx`
- [[04 - Marcado Vivo]] — qué puedes poner dentro de ese JSX
- [🟨 JavaScript MOC](../%F0%9F%9F%A8%20JavaScript/README.md) — los fundamentos de JavaScript que este módulo da por sentados

---
