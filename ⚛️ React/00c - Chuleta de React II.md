# 00c. Chuleta de React II

**Versión original en inglés:** [00c - React Cheatsheet II.md](00c%20-%20React%20Cheatsheet%20II.md)

**Curso:** React
**Tema:** Referencia rápida del kit avanzado: formularios, hooks, context, obtención de datos, enrutado y estilos
**Tags:** `#react` `#cheatsheet` `#reference` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO_A_AVANZADO-F0AD4E?style=for-the-badge" alt="Intermedio a avanzado">
  <img src="https://img.shields.io/badge/Cubre-Capítulos_10_--_15-7C5CFF?style=for-the-badge" alt="Capítulos 10 a 15">
  <img src="https://img.shields.io/badge/Tipo-Chuleta-00C2A8?style=for-the-badge" alt="Chuleta">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

La segunda mitad del kit — todo lo que una página companion de Emberfall necesita de
verdad cuando los basics están firmes: formularios que poseen sus datos, hooks para
efectos y refs, context para estado global, `fetch` para datos remotos, un router para
múltiples pantallas y tres capas de CSS. Cada sentencia de aquí se introdujo en
[[10 - La Fragua]] a [[15 - El Jefe Final]]. El kit central (JSX, componentes, props,
estado, eventos) está en [[00b - Chuleta de React]].

> [!TIP]
> Esta es la chuleta que abres cuando algo *casi* funciona: el formulario que pierde su
> valor, el efecto que deja de hacer fetch, el enlace que recarga la página. Encuentra el
> síntoma en las tablas, salta al patrón y envía la corrección.

**La trama en curso de este módulo: Emberfall**, el sitio companion de un roguelike del
mismo nombre. Todos los patrones de abajo salen en él: el formulario de acceso, el feed de
gatos dorados, el cambio de tema, el test de clase. El código es el mismo código que un
estudio real envía — solo cambian las palabras.

---

## 📝 Formularios

La lista de cinco pasos, en orden — omite uno y el formulario se porta mal:

| Paso | Regla |
| :--- | :--- |
| 1. Inicializar | `useState` guarda cada campo, usualmente un objeto |
| 2. Controlar | `value={...}` en cada `<input>`, `<select>` y `<textarea>` |
| 3. Manejador de cambio | `onChange` escribe `e.target.value` de vuelta al estado |
| 4. Manejador de envío | `onSubmit` en el `<form>` valida y actúa |
| 5. Prevenir el default | `e.preventDefault()` — o el navegador recarga y se come el estado |

```js
// Las etiquetas usan htmlFor (for es una palabra reservada); los inputs llevan name + value + onChange
function SignInForm() {
  const [formData, setFormData] = useState({ email: "", password: "" });

  function handleFormData(e) {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  }

  function handleSubmit(e) {
    e.preventDefault();
    console.log("Bienvenido de nuevo, " + formData.email);
    setFormData({ email: "", password: "" });
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="email">Email</label>
      <input
        type="email"
        id="email"
        name="email"
        value={formData.email}
        onChange={handleFormData}
      />
      <label htmlFor="password">Contraseña</label>
      <input
        type="password"
        id="password"
        name="password"
        value={formData.password}
        onChange={handleFormData}
      />
      <button type="submit">Entrar</button>
    </form>
  );
}
```

| Elemento | Forma controlada |
| :--- | :--- |
| `<input>` | `value` + `onChange` — el estado de React posee el texto |
| `<select>` | `value` en el `<select>` **padre**; sin `selected` en `<option>` |
| `<textarea>` | `value` + `onChange`; `rows` / `cols` opcionales |
| Clave computada | `[e.target.name]: e.target.value` deja que un solo manejador sirva a muchos campos |

---

## 🪝 Hooks

React **16.8** (feb 2019) les dio a los componentes funcionales estado y ciclo de vida. El
caballo de batalla es `useEffect(fn, deps)` — un **efecto secundario** es todo lo que sale
fuera del componente (datos, DOM, temporizadores, pop-ups):

| Array de dependencias | Se ejecuta |
| :--- | :--- |
| `[]` | Una vez, tras el primer render |
| omitido | Tras **cada** render |
| `[count]` | Cuando `count` cambia |

```js
// Limpieza: los intervalos y listeners sobreviven al componente si no devuelves una desmontada
useEffect(function() {
  const intervalId = setInterval(function() {
    setSeconds(function(prevSeconds) { return prevSeconds + 1; });
  }, 1000);
  return function() { clearInterval(intervalId); };
}, []);
```

### `useRef`

Una caja mutable que sobrevive a los renders, guardada en `.current`, que **nunca
re-renderiza**:

```js
const dataRef = useRef([]);        // datos para tu propia contabilidad
dataRef.current.push(Math.random());

const viewRef = useRef(null);      // acceso directo al DOM
<input ref={viewRef} />;
viewRef.current.focus();
```

| | `useState` | `useRef` |
| :--- | :--- | :--- |
| Actualizar dispara re-render | ✅ UI fresca | ❌ en silencio |
| Lectura al montar | vía el valor inicial | `ref.current` |
| Úsalo para | todo lo que la pantalla debe mostrar | nodos DOM, ids de temporizador, dimensiones, asas de animación |

---

## 🗄️ Context

El **prop drilling** (pasar props por muchas capas) muere aquí. Context = un valor, muchos
consumidores, cero intermediarios:

```js
import { createContext, useContext, useState } from "react";

export const ThemeContext = createContext();

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState("dark");
  function toggleTheme() {
    setTheme(theme === "dark" ? "light" : "dark");
  }
  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

// En cualquier punto debajo del provider:
const { theme, toggleTheme } = useContext(ThemeContext);
return <button onClick={toggleTheme}>Cambiar tema</button>;
```

| Pieza | Trabajo |
| :--- | :--- |
| `createContext()` | Crea el canal — expórtalo desde su propio archivo |
| `<Ctx.Provider value={...}>` | Publica el valor; envuelve el subárbol que lo necesita |
| `useContext(Ctx)` | Suscribe un componente al canal |
| Componente provider | Posee el estado (`useState`) para que los consumidores solo lean y llamen |

---

## 📡 Obtención de Datos

`fetch()` es JS nativo. Es un efecto secundario, así que vive en `useEffect` — y necesita
un indicador de carga y una ranura de error, porque todo request tiene tres futuros:

```js
const [data, setData] = useState([]);
const [isLoading, setIsLoading] = useState(false);
const [error, setError] = useState(null);

useEffect(function() {
  async function loadData() {
    setIsLoading(true);
    try {
      const response = await fetch("https://api.thecatapi.com/v1/images/search?limit=10");
      if (response.ok === false) {
        // fetch() se resuelve en 404/500 — comprueba el indicador tú mismo
        throw new Error("Failed to fetch data");
      }
      const json = await response.json();
      setData(json);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  }
  loadData();
}, []); // [] = una vez; omitirlo = bucle infinito de requests

// Renderizando los tres estados:
{isLoading && <p>Cargando...</p>}
{error && <div>{error}</div>}
{!error && !isLoading && data.length > 0 && <GildedList items={data} />}
```

### Filtrar el resultado

```js
const filteredRelics = relicList.filter(function(relic) {
  return relic.name.toLowerCase().startsWith(searchTerm.toLowerCase());
});
```

La lista maestra queda intacta; la lista de pantalla se **deriva** en cada render.

---

## 🗺️ Enrutado

El enrutado del lado del cliente cambia componentes **en el navegador** — sin recargar la
página. El paquete es `react-router-dom`:

```bash
npm install react-router-dom
```

| Pieza | Rol |
| :--- | :--- |
| `<BrowserRouter>` | Uno por app; envuelve todo en el punto de entrada |
| `<Routes>` | Elige el `<Route>` que coincide con la URL actual |
| `<Route>` | `path` + `exact` + `element` — el componente a inyectar |
| `<Link to>` | Navegación interna sin recarga (reemplaza a `<a href>`) |
| `useNavigate()` | Navegación programática |

```js
<Routes>
  <Route path="/" exact element={<Home />} />
  <Route path="/codex" exact element={<Codex />} />
</Routes>

const navigate = useNavigate();
navigate("/codex");  // ir
navigate(-1);        // atrás — caminar por el historial
navigate(1);         // adelante
```

---

## 🎨 Estilos

Tres capas, un hogar por regla — desde el proyecto final de [[15 - El Jefe Final]]:

| Capa | Vive en | Ejemplos |
| :--- | :--- | :--- |
| Global | `index.css` | `html { font-family: Arial; min-height: 100vh; }` |
| Reglas de componente | la misma hoja, con selectores con alcance | `form input { width: 400px; }`, `nav a:hover` |
| Contenido dinámico de API | clases dedicadas | `.artwork img { max-width: 30%; border-radius: 10px; }` |

```css
html {
  display: flex;
  flex-direction: column; /* apila los hijos de arriba abajo */
  align-items: center;
  min-height: 100vh;      /* llena el viewport incluso con poco contenido */
}

.artwork img {
  max-width: 30%;         /* cinturón de seguridad para tamaños de imagen no controlados */
}
```

El `style={{ }}` inline funciona pero rompe la capas — solo propiedades en camelCase
(`backgroundColor`, no `background-color`).

---

## ⚠️ Trampas que Vale la Memoria

| Trampa | Qué pasa de verdad |
| :--- | :--- |
| Enviar sin `preventDefault` | Recarga completa de página; todo el estado perdido |
| `<select>` no controlado | Pon `value` en el padre, no `selected` en las opciones |
| `useEffect` con un objeto cambiante en deps | Se re-ejecuta en cada render — las deps comparan por identidad |
| Intervalo sin limpieza | Sigue disparando tras el desmonte — devuelve una desmontada |
| Mutar `ref.current` para la UI | Nada en pantalla cambia — los refs no re-renderizan |
| `<a href>` dentro de la app | La SPA mata el documento; usa `<Link to>` |
| Dos `<BrowserRouter>` | Dos mapas rivales de la URL — un solo marco |
| Olvidar el export de `createContext` | Cada consumidor crea un context nuevo y silencioso |

---

## 🔗 Ver También

- [[00b - Chuleta de React]] — JSX, componentes, props, estado y eventos (capítulos 01–09)
- [[10 - La Fragua]] — el patrón de formulario controlado detrás de la lista
- [[13 - El Mensajero]] — la historia completa de fetch/carga/error
- [[15 - El Jefe Final]] — cada patrón de esta chuleta, ensamblado en una SPA

---
