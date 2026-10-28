# 03. Balizas y Lentes

**Versión original en inglés:** [03 - Beacons and Lenses.md](./03%20-%20Beacons%20and%20Lenses.md)

**Curso:** CSS
**Capítulo:** 3 — Selectores I
**Tema:** Selectores de tipo, clase e id; nociones de especificidad
**Etiquetas:** `#css` `#tideglass` `#selectors` `#specificity`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Capítulo-3-7C5CFF?style=for-the-badge" alt="Capítulo 3">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

En noches de niebla, las balizas de Tideglass guían a los barcos de vuelta al promontorio. Un haz amplio ilumina toda una clase de marcadores; una lente enfocada señala una boya concreta. Los selectores CSS funcionan igual: pinceles amplios para patrones compartidos, lentes estrechas para casos específicos. Apuntar bien acorta la hoja de estilos y la hace predecible.

## Tres formas de apuntar

Los selectores más comunes cubren la mayoría de las páginas de la estación. Cada uno tiene un alcance distinto.

| Selector | Sintaxis | Apunta a | Uso |
| :--- | :--- | :--- | :--- |
| Tipo (elemento) | `p { }` | Todos los elementos de esa etiqueta | Estilos base o reseteos globales |
| Clase | `.aviso { }` | Elementos con `class="aviso"` | Estilos reutilizables para muchos elementos |
| ID | `#grafica-mareas { }` | El elemento con `id="grafica-mareas"` | Un único elemento en la página |

```css
/* baliza: todos los párrafos */
p {
  color: #dbe9f5;
}

/* lente: cualquier elemento marcado como aviso */
.aviso {
  color: #ff6b35;
  font-weight: bold;
}

/* punto exacto: la única gráfica de la página */
#grafica-mareas {
  border: 1px solid #3a506b;
}
```

Un elemento puede tener varias clases: `class="aviso fila-datos"`. Los IDs deben ser únicos por página — trátalos como excepciones, no como forma de estilizar todo.

> [!NOTE]
> **Las clases se reutilizan, los IDs son únicos**
> Usa una clase si el estilo podría volver a usarse. Usa un ID solo si realmente hay uno solo. Abusar de los IDs dificulta las sobrescrituras por los motivos de especificidad.

## Especificidad: qué regla gana

Cuando dos reglas apuntan al mismo elemento y establecen la misma propiedad, el navegador compara la especificidad. Gana la de mayor especificidad. Si hay empate, gana la que aparezca más tarde en la hoja de estilos (orden de origen).

Conteo aproximado:
- Selector de tipo: menor
- Selector de clase: mayor que tipo
- Selector de ID: mayor que clase

```css
p { color: #9fb3c8; }        /* tipo */
.aviso { color: #ff6b35; }   /* clase — gana sobre tipo */
#alerta-principal { color: #ff3b30; } /* id — gana sobre clase */
```

Si aplican `.aviso` y `p.aviso`, gana la más específica. No adivines — razona sobre los selectores.

> [!WARNING]
> **Evita luchar con `!important`**
> `!important` rompe la cascada natural y complica la depuración en un sitio con varias páginas. Si una regla necesita `!important` para ganar, probablemente el objetivo está mal apuntado. Corrige el apuntado primero.

## Leer una página con niebla

Los selectores permiten estilizar la estación sin tocar cada etiqueta. Un estilo base para `body` da valores por defecto; las clases gestionan variantes; un ID gestiona el único elemento crítico que debe destacar pase lo que pase.

```html
<body>
  <section id="grafica-mareas">
    <p class="fila-datos">Marea alta: 05:23</p>
    <p class="fila-datos aviso">Aviso de marejada ciclónica</p>
  </section>
</body>
```

La gráfica recibe el estilo del ID. Ambas filas comparten `fila-datos`. Solo el aviso lleva `aviso` encima.

## Salida

```text
Coincidencia de selectores:
  p                -> todos los párrafos (tipo)
  .aviso           -> elementos con clase aviso
  #grafica-mareas  -> elemento con id grafica-mareas

Orden aproximado de especificidad: tipo < clase < id
Empate se resuelve por: orden de aparición (gana el posterior)
```

### Tarea 3: Apuntar las balizas

Estila una lista de instrumentos de Tideglass. Usa un selector de tipo para texto base, una clase para filas `lectura`, una clase para `aviso` (más fuerte), y un ID para `#ultima-lectura` (único). Asegúrate de que el aviso supere a la lectura base cuando ambos apliquen. No uses `!important`. Razona qué regla gana.
