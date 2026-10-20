# ⚛️ React: El Renacimiento de la Interfaz (MOC)

**English:** [README.md](./README.md)

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO_A_AVANZADO-F0AD4E?style=for-the-badge" alt="De intermedio a avanzado">
  <img src="https://img.shields.io/badge/Cap%C3%ADtulos-15-7C5CFF?style=for-the-badge" alt="15 capítulos">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
  <img src="https://img.shields.io/badge/Entorno-macOS-lightgrey?style=for-the-badge&logo=apple&logoColor=white" alt="macOS">
</p>

**Nota:**
Este módulo es el Mapa de Contenidos (MOC) de las notas de React de este vault de Obsidian.
React es la biblioteca que convierte páginas estáticas en interfaces vivas — componentes que
se actualizan solos cuando cambian los datos, formularios que gestionan su propio estado,
efectos que alcanzan APIs externas y un enrutador que hace que un solo documento HTML se
sienta como un sitio web completo. Todos los ejemplos son mínimos y construyen el mismo
producto ficticio: el sitio companion de *Emberfall Online*, un panel de gremio, tienda y
red social para el roguelike compartido de la vault.

**Consejo:**
Empieza por [[01 - El Renacimiento]]. Aprende qué es React y por qué existen los componentes
antes de tocar JSX o hooks — cuando el modelo mental de componentes sea memoria muscular, todo
lo demás de este módulo es composición.

**Requisito previo:** [MOC de 🟨 JavaScript](../%F0%9F%9F%A8%20JavaScript/README-ES.md). Este
módulo asume que variables, tipos, funciones, objetos, arreglos y eventos del DOM ya te son
familiares — en particular [[08 - HUD Vivo]] es el predecesor directo de todo lo que viene.
El [MOC de 🌐 HTML](../%F0%9F%8C%90%20HTML/README-ES.md) y el [MOC de 🎨 CSS](../%F0%9F%8E%A8%20CSS/README-ES.md)
completan el trío: React consume la estructura que HTML provee y coexiste con los estilos que
escribe CSS.

> [!NOTE]
> **La narrativa de Emberfall**
> Todos los ejercicios de este módulo pertenecen al mismo producto ficticio: el sitio
> companion de *Emberfall Online*. El HUD del gremio se vuelve un árbol de componentes, la
> publicación social se vuelve un ejercicio de composición, el catálogo de reliquias se vuelve
> un `.map()` sobre el estado, el botón de asistencia a la Arena se vuelve un ejercicio de
> accesibilidad, el cuestionario de clases se vuelve el capstone SPA. La sintaxis no cambia
> entre ejercicios — y ese es el punto: aprendes un solo vocabulario y lo reutilizas en todas
> partes.

---

## 🗺️ Mapa de Contenidos

### 📚 Referencia y Chuletas

* **Chuletas:**
  * [00b - Chuleta de React](./00b%20-%20Chuleta%20de%20React.md) — JSX, componentes, composición, props, estado y eventos.
  * [00c - Chuleta de React II](./00c%20-%20Chuleta%20de%20React%20II.md) — formularios, hooks, contexto, obtención de datos, enrutamiento y estilos.

### 🏛️ I. La Interfaz Renacida (Capítulos 1–4)

* **El Renacimiento:** [01 - El Renacimiento](./01%20-%20El%20Renacimiento.md) — Qué es React, su origen en 2013 en Facebook, diseño declarativo y basado en componentes, antes vs. con React.
* **Punto de Aparición:** [02 - Punto de Aparición](./02%20-%20Punto%20de%20Aparici%C3%B3n.md) — Node.js y npm, andamiaje con Vite, el servidor de desarrollo, hot reloading, estructura del proyecto y el contenedor de montaje `createRoot`.
* **Taller de Glifos:** [03 - Taller de Glifos](./03%20-%20Taller%20de%20Glifos.md) — Qué es JSX, transpilación a `React.createElement`, sintaxis básica de componentes y la regla de los paréntesis.
* **Marcado Vivo:** [04 - Marcado Vivo](./04%20-%20Marcado%20Vivo.md) — La regla de raíz única, fragmentos, expresiones incrustadas, renderizado condicional, atributos y `className`.

### ⚙️ II. El Oficio de Componentes (Capítulos 5–8)

* **Bloques de Construcción:** [05 - Bloques de Construcción](./05%20-%20Bloques%20de%20Construcci%C3%B3n.md) — Componentes funcionales, PascalCase, export/import, composición e instanciación.
* **El Árbol de Habilidades:** [06 - El Árbol de Habilidades](./06%20-%20El%20%C3%81rbol%20de%20Habilidades.md) — Composición, jerarquía, relaciones padre-hijo, flujo de datos unidireccional y la publicación del gremio.
* **Rutas Comerciales:** [07 - Rutas Comerciales](./07%20-%20Rutas%20Comerciales.md) — Props, recepción de props, listas con `.map()`, estado como props y listas de componentes sobre arreglos de estado.
* **La Barra de Vida:** [08 - La Barra de Vida](./08%20-%20La%20Barra%20de%20Vida.md) — `useState`, el setter, la regla de inmutabilidad, temporizadores y actualizaciones funcionales.

### 🎮 III. Interacción y Entrada (Capítulos 9–10)

* **El Mando:** [09 - El Mando](./09%20-%20El%20Mando.md) — Eventos sintéticos, `onClick`, objeto de evento, hover, focus/blur, eventos de teclado y composición accesible.
* **La Fragua:** [10 - La Fragua](./10%20-%20La%20Fragua.md) — Formularios, `htmlFor`, `onChange`, `onSubmit`, componentes controlados, `select`/`textarea` y la lista de verificación.

### ✨ IV. Hooks, Estado y Datos (Capítulos 11–13)

* **El Sistema de Reliquias:** [11 - El Sistema de Reliquias](./11%20-%20El%20Sistema%20de%20Reliquias.md) — Hooks, `useEffect`, el arreglo de dependencias, limpieza, `useRef` y estado vs. refs.
* **El Libro del Gremio:** [12 - El Libro del Gremio](./12%20-%20El%20Libro%20del%20Gremio.md) — Prop drilling, la Context API, `createContext`, proveedores, `useContext` y componentes proveedor personalizados.
* **El Mensajero:** [13 - El Mensajero](./13%20-%20El%20Mensajero.md) — `fetch()`, promesas, estados de carga, `try/catch`, `response.ok`, renderizado de errores y filtrado de listas.

### 🗺️ V. El Producto Completo (Capítulos 14–15)

* **El Mapa del Mundo:** [14 - El Mapa del Mundo](./14%20-%20El%20Mapa%20del%20Mundo.md) — SPAs, enrutamiento del lado del cliente, `react-router-dom`, `BrowserRouter`, `Routes`, `Link` y `useNavigate`.
* **El Jefe Final:** [15 - El Jefe Final](./15%20-%20El%20Jefe%20Final.md) — El capstone: el SPA del cuestionario "¿Qué clase de Emberfall eres?", arquitectura, lógica, rutas condicionales y estilos.

---

## 🎯 Ruta de Aprendizaje

1. **El Renacimiento** → entiende el modelo: UI declarativa, componentes, actualizaciones unidireccionales.
2. **Punto de Aparición** → prepara la fragua: Node, Vite, el servidor de desarrollo y el contenedor raíz.
3. **Taller de Glifos** → aprende el alfabeto: JSX y en qué se transpila.
4. **Marcado Vivo** → haz que el marcado piense: expresiones, condicionales, atributos.
5. **Bloques de Construcción** → escribe componentes: la unidad de todo lo demás.
6. **El Árbol de Habilidades** → compón: jerarquías, padres e hijos.
7. **Rutas Comerciales** → pasa datos: props, listas y estado fluyendo hacia abajo.
8. **La Barra de Vida** → guarda datos: estado que cambia y re-renderiza.
9. **El Mando** → reacciona al jugador: eventos, ratón, teclado, accesibilidad.
10. **La Fragua** → recoge entrada: formularios controlados de `onChange` al envío.
11. **El Sistema de Reliquias** → alcanza fuera: efectos, limpieza, refs.
12. **El Libro del Gremio** → globaliza: contexto en lugar de prop drilling.
13. **El Mensajero** → habla con APIs: fetch, promesas, carga y errores.
14. **El Mapa del Mundo** → añade páginas: enrutamiento sin recargas.
15. **El Jefe Final** → entrega el producto: todo en un SPA de cuestionario.

---

## 🎯 Qué Sabrás Hacer

- Andamiaje una app React con Vite y explicar cada archivo del árbol del proyecto.
- Escribir JSX, saber en qué se transpila y respetar sus reglas de formato.
- Construir y componer componentes funcionales con PascalCase y exports correctos.
- Pasar props, renderizar listas con `.map()` y fluir estado hacia los hijos.
- Gestionar estado con `useState`, actualizarlo inmutablemente y usar actualizaciones funcionales.
- Manejar eventos de ratón, foco y teclado accesiblemente con eventos sintéticos.
- Construir formularios controlados: `htmlFor`, `onChange`, `onSubmit`, `select` y `textarea`.
- Ejecutar efectos secundarios con `useEffect`, limpiarlos y guardar datos mutables con `useRef`.
- Compartir estado globalmente con la Context API y proveedores personalizados.
- Obtener datos de APIs con estados de carga, manejo de errores y filtrado de listas.
- Enrutar entre vistas con `react-router-dom` sin recargas de página completas.
- Ensamblar todo en una aplicación de página única completa.

---

## 🧰 Herramientas

| Herramienta | Por qué |
| :--- | :--- |
| Node.js y npm | Entorno de ejecución y gestor de paquetes de la cadena de herramientas de React |
| Vite | Herramienta de compilación y servidor de desarrollo con hot reloading |
| Cualquier editor de código (VS Code recomendado) | Escribir archivos de componentes `.jsx` |
| Un navegador moderno con DevTools | Ejecutar la app, inspeccionar componentes, ver renders |
| Obsidian (esta vault) | Mantener notas, chuletas y ejercicios en un solo lugar |

---

## 🗺️ Mapa del Curso

| # | Nota | Lecciones | Qué aprendes |
| --- | --- | --- | :--- |
| 00b | [00b - Chuleta de React](./00b%20-%20Chuleta%20de%20React.md) | — | JSX, componentes, props, estado, eventos |
| 00c | [00c - Chuleta de React II](./00c%20-%20Chuleta%20de%20React%20II.md) | — | Formularios, hooks, contexto, fetching, enrutamiento, estilos |
| 01 | [01 - El Renacimiento](./01%20-%20El%20Renacimiento.md) | 01–05 | Qué es React, su historia, diseño declarativo, antes vs. con |
| 02 | [02 - Punto de Aparición](./02%20-%20Punto%20de%20Aparici%C3%B3n.md) | 01–07 | Node, npm, Vite, hot reloading, estructura, `createRoot` |
| 03 | [03 - Taller de Glifos](./03%20-%20Taller%20de%20Glifos.md) | 01–06 | JSX, transpilación, `React.createElement`, sintaxis de componentes |
| 04 | [04 - Marcado Vivo](./04%20-%20Marcado%20Vivo.md) | 01–08 | Raíz única, fragmentos, expresiones, condicionales, atributos |
| 05 | [05 - Bloques de Construcción](./05%20-%20Bloques%20de%20Construcci%C3%B3n.md) | 01–05 | Componentes funcionales, PascalCase, export/import, composición |
| 06 | [06 - El Árbol de Habilidades](./06%20-%20El%20%C3%81rbol%20de%20Habilidades.md) | 01–06 | Composición, jerarquía, padre-hijo, flujo unidireccional |
| 07 | [07 - Rutas Comerciales](./07%20-%20Rutas%20Comerciales.md) | 01–06 | Props, listas `.map()`, estado como props, listas de componentes |
| 08 | [08 - La Barra de Vida](./08%20-%20La%20Barra%20de%20Vida.md) | 01–06 | `useState`, setter, inmutabilidad, temporizadores, actualizaciones funcionales |
| 09 | [09 - El Mando](./09%20-%20El%20Mando.md) | 01–06 | Eventos sintéticos, onClick, objeto de evento, hover, foco, teclado |
| 10 | [10 - La Fragua](./10%20-%20La%20Fragua.md) | 01–07 | Formularios, htmlFor, onChange, onSubmit, componentes controlados |
| 11 | [11 - El Sistema de Reliquias](./11%20-%20El%20Sistema%20de%20Reliquias.md) | 01–06 | Hooks, useEffect, limpieza, useRef, estado vs. refs |
| 12 | [12 - El Libro del Gremio](./12%20-%20El%20Libro%20del%20Gremio.md) | 01–06 | Prop drilling, Context API, proveedores, useContext |
| 13 | [13 - El Mensajero](./13%20-%20El%20Mensajero.md) | 01–06 | fetch, promesas, carga, errores, filtrado de listas |
| 14 | [14 - El Mapa del Mundo](./14%20-%20El%20Mapa%20del%20Mundo.md) | 01–06 | SPAs, react-router-dom, BrowserRouter, Routes, Link, useNavigate |
| 15 | [15 - El Jefe Final](./15%20-%20El%20Jefe%20Final.md) | 01–07 | SPA capstone: arquitectura, lógica, rutas, estilos |

---

## 🎮 Filosofía de Práctica

El código es una máquina que construyes escribiendo. Los ejercicios mantienen ese principio:
cada fragmento se ejecuta tal cual está escrito — los comentarios indican la salida que
deberías obtener de verdad. Cuando algo parezca mal, abre DevTools, encuentra el componente
en la pestaña de Components y compara los props y el estado reales con los que esperabas.

Cada capítulo termina con misiones secundarias que combinan los conceptos del capítulo en una
función completa — el HUD del gremio, la publicación social, el botón de asistencia a la Arena,
la búsqueda del bestiario, el cuestionario de clases — para que nada se quede como dato
aislado.

---

## 🔗 Ver También

- [MOC de 🟨 JavaScript](../%F0%9F%9F%A8%20JavaScript/README-ES.md) — el lenguaje en que se escribe React; requisito previo
- [MOC de 🌐 HTML](../%F0%9F%8C%90%20HTML/README-ES.md) — la estructura cuyo DOM React reemplaza
- [MOC de 🎨 CSS](../%F0%9F%8E%A8%20CSS/README-ES.md) — la mitad de estilos de las mismas páginas
- [MOC de 🟣 CSharp](../%F0%9F%9F%A3%20CSharp/README-ES.md) — el equivalente fuertemente tipado, con el mismo enfoque game-first

---
