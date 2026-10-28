# 07. Luz de Farol

**Versión original en inglés:** [07 - Lantern Light.md](./07%20-%20Lantern%20Light.md)

**Curso:** CSS
**Capítulo:** 7 — Fuentes y Texto
**Tema:** Familias tipográficas, pilas, tamaño, peso, alineación, decoración
**Etiquetas:** `#css` `#tideglass` `#typography` `#fonts`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Capítulo-7-7C5CFF?style=for-the-badge" alt="Capítulo 7">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

La sala de faroles de Tideglass guarda lámparas de repuesto porque la niebla oculta el promontorio. Con poca luz, un tipo legible importa más que uno decorativo. En el sitio de la estación, las lecturas de instrumentos, los avisos y los horarios de visita deben leerse de un vistazo. La tipografía no es solo estética — es claridad bajo presión.

## Elegir una familia tipográfica

`font-family` acepta una lista (pila tipográfica). El navegador prueba la primera; si no está disponible, prueba la siguiente; y acaba con una familia genérica como red de seguridad. Con fuentes del sistema se evitan descargas y se mantiene la coherencia.

```css
body {
  font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
}

code,
.lectura-datos {
  font-family: "JetBrains Mono", "Fira Code", monospace;
}
```

Usa sans-serif para la interfaz, monospace para las lecturas numéricas donde importa la alineación.

> [!NOTE]
> **Las genéricas son obligatorias**
> Termina siempre con una genérica como `serif`, `sans-serif`, `monospace` o `cursive`. Si fallan todas las fuentes nombradas, el navegador elegirá una — sin genérica, el comportamiento es impredecible en la práctica.

## Tamaño, peso e interlineado

`font-size` fija el tamaño (usa `rem` en la mayoría de los casos). `font-weight` controla el grosor (valores comunes 400, 700, o palabras clave como `bold`). `line-height` afecta la legibilidad — muy apretado cansa, muy suelto desconecta. Un `line-height` sin unidad (como `1.6`) escala con el tamaño de fuente y suele ser lo más seguro.

```css
body {
  font-size: 1rem;
  line-height: 1.6;
  font-weight: 400;
}

h1 {
  font-size: 2rem;
  font-weight: 700;
  line-height: 1.2;
}

.lectura-datos {
  font-weight: 600;
  letter-spacing: 0.02em;
}
```

## Alineación y decoración del texto

`text-align` controla la alineación horizontal (`left`, `right`, `center`, `justify`). `text-decoration` añade líneas (`underline`, `line-through`, `none`). Al quitar el subrayado a los enlaces hay que sustituirlo por otros indicadores para mantener la claridad.

```css
.aviso-tormenta {
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

nav a {
  text-decoration: none;
}

nav a:hover {
  text-decoration: underline;
}
```

> [!TIP]
> **Claridad ante originalidad**
> Las mayúsculas pueden ayudar a destacar etiquetas, pero largos bloques en mayúsculas son difíciles de leer. Usa `text-transform` con moderación para etiquetas cortas como encabezados, tags o avisos.

## Por qué importa

La tipografía forma parte de la cascada de legibilidad. Unas fuentes malas ocultan datos importantes. Unas buenas marcan la diferencia entre leer un aviso de tormenta rápido o pasarlo por alto. En Tideglass, esa diferencia es práctica.

## Salida

```text
Cuerpo:      pila sans-serif, 1rem, line-height 1.6, peso 400
Encabezados: mayores, peso 700, line-height más ajustado
Lecturas:    pila monospace, peso 600, ligero espaciado
Avisos:      centrados, mayúsculas, espaciados
Enlaces:     sin subrayado por defecto, con subrayado al pasar el ratón
```

### Tarea 7: Iluminar la lectura

Estila un panel de lecturas de Tideglass. Pon una pila tipográfica en `body` terminando con una genérica. Usa `rem` para `h1` y texto base. Pon `line-height` sin unidad en `body`. Estila `.lectura-datos` con pila monospace. Centra `.aviso-tormenta`, ponlo en mayúsculas con `letter-spacing`. Quita el subrayado de los enlaces de navegación y vuelve a ponerlo en `:hover`. No sacrifiques la visibilidad del foco.
