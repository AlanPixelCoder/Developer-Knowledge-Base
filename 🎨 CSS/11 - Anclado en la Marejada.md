# 11. Anclado en la Marejada

**Versión original en inglés:** [11 - Anchored in the Swell.md](./11%20-%20Anchored%20in%20the%20Swell.md)

**Curso:** CSS
**Capítulo:** 11 — Visualización y Posicionamiento
**Tema:** block/inline/inline-block, static/relative/absolute/fixed/sticky, z-index
**Etiquetas:** `#css` `#tideglass` `#display` `#positioning` `#z-index`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-F7DF1E?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Capítulo-11-7C5CFF?style=for-the-badge" alt="Capítulo 11">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

En la marejada, las boyas derivan con la corriente a menos que estén ancladas. Los elementos en CSS fluyen naturalmente a menos que se cambie su comportamiento o se anclen a contextos distintos. Entender `display` y `position` permite crear diseños estables incluso cuando el contenido cambia como la marea.

## Display: cómo se sitúan los elementos en el flujo

Cada elemento tiene un valor `display` por defecto. Los principales:
- `block` - ocupa todo el ancho disponible, empieza en una nueva línea (ej. `div`, `p`, `h1`)
- `inline` - fluye con el texto, ignora width/height (ej. `span`, `a`)
- `inline-block` - fluye como inline pero acepta width/height y padding/margin (útil para botones)
- `none` - se elimina completamente del flujo

```css
.enlace-nav {
  display: inline-block;
  padding: 8px 12px;
}

.alerta-oculta {
  display: none; /* no visible, no está en el layout */
}
```

Cambiar `display` es poderoso, pero hay que tener cuidado de no romper la semántica. Un enlace debe seguir siendo un enlace.

> [!TIP]
> **Inline vs inline-block**
> Si necesitas dar padding vertical a un enlace para que sea clicable en una pantalla pequeña, `inline-block` o cómo se comporta el padding importa. Justifica el cambio por lo que quieres conseguir.

## Position: anclar en distintos contextos

`position` controla cómo se coloca un elemento:
- `static` - por defecto, flujo normal
- `relative` - relativo a su posición normal; el desplazamiento no lo saca del flujo
- `absolute` - relativo al ancestro posicionado más cercano (cualquiera menos static); se saca del flujo
- `fixed` - relativo a la ventana (viewport); se saca del flujo, se queda al hacer scroll
- `sticky` - alterna entre relative y fixed según el scroll

```css
.insignia-estado {
  position: absolute;
  top: 8px;
  right: 8px;
}

.volver-arriba {
  position: fixed;
  bottom: 16px;
  right: 16px;
}

.barra-aviso {
  position: sticky;
  top: 0;
}
```

> [!WARNING]
> **Absolute necesita un ancla**
> Si un elemento es `position: absolute` y ninguno de sus ancestros está posicionado (relative/absolute/fixed/sticky), se posicionará respecto a la ventana o al bloque contenedor inicial. Siempre crea un contexto de posicionamiento con `position: relative` en el padre cuando quieras posicionar absoluto dentro de él.

## Z-index: orden de apilamiento

Cuando los elementos se solapan (por absolute/fixed/relative), `z-index` controla cuál queda encima. Los valores mayores ganan. `z-index` solo funciona en elementos posicionados (no `static`).

```css
.fondo-modal {
  position: fixed;
  z-index: 1000;
}

.contenido-modal {
  position: relative;
  z-index: 1001;
}
```

## Pensar en un layout de Tideglass

Imagina una página de la estación: una barra de avisos sticky arriba, una navegación fija, una gráfica con una insignia posicionada absolutamente dentro de un panel (anclada por relative en el panel). La lógica es clara: flujo para contenido normal, anclaje para excepciones.

## Salida

```text
Display: block/inline/inline-block/none
Position: static(por defecto) | relative | absolute | fixed | sticky
Absolute: necesita ancestro posicionado para anclaje predecible
Fixed: relativo a la ventana
Sticky: pasa de relativo a fijo
Z-index: solo en elementos posicionados, gana el mayor
```

### Tarea 11: Anclar la marejada

Construye un fragmento de layout de la estación Tideglass. Haz `.barra-nav` `position: sticky` arriba. Crea `.panel-indicador` con `position: relative`. Pon `.insignia-aviso` dentro con `position: absolute` anclado al panel. Añade `.estado-muelle` como `position: fixed`. Usa `display: inline-block` en los enlaces de navegación. Razona qué elementos salen del flujo.
