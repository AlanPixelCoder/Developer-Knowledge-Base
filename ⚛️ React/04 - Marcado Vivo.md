# 04. Marcado Vivo

**Versión original en inglés:** [04 - Living Markup.md](04%20-%20Living%20Markup.md)

**Curso:** React
**Tema:** La regla de la raíz única, los fragmentos, la inserción de expresiones JavaScript, el renderizado condicional, los atributos estáticos y dinámicos y `className`
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE_A_INTERMEDIO-6CC24A?style=for-the-badge" alt="Principiante a Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-01_--_08-7C5CFF?style=for-the-badge" alt="Lecciones 01 a 08">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

El capítulo 03 te enseñó los glifos. Este capítulo los hace **respirar**: cómo la regla de la
raíz única y los fragmentos mantienen el marcado unido, cómo insertar expresiones JavaScript
vivas con llaves, cómo mostrar distinto marcado según una condición, y cómo los atributos —
estáticos y dinámicos — y la peculiaridad de `className` transportan datos a la página. La
referencia rápida de todo el capítulo está en [[00b - Chuleta de React]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Un componente React devuelve exactamente **un** elemento raíz, y dentro de ese marcado las
> llaves `{ }` te dejan insertar cualquier expresión JavaScript — valores, condicionales,
> atributos dinámicos — mientras que `className` sustituye a la palabra reservada `class`.

---

## 01. La Regla de la Raíz Única

Un `return` puede contener **solo UN elemento raíz**. Dos hermanos en el nivel superior:

```javascript
// ❌ Dos raíces — esto no compila
return (
  <h1>Deep Halls</h1>
  <p>Warden of the Ninth Floor</p>
);
```

Dos elementos uno al lado del otro sin un padre compartido es un error de sintaxis.
Envuélvelos en un único contenedor:

```javascript
// ✅ Una raíz envolviendo a los hermanos
return (
  <div>
    <h1>Deep Halls</h1>
    <p>Warden of the Ninth Floor</p>
    <ul>
      <li>Ember Gate</li>
      <li>Frozen Cistern</li>
      <li>The Ninth Floor</li>
    </ul>
  </div>
);
```

El `<div>` es la raíz; el `<h1>`, el `<p>` y el `<ul>` son sus hijos, y los `<li>` son las
fechas de la gira de la incursión — ubicaciones de misiones. El mismo árbol de elementos que
dibujaste para el grupo en el curso de HTML, ahora como valor de retorno.

> [!IMPORTANT]
> Los paréntesis alrededor de todo no son decoración opcional: sin ellos, la inserción
> automática de punto y coma (del capítulo [[03 - Taller de Glifos]]) trunca el return tras la
> primera línea. Paréntesis más una raíz única es todo el contrato.

### Misión: La Tarjeta de Incursión

Construye una tarjeta de objeto de Emberfall: un `<div>` raíz que contenga un
`<h1>Deep Halls</h1>`, un `<p>Warden of the Ninth Floor</p>` y un `<ul>` de al menos tres
ubicaciones de misión. Luego borra el `<div>` y observa cómo el compilador rechaza las dos
raíces desnudas. Vuelve a ponerlo.

---

## 02. El Rune del Fragmento

A veces quieres hermanos **sin** un `<div>` extra contaminando el DOM. Un **React Fragment**
los envuelve y **no emite ningún nodo del DOM**:

```javascript
return (
  <>
    <h1>Deep Halls</h1>
    <p>Warden of the Ninth Floor</p>
  </>
);
```

`<>...</>` es la abreviatura de `React.Fragment`. El documento del navegador **no** recibe un
elemento envoltorio entre el `<h1>` y el `<p>` — el fragmento es un padre fantasma que
satisface la regla de la raíz única mientras deja el HTML real limpio.

> [!TIP]
> Recurre a un fragmento siempre que la única razón de tu `<div>` fuera la regla de la raíz
> única. Si el `<div>` lleva una clase o es un contenedor de maquetación real, consérvalo; si
> existe solo para complacer al compilador, sustitúyelo por `<>`.

### Misión: Des-Div el HUD

Toma el HUD del gremio y envuelve su barra de vida y su lista de misiones en `<>...</>` en vez
de un `<div>`. En el inspector de elementos del navegador, confirma que ni la barra ni la
lista tienen un elemento envoltorio. Acabas de eliminar un `<div>` que no hacía nada salvo
satisfacer la regla — una dieta contra la sopa de `<div>`.

---

## 03. Expresiones Vivas

Envuelve una expresión JavaScript en **llaves** `{ }` y React renderiza su valor. Así entran
los datos en el marcado:

```javascript
const articleTitle = "As We May Think";
const articleAuthor = "Vannevar Bush";
const readNumber = 750;

return (
  <article>
    <h2>{articleTitle}</h2>
    <p>By {articleAuthor}</p>
    <p>Read {readNumber} times</p>
  </article>
);
```

Cualquier expresión JavaScript válida que resuelva a **un solo valor** funciona dentro de
`{ }`: una variable, `2 + 2`, `name.toUpperCase()`, un ternario, una llamada a función. El
acceso completo a miembros (`props.title`), la aritmética, los métodos de cadena — todo vale.
Lo que **no** funciona es una sentencia (`if`, `for`) o cualquier cosa que no devuelva nada
con sentido.

> [!WARNING]
> **El error clásico**
> Poner una sentencia o un objeto literal donde corresponde una expresión. `{ if (signedIn) ... }`
> es inválido dentro de JSX, y `{ { a: 1 } }` no renderiza nada útil. Usa una **expresión** —
> un ternario o `&&` para condiciones (sección 04), y `Object.entries` / `.map` para rehacer
> objetos antes de renderizar.

### Misión: Entrada de Lore

Retematiza el artículo de arriba como una entrada de lore de Emberfall: `entryTitle`, `author`
y un `readNumber` de lecturas del capítulo. Renderiza los tres con llaves. Luego cambia un
valor, guarda y observa cómo se actualiza solo ese texto — la recarga en caliente de
[[02 - Punto de Aparición]] ejecutando una expresión viva.

---

## 04. Renderizado Condicional

Tres formas, de la más verbosa a la más compacta:

### 1. Asignar en una variable

```javascript
let page = null;

if (signedIn) {
  page = <div>Panel del miembro del gremio</div>;
} else {
  page = <div>Inicia sesión para entrar al salón del gremio</div>;
}

return <main>{page}</main>;
```

Una variable guarda el JSX que corresponda y `{page}` lo renderiza. Claro y depurable, a
costa de código repetitivo.

### 2. Ternario

```javascript
return (
  <main>
    {signedIn ? <GuildDashboard /> : <LoginGate />}
  </main>
);
```

`condición ? a : b` elige una de dos ramas de marcado en línea. Es la forma o-una-o-otra más
común en código real.

### 3. AND lógico

```javascript
return (
  <main>
    {signedIn && <GuildDashboard />}
  </main>
);
```

`condición && marcado` renderiza el marcado solo cuando la condición es verdadera, y no
renderiza nada en caso contrario — sin rama else. Úsalo cuando solo hay un caso de «muéstralo».

> [!TIP]
> Elige según el número de ramas: `&&` para cero-o-uno, ternario para exactamente-dos, un
> `if`/`else` con variable cuando las ramas crezcan o necesiten nombre. Mezclar las tres en un
> mismo return es un mal olor — divide el componente.

### Misión: La Puerta de Entrada

En un componente, define `const signedIn = false;`. Renderiza un `LoginGate` con `&&`, luego
cambia a un ternario que muestre también un `GuildDashboard` cuando sea true. Alterna
`signedIn` y guarda — el suelo del salón cambia con un solo booleano.

---

## 05. Atributos Estáticos

Los atributos se parecen al HTML. `src`, `alt`, `href`, `id` toman cadenas entre comillas
exactamente como en el curso de HTML:

```javascript
// Una ruta de avatar de gremio — cadenas estáticas normales
<img src="username/camera/recents/today.png" alt="a guild selfie" />
```

Nada sorprendente aquí: valores entre comillas, misma sintaxis, mismo significado. Esta es la
mitad fácil de los atributos.

---

## 06. Atributos Dinámicos

Para que un atributo dependa de una variable JavaScript, **quítale las comillas** y envuelve
el valor en llaves:

```javascript
const tokyoUrl = "https://i.imgur.com/0Ax1wzO.png";
const tokyoImage = <img src={tokyoUrl} alt="Tokyo" />;
```

`src={tokyoUrl}` evalúa la variable y usa lo que contenga — sin comillas dentro de las llaves.
Cambia `tokyoUrl` y el origen de la imagen sigue en el siguiente render. Cualquier expresión
funciona: `src={avatarUrl}`, `id={"slot-" + index}`, `alt={item.name}`.

> [!WARNING]
> **El error clásico**
> Envolver las llaves en comillas: `src="{tokyoUrl}"` renderiza el texto literal `{tokyoUrl}`
> como URL. Las comillas hacen una cadena estática; las llaves hacen una expresión viva.
> Eliges una, nunca las dos.

### Misión: La Forja de Avatares

Declara `const avatarUrl = "username/camera/recents/today.png";` y renderiza un `<img>`
cuyo `src` sea dinámico. Apunta `avatarUrl` a otra ruta, guarda y observa cómo cambia el
retrato sin tocar el marcado.

---

## 07. `className`

`class` es una **palabra clave reservada de JavaScript** (piensa en `class Planet`), así que
JSX no puede usarla para el atributo HTML. La grafía de React es **`className`**:

```javascript
<button className="forge-button">Enter the Deep Halls</button>
```

`className` acepta el mismo valor que aceptaría el atributo `class`, y también acepta valores
**dinámicos**, porque es solo un atributo:

```javascript
const isLocked = true;
<button className={isLocked ? "forge-button is-locked" : "forge-button"}>
  {isLocked ? "Locked" : "Enter the Deep Halls"}
</button>
```

El CSS de tu hoja de estilos sigue apuntando a `.forge-button` — solo cambia el nombre del
lado de JSX.

> [!NOTE]
> El mismo problema de palabras reservadas produce un grupo de renombres de JSX que volverás
> a encontrar: `class` → `className`, `for` → `htmlFor` (capítulo [[10 - La Fragua]]), y
> propiedades de estilo en línea que van en camelCase (`background-color` →
> `backgroundColor`, capítulo [[09 - El Mando]]). Aprende el patrón una vez — JSX renombra las
> colisiones.

### Misión: Restiliza el Botón

Toma un botón de un proyecto HTML antiguo con `class="login-button"` y tráelo a JSX. Renombra
el atributo a `className="forge-button"`, mantén el CSS apuntando a `.forge-button` y añade
una variante dinámica con un ternario. La hoja de estilos no se entera de que algo se movió.

---

## 08. La Interfaz que Respira

### Checkpoint: Resumen del capítulo

- **Raíz única:** un elemento por return; envuelve a los hermanos en un contenedor o un fragmento.
- **Fragmento** `<>...</>` agrupa hermanos y **no emite ningún nodo del DOM**.
- Las **llaves** `{ }` insertan cualquier **expresión** JavaScript de un solo valor en el marcado.
- El **renderizado condicional** tiene tres formas: una variable con `if`/`else`, un
  **ternario** (`? :`) y el **AND lógico** (`&&`) sin rama else.
- **Atributos**: las cadenas estáticas se quedan como en HTML; los valores dinámicos quitan
  las comillas y usan `{expresión}`.
- **`className`** reemplaza a `class` porque `class` es reservada en JavaScript.

### La Tarjeta Viva

Todo en un componente — la raíz única, un fragmento, expresiones vivas, un ternario, un
atributo estático y uno dinámico:

```javascript
function RelicCard(props) {
  const { name, imageUrl, rarity } = props;
  const isLegendary = rarity === "legendary";

  return (
    <>
      <h2>{name}</h2>
      <img src={imageUrl} alt={name} width="200" />
      {isLegendary ? (
        <p className="badge legendary">Legendary! 🔥</p>
      ) : (
        <p className="badge">Common</p>
      )}
    </>
  );
}

export default function App() {
  return (
    <div className="catalog">
      <RelicCard
        name="Ember Blade"
        imageUrl="https://i.imgur.com/0Ax1wzO.png"
        rarity="legendary"
      />
    </div>
  );
}
```

Reléelo contra las reglas: la raíz de App es un `<div>`; `RelicCard` devuelve un fragmento sin
envoltorio; `{name}`, `{imageUrl}` y el ternario son expresiones vivas; `width` y `alt` son
estáticos; `src={imageUrl}` es dinámico; `className` sustituye a `class`.

> [!TIP]
> **Versión para game dev**
> Esto es exactamente cómo se dibuja un widget de HUD: un panel raíz, ranuras hijas agrupadas
> sin andamiaje extra y atributos atados a valores vivos. Cambia la reliquia por una barra de
> vida, la rareza por un nivel de daño y el ternario por `hp < 20 ? <Critical/> : <Stable/>` —
> la misma forma de componente construye todo el sitio companion.

---

## ⚡ XP Ganados: Ideas Clave

- 🌳 **Una raíz por return.** Dos hermanos desnudos es un error de compilación; envuélvelos.
- 👻 El **fragmento** `<>...</>` satisface la regla de la raíz única sin añadir un nodo del
  DOM — la cura contra la sopa de `<div>`.
- 🧮 Las **llaves** `{ }` interpolan cualquier **expresión** JavaScript de un solo valor —
  variables, aritmética, métodos, ternarios.
- 🔀 Los **condicionales** vienen en tres formas: `if`/`else` a una variable, el **ternario**
  `? :` y el **AND lógico** `&&` para el caso sin else.
- 🏷️ Los **atributos** son cadenas estáticas por defecto; para atarlos a una variable, quita
  las comillas y usa `{expresión}`.
- 🔤 **`className`** reemplaza a `class` — `class` es reservada en JavaScript. La misma
  colisión produce después `htmlFor` y estilos en línea en camelCase.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🃏 Rejillas de tarjetas (objetos, perfiles, productos) donde cada tarjeta es una raíz con
  campos vivos
- 🔐 Vistas autenticadas vs. invitado controladas por un booleano y un ternario o `&&`
- 🖼️ Avatares, imágenes de producto e iconos cuyas URLs llegan de los datos como atributos
  dinámicos
- 🎨 Clases CSS condicionales para estados bloqueado, legendario o resaltado
- 🧩 Fragmentos que mantienen el marcado de listas y rejillas libre de divs envoltorio inútiles

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Reescribe un return de dos raíces para que compile, una vez con un `<div>` y otra con un
   fragmento.
2. Renderiza tu XP de gremio como `{xp}` y luego como `{xp * 2}` — demuestra que funcionan
   las expresiones, no solo las variables, dentro de las llaves.
3. Construye las tres formas condicionales (variable, ternario, `&&`) para el mismo estado de
   sesión.
4. Haz una imagen de tarjeta cuyo `src` venga de una variable y cuyo `alt` sea una cadena
   estática.
5. **Pelea de jefe:** construye un componente `RelicCard` completo — raíz de fragmento, imagen
   dinámica, `className` dinámico con ternario y un `<ul>` de estadísticas renderizado desde
   un array con `.map`. Renderiza tres tarjetas en un `App` y verifica que el marcado no tenga
   divs envoltorio en ninguna parte donde no debería.

---

## 🔗 Ver También

- [[03 - Taller de Glifos]] — el capítulo anterior: JSX, transpilación y la regla de los paréntesis
- [[05 - Bloques de Construcción]] — siguiente capítulo: componentes funcionales, nombres, export e import
- [[09 - El Mando]] — eventos y las reglas de estilo en línea en camelCase que `className` anticipa
- [[10 - La Fragua]] — formularios, donde `htmlFor` se une a `className` como renombre de palabra reservada

---
