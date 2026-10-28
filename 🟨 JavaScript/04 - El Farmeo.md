# 04. El Farmeo

**Versión original en inglés:** [04 - The Farm.md](04%20-%20The%20Farm.md)

**Curso:** JavaScript
**Capítulo:** 4 — Bucle de Enfriamiento
**Tema:** while, for, break, continue
**Etiquetas:** `#javascript` `#bucles` `#iteracion` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Cap%C3%ADtulo-4-7C5CFF?style=for-the-badge" alt="Capítulo 4">
  <img src="https://img.shields.io/badge/Trama-Gremio%20de%20Gabinetes-FF6B35?style=for-the-badge" alt="Gremio de Gabinetes">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

Tras una sobrecarga, las aletas de enfriamiento del gabinete necesitan un bucle temporizado. No quieres copiar y pegar diez `console.log()`, quieres que el script repita el trabajo hasta que una condición diga que pare. Ahí entra la iteración.

## while: comprobar primero

`while` comprueba la condición antes de cada pasada. Si es falsa al inicio, el cuerpo se ejecuta cero veces.

```js
let carga = 0;
while (carga < 3) {
  carga = carga + 1;
  console.log("REFRIGERANTE: CICLO " + carga);
}
console.log("REFRIGERANTE: LISTO");
```

## Salida

```text
REFRIGERANTE: CICLO 1
REFRIGERANTE: CICLO 2
REFRIGERANTE: CICLO 3
REFRIGERANTE: LISTO
```

> [!CAUTION]
> Todo `while` necesita un modo para que la condición se vuelva falsa. Si nada dentro modifica una variable que comprueba la condición, el bucle nunca termina. Ahí está la trampa del bucle infinito.

## for: número conocido

Cuando sabes el número exacto de repeticiones, `for` mantiene el contador y su actualización en un solo sitio. Es simplemente `while` con la contabilidad trasladada a la cabecera.

```js
for (let pulso = 1; pulso <= 4; pulso++) {
  console.log("VENTILADOR: PULSO " + pulso);
}
```

## Salida

```text
VENTILADOR: PULSO 1
VENTILADOR: PULSO 2
VENTILADOR: PULSO 3
VENTILADOR: PULSO 4
```

| Cláusula | Cuándo | Propósito |
| :--- | :--- | :--- |
| `let pulso = 1` | una vez | inicializar |
| `pulso <= 4` | antes de cada pasada | comprobar |
| `pulso++` | después de cada pasada | actualizar |

## break y continue

`break` sale del bucle por completo. `continue` pasa a la siguiente iteración (y en un `for` ejecuta la cláusula de actualización).

```js
for (let ranura = 1; ranura <= 6; ranura++) {
  if (ranura === 3) continue; // saltar aleta bloqueada
  if (ranura === 5) break;    // parada de emergencia
  console.log("ALETA: ACTIVA " + ranura);
}
```

## Salida

```text
ALETA: ACTIVA 1
ALETA: ACTIVA 2
ALETA: ACTIVA 4
```

> [!WARNING]
> `break` y `continue` son potentes, pero dificultan seguir el flujo. Primero intenta ajustar la condición. Úsalos solo ante una excepción real, como una ranura bloqueada o una parada de emergencia.

## ¿Por qué elegir una forma u otra?

La elección entre `while` y `for` es cuestión de claridad, no de capacidad. Usa `while` cuando la parada sea un evento ("hasta que esté estable"), usa `for` cuando el número de pasadas sea fijo ("hacer exactamente N veces"). En cualquier caso, el motor repite mecánicamente: lo que evita errores es que la condición de parada sea obvia e imposible de pasar por alto.

**Siguiente:** [[05 - Inventario]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Pie amarillo" />
</p>
