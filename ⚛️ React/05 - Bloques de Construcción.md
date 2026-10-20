# 05. Bloques de Construcción

**Versión original en inglés:** [05 - Building Blocks.md](05%20-%20Building%20Blocks.md)

**Curso:** React
**Tema:** componentes funcionales, reglas de nombrado de componentes, PascalCase, export e import, composición de componentes, definir frente a instanciar, comentarios JSX
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-01_--_05-7C5CFF?style=for-the-badge" alt="Lecciones">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

El sitio companion de Emberfall no es una sola pantalla — son decenas de piezas pequeñas:
un widget de vida, una fila de misión, un botón de seguir, un banner de saludo. Hasta ahora
has estado pegando JSX crudo en un solo archivo. Este capítulo presenta los **bloques de
construcción** con los que React está hecho de verdad: los **componentes funcionales** —
unidades reutilizables que nombras, exportas, importas y renderizas como sellos en un
taller. Al final habrás forjado un componente `Greetings` y lo habrás invocado desde `App`.
La referencia rápida de todo el capítulo está en [[00b - Chuleta de React]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Un componente de React es una función JavaScript normal y corriente nombrada en
> **PascalCase** que devuelve JSX, que se envía con `export default` y que se invoca dentro
> de otro componente con un import y una etiqueta autocontenida como `<Greetings />`.

---

## 01. El Patio de Construcción

> [!NOTE]
> **Información clave**
> Los componentes son los **bloques de construcción** principales de la interfaz de usuario
> en React. JSX es el lenguaje visual; los componentes son las **unidades funcionales**. Un
> componente funcional es una función JavaScript que devuelve JSX — React renderiza como si
> fuera una etiqueta HTML cualquier función cuyo nombre empieza por mayúscula.

Cada pantalla del panel del gremio es una pila de estas unidades. La separación de
responsabilidades es sencilla:

| Capa | Trabajo | Ejemplo |
| :--- | :--- | :--- |
| **JSX** | Describe cómo **se ve** la interfaz | `<h1>¡Bienvenido!</h1>` |
| **Componente** | Envuelve una pieza de interfaz que puedes **reutilizar y nombrar** | `function Greetings() { ... }` |

Las reglas de JSX de [[03 - Taller de Glifos]] y las expresiones de [[04 - Marcado Vivo]]
viven **dentro** del `return` de un componente. Los componentes son las cajas en las que
esas reglas se embarcan: un componente, un trabajo, un archivo.

> [!TIP]
> Piensa en los componentes como en piezas prefabricadas. La barra de vida, la tarjeta de
> misión y la cabecera con el avatar se construyen una vez y se estampan donde haga falta —
> cambia la pieza y todas sus copias del sitio se actualizan.

---

## 02. Los Ritos del Nombre

### Las tres reglas clave

> [!NOTE]
> **Información clave**
> Tres reglas deciden si React acepta tu componente: nombrado en **PascalCase** (React
> distingue los componentes de las etiquetas HTML por la letra inicial mayúscula), un
> **único elemento raíz** por return y **`export default`** para tener acceso al módulo.

| Regla | Requisito | Por qué existe |
| :--- | :--- | :--- |
| **PascalCase** | `Greetings`, nunca `greetings` | React distingue componentes de etiquetas HTML por esa mayúscula inicial |
| **Único elemento raíz** | Un solo raíz por `return`; envuelve los hermanos en un `<div>` o en un Fragment | Un return solo puede exponer un árbol — la regla de [[04 - Marcado Vivo]] |
| **`export default`** | `export default function Greetings() { ... }` | Da a otros archivos acceso al módulo del componente |

### Misión: Comprobación de Nombres

Audita tres nombres antes que React: `guildHeader` (en minúscula — React lo leería como
una etiqueta HTML), `guild_header` (snake_case — un estilo de nombre que los componentes
nunca usan) y `GuildHeader` (PascalCase — el único que sale del taller). Renombra tu último
componente a PascalCase y comprueba que la etiqueta que escribes en JSX coincide con él
**carácter a carácter**.

> [!WARNING]
> **El error que todos cometen una vez**
> Escribes `<greetings />` en minúscula y React no se queja — trata `greetings` como un
> elemento HTML desconocido y no renderiza nada útil. La misma trampa al otro lado: defines
> un componente, olvidas `export default`, lo importas y el import es `undefined`. Los dos
> fallos son silenciosos hasta que te quedas mirando una pantalla en blanco.

---

## 03. La Primera Forja

### Construir `Greetings`

A forjar. Un componente, un archivo, las tres reglas aplicadas:

```js
import React from "react";

export default function Greetings() {
  return (
    <div>
      <h1>¡Bienvenido de nuevo, Guardián del Noveno Piso!</h1>
      <p>La cola de la incursión de las Salas Profundas está abierta.</p>
    </div>
  );
}
```

Anatomía del archivo:

- `import React from "react";` — la línea de apertura estándar de un archivo de componente.
- `export default function Greetings() { ... }` — la función **es** el componente, y el
  export se lo entrega a todos los demás archivos del proyecto.
- `return ( ... );` — los paréntesis evitan que la inserción automática de punto y coma
  corte el JSX multilínea, tal como en [[03 - Taller de Glifos]].
- El raíz `<div>` satisface la regla de un solo elemento; el `<h1>` y el `<p>` viajan
  dentro de él.

### Misión: Heraldo

Escribe un segundo componente llamado `QuestStatus` que informe el progreso de hoy.
Mantén PascalCase, un solo raíz y el export:

```js
export default function QuestStatus() {
  return (
    <div>
      <h2>Misiones Diarias</h2>
      <p>3 de 5 completadas</p>
    </div>
  );
}
```

Dos archivos, dos componentes, cero código compartido — y ninguno de los dos puede
funcionar solo. Esa es la idea: los componentes están hechos para **usarse**, que es lo que
hace la siguiente sección.

---

## 04. Círculo de Invocación

### Importar y componer

Un componente solo se vuelve útil cuando otro componente lo renderiza. `App.js` importa
`Greetings` y lo deja caer en su marcado con una etiqueta **autocontenida**:

```js
import Greetings from "./Greetings.js";

export default function App() {
  return (
    <div>
      <Greetings />
    </div>
  );
}
```

La mecánica:

- La ruta de import `"./Greetings.js"` apunta al archivo donde vive el componente.
- El nombre importado debe coincidir con el exportado, **incluida la mayúscula**.
- `<Greetings />` es autocontenida — los componentes no llevan etiqueta de cierre cuando
  no tienen hijos, igual que `<img />` o `<br />`.
- Renderizar un componente dentro de otro se llama **composición**: ahora `App` *contiene*
  `Greetings`.

### Misión: Lista Completa

Compón tus dos componentes en `App` — el saludo primero, el rastreador de misiones debajo:

```js
import Greetings from "./Greetings.js";
import QuestStatus from "./QuestStatus.js";

export default function App() {
  return (
    <div>
      <Greetings />
      <QuestStatus />
    </div>
  );
}
```

Guarda el archivo y el servidor de desarrollo imprime los dos bloques. No tocaste
`Greetings` para ponerlo en la página — lo **colocaste**, y React hizo el resto.

---

## 05. Definir e Invocar

### Dos mitades de la misma runa

Cada componente de React recorre el mismo flujo de tres pasos. **Definir** crea el
componente; **instanciar** es el acto de ponerlo en pantalla — y ocurren en archivos
distintos:

1. **Exportar el componente** — `export default function FunctionComponent() { ... }` en su
   propio archivo. Todavía no se renderiza nada.
2. **Importarlo** — `import FunctionComponent from "file/path/to/FunctionComponent.js";`
   en el archivo que lo necesita. Sigue sin renderizarse nada.
3. **Renderizarlo** — escribe `<FunctionComponent />` dentro del marcado de otro
   componente. Ahora está en pantalla.

```js
// 1. Definir y exportar — FunctionComponent.js
export default function FunctionComponent() {
  return <div>Existo en cuanto alguien me renderiza.</div>;
}

// 2. Importar — desde "file/path/to/FunctionComponent.js"
import FunctionComponent from "file/path/to/FunctionComponent.js";

// 3. Instanciar — dentro del return de otro componente
export default function App() {
  return (
    <div>
      <FunctionComponent />
    </div>
  );
}
```

Un componente exportado y sin usar no cuesta nada; un componente que nunca se exporta no
se puede importar jamás. Definir sin instanciar es una pieza prefabricada que sigue en el
patio.

### Comentar dentro del marcado

Dentro de JSX, los comentarios con `//` son **errores de sintaxis** — el analizador está
leyendo marcado, no JavaScript. Los comentarios JSX viven entre llaves, envueltos en un
comentario de bloque:

```js
export default function Greetings() {
  return (
    <div>
      {/* Esta línea nunca llega al DOM */}
      <h1>¡Bienvenido de nuevo, Guardián del Noveno Piso!</h1>
    </div>
  );
}
```

Fuera del marcado — encima de la función, entre imports — los comentarios normales `//` y
`/* ... */` funcionan como siempre. Regla general: **dentro de las etiquetas, usa
`{/* ... */}`.**

---

## ⚡ XP Ganados: Ideas Clave

- 🧱 Los componentes son los **bloques de construcción** principales de React: JSX es el
  lenguaje visual, los componentes son las unidades funcionales.
- 🏷️ **PascalCase** es como React distingue tus componentes de las etiquetas HTML — los
  nombres en minúscula se renderizan como elementos desconocidos.
- 📦 Un **único elemento raíz** por return; `export default` es lo que hace importable a un
  componente.
- 🗡️ `<Greetings />` es una instanciación **autocontenida** — colocar en pantalla un
  componente ya definido.
- 🔁 El flujo es siempre **definir → importar → renderizar**, en tres pasos distintos.
- 💬 `{/* ... */}` es la única sintaxis de comentario que sobrevive dentro del marcado JSX.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🧩 kits de UI reutilizables: botones, tarjetas, insignias y avatares definidos una vez y
  usados en todas las páginas
- 🏗️ sistemas de diseño — una librería de componentes es un patio lleno de piezas exportadas
- 🧱 reparto por funcionalidades: cada equipo envía su propio archivo de componente y lo
  compone en la raíz
- ♻️ diseños sin copias — la misma `Post` estampada en un feed, un perfil y una vista previa
- 📝 JSX legible — `<GuildHeader />` dice más que cincuenta líneas de marcado anidado

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Renombra todos los componentes de este capítulo a camelCase, renderízalos y observa qué
   hace React con una etiqueta en minúscula.
2. Escribe un componente `HealthBar` con un único raíz `<div>` y renderízalo desde `App`.
3. Divide tu `App` en tres componentes (`Header`, `Feed`, `Footer`) y compón los tres con
   imports y etiquetas autocontenidas.
4. Añade un comentario `{/* ... */}` dentro del marcado de cada componente y confirma que
   ninguno llega a la página renderizada.
5. **Pelea de jefe:** construye un componente `GuildRoster` que renderice un `Greetings`
   **y** un `QuestStatus`, y luego importa `GuildRoster` en `App` — un componente que
   invoca a otros componentes, tres niveles de profundidad, con todos los nombres en
   PascalCase.

---

## 🔗 Ver También

- [[00b - Chuleta de React]] — anatomía y reglas de componentes en una página
- [[03 - Taller de Glifos]] — capítulo anterior: JSX, el lenguaje que hablan los componentes
- [[04 - Marcado Vivo]] — capítulo anterior: qué va dentro del `return` de un componente
- [[06 - El Árbol de Habilidades]] — siguiente capítulo: componer componentes en jerarquías
- [[07 - Rutas Comerciales]] — más adelante: enviar datos a los componentes con props
- [[08 - La Barra de Vida]] — más adelante: componentes que recuerdan cosas con estado

---
