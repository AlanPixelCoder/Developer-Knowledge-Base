# 05. Inventario

**Versión original en inglés:** [05 - Inventory.md](05%20-%20Inventory.md)

**Curso:** JavaScript
**Capítulo:** 5 — Caja de Repuestos
**Tema:** arrays, índices, métodos, mutación
**Etiquetas:** `#javascript` `#arrays` `#metodos` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Cap%C3%ADtulo-5-7C5CFF?style=for-the-badge" alt="Capítulo 5">
  <img src="https://img.shields.io/badge/Trama-Gremio%20de%20Gabinetes-FF6B35?style=for-the-badge" alt="Gremio de Gabinetes">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

La caja de repuestos del Gremio guarda una lista ordenada: fusibles, relés, arandelas y algún condensador suelto. Cuando la lista crece o se reduce entre reparaciones, las variables no bastan. Un array guarda los elementos en orden y permite acceder por índice, añadir, quitar o buscar.

## Almacenamiento ordenado

Los arrays usan corchetes `[]` y comas para separar valores. Los índices empiezan en `0`.

```js
let cajaRepuestos = ["fusible", "relé", "arandela", "condensador"];
console.log(cajaRepuestos[0]);
console.log(cajaRepuestos[2]);
console.log("Cantidad: " + cajaRepuestos.length);
```

## Salida

```text
fusible
arandela
Cantidad: 4
```

> [!IMPORTANT]
> El primer elemento tiene índice 0, no 1. El último índice es `length - 1`. Un error de desfase es la forma más común de coger la pieza equivocada.

## Modificar la caja

Los arrays son mutables. Métodos como `push()`, `pop()`, `unshift()`, `shift()` o `splice()` cambian el array in situ. Hay que saber qué extremo se toca y si se necesita el valor eliminado.

```js
let cajaRepuestos = ["fusible", "relé"];
cajaRepuestos.push("diodo");      // añadir al final
console.log(cajaRepuestos);
cajaRepuestos.unshift("arandela"); // añadir al principio
console.log(cajaRepuestos);
let ultimo = cajaRepuestos.pop();  // quitar del final
console.log("Eliminado: " + ultimo);
console.log(cajaRepuestos);
```

## Salida

```text
["fusible", "relé", "diodo"]
["arandela", "fusible", "relé", "diodo"]
Eliminado: diodo
["arandela", "fusible", "relé"]
```

> [!WARNING]
> `push/pop` actúan sobre el final (baratos y muy comunes). `unshift/shift` actúan sobre el principio (reindexan todo el array). En una caja pequeña da igual, pero en listas grandes conviene tenerlo en cuenta.

## Buscar piezas

Para comprobar si hay una pieza sin recorrerla a mano se usan `includes()` o `indexOf()`.

```js
let cajaRepuestos = ["fusible", "relé", "arandela"];
console.log(cajaRepuestos.includes("relé")); // true
console.log(cajaRepuestos.indexOf("arandela")); // 2
console.log(cajaRepuestos.indexOf("bobina"));   // -1 (no existe)
```

## Salida

```text
true
2
-1
```

> [!TIP]
> `indexOf()` devuelve `-1` cuando no lo encuentra, no `false`. Si la lógica depende de "existe", comprueba explícitamente `-1`.

## ¿Por qué usar arrays?

Los arrays agrupan elementos relacionados bajo un mismo nombre, mantienen el orden y ofrecen métodos para reestructurar la lista sin crear decenas de variables. La contrapartida: la mutación es fácil de olvidar. Si dos partes del script modifican el mismo array, el orden de lectura importa: el estado de la caja puede cambiar entre comprobaciones.

**Siguiente:** [[06 - Funciones de Habilidad]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Pie amarillo" />
</p>
