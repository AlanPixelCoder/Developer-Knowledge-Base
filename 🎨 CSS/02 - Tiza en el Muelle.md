# 02. Tiza en el Muelle

**Versión original en inglés:** [02 - Chalk on the Pier.md](./02%20-%20Chalk%20on%20the%20Pier.md)

**Curso:** CSS
**Capítulo:** 2 — Color y Medida
**Tema:** Colores con nombre, rgb/hex, unidades absolutas vs relativas
**Etiquetas:** `#css` `#tideglass` `#colors` `#units`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Capítulo-2-7C5CFF?style=for-the-badge" alt="Capítulo 2">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Con la marea baja, las tablas del muelle quedan resbaladizas por la sal. Los voluntarios marcan los límites de marea con tiza — rápido, visible y fácil de borrar cuando sube el agua. El sitio de Tideglass hace algo parecido: los colores indican significado (avisos, seguro, sin conexión), y los tamaños deben funcionar tanto en un móvil en el bolsillo como en un terminal de gráficas en el cobertizo de botes.

## Color con una función

Un color solo es útil si tiene significado. En Tideglass, las alertas de tormenta deben destacarse sin deslumbrar, y las etiquetas de datos deben leerse de un vistazo. CSS ofrece tres formas comunes de escribir el mismo matiz: colores con nombre, `rgb()` y hexadecimal.

```css
.aviso {
  color: crimson;        /* con nombre */
}

.marea-alta {
  color: rgb(255, 107, 53); /* rojo, verde, azul */
}

.sin-conexion {
  color: #7c8c92;        /* hex rrggbb */
}
```

`rgb()` recibe tres números de 0 a 255. Los pares hex van de `00` a `ff`. La forma abreviada `#f00` equivale a `#ff0000`. Los tres describen luz; elige uno y sé coherente.

> [!CAUTION]
> **El significado pesa más que la estética**
> Lo "bonito" no es un requisito para una etiqueta de aviso. Si el texto de una alerta de tormenta no destaca lo suficiente sobre su fondo, está roto aunque la paleta parezca más atractiva. Cuando hay duda, prioriza el contraste para el texto.

## Medir para superficies reales

Los píxeles tienta — fijos y precisos. Pero una etiqueta que se ve bien en un monitor ancho se aprieta en una pantalla estrecha. Las unidades deciden qué se adapta y qué se queda. Se dividen en absolutas y relativas.

| Unidad | Tipo | Comportamiento | Cuándo usar |
| :--- | :--- | :--- | :--- |
| `px` | absoluta | Tamaño exacto | Bordes, sombras, detalles que no deben escalar mucho |
| `pt`, `cm` | absoluta | Unidades físicas; poco usadas en pantalla | Solo estilos de impresión |
| `%` | relativa | Relativa al tamaño del elemento padre | Anchos que deben crecer/encoger con el contenedor |
| `em` | relativa | Relativa al tamaño de fuente del elemento (puede acumularse) | Escalado local dentro de un componente |
| `rem` | relativa | Relativa al tamaño de fuente raíz (`html`) | Escalas tipográficas coherentes en toda la página |

## Por qué el apilado perjudica

`em` se acumula. Si un contenedor pone `font-size: 1.2em` y su hijo también `font-size: 1.2em`, el hijo queda a 1.44 veces la base original — fácil de perder el control. `rem` se ancla a `<html>`, así que `1.5rem` siempre es 1.5 veces la raíz sin importar la anidación. Para la mayoría de las escalas de texto, `rem` es el que se mantiene honesto.

```css
html {
  font-size: 16px; /* base */
}

.etiqueta-datos {
  font-size: 1.25rem; /* 20px */
}

.anidado .etiqueta-datos {
  font-size: 1.25rem; /* sigue siendo 20px */
}
```

> [!TIP]
> **Ancla a la raíz**
> Si lo necesitas, fija una base sensata en `html` y usa `rem` para el texto. Usa `em` solo cuando busques intencionalmente un escalado local acumulativo (raro en una página con muchos datos).

## Leer sin adivinar

El ancho es el caso más común para ver unidades en acción. Un ancho en porcentaje ocupa parte del contenedor; uno en píxeles ignora el espacio disponible. Ninguno es "mejor" — cada uno le dice al diseño qué hacer.

```css
.panel-instrumentos {
  width: 80%; /* se adapta al padre */
}

.separador-indicador {
  width: 1px;  /* fijo */
}
```

## Salida

```text
aviso:        crimson
marea-alta:   rgb(255, 107, 53)
sin-conexion: #7c8c92
etiqueta-datos: 1.25rem (20px si la raíz es 16px)
ancho panel:   80% del padre
separador:     1px fijo
```

### Tarea 2: Marcas de tiza para las lecturas

Crea una pequeña lista de lecturas de Tideglass. Estila tres estados (seguro, subiendo, tormenta) con tres notaciones de color distintas. Dale a las etiquetas un tamaño en `rem` pensado sobre una raíz de 16px. Dale a un panel `width: 90%` y a un separador fino `width: 1px`. No adivines — piensa si son absolutas o relativas al escribir.
