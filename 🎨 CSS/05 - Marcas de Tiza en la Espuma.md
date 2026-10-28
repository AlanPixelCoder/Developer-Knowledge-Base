# 05. Marcas de Tiza en la Espuma

**Versión original en inglés:** [05 - Chalk Marks in the Foam.md](./05%20-%20Chalk%20Marks%20in%20the%20Foam.md)

**Curso:** CSS
**Capítulo:** 5 — Pseudoelementos
**Tema:** ::first-line, ::first-letter, ::before, ::after, content
**Etiquetas:** `#css` `#tideglass` `#pseudo-elements` `#generated-content`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Capítulo-5-7C5CFF?style=for-the-badge" alt="Capítulo 5">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Cuando baja la marea, los voluntarios marcan avisos con tiza sobre el hormigón húmedo. Esas marcas no forman parte del texto permanente — se añaden para dar énfasis en ese momento: una inicial capitular, una etiqueta "PRECAUCIÓN", una pequeña marca delante del número de una boya. Los pseudoelementos CSS hacen lo mismo: permiten estilizar partes del contenido existente o añadir contenido generado sin editar el HTML.

## Estilizar partes del texto

`::first-letter` estiliza el primer carácter de un bloque. `::first-line` estiliza la primera línea según el ancho — es fluido, no depende de un número fijo de caracteres.

```css
.aviso-marea::first-letter {
  font-size: 2rem;
  color: #ff6b35;
  float: left;
  margin-right: 0.4rem;
}

.aviso-marea::first-line {
  font-weight: bold;
  letter-spacing: 0.02em;
}
```

Estos son toques tipográficos sobre párrafos existentes. Hay que usarlos con moderación — una página de la estación debe seguir siendo legible con poca luz.

## Añadir marcas delante y detrás

`::before` y `::after` crean pseudoelementos que se tratan como hijos del elemento seleccionado. Para que se muestren, es obligatorio usar `content`. Sin `content`, no se renderizan.

```css
.boya::before {
  content: "⚓ ";
  color: #7fc3ff;
}

.advertencia::after {
  content: " [AVISO DE TORMENTA]";
  color: #ff6b35;
  font-weight: bold;
}
```

El texto viene de CSS, no del HTML. Eso sirve para etiquetas puramente presentativas o para marcadores uniformes en muchos elementos.

> [!WARNING]
> **El contenido generado no está en el DOM**
> Los lectores de pantalla pueden o no anunciar el `content`. Trata `::before`/`::after` como decorativos o como etiquetas claramente redundantes. Nunca pongas información crítica (como un teléfono) solo en contenido generado — si debe encontrarse, tiene que estar en el HTML.

## Por qué existe esto

Los pseudoelementos evitan crear elementos HTML "vacíos" solo para usar ganchos de estilo. Un párrafo mantiene su texto natural; CSS añade la marca de tiza. Así el marcado se mantiene semántico y el estilo es flexible. Pero también significa que el texto fuente del HTML no cuenta toda la historia visual — conviene recordarlo al copiar contenido.

## Leer las marcas de espuma

```html
<p class="aviso-marea">La marea sube y arrastra escombros por la rampa inferior. Asegura el equipo y evita el borde del espigón hasta que se levante el aviso.</p>
<p class="boya">Boya 4 - Canal Oeste</p>
<p class="advertencia">Aterrizaje inferior cerrado</p>
```

El aviso recibe la inicial ampliada y la primera línea resaltada. La boya recibe la marca de ancla. La advertencia recibe la etiqueta. Ninguno de esos símbolos existe en el HTML.

## Salida

```text
.aviso-marea
  ::first-letter -> ampliada, naranja, flotada
  ::first-line    -> negrita, espaciado ligero

.boya::before     -> "⚓ " insertado antes del texto
.advertencia::after -> " [AVISO DE TORMENTA]" insertado después del texto
```

### Tarea 5: Marcar la marea que baja

Añade marcas de tiza a una entrada del registro de Tideglass. Estila `::first-letter` y `::first-line` en un párrafo de aviso. Usa `::before` en `.marcador` para añadir `"» "`. Usa `::after` en `.estado` para añadir `" — revisado"`. Asegúrate de que `content` esté presente. Recuerda: el contenido generado no sustituye a datos reales en el HTML.
