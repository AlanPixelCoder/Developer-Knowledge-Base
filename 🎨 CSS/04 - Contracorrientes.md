# 04. Contracorrientes

**Versión original en inglés:** [04 - Crosscurrents.md](./04%20-%20Crosscurrents.md)

**Curso:** CSS
**Capítulo:** 4 — Selectores II
**Tema:** Agrupación, combinador hijo, encadenamiento
**Etiquetas:** `#css` `#tideglass` `#selectors` `#combinators`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Capítulo-4-7C5CFF?style=for-the-badge" alt="Capítulo 4">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

En el estrecho de la bahía de Tideglass, las corrientes se cruzan y empujan en direcciones distintas. Un barco descuidado queda atrapado en ambas. Uno prudente elige un canal. Los selectores tienen sus propias corrientes: la agrupación comparte reglas, los combinadores siguen relaciones en el marcado y el encadenamiento exige que el elemento cumpla todas las partes.

## Compartir la carga con agrupación

Cuando varios selectores distintos necesitan exactamente las mismas declaraciones, agruparlos ahorra líneas y evita errores. Se separan con comas.

```css
h1,
h2,
.titulo-instrumento {
  color: #f0f6ff;
  font-family: "Inter", system-ui, sans-serif;
}
```

La coma significa "o". No hace falta relación — solo estilos compartidos. Si un selector del grupo es inválido, en algunos casos el grupo completo puede comportarse mal, pero lo práctico es mantener grupos pequeños y claros.

## Seguir la marea con combinadores

A veces solo quieres estilizar elementos que están en un lugar concreto del árbol HTML. El combinador hijo (`>`) solo coincide con hijos directos. Esa precisión importa en páginas de instrumentos con listas anidadas.

```css
.panel-mareas > h2 {
  margin-top: 0;
  border-bottom: 1px solid #3a506b;
}
```

Solo un `h2` que sea hijo directo de `.panel-mareas` recibe ese estilo. Un `h2` más profundo dentro de un subpanel no se ve afectado. Así se evitan estilos no deseados en componentes reutilizados.

> [!TIP]
> **Sé explícito cuando la profundidad importa**
> Si el estilo es para "el encabezado de este panel", usa `>`. Si realmente es para "cualquier encabezado dentro de este panel", existen selectores descendientes, pero conviene priorizar la precisión para evitar sorpresas.

## Encadenar para una captura estrecha

Encadenar significa juntar selectores sin espacio: `p.aviso` significa "un párrafo que además tenga la clase aviso". Ambas condiciones deben cumplirse. Eso es distinto a un descendiente.

```css
p.aviso {
  background-color: #2a1f0f;
  border-left: 3px solid #ff6b35;
  padding: 0.5rem 0.75rem;
}
```

Un `div.aviso` no coincidiría. Un `p` sin `aviso` tampoco. El encadenamiento es perfecto para variantes que solo tienen sentido en ciertos elementos.

> [!WARNING]
> **Sin espacio cambia todo**
> `.panel .aviso` (con espacio) significa "un aviso dentro de un panel". `.panel.aviso` (sin espacio) significa "un panel que además es un aviso". Lee de izquierda a derecha, pero vigila el espacio — ahí está la diferencia entre relación y condiciones combinadas.

## Leer la contracorriente

Todo junto en una tarjeta de datos de la estación:

```html
<section class="panel-mareas">
  <h2>Lecturas del Cobertizo de Botes</h2>
  <ul class="lista-lecturas">
    <li>Temperatura del agua: 12°C</li>
    <li class="aviso">Caída de salinidad: revisar toma</li>
  </ul>
  <p class="aviso">Aviso general: asegurar objetos sueltos</p>
</section>
```

```css
h1, h2, .titulo-instrumento { color: #f0f6ff; }
.panel-mareas > h2 { margin-top: 0; }
p.aviso { border-left: 3px solid #ff6b35; }
```

El `h2` directo del panel recibe la regla. El `li.aviso` no es un `p`, así que `p.aviso` no lo estiliza. El `p.aviso` sí se estiliza. Pequeños detalles, gran diferencia cuando la página crece.

## Salida

```text
Mapa de contracorrientes:
  h1, h2, .titulo     -> agrupado (o)
  .panel > h2         -> solo hijo directo
  p.aviso             -> elemento Y clase
  .panel .aviso       -> aviso dentro de panel
  .panel.aviso        -> elemento panel que tiene clase aviso
```

### Tarea 4: Navegar el estrecho

Estila un tablón de visitas de Tideglass. Agrupa `h1` y `h2` para compartir color. Usa `>` para estilizar solo el `h3` directo de `.panel-visitas`. Encadena `p.aviso` para un estilo de aviso en párrafo que no afecte a `li.aviso`. Debes poder explicar por qué cada regla acierta o falla con un marcado de ejemplo. Cambia una coma para ver el efecto de la agrupación.
