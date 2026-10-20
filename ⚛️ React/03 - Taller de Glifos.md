# 03. Taller de Glifos

**Versión original en inglés:** [03 - Glyph Workshop.md](03%20-%20Glyph%20Workshop.md)

**Curso:** React
**Tema:** Qué es JSX, la transpilación, `React.createElement`, la sintaxis básica de componentes, las extensiones de archivo y la regla de los paréntesis
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE_A_INTERMEDIO-6CC24A?style=for-the-badge" alt="Principiante a Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-01_--_06-7C5CFF?style=for-the-badge" alt="Lecciones 01 a 06">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

En el punto de aparición conociste el toolchain. Ahora conoces el **lenguaje que compila**:
**JSX**. Este capítulo es el taller donde los glifos con forma de HTML se escriben
directamente dentro de JavaScript, se muelen hasta las llamadas nativas
`React.createElement` que el navegador sí puede ejecutar, y se envuelven en los paréntesis
que evitan que el compilador se coma tu marcado. La referencia rápida de todo el capítulo
está en [[00b - Chuleta de React]].

> [!NOTE]
> **Todo el capítulo en una frase**
> **JSX** es una extensión de sintaxis que te deja escribir marcado con forma de HTML dentro
> de JavaScript; un **transpilador** lo reescribe como llamadas `React.createElement(...)`
> que los navegadores pueden ejecutar.

---

## 01. El Lenguaje de los Glifos

**JSX** significa **JavaScript Syntax Extension** (extensión de sintaxis de JavaScript) —
también lo verás llamado **JavaScript XML**. Es **azúcar sintáctico** sobre la API nativa de
React: una forma más amable de escribir que significa exactamente lo mismo para la máquina,
igual que `+= 1` significa lo mismo que `= x + 1`.

El problema que resuelve: los navegadores **no pueden ejecutar JSX directamente**. El `<h1>`
que ves no es HTML que el navegador conozca — es un glifo del taller de React, y debe ser
**transpilado** (traducido) a JavaScript puro antes de poder ejecutarse.

```javascript
// Lo que escribes (JSX):
let heading = <h1 id="welcome-heading">Welcome!</h1>;

// Lo que produce el transpilador (JavaScript puro):
let heading = React.createElement("h1", { id: "welcome-heading" }, "Welcome!");
```

Lee las dos líneas con cuidado — son la misma instrucción. El primer argumento de
`React.createElement` es el **nombre de la etiqueta** (`"h1"`), el segundo es el **objeto de
atributos** (`{ id: "welcome-heading" }`) y cada argumento posterior es un **hijo**
(`"Welcome!"`).

### Misión: Traduce a Mano

Toma este cartel de Emberfall y reescríbelo como la llamada a `React.createElement` que
produciría un transpilador:

```javascript
<header id="main-header">Emberfall Launcher ☕</header>
```

Respuesta: etiqueta `"header"`, atributos `{ id: "main-header" }`, un hijo de texto. Deberías
llegar a:

```javascript
React.createElement("header", { id: "main-header" }, "Emberfall Launcher ☕");
```

Haz diez de estos y JSX deja de ser magia. Se vuelve una forma de escribir.

---

## 02. Los Transpiladores

Un **transpilador** es una herramienta que lee código fuente en un lenguaje y lo escribe en
otro (o en una versión más nueva/vieja del mismo). En el mundo de React, los transpiladores
que convierten JSX en JavaScript que el navegador entiende son:

| Herramienta | Dónde la encuentras |
| :--- | :--- |
| **Babel** | El clásico predeterminado de siempre; sigue por todas partes en tutoriales y configuraciones |
| **SWC** | El **S**peedy **W**eb **C**ompiler basado en Rust — la opción rápida que ofrece Vite |
| **esbuild** | Un bundler/transpilador basado en Go extremadamente rápido que Vite usa por dentro |

> [!NOTE]
> Rara vez invocas un transpilador a mano. Vite cablea uno en el pipeline: guardas un archivo
> `.jsx`, el transpilador lo reescribe y el navegador recibe JavaScript puro. La recarga en
> caliente de [[02 - Punto de Aparición]] es este paso ejecutándose en cada pulsación.

### Misión: Elige tu Forja

Vuelve a crear un proyecto con `npm create vite@latest` y elige esta vez
`JavaScript + SWC` en vez de `JavaScript` a secas. La app se comporta igual — solo has
cambiado el transpilador del pipeline. Ese es el punto: JSX entra, JavaScript sale, y la
forja de en medio es reemplazable.

---

## 03. El Conjuro del Componente

JSX vive dentro de **componentes**. La sintaxis básica de un componente es una función que
**devuelve marcado**:

```javascript
export default function App() {
  return (
    <div>
      <h1>Hello, World!</h1>
    </div>
  );
}
```

Tres cosas a notar, todas las cuales usarás en cada uno de tus componentes:

1. El nombre de la función va **en mayúscula** (`App`). React usa la mayúscula para
   distinguir tus componentes de las etiquetas HTML. El detalle completo está en
   [[05 - Bloques de Construcción]].
2. Usa las palabras clave `export default` para que otros archivos puedan importarlo.
3. **Devuelve** JSX — el marcado es la salida del componente, su valor de retorno.

`<h1>Hello, World!</h1>` ya es una expresión JSX; `<div>...</div>` lo envuelve para que el
componente tenga una sola raíz (la regla que [[04 - Marcado Vivo]] machacará).

> [!WARNING]
> **El error clásico**
> Escribir `return` en una línea y el marcado en la siguiente:
>
> ```javascript
> return
>   <div>...</div>; // ❌ ¡devuelve undefined!
> ```
>
> La **inserción automática de punto y coma (ASI)** de JavaScript inserta un punto y coma
> tras `return`, y la función devuelve `undefined` — el marcado nunca se alcanza y no se
> renderiza nada. Por eso existen los paréntesis, y por eso existe la sección siguiente.

---

## 04. Los Runes de Paréntesis

Envuelve el JSX multilínea en **paréntesis** `( )`:

```javascript
export default function App() {
  return (
    <div>
      <h1>Hello, World!</h1>
      <p>Welcome to the Emberfall codex.</p>
    </div>
  );
}
```

Los paréntesis **no** cambian lo que significa el marcado. Le dicen a JavaScript «la expresión
del `return` continúa en la línea siguiente» — venciendo al **ASI**. Con ellos, el marcado
llega al return; sin ellos, en varias líneas, el ASI convierte tu componente en uno que no
devuelve nada en absoluto.

> [!TIP]
> Adopta el hábito pronto: en cuanto un componente abarque más de una línea de marcado, pon
> el `(` de apertura justo después de `return` y el `)` de cierre en su propia línea. La
> mayoría de editores y linters lo formatearán así por ti de todos modos.

### Misión: Salva a los Escribas

Toma la última expresión JSX multilínea que hayas escrito (o el Recibo del Mercader
renderizado como marcado) y quítale los paréntesis a propósito. Guarda y observa cómo el
componente no renderiza nada. Luego vuelve a ponerlos y observa cómo se cura. Ya viste
morder el ASI; no lo olvidarás.

---

## 05. La Extensión de Archivo

JSX puede vivir en archivos con cualquiera de las dos extensiones:

| Extensión | Significado |
| :--- | :--- |
| `.js` | JavaScript puro — el diseño clásico ponía los componentes aquí |
| `.jsx` | JavaScript que contiene marcado JSX — la convención de Vite, una pista explícita al compilador y al editor |

Ambas compilan cuando hay un transpilador cableado. El scaffold de Vite usa `.jsx` para
hacer inconfundible la presencia de JSX: `src/App.jsx` anuncia a simple vista que su contenido
es JavaScript con marcado, no un archivo de utilidades.

> [!NOTE]
> La elección `.jsx` es una convención, no un requisito. Al compilador le da igual — analiza
> cada archivo de la misma forma. Los equipos eligen `.jsx` para que un humano que escanee
> el árbol de archivos distinga el marcado de la lógica sin abrir nada.

### Misión: Renombra la Forja

Renombra `src/App.jsx` a `src/App.js` y arregla el import en el archivo que lo importa.
Arranca el servidor de desarrollo: funciona. Ahora vuelve a renombrarlo. La lección: la
extensión es una señal, y cualquier linter o compañero de equipo que dependa de esa señal te
agradecerá que la mantengas precisa.

---

## 06. Glifos de un Vistazo

### Checkpoint: Resumen del capítulo

- **JSX** es una extensión de sintaxis de JavaScript (JavaScript XML) — azúcar sintáctico
  sobre `React.createElement`.
- Los navegadores no pueden ejecutar JSX; los **transpiladores** (Babel, SWC, esbuild) lo
  reescriben.
- `React.createElement(etiqueta, atributos, ...hijos)` es en lo que se convierte cada
  elemento JSX.
- Un componente es una **función con mayúscula inicial** que devuelve JSX, exportada con
  `export default`.
- JSX vive en archivos `.js` o `.jsx`.
- El JSX multilínea necesita **paréntesis** para esquivar la inserción automática de punto y coma.

### El Kit de Piezas

Aquí está el mismo componente, mostrado en ambos lenguajes uno al lado del otro, para que el
mapeo quede delante de ti:

```javascript
// Conjuro de glifos JSX
export default function App() {
  return (
    <div className="hud">
      <h1>Emberfall Launcher ☕</h1>
    </div>
  );
}
```

```javascript
// En lo que el transpilador lo muele
export default function App() {
  return React.createElement(
    "div",
    { className: "hud" },
    React.createElement("h1", null, "Emberfall Launcher ☕")
  );
}
```

Fíjate en `className` en ambos — `class` es una palabra clave de JavaScript, una distinción
que [[04 - Marcado Vivo]] cubre por completo. Fíjate también en que el elemento anidado se
convierte en el tercer argumento de la llamada exterior: los hijos son argumentos, hasta el
fondo.

> [!TIP]
> **Versión para game dev**
> Piensa en JSX como un DSL de scripting para construir árboles de escena. Escribes el árbol
> con una forma que un humano lee al instante; el motor recibe una lista plana de llamadas
> «crea nodo». Cada framework de interfaz, cada editor de juegos, cada motor CSS-in-JS tiene
> este mismo paso de compilación por debajo — este capítulo solo te deja verlo ocurriendo.

---

## ⚡ XP Ganados: Ideas Clave

- 🏷️ **JSX** = JavaScript Syntax Extension (también JavaScript XML): azúcar sobre la API
  nativa de React. Los navegadores no pueden ejecutarlo.
- 🔧 Los **transpiladores** — **Babel**, **SWC**, **esbuild** — reescriben JSX a JavaScript
  que el navegador entiende. Vite ejecuta uno en su pipeline en cada guardado.
- 🧱 `React.createElement(etiqueta, atributos, ...hijos)` es en lo que se desazucara cada
  elemento JSX: cadena de etiqueta, objeto de atributos, hijos como argumentos.
- ✍️ Un componente es una función **con mayúscula inicial** que devuelve JSX, exportada con
  `export default`.
- 📄 JSX vive en archivos `.js` o `.jsx`; `.jsx` es la convención de Vite que señala el marcado.
- 🧷 Envuelve el JSX multilínea en `( )` — si no, la **inserción automática de punto y coma**
  hace que tu función devuelva `undefined`.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🖥️ Cada interfaz React que hayas usado se compila de JSX a `createElement` (o el equivalente
  en tiempo de ejecución) antes de llegar al navegador
- 🧰 Entender la salida es lo que necesitas cuando un error de build señala las tripas y no tu
  código fuente
- 🎛️ El paso de transpilación de Babel y SWC es el mismo que impulsa TypeScript, el soporte
  de sintaxis moderna y la minificación
- 🧩 Los DSL con forma de JSX resuenan por todo el ecosistema: styled-components, MDX y los
  constructores de escenas de editores de juegos reutilizan el patrón
- 📐 La regla de los paréntesis contra el ASI salva el bug más común de «¿por qué no
  renderiza nada?»

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Traduce tres carteles JSX (header, list, button) a `React.createElement` a mano.
2. Escribe un componente con nombre en mayúscula y otro en minúscula y observa qué hace React
   distinto.
3. Rompe el ASI a propósito: `return` y el marcado en líneas separadas. Lee el resultado vacío.
4. Añade un `<span>` anidado dentro de tu componente e identifica su posición en la lista de
   argumentos de `createElement`.
5. **Pelea de jefe:** toma el HUD del gremio de [[01 - El Renacimiento]] (barra de vida +
   lista de misiones) y escríbelo primero en JSX con paréntesis, luego traduce a mano todo a
   llamadas `React.createElement` anidadas — incluyendo el `className` y los elementos hijos.
   Si tus dos versiones renderizan idénticas, dominas el taller.

---

## 🔗 Ver También

- [[01 - El Renacimiento]] — el capítulo que presentó los componentes y JSX por su nombre
- [[02 - Punto de Aparición]] — el toolchain que transpila esta sintaxis en cada guardado
- [[04 - Marcado Vivo]] — todo lo que puedes poner dentro de JSX: expresiones, condiciones, atributos
- [[05 - Bloques de Construcción]] — los componentes y sus reglas de nombre y exportación al completo

---
