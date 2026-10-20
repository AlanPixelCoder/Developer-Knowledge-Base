# 15. El Jefe Final

**Versión original en inglés:** [15 - The Final Boss.md](15%20-%20The%20Final%20Boss.md)

**Curso:** React
**Tema:** Arquitectura del proyecto final, jerarquía de componentes, enrutado, gestión de estado, obtención de datos, lógica del test, renderizado condicional en rutas, providers de context y estilos
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-AVANZADO-F0AD4E?style=for-the-badge" alt="Avanzado">
  <img src="https://img.shields.io/badge/Lecciones-01_--_07-7C5CFF?style=for-the-badge" alt="Lecciones 01 a 07">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

El final del módulo. Empezaste con un `console.log()` en una pestaña del navegador; ahora tienes el
kit completo — JSX, componentes, props, estado, eventos, formularios, hooks, context, fetch y
enrutado. El **jefe final** es donde todo pelea junto: el test **"¿Qué clase de Emberfall eres?"** —
una página de aterrizaje, un formulario de nombre, una ronda de preguntas y una tarjeta de resultado
cuyo retrato se obtiene en vivo del archivo del gremio. Referencia rápida: [[00c - Chuleta de React II]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Una SPA, cinco componentes, un provider de context, un router, un `useEffect` con fetch y tres capas de CSS — la arquitectura de cada proyecto React de tamaño medio.

---

## 01. El Jefe Final

> [!NOTE]
> **Información clave**
> Un proyecto final no se gana con APIs nuevas — se gana con **arquitectura**: qué es un componente, dónde vive el estado, qué es global y qué herramienta de qué capítulo resuelve cada problema.

Antes de escribir una línea, recorre los cuatro pilares de la construcción:

| Pilar | Qué cubre | Fraguado en |
| :--- | :--- | :--- |
| **Jerarquía de componentes** | Header, Home, Question, UserForm, Results | [[05 - Bloques de Construcción]], [[06 - El Árbol de Habilidades]] |
| **Enrutado** | React Router entre la página de aterrizaje y el test | [[14 - El Mapa del Mundo]] |
| **Gestión de estado** | `useState` para selecciones/puntuación/resultado, `useContext` para el nombre del jugador | [[08 - La Barra de Vida]], [[12 - El Libro del Gremio]] |
| **Obtención de datos externos** | `useEffect` + `fetch()` para el retrato del resultado desde el archivo del gremio | [[11 - El Sistema de Reliquias]], [[13 - El Mensajero]] |

Lee la tabla como un plan de batalla: cada fila es un capítulo que ya superaste, y la pelea con el jefe es ejecutar los cuatro **a la vez, en una sola base de código**.

---

## 02. El Campamento: Distribución de Archivos

> [!NOTE]
> **Información clave**
> Vite compila los archivos `.jsx` por defecto. La **extensión `.jsx`** avisa al compilador y al
> desarrollador que hojea la lista de archivos de que dentro hay marcado JSX. La `.js` más antigua
> también sirve; la convención es `.jsx` para todo lo que devuelve marcado.

El test vive en una carpeta `components/`, una responsabilidad por archivo:

```text
src/
├── components/
│   ├── Header.jsx      ← título + navegación con <Link>
│   ├── Home.jsx        ← página de aterrizaje, la llamada "haz el test"
│   ├── UserForm.jsx    ← nombre previo al test, escribe en el context
│   ├── Question.jsx    ← pregunta actual, opciones como botones
│   └── Results.jsx     ← clase final + retrato obtenido
├── UserContext.jsx     ← nombre global del jugador (Provider + hook)
├── App.jsx             ← estado del test, enrutado, cableado del provider
└── index.jsx           ← createRoot + <BrowserRouter>
```

Cada archivo posee exactamente un trabajo. `Question.jsx` nunca sabe quién es el jugador; `Results.jsx`
nunca sabe cómo se puntuó el test — ese aislamiento es la recompensa de [[06 - El Árbol de Habilidades]].

---

## 03. El Motor del Test

Todo el estado del test vive en `App` para que el router de abajo pueda verlo. Dos llamadas a `useState`
guardan el viaje — la **pregunta actual** y **las respuestas hasta ahora** — y dos más el desenlace: la clase y su retrato.

```js
import React, { useState, useEffect } from "react";
import Question from "./components/Question.jsx";
import Results from "./components/Results.jsx";

const questions = [
  {
    text: "Una antorcha parpadea en los Salones Profundos. Tú...",
    options: ["Seguir adelante solo", "Retroceder y reagruparse"],
  },
  {
    text: "Un gremio rival se burla de tu emblema. Tú...",
    options: ["Responder con acero", "Responder con sátira"],
  },
];

function determineElement(answers) {
  // Puntúa el recorrido: mayoría de primeras opciones = Pyromancer, si no Warden
  const flames = answers.filter(function(a) { return a === 0; }).length;
  return flames > answers.length / 2 ? "Pyromancer" : "Warden";
}

function App() {
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState([]);
  const [element, setElement] = useState(null);
  const [artwork, setArtwork] = useState("");

  function handleAnswer(optionIndex) {
    // Guarda la respuesta y avanza — un clic, dos actualizaciones de estado
    setAnswers([...answers, optionIndex]);
    setCurrentQuestionIndex(currentQuestionIndex + 1);
  }

  useEffect(function() {
    // Acaba de responderse la última pregunta: puntuar y obtener el retrato
    if (currentQuestionIndex === questions.length && answers.length > 0) {
      const result = determineElement(answers);
      setElement(result);
      fetchArtwork(result);
    }
  }, [currentQuestionIndex]);
```

La comparación del `useEffect` es el detector de meta: mientras `currentQuestionIndex < questions.length`
el test sigue preguntando; en el instante en que el índice **iguala** la longitud de la lista,
`determineElement(answers)` puntúa el recorrido, `setElement` guarda la clase y `fetchArtwork(...)`
llama al archivo del gremio.

```js
  async function fetchArtwork(query) {
    try {
      const response = await fetch(
        "https://collectionapi.metmuseum.org/public/collection/v1/search?q=" + query
      );
      const data = await response.json();
      const objectUrl =
        "https://collectionapi.metmuseum.org/public/collection/v1/objects/" +
        data.objectIDs[0];
      const objectResponse = await fetch(objectUrl);
      const artworkData = await objectResponse.json();
      setArtwork(artworkData.primaryImageSmall);
    } catch (err) {
      console.log("Archivo del gremio inaccesible: " + err.message);
    }
  }
```

El pipeline del retrato es el capítulo [[13 - El Mensajero]] de principio a fin — endpoint de búsqueda,
luego endpoint de objeto, luego la URL de la imagen aparcada en estado — con la API del MET Museum
haciendo de archivo del gremio.

### El Componente Question

`Question.jsx` recibe todo por props y convierte las opciones en botones con `.map()`:

```js
function Question({ question, options, onAnswer }) {
  return (
    <div>
      <h2>{question.text}</h2>
      {options.map(function(option, index) {
        return (
          <button key={option} onClick={function() { onAnswer(index); }}>
            {option}
          </button>
        );
      })}
    </div>
  );
}
```

### Misión: Tercer Camino

Añade una tercera opción a cada pregunta y una rama `"Trickster"` a `determineElement`.
Confirma que la meta se dispara exactamente una vez — sin llamadas dobles a
`fetchArtwork` en la pestaña de Red.

---

## 04. Dos Caminos, Una Puerta

La ruta del test no es un componente — es un **condicional**, decidido en tiempo de
render: preguntas mientras dura la partida, resultados cuando termina.

```js
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/form" element={<UserForm />} />
  <Route path="/quiz" element={
    currentQuestionIndex < questions.length
      ? <Question
          question={questions[currentQuestionIndex]}
          options={questions[currentQuestionIndex].options}
          onAnswer={handleAnswer}
        />
      : <Results element={element} artwork={artwork} />
  } />
</Routes>
```

El ternario dentro de `element` es el mismo renderizado condicional de [[04 - Marcado Vivo]], elevado al
nivel del enrutado: **una URL, dos componentes**, cambiados solo por estado. El jugador nunca navega
entre preguntas — la URL se queda en `/quiz` mientras el contenido avanza por debajo.

> [!WARNING]
> **El error que todos cometen una vez**
> Olvidar que la rama se re-renderiza en **cada** cambio de estado. Pon un
> `console.log("render de la ruta del test")` dentro de la rama del ternario y mira cómo se dispara con
> cada respuesta — luego mueve el trabajo pesado (el fetch) al guard del `useEffect`, donde se ejecuta
> una sola vez por finalización.

---

## 05. La Escriba del Gremio

El nombre del jugador se escribe en una pantalla (`UserForm`) y se lee en otra (`Results`). Eso es
estado global — el trabajo de [[12 - El Libro del Gremio]]: `createContext()`, un Provider, `useContext`.

```js
import { createContext, useContext, useState } from "react";

export const UserContext = createContext();

export function UserProvider({ children }) {
  const [name, setName] = useState("");
  return (
    <UserContext.Provider value={{ name, setName }}>
      {children}
    </UserContext.Provider>
  );
}

export function useUser() {
  return useContext(UserContext);
}
```

Córtalo alrededor de las rutas, para que cada página pueda alcanzar el nombre:

```js
import { UserProvider } from "./UserContext.jsx";

function App() {
  // ...el estado del test de la sección 03...
  return (
    <UserProvider>
      <Header />
      <Routes>
        {/* las rutas de la sección 04 viven dentro del provider */}
      </Routes>
    </UserProvider>
  );
}
```

Entonces cada consumidor hace su único trabajo: **`UserForm` escribe** (`setName` desde el `onChange` del input) y **`Results` lee**:

```js
import { useContext } from "react";
import { UserContext } from "../UserContext.jsx";

function Results({ element, artwork }) {
  const { name } = useContext(UserContext);
  return (
    <div>
      <h1>¡{name}, eres {element}!</h1>
      <div className="artwork">
        <img src={artwork} alt={"Retrato de " + element} />
      </div>
    </div>
  );
}
```

Una sola fuente de verdad, cero prop drilling a través del router.

---

## 06. Tres Capas de Pintura

El proyecto final se estila en tres capas, y saber a qué capa pertenece cada regla es mitad de la higiene de CSS en React.

### Capa 1 — Global: `index.css`

```css
html {
  font-family: Arial;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #f0f0f0;
  min-height: 100vh;
}
```

`min-height: 100vh` hace que la página **llene el viewport** incluso con tres líneas de contenido.
`flex-direction: column` apila los hijos de arriba abajo — el `row` por defecto los alinearía en horizontal.

### Capa 2 — Reglas de componente

```css
form {
  max-width: 400px;
  margin: 2rem auto;
}
form label {
  display: block;
}
form input {
  width: 400px;
  padding: 10px;
  border-radius: 5px;
}
nav a:hover {
  text-decoration: underline;
}
button:hover {
  background-color: #c4c4c4;
}
```

CSS puro, una hoja de estilos, sin librerías — `nav a:hover` y `button:hover` dan a cada enlace y botón del sitio el mismo comportamiento al pasar el cursor sin tocar un solo componente.

### Capa 3 — Contenido dinámico de API

```css
.artwork {
  text-align: center;
}
.artwork img {
  max-width: 30%;
  border-radius: 10px;
}
```

El retrato viene de una API que no controlas — puede medir 3000px. `max-width: 30%` es el cinturón de
seguridad: el arte gigante **escala hacia abajo** hasta la maquetación en vez de reventarla.

---

## 07. La Pantalla de Victoria

### Checkpoint: Todo el Módulo en una Lista

- **[[01 - El Renacimiento]] → [[04 - Marcado Vivo]]**: React es declarativo y basado en componentes; JSX se transpila a `React.createElement`; el marcado incrusta `{expresiones}` y renderiza condicionalmente.
- **[[05 - Bloques de Construcción]] → [[07 - Rutas Comerciales]]**: los componentes son funciones en PascalCase; las props fluyen padre → hijo; `.map()` convierte datos en listas.
- **[[08 - La Barra de Vida]] → [[10 - La Fragua]]**: `useState` impulsa los re-renders; los eventos son sintéticos y camelCase; los formularios se controlan desde el estado.
- **[[11 - El Sistema de Reliquias]] → [[12 - El Libro del Gremio]]**: los hooks traen efectos, refs y limpieza; el context elimina el prop drilling.
- **[[13 - El Mensajero]] → [[14 - El Mapa del Mundo]]**: `fetch` dentro de `useEffect` con estados de carga y error; el router cambia páginas sin recargar.

### Requisitos del Proyecto: "¿Qué clase de Emberfall eres?"

| Requisito | Construido con |
| :--- | :--- |
| Cabecera con navegación `<Link>` | Sección 04 + [[14 - El Mapa del Mundo]] |
| Pantalla de nombre previa al test | `UserForm` + context (sección 05) |
| Secuencia de preguntas con botones de opción | `Question` + `.map()` (sección 03) |
| Puntuación → clase final | `determineElement(answers)` (sección 03) |
| Retrato del resultado desde una API externa | `fetchArtwork` + `useEffect` (sección 03) |
| Una URL para toda la partida del test | `element` condicional (sección 04) |
| Maquetación coherente y sin roturas | Tres capas de CSS (sección 06) |

> [!TIP]
> **Versión para game dev**
> Este proyecto final es un vertical slice: la misma arquitectura escala a un lector de parches, una
> lista de gremios, una tienda — cambia `questions` por productos y el motor del test es un catálogo.
> Cada SPA definitorio es este esqueleto con otro dataset en la fragua. El jefe ha caído; ve y construye la expansión.

---

## ⚡ XP Ganados: Ideas Clave

- 🏗️ Un proyecto final se gana con **arquitectura**: jerarquía, enrutado, estado y obtención, decididos antes del código.
- 🧩 Un archivo, un trabajo — `Question` nunca lee el nombre, `Results` nunca lee la puntuación.
- 🔀 Un ternario dentro de `element` da una URL con dos componentes, cambiados solo por estado.
- 🗄️ Los datos globales (el nombre del jugador) van en un Provider de context — se escribe una vez, se lee en cualquier parte.
- 🖼️ Arte de una API sin control necesita `max-width` — nunca dejes que los píxeles remotos elijan el tamaño de tu maquetación.
- 🏁 El `useEffect` de meta compara `currentQuestionIndex` con `questions.length` y puntúa exactamente una vez.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🧪 Tests de personalidad y flujos de recomendación ("¿qué plan te conviene?")
- 📋 Formularios multipaso: asistentes de configuración, altas, solicitudes de empleo — el mismo estado de índice y respuestas
- 🏆 Pantallas de resultado que obtienen un asset externo: certificados, boletines de notas, arte generado
- 🗂️ Cualquier SPA donde una URL aloja una secuencia con estado en vez de una sola vista
- 🎓 La plantilla para un proyecto de portafolio: enrutado + context + fetch + formularios, todo en uno

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Persiste `answers` en `localStorage` para que un recarga de página retome el test en la misma pregunta.
2. Añade una barra de progreso dirigida por `currentQuestionIndex / questions.length` dentro de `Header`.
3. Dale al test una ruta `/results` y `navigate()` allí cuando termine la partida — compáralo con el enfoque de `element` condicional de la sección 04.
4. Extiende `UserForm` con un desplegable controlado de clase favorita (capítulo [[10 - La Fragua]]) guardado en el mismo context.
5. **Pelea de jefe:** convierte el proyecto final en un lector de notas de parche — obtén el feed de releases de GitHub con el patrón `useEffect` de la sección 03, lista las entradas con `.map()`, enrútalas en `/news` y deja intactos la cabecera, el context y las tres capas de CSS.

---

## 🔗 Ver También

- [[00c - Chuleta de React II]] — cada API que usa este proyecto final, en una página
- [[14 - El Mapa del Mundo]] — el equipaje de enrutado con el que navega el test
- [[13 - El Mensajero]] — el patrón de fetch/carga/error detrás de `fetchArtwork`
- [[12 - El Libro del Gremio]] — el patrón de context detrás de `UserProvider`
- [[01 - El Renacimiento]] — donde empezó todo el viaje

---
