# 10. Amarrado

**Versión original en inglés:** [10 - Tied Off.md](./10%20-%20Tied%20Off.md)

**Curso:** CSS
**Capítulo:** 10 — Espaciado y Dimensionado de Caja
**Tema:** Padding/margen, centrado con auto, box-sizing: border-box, resets
**Etiquetas:** `#css` `#tideglass` `#box-sizing` `#centering` `#reset`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-F7DF1E?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Capítulo-10-7C5CFF?style=for-the-badge" alt="Capítulo 10">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

En el muelle de Tideglass, las cuerdas se amarran con cuidado: si hay demasiada holgura, el equipo deriva; si hay muy poca, no cabe. El espaciado en CSS es igual — el padding da aire por dentro, el margen da espacio entre elementos. El truco está en saber cuál usar, y controlar cómo se calcula el ancho para que los paneles no luchen entre sí.

## Padding y margen

`padding` añade espacio dentro del borde (entre contenido y borde). `margin` añade espacio fuera (entre elementos). Ambos aceptan 1-4 valores (arriba, derecha, abajo, izquierda) o abreviaturas como `padding: 10px 20px;` (vertical horizontal).

```css
.entrada-registro {
  padding: 12px 16px;
  margin: 0 0 10px 0;
}

.aviso-muelle {
  margin: 16px auto;
  padding: 8px 12px;
}
```

El fondo cubre el padding, pero no el margen. Los márgenes verticales pueden colapsarse entre elementos bloque adyacentes — hay que tenerlo en cuenta, sin entrar en pánico.

> [!NOTE]
> **Elige con intención**
> ¿Necesitas espacio para que el texto no toque el borde? Padding. ¿Necesitas espacio entre esta caja y la siguiente? Margen. Si dudas, pregunta: ¿está dentro del límite pintado o entre límites?

## Centrar con margin: auto

Para un elemento de bloque con `width` definido, `margin: 0 auto;` lo centra horizontalmente en su contenedor. Los márgenes izquierdo y derecho se reparten el espacio restante por igual.

```css
.panel-instrumentos {
  width: 320px;
  margin: 0 auto; /* arriba/abajo 0, izquierda/derecha auto */
}
```

Solo funciona para elementos bloque con ancho explícito (o restringido). No centra elementos inline ni verticalmente en la mayoría de los casos simples.

## Box sizing: la solución para diseños predecibles

Con `box-sizing: content-box` (por defecto), `width: 320px` significa solo el ancho del contenido. El padding y el borde se suman. Con `box-sizing: border-box`, `width: 320px` significa que contenido + padding + borde caben dentro de 320px. Eso facilita mucho colocar paneles uno al lado de otro.

```css
* {
  box-sizing: border-box;
}

.panel-instrumentos {
  width: 320px;
  padding: 16px;
  border: 1px solid #3a506b;
  /* ancho renderizado total = 320px */
}
```

Aplicar `box-sizing: border-box` a todos los elementos con `*` es un reset pragmático y común que hace los diseños predecibles. No elimina padding/borde, los incluye en el ancho declarado.

> [!WARNING]
> **Lo predecible vence a lo ingenioso**
> Cambiar a `border-box` no es "hacer trampas". Es una decisión deliberada para que las matemáticas coincidan con lo que se escribió. Muchas hojas de estilo modernas lo hacen por esa razón exacta.

## Por qué importa la disciplina con las cuerdas

Bien amarrado, las cuerdas no se cruzan. En CSS, si el cálculo del ancho coincide con lo que se pretende, se pueden construir páginas con varios paneles sin restar padding y bordes constantemente. Ahí está el valor de `border-box`.

## Salida

```text
Padding: espacio dentro del borde (cubierto por el fondo)
Margen:  espacio fuera del borde (no cubierto)
margin: 0 auto: centra un bloque con ancho definido horizontalmente
content-box: width = solo contenido (sumar padding+borde)
border-box:   width = contenido + padding + borde (más fácil)
```

### Tarea 10: Amarrar el muelle

Construye un diseño con paneles del muelle de Tideglass. Dale a `.panel-muelle` padding, margen y borde. Usa `margin: 0 auto` para centrarlo. Aplica `box-sizing: border-box` a todos los elementos (`* { box-sizing: border-box; }`). Demuestra por razonamiento que, con border-box, un panel de `width: 300px` con padding y borde sigue cabiendo en 300px. Crea un segundo panel y observa el espacio entre ellos con el margen.
