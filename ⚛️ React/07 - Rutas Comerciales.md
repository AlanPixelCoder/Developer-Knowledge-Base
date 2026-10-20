# 07. Rutas Comerciales

**Versión original en inglés:** [07 - Trade Routes.md](07%20-%20Trade%20Routes.md)

**Curso:** React
**Tema:** props, pasar props, recibir props, props como cualquier tipo de JavaScript, renderizar listas con `.map()`, estado como props, listas de componentes y mapeo de estado
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-01_--_06-7C5CFF?style=for-the-badge" alt="Lecciones">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

Las caravanas mueven mercancías entre los puestos de Emberfall; las **props** mueven
datos entre tus componentes. El árbol de [[06 - El Árbol de Habilidades]] dio a cada
componente un lugar — este capítulo les da una voz. Al final pasarás props a notificaciones
y menús, renderizarás catálogos enteros con `.map()`, entregarás estado como props y
construirás una galería de reliquias que mapea datos en componentes. Referencia:
[[00b - Chuleta de React]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Las **props** (abreviatura de *properties*) son fragmentos de datos entregados a
> elementos y componentes JSX — el mecanismo del flujo de información **unidireccional**
> padre → hijo de React — y pueden ser de cualquier tipo de JavaScript: cadenas, booleanos,
> objetos, funciones.

---

## 01. Caravanas de Datos

> [!NOTE]
> **Información clave**
> Las props son los fragmentos de datos que entregas a elementos y componentes JSX, y la
> única carretera autorizada del flujo de información **unidireccional** padre → hijo. Un
> padre empaqueta datos; el hijo los recibe y los renderiza.

Dos hechos mantienen honestas a las caravanas:

- **Las props son de solo lectura.** Un hijo nunca edita las props que recibe — las
  muestra. Cambiar datos significa cambiarlos en el padre, que luego vuelve a renderizar al
  hijo (la regla unidireccional de [[06 - El Árbol de Habilidades]]).
- **Todo es una prop.** Los atributos que has usado todo el rato — `src`, `alt`, `href`,
  `id` — son props de elementos HTML normales. Tus propios componentes simplemente añaden
  otras nuevas.

```js
// Props en un elemento HTML normal
<img src="/avatar.png" alt="Avatar" />

// Props en tu propio componente
<Notification message="Incursión esta noche" isRead={true} />
```

---

## 02. Enviar un Paquete

### Pasar props

Las props se escriben **exactamente como atributos HTML**, en la etiqueta de apertura,
separadas por espacios:

```js
<Notification message="¡El festín de GuildMasterVex es hoy!" isRead={true} />
```

- `message="..."` — una **cadena**, escrita entre comillas, igual que `alt` o `src`.
- `isRead={true}` — un **booleano**, escrito entre llaves porque `{true}` es una
  expresión JavaScript.

### Cualquier tipo de JavaScript viaja por la ruta

Las llaves `{}` abren la ruta a cualquier tipo que tenga JavaScript:

| Tipo | Cómo se pasa | Ejemplo |
| :--- | :--- | :--- |
| **Cadena** | comillas o llaves | `message="¡El festín de GuildMasterVex es hoy!"` |
| **Booleano** | literal dentro de llaves | `isRead={true}` |
| **Número** | literal dentro de llaves | `attendees={120}` |
| **Objeto / array** | expresión dentro de llaves | `event={{ title: "Noche de Arena" }}` |
| **Función** | referencia **sin** paréntesis | `onRead={markAsRead}` |

> [!WARNING]
> **El error que todos cometen una vez**
> Escribir `isRead="false"` — una cadena no vacía es **verdadera**, así que el componente
> ve `true`. Las cadenas mienten sobre los booleanos; usa `{false}`. Y nunca escribas
> `onRead={markAsRead()}` con paréntesis: eso **llama** a la función durante el render en
> vez de pasarla.

### Misión: Dos Etiquetas

Envía un `Notification` con tres props: una cadena `message` sobre el torneo de arena de
esta noche, `isRead={false}` y una prop numérica `attendees={64}`. Después predice qué
imprime el hijo cuando hagas `console.log(props)` — y compruébalo en la siguiente
sección.

---

## 03. Abrir el Paquete

### Recibir props

Un componente recibe las props como su **único parámetro**, convencionalmente llamado
`props` — y `props` es un objeto:

```js
function GuildCanteen(props) {
  console.log(props);
  return (
    <div className="menu-card">
      <h2>{props.dish}</h2>
      <p>{props.description}</p>
    </div>
  );
}
```

Usado desde un padre:

```js
<GuildCanteen dish="Guiso de Brasa" description="Restaura 40 PV. Se sirve caliente." />
```

Lo que imprime `console.log(props)` es un solo objeto:

```json
{ "dish": "Guiso de Brasa", "description": "Restaura 40 PV. Se sirve caliente." }
```

Tres reglas del paquete:

1. **Un solo parámetro.** Por muchas props que sean, llegan juntas dentro de ese único
   objeto.
2. **Acceso con punto.** `props.dish`, `props.description` — el mismo acceso a propiedades
   de JavaScript puro.
3. **Llaves para leer.** Dentro de JSX, `{props.dish}` evalúa la expresión e imprime el
   valor.

> [!TIP]
> La destructuración es el atajo: `function GuildCanteen({ dish, description }) { ... }`
> desempaqueta el objeto en la lista de parámetros. Los datos que llegan son idénticos —
> solo se desempaquetan antes de usarlos.

---

## 04. La Caravana del Catálogo

### Renderizar listas con `.map()`

Una tienda es la misma tarjeta cincuenta veces. En vez de cincuenta copias de JSX, guardas
una plantilla y dejas que **`.map()`** la estampe una vez por artículo — el método de array
de la vault de JavaScript, ahora moviendo marcado:

```js
const catalogItems = [
  { name: "Fragmento de Brasa", category: "Fabricación" },
  { name: "Linterna del Guardián", category: "Equipo" },
  { name: "Hoja Ceniza", category: "Arma" },
];

export default function Catalog() {
  return (
    <div>
      {catalogItems.map(function (item) {
        return (
          <div>
            <h2>{item.name}</h2>
            <h3>Especialidad: {item.category}</h3>
          </div>
        );
      })}
    </div>
  );
}
```

Léelo como una transacción: **por cada `item` en `catalogItems`, devuelve este bloque de
marcado** — y `.map()` recoge todos los bloques devueltos en un array de elementos que
React renderiza en orden.

> [!TIP]
> Añade un `key` al elemento más externo de cada bloque devuelto — `key={item.name}` — y
> React podrá distinguir a los hermanos cuando la lista cambie. La consola te recuerda si
> lo olvidas; el resto del patrón sigue siendo exactamente el mismo.

### Misión: Reabastecer los Estantes

Haz que `catalogItems` tenga cinco artículos y añade una tercera línea por tarjeta:
`<p>{item.category}</p>`. Confirma que aparecen cinco tarjetas desde una sola plantilla —
luego borra dos artículos del array y mira cómo desaparecen dos tarjetas. La plantilla
nunca cambió; cambiaron los datos.

---

## 05. El Marcador Compartido

### Estado como props

Las props se ponen interesantes cuando los datos de arriba son **estado**. El componente
`Game` posee las puntuaciones; los hijos `Player` solo las reciben:

```js
import React, { useState } from "react";
import Player from "./Player.js";

export default function Game() {
  const [scores, setScores] = useState([0, 0, 0]);

  return (
    <div>
      <Player score={scores[0]} />
      <Player score={scores[1]} />
      <Player score={scores[2]} />
    </div>
  );
}
```

```js
export default function Player(props) {
  return (
    <div className="player-row">
      <span>Puntuación: {props.score}</span>
    </div>
  );
}
```

Un solo `useState([0, 0, 0])` arriba, tres caravanas `<Player score={...} />` abajo. Los
beneficios son los dos pilares del diseño guiado por props:

- **Reutilizabilidad** — `Player` sigue siendo **abstracto**. Renderiza cualquier número
  que llegue en `props.score`; no sabe ni le importa si es el jugador uno o el tres.
- **Fuente única de verdad** — las puntuaciones viven en **un** solo lugar. El día en que
  `Game` llame a `setScores`, el padre se vuelve a renderizar y cada hijo se renderiza de
  nuevo con las cifras frescas. Ningún hijo guarda una copia privada que pueda desincronizarse.

---

## 06. La Galería de Reliquias

### Listas de componentes y mapeo de estado

El patrón final combina todo lo de este capítulo: una **lista de componente** recibe un
array a través de props, lo `.map()`ea en **componentes hijos**, y cada hijo renderiza su
propio fragmento de datos. La forma antigua de la galería de películas, rehecha como
catálogo de objetos:

| Galería de películas | Galería de reliquias de Emberfall |
| :--- | :--- |
| `<TrendingList>` | `<RelicList>` |
| `props.movies` | `props.relics` |
| `<Movie title releaseYear imageUrl />` | `<Relic name rarity imageUrl />` |

El componente de lista hace el mapeo:

```js
import React from "react";
import Relic from "./Relic.js";

export default function RelicList(props) {
  return (
    <div className="relic-list">
      {props.relics.map(function (relic) {
        return (
          <Relic
            name={relic.name}
            rarity={relic.rarity}
            imageUrl={relic.imageUrl}
          />
        );
      })}
    </div>
  );
}
```

El hijo recibe a través de `props` y renderiza cada campo:

```js
export default function Relic(props) {
  return (
    <div className="relic-card">
      <img src={props.imageUrl} alt={props.name} />
      <h3>{props.name}</h3>
      <p>Rareza: {props.rarity}</p>
    </div>
  );
}
```

La caravana llega en tres saltos: `App` → `RelicList` (el array) → cada `Relic` (los
datos de una reliquia). Un `.map()`, una plantilla por tarjeta, cero marcado duplicado.

### Misión: Quinta Reliquia

Añade una cuarta reliquia al array y renderiza la lista con
`<RelicList relics={relicItems} />`. Luego dale a `Relic` una prop nueva — `origin` — e
imprímela debajo de la rareza. Solo cambian dos archivos: el padre que empaqueta el
paquete, y el hijo que lo abre.

---

## ⚡ XP Ganados: Ideas Clave

- 📦 Las **props** son fragmentos de datos entregados a elementos y componentes JSX — la
  carretera **unidireccional** padre → hijo de React.
- ✍️ Pasa props como atributos HTML; léelas en el hijo como `props.name` dentro de llaves
  `{}`.
- 🧳 Viaja cualquier tipo de JavaScript: cadenas, booleanos, números, objetos, funciones —
  llaves para todo lo que no sea una cadena simple.
- 🚫 Las props son de **solo lectura**; los hijos muestran, los padres deciden.
- 🔁 `{items.map(function (item) { return <Card />; })}` estampa un elemento por artículo.
- 🏆 El estado pasado como props te da reutilizabilidad y una **fuente única de verdad**.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🔔 Notificaciones, avisos e insignias alimentadas por props desde un almacén central
- 🛒 Rejillas de productos y catálogos renderizadas con `.map()` desde una plantilla
- 🏆 Marcadores, clasificaciones y listas de jugadores — estado arriba, números abajo
- 🎨 Variantes de tema y tamaño: un solo componente `<Button color="ember" size="lg" />`,
  muchos aspectos
- 🧾 Campos de formulario renderizados desde un array de configuración (`label`, `type`,
  `placeholder` como props)

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Dale a `Notification` una cuarta prop `type="raid"` y renderízala como insignia en el
   hijo.
2. Escribe un componente `HealthBar` que reciba las props `current` y `max` y renderice
   ambos números.
3. Convierte tu catálogo en un `.map()` sobre un array de cuatro artículos — sin tarjetas
   duplicadas.
4. Extiende `Game` a cuatro jugadores añadiendo `<Player score={scores[3]} />` y un cuarto
   valor inicial.
5. **Pelea de jefe:** construye un `<GuildRoster members={memberList} />` donde `members`
   es un array de objetos (`{ name, className, level }`), mapeado a un hijo `MemberCard`
   que renderiza los tres campos a través de props — array dentro, lista de componentes
   fuera.

---

## 🔗 Ver También

- [[00b - Chuleta de React]] — sintaxis de props, paso de datos y `.map()` en una página
- [[05 - Bloques de Construcción]] — capítulo anterior: los componentes por los que viajan
  estos paquetes
- [[06 - El Árbol de Habilidades]] — capítulo anterior: el árbol padre-hijo por el que
  bajan las props
- [[08 - La Barra de Vida]] — siguiente capítulo: el estado, el dato que cambia por sí solo
- [[09 - El Mando]] — más adelante: pasar funciones como props para manejar eventos reales
- [[04 - Marcado Vivo]] — expresiones dentro de `{}` y renderizado condicional junto a tus
  listas

---
