# 01. El Renacimiento

**Versión original en inglés:** [01 - The Rebirth](./01%20-%20The%20Rebirth.md)

**Course:** React
**Capítulo:** I. El Renacer de la Interfaz
**Tema:** El primer paso para reconstruir el Consola del Arsenal
**Etiquetas:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Lessons-01_--_05-7C5CFF?style=for-the-badge" alt="Lecciones 01 a 05">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Trama">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

Tras la última incursión, la Consola del Arsenal de Emberfall quedó hecha pedazos. Los sellos se habían ido superponiendo con los años y un cambio en el recuento obligaba a rastrear scripts frágiles en tres sitios distintos. Para que el Arsenal resistiera la siguiente oleada de reparaciones, los Guardianes decidieron reconstruir sus lecturas desde cero: no añadiendo más llamadas al DOM, sino dejando que la interfaz se describiera a sí misma a partir de sus datos. Este es el primer paso: entender por qué React merece un sitio en el banco de trabajo.

> [!NOTE]
> El objetivo no es memorizar fechas, sino cambiar de mentalidad: describe *qué* debe aparecer para un conjunto de valores, y deja que la biblioteca se encargue de *cómo* actualizar la página.

## Why patching fails under pressure

Cuando un escriba del Arsenal actualiza la salud de un Guardián herido, ese valor aparece en al menos tres sitios a la vez: la franja de estado, la lista de triaje y el listado de guardias. Con manipulación directa del DOM, cada uno requiere su propia consulta y su propia asignación. Un solo descuido basta para que la consola mienta a un escriba cansado.

```javascript
// Brittle: three places, three chances to drift
const statusHp = document.querySelector("#status-hp");
statusHp.textContent = "HP: 72 / 100";

const triageHp = document.querySelector("#triage-hp");
triageHp.textContent = "HP: 72 / 100";

const rosterHp = document.querySelector("#roster-hp");
rosterHp.textContent = "HP: 72 / 100";
```

Cuantos más lugares repitan un valor, más difícil será mantenerlos sincronizados. La solución no es «tener más cuidado», sino dar a cada elemento repetido una única fuente de verdad.

## A different contract

React propone un trato distinto. En lugar de hurgar en la página para cambiar nodos, escribes pequeñas funciones llamadas **componentes** que devuelven marcado para los datos que reciben. Actualizas los datos en un solo lugar y todos los componentes que los usan se vuelven a renderizar con los nuevos valores. React solo toca las partes reales del DOM que han cambiado, gracias a su modelo de conciliación.

```javascript
function HealthStrip(props) {
  return <div className="health-strip">HP: {props.hp} / 100</div>;
}

// One definition, used in every panel that needs the readout
<HealthStrip hp={72} />
```

> [!TIP]
> Piensa en los componentes como placas grabadas del Arsenal: graba el patrón una vez, répítelo donde haga falta y cambia el grabado solo cuando la regla cambie.

## The mindset that carries forward

Hay dos ideas que conviene asentar antes de encender la fragua. Primero, **declarativo**: describe cómo debe verse la interfaz para un estado dado, en lugar de dar una lista de mutaciones al DOM. Segundo, **basado en componentes**: divide la consola en piezas independientes, reutilizables y componibles, sin que la lógica de actualización se filtre entre ellas.

> [!IMPORTANT]
> React es una biblioteca, no un framework. Se centra en renderizar la interfaz. Las herramientas que iremos añadiendo resolverán otros problemas, y eso es intencional.

## Output

```text
La Consola del Arsenal se describirá a sí misma a partir de sus datos.
Cada componente se hará cargo de su propio fragmento de esos datos.
```

## Why this matters

Reconstruir la consola no es un simple cambio estético. Al centralizar cómo se renderiza un valor, se evita toda una clase de errores de desincronización. Aún más importante, se empieza a pensar en términos de *flujo de datos*, no de *cirugía sobre el DOM*. Ese cambio hace que el resto del módulo — props, estado, efectos y enrutamiento — resulte natural, no un conjunto de trucos aislados. Ahora hay que encender la fragua: es hora de preparar el taller y montar el primer componente.

**Siguiente:** [[02 - Punto de Aparición]]
