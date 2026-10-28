# 01. Primer Amanecer en Tideglass

**Versión original en inglés:** [01 - Tideglass First Light.md](./01%20-%20Tideglass%20First%20Light.md)

**Curso:** CSS
**Capítulo:** 1 — Fundamentos
**Tema:** Reglas en cascada, anatomía de una regla, vincular hojas de estilo
**Etiquetas:** `#css` `#tideglass` `#basics` `#cascade`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Capítulo-1-7C5CFF?style=for-the-badge" alt="Capítulo 1">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

El Observatorio Tideglass se encuentra en un promontorio gris, donde la sal come la madera sin pintar. El sitio público debe resistir las tormentas: alto contraste, sin adornos que oculten las advertencias. HTML dio a la estación su estructura — páginas de instrumentos, gráficas de mareas, horarios de visita, una tabla de datos y un pequeño formulario. CSS es lo que hace todo eso legible cuando se mira entre la lluvia y el viento.

El trabajo no es decorar. El trabajo es mantener los hechos visibles.

## Una tormenta necesita estructura, no decoración

HTML describe qué es una cosa: `header`, `nav`, `main`, `section`, `table`, `form`. CSS describe cómo se ven. Mezclarlos difumina las responsabilidades — si un encabezado es difícil de leer, se cambia un estilo, no el marcado. Mantenerlos separados permite reestilizar para modo de alto contraste sin reescribir los datos de mareas.

> [!NOTE]
> **Separación de responsabilidades**
> El contenido va en HTML. La presentación va en CSS. La lógica va en otro lugar. Cruza esa línea solo si no hay un camino más limpio, y aún así con cautela.

## La regla como contrato

Una regla CSS es un contrato entre un selector y unas declaraciones. El selector nombra los objetivos; las declaraciones dicen qué cambiar. Sin objetivo, no hay efecto. Un selector roto es solo una regla que el navegador nunca aplica — silenciosa y fácil de pasar por alto.

```css
header {
  background-color: #0f1f2b;
  color: #f0f6ff;
}

nav a {
  color: #7fc3ff;
}
```

La primera regla apunta a todo `<header>`. La segunda apunta a los enlaces dentro de `<nav>`. Cada declaración termina con punto y coma. Una regla puede tener muchas declaraciones; una declaración cambia una propiedad.

> [!WARNING]
> **El silencio es lo normal**
> CSS no lanza errores por un error tipográfico. Si se escribe `backgroud-color` mal, el navegador ignora esa declaración y sigue adelante. Cuando una página queda a medio pintar, lee el archivo de arriba abajo — el fallo suele estar en la puntuación o en una propiedad mal escrita antes de lo que se rompió.

## Conectar la pintura a las páginas

Una hoja de estilos debe vincularse a un documento HTML. En un sitio con varias páginas, una hoja externa mantiene la coherencia y facilita las actualizaciones.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <link href="tideglass.css" rel="stylesheet" />
  <title>Observatorio Tideglass — Lecturas de Mareas</title>
</head>
<body>
  <header>Observatorio Tideglass</header>
</body>
</html>
```

Con tener `tideglass.css` en la misma carpeta basta. Un camino relativo como `tideglass.css` es suficiente. Los comentarios en CSS (`/* ... */`) son para personas y desaparecen para el navegador — útiles para marcar paletas de tormenta sin borrarlas.

## Por qué importa la "cascada" desde el primer día

El nombre *Hojas de Estilo en Cascada* no es publicidad. Cuando varias reglas pueden aplicarse al mismo elemento y establecer la misma propiedad, el navegador necesita un desempate. Esa cascada llega más adelante con detalle, pero conviene recordarlo ya: el orden, el origen y la especificidad cuentan. En una estación que debe leerse, lo predecible vence a lo ingenioso.

## Salida

```text
Fondo de header: #0f1f2b
Texto de header: #f0f6ff
Enlaces de nav:   #7fc3ff
```

### Tarea 1: Encabezado legible en tormenta

Escribe una hoja de estilos externa para una página de instrumentos de Tideglass. Haz el `<header>` de alto contraste, dale a los enlaces de `<nav>` un color distinto pero legible sobre fondo oscuro, y añade un comentario que marque "paleta de tormenta". Usa selectores simples y cuenta los puntos y coma.

> [!TIP]
> **Prueba por sustracción**
> Comenta una sola declaración, imagina la recarga y pregúntate qué cambió. Eso es más rápido que adivinar — y crea el hábito de leer lo que el navegador sí aplica.
