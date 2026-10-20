# 13. El Mensajero

**Versión original en inglés:** [13 - The Courier.md](13%20-%20The%20Courier.md)

**Curso:** React
**Tema:** fetch(), obtención de datos como efecto secundario, promesas, estado de carga, try/catch, response.ok, renderizado de errores y filtrado de listas
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO_A_AVANZADO-F0AD4E?style=for-the-badge" alt="Intermedio a avanzado">
  <img src="https://img.shields.io/badge/Lecciones-01_--_06-7C5CFF?style=for-the-badge" alt="Lecciones 01 a 06">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

Todo lo construido hasta ahora funciona con datos que ya estaban dentro de la app. El
sitio companion de Emberfall no funciona así: el feed de assets de gatos dorados, la
lista del gremio y la bóveda de reliquias viven detrás de **APIs**. Este capítulo te
entrega al mensajero que corre a por ellas — la API nativa `fetch()`, llamada desde
dentro de `useEffect` — más los tres futuros que todo request puede tener (esperando,
entregado, fallido) y el banco de búsqueda que filtra lo que sea que llegue. La
referencia rápida de este capítulo y del resto de la segunda mitad del módulo:
[[00c - Chuleta de React II]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Obtén datos remotos dentro de `useEffect` y luego maneja los tres desenlaces posibles
> — aún cargando, entregado o fallido — antes de renderizar la lista filtrada que el
> jugador de verdad quiere ver.

---

## 01. El Gremio de Mensajeros

> [!NOTE]
> **Información clave**
> `fetch()` es parte de **JavaScript nativo** — no requiere librería. El único trabajo de
> React es decidir **cuándo** se ejecuta: obtener datos es un **efecto secundario**
> asíncrono, así que vive dentro de `useEffect()` con un array de dependencias vacío
> `[]`, que lo ejecuta exactamente una vez tras el primer render.

Las apps modernas traen datos de fuentes externas — APIs, feeds, bases de datos remotas.
React no trae su propio cliente de datos; usa el `fetch()` del navegador, exactamente
igual que lo haría JavaScript puro.

### El Feed de Assets de Gatos Dorados

Los retratos de gatos dorados de la tienda vienen de una API pública real:
`https://api.thecatapi.com/v1/images/search?limit=10`. La regla para todo lo parecido:
el request sale **fuera** del componente, así que es un efecto secundario, así que corre
dentro de `useEffect` — nunca en el cuerpo del render:

```js
import React, { useState, useEffect } from "react";

function CatImages() {
  const [catImages, setCatImages] = useState([]);

  useEffect(function() {
    // Efecto secundario asíncrono: pide al feed de gatos dorados diez retratos
    async function fetchCatImages() {
      const response = await fetch(
        "https://api.thecatapi.com/v1/images/search?limit=10"
      );
      const data = await response.json();
      setCatImages(data);
    }
    fetchCatImages();
  }, []); // [] = se ejecuta una vez al montar; sin él, cada render repite el request

  return (
    <div className="cat-grid">
      {catImages.map(function(image) {
        return <img key={image.id} src={image.url} alt="Gato dorado" />;
      })}
    </div>
  );
}
```

Lee el efecto línea a línea:

| Línea | Qué hace |
| :--- | :--- |
| `async function fetchCatImages()` | Declara el request **dentro** del efecto, para que cierre sobre el estado del componente |
| `await fetch(...)` | Envía el request; la ejecución se pausa hasta que llegue la respuesta |
| `await response.json()` | Analiza el cuerpo como JSON — también es una promesa, también se espera |
| `setCatImages(data)` | El setter dispara el re-render que pinta la cuadrícula |
| `[]` | Array de dependencias: tras el primer render, y nunca más |

> [!WARNING]
> **El error que todos cometen una vez**
> Obtener datos desde el cuerpo del efecto **sin** el array de dependencias hace que
> React reejecute el efecto tras cada render: el setter provoca un render, el render
> repite el request, el request vuelve a guardar estado — un bucle infinito de requests
> que agota la cuota de la API en segundos. El `[]` no es decoración opcional.

### Misión: Corredor del Feed

Clona el esqueleto en un componente `PatchNotes()` que obtenga
`https://api.github.com/repos/facebook/react/releases?per_page=3` y renderice
`release.name` de cada elemento. Abre la pestaña de Red y confirma que se dispara
**exactamente un request** al montar — luego quita el `[]` y mira cómo se inunda la
pestaña.

---

## 02. Tres Estados de una Promesa

Una **promesa** es un objeto que representa un valor que aún no existe. `fetch()`
siempre devuelve una, y cada promesa vive en exactamente uno de tres estados:

| Estado | Significado | Qué debe mostrar la UI |
| :--- | :--- | :--- |
| **Pendiente** | El request salió; no hay respuesta aún | La puerta de carga |
| **Cumplida** | La respuesta llegó y `response.json()` la analizó | Los datos |
| **Rechazada** | La red murió, CORS rechazó, la máquina está offline | El mensaje de error |

`async`/`await` es azúcar sintáctico sobre esos estados: `await` suspende la función
mientras la promesa está pendiente y la reanuda con el valor resuelto — o **lanza un
error** si se rechaza, que es exactamente lo que recoge el bloque `catch` del apartado
siguiente. Los mismos tres estados a la manera clásica:

```js
fetch("https://api.thecatapi.com/v1/images/search?limit=10")
  .then(function(response) { return response.json(); })  // camino del cumplimiento
  .then(function(data) { setCatImages(data); })
  .catch(function(err) { setError(err.message); });      // camino del rechazo
```

> [!TIP]
> `await` pausa **una corrutina**, no la página. El componente sigue renderizando mientras
> esperas — por eso existe el apartado siguiente: sin un indicador de carga, la UI se
> queda en un cuadro vacío y los jugadores asumen que el juego está roto.

---

## 03. La Puerta de Carga

`async`/`await` pausa la ejecución, pero la pantalla no se pausa con ella — así que
cuéntale al jugador qué pasa con un estado de carga:

```js
const [isLoading, setIsLoading] = useState(false);
const [loadingMessage, setLoadingMessage] = useState("Invocando gatos dorados...");
```

Actívalos al **inicio** del efecto, límbialos cuando **llegan los datos**:

```js
useEffect(function() {
  async function fetchCatImages() {
    setIsLoading(true);              // se abre la puerta
    const response = await fetch(
      "https://api.thecatapi.com/v1/images/search?limit=10"
    );
    const data = await response.json();
    setCatImages(data);
    setIsLoading(false);             // llegaron los datos — cierra la puerta
    setLoadingMessage("");
  }
  fetchCatImages();
}, []);
```

Y renderiza el indicador solo mientras el request está en vuelo:

```js
{isLoading && <p className="loading">{loadingMessage}</p>}
{!isLoading && <h2>Galería de Gatos Dorados</h2>}
```

El patrón se generaliza a todo `fetch` del módulo: **abre la puerta antes de pedir,
ciérrala cuando aterrice la respuesta** — en un bloque `finally` cuando entran en juego
los errores.

### Misión: Espejo Lento

Envuelve el fetch de tu `PatchNotes()` con el mismo par de indicadores, con el mensaje
`"Consultando el libro del gremio..."`. Usa la limitación de red de la pestaña (Slow 3G)
para ver aparecer y desaparecer la línea de carga.

---

## 04. Cuando el Mensajero se Pierde

> [!NOTE]
> **Información clave**
> `fetch()` **no** rechaza en errores HTTP. Un `404` o un `500` es una promesa
> perfectamente *resuelta* — lo único que la rechaza es un fallo real de red. Tienes que
> comprobar `response.ok` tú mismo y lanzar el error.

Rodea el request de `try`/`catch`, guarda `error.message` en estado y renderízalo:

```js
async function fetchCatImages() {
  setIsLoading(true);
  try {
    const response = await fetch(
      "https://api.thecatapi.com/v1/images/search?limit=10"
    );
    if (response.ok === false) {
      // 404, 500... a fetch() le da igual, así que haz el fallo explícito
      throw new Error("Failed to fetch data");
    }
    const data = await response.json();
    setCatImages(data);
  } catch (err) {
    setError(err.message);     // guarda solo el mensaje — es lo que renderizas
  } finally {
    setIsLoading(false);       // se ejecuta en el éxito Y en el fallo
  }
}
```

`response.ok` es `true` para `200`–`299` y `false` para todo lo demás. Convertir ese
indicador en un `Error` lanzado hace que un solo `catch` maneje cada fallo — estado
inválido, red muerta, JSON mal formado — por el mismo camino de código.

### Renderizar el Error

Los errores son solo estado, así que se renderizan con el mismo guard `&&` de siempre:

```js
{error && <div>{error}</div>}
{!error && <h1>¡Sin errores!</h1>}
```

Como `error` vale `null` en reposo, las dos líneas se condensan en el atajo `||` — el
lado izquierdo se renderiza si es truthy, el derecho en caso contrario:

```js
{error || <h1>¡Sin errores!</h1>}
```

### Misión: Línea de Suministro Rota

Apunta el fetch a una ruta incorrecta (`https://api.thecatapi.com/v1/images/serch?limit=10`),
recarga y mira cómo `Failed to fetch data` toma la pantalla. Luego corrige la ruta y
confirma que el error se limpia en el siguiente render.

---

## 05. El Filtro del Bestiario

Las listas llegan de las APIs **completas**; los jugadores las buscan **por partes**.
`.filter()` es el puente: recorre un array y devuelve un **nuevo** array con solo los
elementos cuyo callback devuelve `true`. El original no se toca:

```js
const filteredCreatures = creatures.filter(function(creature) {
  return creature.name.toLowerCase().startsWith(searchTerm.toLowerCase());
});
```

| Pieza | Por qué está ahí |
| :--- | :--- |
| `.filter(...)` | Devuelve un nuevo array; la lista maestra queda intacta |
| `.toLowerCase()` en **ambos** lados | `searchTerm` y `name` se normalizan, así que la búsqueda ignora mayúsculas |
| `.startsWith(...)` | La coincidencia es por prefijo: `"ash"` encuentra `"Ashen Wolf"` |

Cualquier expresión válida que devuelva un booleano sirve: comparar `rarity`, comprobar
`level <= 5`, test de pertenencia con `.includes()`.

### Misión: Escriba de Bestias

Con `const searchTerm = "cinder";` y una criatura llamada `"Cinder Hound"`, predice la
longitud de `filteredCreatures` **antes** de ejecutarlo. Luego añade una criatura
llamada `"Ember Hound"` y revisa de nuevo — ¿cambió el filtro, o tu suposición?

---

## 06. El Banco de Búsqueda: Maestra vs Pantalla

La búsqueda de reliquias de la tienda funciona con dos listas, y saber cuál es cuál es
todo el truco:

- **Lista maestra** (`relicList`) — la fuente de verdad. Nunca mutada, nunca filtrada en el sitio.
- **Lista de pantalla** (`filteredRelicList`) — **deriva** de la maestra en cada render,
  desde lo que `searchTerm` valga en ese momento.

```js
import React, { useState } from "react";

function RelicSearch() {
  const [searchTerm, setSearchTerm] = useState("");
  const relicList = [
    { name: "Ember Shard", rarity: "Legendary" },
    { name: "Ashen Compass", rarity: "Rare" },
    { name: "Cinder Bell", rarity: "Uncommon" },
  ];

  // Se deriva en cada render: la maestra, filtrada por la búsqueda actual
  const filteredRelicList = relicList.filter(function(relic) {
    return relic.name.toLowerCase().startsWith(searchTerm.toLowerCase());
  });

  return (
    <div>
      <input
        type="text"
        value={searchTerm}
        onChange={function(e) { setSearchTerm(e.target.value); }}
        placeholder="Busca en la bóveda de reliquias"
      />
      {filteredRelicList.map(function(relic) {
        return (
          <div key={relic.name}>
            <h2>{relic.name}</h2>
            <h3>Rareza: {relic.rarity}</h3>
          </div>
        );
      })}
    </div>
  );
}
```

El flujo de datos es un pipeline en un solo sentido: **tecla → `setSearchTerm` → render →
refiltrar la maestra → pintar la lista de pantalla**. Borra el término de búsqueda y el
catálogo completo reaparece, porque la maestra nunca se redujo.

> [!TIP]
> **Versión para game dev**
> Esta es la pantalla de inventario de cada RPG jamás lanzado: una tabla maestra de
> datos, una cadena de consulta y una vista que no es más que `master.filter(...)` dibujado
> en pantalla. El mismo pipeline mueve el registro de misiones, la casa de subastas y el
> bestiario — ver [[07 - Rutas Comerciales]] para la cara de props de la misma idea.

---

## ⚡ XP Ganados: Ideas Clave

- 📡 `fetch()` es JavaScript nativo; React decide **cuándo** se ejecuta — dentro de `useEffect(..., [])`.
- 🔁 Un `[]` ausente es un bucle infinito de requests: render → fetch → setState → render.
- ⏳ Toda promesa está **pendiente**, **cumplida** o **rechazada** — tu UI le debe una respuesta a cada estado.
- 🚦 `isLoading` + `loadingMessage` mantienen la pantalla honesta mientras `await` hace su trabajo.
- 🚫 `fetch()` nunca rechaza en `404`/`500` — comprueba `response.ok` y lanza el error tú mismo.
- 🧹 `.filter()` devuelve un **nuevo** array; la maestra queda intacta, la de pantalla se deriva.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🛒 Tiendas e inventarios: listas de productos traídas de una API al montar
- 📰 Feeds: notas de parche, publicaciones del gremio, cronologías sociales — todo `fetch` + `.filter()`
- 🔍 Búsqueda al escribir sobre catálogos remotos (reliquias, bestiario, jugadores)
- ⚠️ Una forma de boundary de error: mostrar requests fallidos en vez de pantallas en blanco
- ⏳ Skeleton screens y spinners — la puerta de carga con otro disfraz

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Añade un segundo efecto a `CatImages` que obtenga `?limit=5` en su propio estado, con su propio indicador de carga.
2. Renderiza el objeto `error` crudo con `{error && <div>{error}</div>}`, luego cámbialo por `error.message` y compara.
3. Extiende `RelicSearch` con un desplegable de rareza que se componga con la búsqueda de texto (`&&` de dos filtros).
4. Construye un componente `Bestiary()` cuya lista maestra viva en estado y cuya lista de pantalla se filtre por `searchTerm`.
5. **Pelea de jefe:** construye un hook personalizado `useCatFeed()` que sea dueño de `catImages`, `isLoading` y `error`, y los devuelva los tres — luego úsalo en dos componentes distintos y confirma que la pestaña de Red muestra dos ciclos de vida de request independientes.

---

## 🔗 Ver También

- [[00c - Chuleta de React II]] — los patrones de `fetch`, carga y filtrado de este capítulo en una página
- [[12 - El Libro del Gremio]] — context, la otra forma de mover datos por el árbol
- [[11 - El Sistema de Reliquias]] — fundamentos de `useEffect`: dependencias y limpieza
- [[14 - El Mapa del Mundo]] — siguiente capítulo: enrutar las páginas donde se pintan estos feeds

---
