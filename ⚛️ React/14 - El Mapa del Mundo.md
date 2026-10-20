# 14. El Mapa del Mundo

**Versión original en inglés:** [14 - The World Map.md](14%20-%20The%20World%20Map.md)

**Curso:** React
**Tema:** Aplicaciones de página única, enrutado del lado del cliente, react-router-dom, BrowserRouter, Routes, Route, Link, useNavigate y el historial
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-6CC24A?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-01_--_06-7C5CFF?style=for-the-badge" alt="Lecciones 01 a 06">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

El sitio companion de Emberfall ha crecido más allá de una sola pantalla: necesita una
página de Inicio, un Códice, un mostrador de Soporte — y los jugadores esperan URLs
reales, un botón de atrás que funcione y enlaces que puedan compartir en el chat del
gremio. Este capítulo es el mapa del mundo que ata esas pantallas: **enrutado del lado
del cliente** con `react-router-dom`, el paquete que decide qué componente se muestra en
cada URL **sin recargar jamás la página**. La referencia rápida de este capítulo:
[[00c - Chuleta de React II]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Envuelve la app en `<BrowserRouter>`, declara las páginas con `<Route path element>`,
> cámbialas con `<Link to>` o `useNavigate()` — y la URL del navegador se convierte en un
> visor de tu árbol de componentes en lugar de una petición a un servidor.

---

## 01. Una Página, Muchas Puertas

> [!NOTE]
> **Información clave**
> Una **aplicación de página única (SPA)** sirve un solo documento HTML y cambia su
> contenido en el navegador. Los usuarios aún esperan URLs, el botón de atrás y enlaces
> compartibles — así que el enrutado se decide **dentro del navegador**: eso es
> **enrutado del lado del cliente**, y no ocurre ninguna recarga completa.

Los sitios clásicos son de varias páginas: cada clic pide un documento HTML nuevo, la
página vieja muere y la nueva arranca desde cero — incluidos el estado del juego, el
tema y cada menú desplegable abierto. Una SPA mantiene vivo un único documento y va
cambiando **componentes** dentro de él.

El núcleo de React no trae enrutado. La respuesta estándar es el paquete externo
**`react-router-dom`**, que entrega exactamente cuatro piezas a tu nivel:

| Componente | Rol |
| :--- | :--- |
| `<BrowserRouter>` | El marco del portal — una sola instancia, envuelve toda la app, observa la URL |
| `<Routes>` | La leyenda del mapa — escanea la URL actual y elige el `<Route>` que coincide |
| `<Route>` | Una puerta: un `path` emparejado con el `element` (componente) que inyecta |
| `<Link>` | Un cartel — el equivalente consciente del router para `<a href>` dentro de la app |

> [!WARNING]
> **El error que todos cometen una vez**
> Alcanzar por hábito `<a href="/codex">`. El navegador lo trata como una navegación a
> otro documento: recarga completa, estado de la SPA perdido. Dentro de la app, cada
> enlace interno es un `<Link to="...">`.

---

## 02. El Equipaje de Viaje

El enrutado es una dependencia como cualquier otra — instálala en el proyecto Vite de
[[02 - Punto de Aparición]]:

```bash
# Añade enrutado del lado del cliente al proyecto
npm install react-router-dom
```

Luego importa las piezas donde las uses:

```js
import { BrowserRouter, Routes, Route, Link, useNavigate } from "react-router-dom";
```

Todo lo anterior es **un solo paquete** — `react-router-dom` — pero cada import es una
herramienta distinta: el marco, el mapa, las puertas, los carteles y el botón de viaje
rápido, en el orden en que los conocerás en este capítulo.

---

## 03. El Marco del Portal

El `<BrowserRouter>` envuelve la app en el punto de entrada, igual que el envoltorio
`<StrictMode>` de la configuración de Vite:

```js
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>
);
```

Un solo `<BrowserRouter>` para toda la app. No produce salida visible — su trabajo es
observar la barra de URL y dar a cada `<Route>` y `<Link>` de debajo acceso a la
ubicación actual. Dos marcos (uno por página) significan dos mapas del mismo territorio:
discordarán sobre dónde estás.

### Misión: Comprobación del Marco

Toma el `index.js` del capítulo [[02 - Punto de Aparición]], añade el import y el
envoltorio, y confirma que la app sigue renderizando. Quita `<BrowserRouter>` a
propósito, haz clic en un `<Link>` y lee el error — conocer el mensaje de fallo es mitad
del depurado del enrutado.

---

## 04. Marcando los Senderos

Dentro de `<App>`, `<Routes>` contiene cada `<Route>` del sitio. Reconvertimos las tres
páginas del sitio companion a Inicio, Códice y Soporte:

```js
function App() {
  return (
    <div>
      <NavBar />
      <Routes>
        <Route path="/" exact element={<Home />} />
        <Route path="/codex" exact element={<Codex />} />
        <Route path="/support" exact element={<Support />} />
      </Routes>
    </div>
  );
}
```

Cada puerta tiene tres partes:

| Prop | Qué es | Ejemplo |
| :--- | :--- | :--- |
| `path` | La cadena de URL que vigila la puerta | `"/codex"` |
| `exact` | Hacer match del path **exactamente** — sin extras | `exact` |
| `element` | El componente inyectado cuando la puerta gana | `<Codex />` |

El navegador está en `/` → se renderiza `<Home />`. Navega a `/codex` → `<Routes>`
detecta que la URL cambió, `<Codex />` sube al escenario y el documento jamás se
recargó.

> [!TIP]
> `exact` importa porque React Router coincide los paths **por prefijo** por defecto: sin
> él, `path="/"` también reclamaría `/codex` y `/support`, y la página de aterrizaje se
> comería todo el mapa. Coincide con precisión y el router nunca tiene que adivinar.

### Misión: Territorio Nuevo

Añade una puerta `path="/guild"` para un componente `Guild`, luego visita `/guild` en la
barra de direcciones. Confirma que la URL, el componente renderizado y la ausencia de
cualquier recarga de página coinciden.

---

## 05. Los Carteles

`<Link>` reemplaza a `<a href>` para la navegación **interna**. La prop `to` reemplaza a
`href`; el router intercepta el clic, actualiza la URL y cambia el componente — sin
recarga:

```js
import { Link } from "react-router-dom";

function NavBar() {
  return (
    <nav>
      <Link to="/">Inicio</Link>
      <Link to="/codex">Códice</Link>
      <Link to="/support">Soporte</Link>
    </nav>
  );
}
```

| Ancla `<a>` | Cartel `<Link>` |
| :--- | :--- |
| `href="/codex"` | `to="/codex"` |
| Recarga completa de página | URL y UI se actualizan en el sitio |
| Abandona la SPA | Nunca abandona la SPA |
| Úsalo para sitios externos | Úsalo para cada página dentro de la app |

### Misión: Auditoría de Navegación

Recorre cualquier sitio de producción y cuenta los enlaces internos que matarían una SPA
si fueran tags `<a>` — luego escribe la misma navegación para el sitio companion con
`<Link>` y mira la pestaña de Red quedarse vacía mientras haces clic por todas partes.

---

## 06. Viaje Rápido

`<Link>` cubre los clics en carteles visibles. Hay navegaciones **sin elemento** al que
hacer clic: una redirección tras iniciar sesión, un botón "volver a la tienda" tras el
pago, la flecha de atrás del navegador dentro de tu propia UI. Eso es `useNavigate()`:

```js
import { useNavigate } from "react-router-dom";

function SignIn() {
  const navigate = useNavigate();

  function handleSubmit(e) {
    e.preventDefault();
    // las credenciales se validan en otro sitio — envía al jugador a casa
    navigate("/home");
  }

  return (
    <form onSubmit={handleSubmit}>
      <button type="submit">Entrar a la sala del gremio</button>
    </form>
  );
}
```

`navigate(path)` salta a cualquier URL que tus `<Routes>` conozcan. El historial — el
mismo historial detrás de los botones de atrás y adelante del navegador — también se
pilota:

| Llamada | Efecto |
| :--- | :--- |
| `navigate("/codex")` | Empuja `/codex` al historial y va hasta allí |
| `navigate(-1)` | **Atrás** — un paso abajo en el historial |
| `navigate(1)` | **Adelante** — un paso arriba, si existe |

> [!TIP]
> **Versión para game dev**
> Esto es un sistema de viaje rápido del mapa del mundo: carteles (`<Link>`) para los
> destinos marcados, un hechizo de teletransporte (`navigate()`) para todo lo
> programático, y el historial como el rastro de migas de pan de vuelta al último punto de
> referencia. El proyecto final de [[15 - El Jefe Final]] usa exactamente este equipaje
> para moverse entre la página de aterrizaje y el test de clase.

---

## ⚡ XP Ganados: Ideas Clave

- 🗺️ Una **SPA** mantiene vivo un documento HTML y cambia componentes; el enrutado del lado del cliente elige el componente **en el navegador**.
- 📦 El enrutado no es React central — es `react-router-dom`, instalado como cualquier otra dependencia.
- 🖼️ `<BrowserRouter>` envuelve la app **una vez**, en el punto de entrada, junto a `<StrictMode>`.
- 🚪 Un `<Route>` es `path` + `exact` + `element` — cadena de URL, coincidencia exacta, componente a inyectar.
- 🪧 `<Link to>` reemplaza a `<a href>` internamente: sin recarga, URL y UI se actualizan juntas.
- ⚡ `useNavigate()` navega sin clic; `navigate(-1)` / `navigate(1)` caminan por el historial.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🏠 Sitios de múltiples pantallas: paneles, tiendas, escritorios de ayuda — un documento, muchas URLs
- 🔐 Redirecciones tras iniciar sesión con `navigate("/home")` tras enviar un formulario
- 🧭 Pestañas y paneles que deben seguir siendo marcables y compartibles en el chat
- ↩️ Botones de atrás en la app que se comportan exactamente como los del navegador
- 🛒 Flujos de compra: carrito → pago → confirmación, sin perder jamás el estado de la SPA

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Añade una ruta `NotFound` con `path="*"` y confirma que cada URL desconocida aterriza allí.
2. Construye un pie de página con `<Link to="/support">Reportar un error</Link>` y verifica que la pestaña de Red queda vacía al hacer clic.
3. Conecta un botón "Volver al códice" que llame a `navigate(-1)` en lugar de codificar una ruta.
4. Registra `window.location.pathname` en cada render dentro de `<App>` y míralo cambiar mientras navegas.
5. **Pelea de jefe:** combina los capítulos [[13 - El Mensajero]] y este — obtén una nota de parche aleatoria de la API de releases de GitHub en una página `PatchNote`, enrútala en `/news` y añade un `<Link to="/news">` a la barra de navegación.

---

## 🔗 Ver También

- [[00c - Chuleta de React II]] — la tabla de enrutado y `useNavigate` en una página
- [[02 - Punto de Aparición]] — donde se creó el proyecto Vite (y el `index.js` que acabas de envolver)
- [[15 - El Jefe Final]] — el test de clase del proyecto final que enruta entre la página de aterrizaje y las preguntas
- [[13 - El Mensajero]] — capítulo anterior: obtener los datos que estas páginas muestran

---
