# 06. Funciones de Habilidad

**Versión original en inglés:** [06 - Skill Functions.md](06%20-%20Skill%20Functions.md)

**Curso:** JavaScript
**Capítulo:** 6 — Rutinas de Reparación
**Tema:** funciones, parámetros, return, ámbito, funciones flecha
**Etiquetas:** `#javascript` `#funciones` `#ambito` `#flecha` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Cap%C3%ADtulo-6-7C5CFF?style=for-the-badge" alt="Capítulo 6">
  <img src="https://img.shields.io/badge/Trama-Gremio%20de%20Gabinetes-FF6B35?style=for-the-badge" alt="Gremio de Gabinetes">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

En el banco de reparaciones hay rutinas estándar: volver a colocar un relé, limpiar contactos, probar un fusible. Repetir las mismas líneas invita a errores. Una función nombra una rutina, recibe datos y devuelve un resultado para poder llamarla desde cualquier sitio.

## Nombrar una rutina

Se declara con `function`, se le pone un nombre claro, se añaden paréntesis y un bloque. Se llama por su nombre seguido de `()`.

```js
function registrarArranque() {
  console.log("REPARACIÓN: PRUEBA DE ARRANQUE EJECUTADA");
}
registrarArranque();
registrarArranque();
```

## Salida

```text
REPARACIÓN: PRUEBA DE ARRANQUE EJECUTADA
REPARACIÓN: PRUEBA DE ARRANQUE EJECUTADA
```

## Entradas y salidas

Los parámetros permiten pasar valores. `return` envía un valor de vuelta. Si no hay `return`, la función devuelve `undefined`.

```js
function comprobarFusible(tension) {
  if (tension >= 5) {
    return "FUSIBLE: OK";
  } else {
    return "FUSIBLE: SUSTITUIR";
  }
}
console.log(comprobarFusible(6));
console.log(comprobarFusible(3));
```

## Salida

```text
FUSIBLE: OK
FUSIBLE: SUSTITUIR
```

> [!IMPORTANT]
> Los parámetros son nombres locales para los valores que se pasan. `return` finaliza la función y produce un valor que se puede guardar en una variable, pasar a `console.log()` o usar en una expresión.

## Ámbito: lo que queda dentro

Las variables declaradas dentro de una función son locales a esa función. Las declaradas fuera están en un ámbito más amplio y son visibles dentro, pero modificar variables globales sin control acopla las rutinas entre sí.

```js
let idBanco = "BANCO-2"; // global para este script
function informeRele(cantidad) {
  let estado = "EN EJECUCIÓN"; // local
  console.log(idBanco + ": " + cantidad + " relés - " + estado);
}
informeRele(3);
// console.log(estado); // error si se descomenta
```

## Salida

```text
BANCO-2: 3 relés - EN EJECUCIÓN
```

> [!WARNING]
> Evita apoyarte en globales para todo. Pasa lo que necesite la rutina como parámetros. Así la función es más fácil de razonar y mucho menos propensa a romperse cuando otros cambios afecten al código.

## Funciones flecha

Las funciones flecha permiten una sintaxis más corta. En devoluciones simples se pueden omitir `{}` y `return`.

```js
const vatiosACarga = (amperios, voltios) => amperios * voltios;
console.log("CARGA: " + vatiosACarga(2, 12) + "W");
```

## Salida

```text
CARGA: 24W
```

Las funciones flecha no sustituyen a todo (sobre todo con `this` más adelante), pero son prácticas para cálculos puros pequeños, como las conversiones del banco de reparaciones. La clave es la legibilidad: usa la forma que deje la intención más clara.

**Siguiente:** [[07 - Ficha de Personaje]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Pie amarillo" />
</p>
