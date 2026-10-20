# 06. El Árbol de Habilidades

**Versión original en inglés:** [06 - The Skill Tree.md](06%20-%20The%20Skill%20Tree.md)

**Curso:** React
**Tema:** composición de componentes, jerarquía de componentes, relaciones padre-hijo, flujo de datos unidireccional, construcción de la publicación del gremio, ensamblaje final
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

Un componente solo es un ladrillo. El feed del gremio de Emberfall — avatar, nombre de
usuario, pie de foto, botón de seguir, botón de me gusta — es un **muro**, y los muros se
construyen apilando ladrillos en un orden elegido. Este capítulo trata de la
**composición**: combinar componentes pequeños y especializados en estructuras
jerárquicas, y de entender el árbol padre-hijo en el que toda aplicación React se
convierte en secreto. Al final habrás ensamblado la tarjeta `Post` completa, archivo a
archivo. Referencia: [[00b - Chuleta de React]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Las interfaces de React son **árboles**: un componente raíz (`App`) es padre de todos
> los demás, los componentes pequeños y especializados se anidan dentro de los grandes, y
> los datos siempre viajan **cuesta abajo** — del padre al hijo, nunca al revés.

---

## 01. El Ritual de Composición

> [!NOTE]
> **Información clave**
> La **composición** es el acto de combinar componentes pequeños y especializados en
> estructuras jerárquicas. En lugar de un archivo que contiene la página entera, cada
> componente se ocupa de un trabajo y los componentes grandes se construyen anidando
> pequeños dentro de su marcado.

Los beneficios son los que ya conoces de [[05 - Bloques de Construcción]], ahora
multiplicados:

- **Un trabajo por componente.** Un `LikeButton` que solo da me gusta es más fácil de
  escribir, probar y reutilizar que una función del tamaño de una página que además
  sigue, además consulta datos.
- **Piezas intercambiables.** Sustituye el botón de seguir por un botón de mensaje y a
  `Post` no le importa.
- **Vocabulario compartido.** Todo el desarrollador del sitio de Emberfall dice `Post`,
  `Header`, `Button` — y se refiere al mismo archivo.

La estructura que resulta nunca es plana. Siempre es un árbol con exactamente un raíz.

---

## 02. Leer el Árbol de Habilidades

### La jerarquía de la publicación del gremio

Esta es la jerarquía de la publicación que vas a construir:

```text
App (Contenedor de Nivel Superior)
 └── Post (Contenedor de Tarjeta)
      ├── FollowButton (Widget de Acción)
      └── LikeButton (Interruptor Interactivo)
```

Léelo como un árbol de habilidades al revés — todo se desbloquea **desde la raíz hacia
afuera**:

| Nodo | Rol | Hijos |
| :--- | :--- | :--- |
| **App** | Contenedor de nivel superior; la raíz de toda la aplicación | `Post` |
| **Post** | Contenedor de tarjeta: avatar, nombre de usuario, pie de foto | `FollowButton`, `LikeButton` |
| **FollowButton** | Widget de acción: seguir / dejar de seguir | ninguno |
| **LikeButton** | Interruptor interactivo: contador de me gusta y corazón | ninguno |

Dos términos que oirás en todo repositorio de React:

- **Padre** — un componente que renderiza a otro. `Post` es padre de los dos botones.
- **Hijo** — un componente renderizado **dentro** de otro. `LikeButton` es hijo de `Post`.

Un componente puede ser padre e hijo a la vez: `Post` es hijo de `App`.

### Misión: Traza tu Propio Árbol

Dibuja el árbol del feed de misiones de Emberfall antes de escribir código: un contenedor
raíz `QuestFeed`, una tarjeta `QuestRow` por misión, y dentro de cada fila un
`RewardBadge` y un `ClaimButton`. Escribe los cuatro nombres en PascalCase y conecta los
nodos con `└──` y `├──` exactamente como arriba. Si no puedes señalar la raíz con un solo
dedo, el árbol está mal.

---

## 03. Forjar la Publicación

### `Post.js`

El contenedor de tarjeta. Importa los dos widgets, renderiza los metadatos de la
publicación en la cabecera y deja que los botones hagan su trabajo en el pie:

```js
import React from "react";
import FollowButton from "./FollowButton.js";
import LikeButton from "./LikeButton.js";

export default function Post() {
  return (
    <div className="post-container">
      <header>
        <img src="/avatar.png" alt="Avatar" />
        <h2>WardenOfTheNinth</h2>
        <FollowButton />
      </header>
      <p>Limpié las Salas Profundas sin una sola antorcha.</p>
      <footer>
        <LikeButton />
      </footer>
    </div>
  );
}
```

Qué hace cada línea:

- Los dos imports son las **aristas** del árbol — aquí es donde la composición ocurre, en
  la parte de arriba del archivo.
- `className="post-container"` es el gancho de estilos (JSX usa `className`, no `class`).
- `<img src="/avatar.png" alt="Avatar" />` es un atributo estático igual que en HTML.
- `Post` nunca explica **cómo** seguir ni dar me gusta — solo decide **dónde** aparecen
  esos widgets. Esa indiferencia es lo que hace reutilizables a los botones.

> [!WARNING]
> **El error que todos cometen una vez**
> Escribir el marcado de los botones dentro de `Post` "solo por ahora". Dos archivos más
> tarde hace falta el mismo botón en la página de perfil, y estás copiando JSX de un
> archivo a otro. Construye el widget como componente propio **primero**, y luego colócalo.

---

## 04. El Guardián Raíz

### `App.js`

El contenedor de nivel superior aloja la publicación. Nada más — el trabajo de la raíz es
estar arriba y renderizar lo que debe estar en pantalla:

```js
import React from "react";
import Post from "./Post.js";

export default function App() {
  return (
    <div>
      <Post />
    </div>
  );
}
```

`App` importa `Post` y lo instancia con la etiqueta autocontenida de
[[05 - Bloques de Construcción]]. React renderiza `App`, React renderiza `Post` y React
renderiza los dos botones de dentro — un recorrido del árbol, de arriba abajo.

### Misión: Segundo Asiento

Añade un segundo `<Post />` debajo del primero y guarda. Aparecen dos tarjetas idénticas,
lado a lado — dos instancias del mismo componente, una sola definición. Después borra la
segunda: componer es barato, y deshacerlo también.

---

## 05. Ensamblaje Final

### Checkpoint: Resumen del capítulo

- La **composición** = combinar componentes pequeños y especializados en estructuras
  jerárquicas.
- Toda aplicación de React es un árbol con **un solo raíz**; los padres renderizan a los
  hijos.
- `Post` agrega los metadatos y los botones; nunca implementa los widgets él mismo.
- Los datos fluyen solo **padre → hijo** — el tema de la siguiente sección.

### El árbol de archivos terminado

```text
App.js
 └── Post.js
      ├── FollowButton.js
      └── LikeButton.js
```

Cada archivo y su rol:

| Archivo | Rol en el árbol |
| :--- | :--- |
| `App.js` | Raíz que aloja `<Post />`; el punto de entrada de todo el árbol de componentes |
| `Post.js` | Agrega los metadatos de la publicación — avatar, nombre, pie de foto — y los dos botones |
| `FollowButton.js` | Posee el estado del interruptor seguir / dejar de seguir de esta publicación |
| `LikeButton.js` | Posee el contador de me gusta y la animación del corazón de esta publicación |

Las flechas de ese árbol no son decoración: son la dirección en la que React permite que
viajen los datos. Esa restricción es todo el tema de la sección 06 — y del siguiente
capítulo.

---

## 06. Solo Cuesta Abajo

### La arquitectura padre-hijo

Los componentes de React forman un **árbol invertido**: un raíz arriba, las ramas
extendiéndose hacia abajo. `<App>` es padre de todo; cada generación de abajo es hijo de
la de arriba:

```text
        <App>            ← padre de Post
          │
        <Post>            ← hijo de App, padre de los botones
        /    \
<FollowButton> <LikeButton>   ← hijos de Post
```

### La regla unidireccional

> [!NOTE]
> **Información clave**
> Los datos fluyen **solo del padre al hijo** — flujo de datos unidireccional. Un padre
> puede entregar información hacia abajo a un hijo; un hijo nunca puede llegar arriba y
> recablear a su padre. Cuando los datos de un padre cambian, React vuelve a renderizar al
> padre, y el nuevo render se filtra por toda la rama.

En la práctica eso significa:

- El **padre posee la verdad**; los hijos muestran lo que les dan.
- Los hermanos nunca hablan directamente entre sí — comparten un padre.
- Para cambiar algo alto en el árbol, se cambia **alto en el árbol**.

El mecanismo formal para entregar datos cuesta abajo se llama **props**, y es todo el
tema de [[07 - Rutas Comerciales]]. El mecanismo para que un componente recuerde sus
propios cambios — el interruptor de seguir, el contador de me gusta — es el **estado**,
cubierto en [[08 - La Barra de Vida]].

> [!TIP]
> **Versión para game dev**
> Todo HUD de juego es el mismo árbol. La pantalla raíz es `App`; el panel de vida, el
> minimapa y el rastreador de misiones son contenedores; las barras, los indicadores y las
> filas sueltas son widgets. Si alguna vez has colocado un widget dentro de una pantalla en
> el editor de UI de un motor, ya conoces la arquitectura de React — lo único nuevo es la
> dirección de las flechas.

---

## ⚡ XP Ganados: Ideas Clave

- 🌳 La **composición** combina componentes pequeños y especializados en estructuras
  jerárquicas.
- 📁 Un trabajo por componente, un archivo por componente — cambia widgets sin tocar la
  tarjeta.
- 🌲 Toda aplicación de React es un **árbol invertido** con exactamente un raíz: `<App>`.
- 👨‍👦 El **padre** renderiza al **hijo**; un componente puede ser las dos cosas a la vez.
- ⬇️ Los datos fluyen **solo padre → hijo**; los hermanos se comunican a través de su padre.
- 🧱 `Post` agrega metadatos y widgets — nunca los reimplementa.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 📰 Feeds sociales — cada tarjeta de cada timeline es un contenedor estilo `Post` con
  widgets
- 🎮 Diseños de HUD: pantalla raíz → paneles → barras, indicadores y filas, exactamente
  este árbol
- 🛍️ Tarjetas de producto: imagen, título y precio compuestos a partir de piezas menores
  reutilizables
- 🧰 Sistemas de diseño construidos como árboles de componentes en vez de marcado copiado
- 👥 Escala de equipo — muchos desarrolladores poseen componentes hoja mientras uno posee
  la raíz

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Redibuja la jerarquía de la publicación del gremio de memoria y compárala con el árbol
   de la sección 02.
2. Escribe `FollowButton.js` y `LikeButton.js` como componentes independientes que devuelvan
   un solo `<button>`, y compón ambos dentro de `Post`.
3. Construye el árbol `QuestFeed` de tu misión — `QuestFeed`, `QuestRow`, `RewardBadge`,
   `ClaimButton` — con un archivo por componente.
4. Añade un `<Post />` a `App` hasta completar tres y confirma que se renderizan tres
   tarjetas desde una sola definición.
5. **Pelea de jefe:** ensambla un árbol de página de perfil — `App` → `ProfileHeader` →
   (`Avatar`, `FollowButton`) y `App` → `Post` ×2 — con cada archivo importando a sus
   propios hijos, y dibuja el árbol final en un bloque `text` al final de tus notas.

---

## 🔗 Ver También

- [[00b - Chuleta de React]] — reglas de componentes y composición en una página
- [[04 - Marcado Vivo]] — capítulo anterior: expresiones y renderizado condicional dentro de un componente
- [[05 - Bloques de Construcción]] — capítulo anterior: definir, exportar e instanciar componentes
- [[07 - Rutas Comerciales]] — siguiente capítulo: enviar datos por el árbol con props
- [[08 - La Barra de Vida]] — más adelante: permitir que los widgets hijos recuerden sus propios cambios
- [[09 - El Mando]] — más adelante: conectar los widgets de este árbol a eventos reales de usuario

---
