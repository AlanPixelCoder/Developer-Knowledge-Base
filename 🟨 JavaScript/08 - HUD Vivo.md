# 08. HUD Vivo

**Versión original en inglés:** [08 - Living HUD.md](08%20-%20Living%20HUD.md)

**Curso:** JavaScript
**Capítulo:** 8 — Panel Trasero
**Tema:** selección del DOM, innerText, style, addEventListener
**Etiquetas:** `#javascript` `#dom` `#eventos` `#hud` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-FF6B35?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Cap%C3%ADtulo-8-7C5CFF?style=for-the-badge" alt="Capítulo 8">
  <img src="https://img.shields.io/badge/Trama-Gremio%20de%20Gabinetes-FF6B35?style=for-the-badge" alt="Gremio de Gabinetes">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

El panel trasero de un gabinete tiene luces de estado y marcadores. Hasta ahora el script solo escribía en la consola. Para encender esos marcadores, JavaScript tiene que tocar la página: encontrar elementos, cambiar su texto, ajustar estilos y reaccionar a pulsaciones. Ahí entra el DOM.

## Encontrar elementos

Se usa `document.querySelector()` para obtener el primer elemento que coincida con un selector CSS. Lo más práctico es dar a los elementos un atributo `id`.

```js
// Suponiendo <span id="marcadorCreditos">0</span>
let marcador = document.querySelector("#marcadorCreditos");
console.log(marcador);
```

> [!NOTE]
> El selector `#id` apunta a un ID. `.clase` apunta a clases. `button` apunta a una etiqueta. Si no hay coincidencia, `querySelector` devuelve `null`. Intentar leer propiedades de `null` lanzará un error, así que conviene asegurarse de que el elemento existe.

## Cambiar texto y estilos

El texto visible se actualiza con `innerText`. Los estilos CSS en línea se cambian con `.style`.

```js
let marcador = document.querySelector("#marcadorCreditos");
marcador.innerText = "CRÉDITOS: 3";
marcador.style.color = "#F7DF1E";
marcador.style.fontWeight = "bold";
```

## Salida

```text
(el marcador se actualiza en la página)
```

El cambio visual ocurre en el navegador, pero la acción es determinista: encontrar, asignar texto nuevo, asignar propiedades de estilo. `innerText` se centra en el texto visible; `innerHTML` existe, pero puede ser peligroso si se inyecta contenido no confiable.

> [!WARNING]
> Escribir entrada de usuario directamente en `innerHTML` abre la puerta a inyección. Para texto de estado plano, es preferible usar `innerText`.

## Reaccionar con eventos

Un botón no hace nada hasta que se escucha un clic. `addEventListener("click", manejador)` conecta una función para que se ejecute cuando ocurra el evento.

```js
let botonInsertar = document.querySelector("#insertarMoneda");
let marcador = document.querySelector("#marcadorCreditos");
let creditos = 0;

botonInsertar.addEventListener("click", function() {
  creditos = creditos + 1;
  marcador.innerText = "CRÉDITOS: " + creditos;
  marcador.style.color = creditos >= 3 ? "#2DD4BF" : "#F7DF1E";
});
```

## Salida

```text
(al pulsar se actualiza el marcador en la página)
```

> [!TIP]
> El manejador es solo una función. Se puede usar una función con nombre o una función flecha. La lógica es la misma que en la consola: variables, condicionales, aritmética, pero ahora conectada a la página.

## ¿Por qué el DOM?

La consola es un banco de pruebas. El HUD es el gabinete hablando al piloto. Combinando selección, modificación de texto/estilos y escuchadores de eventos, el HTML estático se convierte en un display vivo que responde a las acciones. Todos los conceptos de los capítulos 1–7 (variables, condicionales, bucles, arrays, funciones, objetos) siguen siendo los mismos; solo cambia el destino de salida: pasa de la consola a la página.

**Fin del módulo — Gremio de Gabinetes: Completado**

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Pie amarillo" />
</p>
