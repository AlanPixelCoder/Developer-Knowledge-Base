# 09. El Mando

**Versión original en inglés:** [09 - The Controller.md](09%20-%20The%20Controller.md)

**Curso:** React
**Tema:** eventos sintéticos, onClick, objeto de evento, estilos en línea con camelCase, eventos de ratón, focus/blur, tabIndex, eventos de teclado, e.key, composición de eventos para accesibilidad
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-01_--_06-7C5CFF?style=for-the-badge" alt="Lecciones">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

Las puertas de la Arena de Emberfall acaban de abrirse. Los espectadores inundan las gradas, los retadores pisan la arena y el HUD del gremio debe responder en el instante en que alguien pulse un botón, pase el ratón por un estandarte o presione una tecla para ponerse en guardia. Hasta este punto, tus componentes han sido estatuas: se renderizaban con marcado estático o cambiaban solo cuando el estado lo hacía por su cuenta. Ahora es hora de empuñar **El Mando**: el sistema de eventos de React. Cada clic, toque, desplazamiento, enfoque o pulsación de tecla se convierte en una orden que puedes interceptar, validar y enrutar a través del sitio companion de Emberfall.

> [!NOTE]
> **Todo el capítulo en una frase**
> React envuelve los eventos nativos del navegador en una capa de eventos sintéticos y te permite adjuntar manejadores en camelCase (como `onClick`, `onMouseOver`, `onFocus`, `onKeyDown`) a los elementos, para que tu HUD de Emberfall reaccione a la entrada del usuario al instante, manteniéndose accesible para teclado y tecnologías de asistencia.

---

## 01. Eventos sintéticos

> [!NOTE]
> **Información clave**
> React envuelve los eventos nativos del navegador en un **envoltorio de eventos sintéticos** para garantizar la consistencia entre navegadores. Los manejadores se escriben en **camelCase** (por ejemplo, `onClick`), no en minúsculas como en HTML.

Los eventos son las interacciones del usuario: clics, envíos de formularios, cargas de página, etc. En React, debes pasar funciones a los manejadores de eventos, no cadenas.

### Misión: Un botón que responde

```javascript
function handleClick() {
  alert("¡Hola! ¡Hiciste clic en mí!");
}

function App() {
  return <h1 onClick={handleClick}>Haz clic aquí</h1>;
}

export default App;
```

**Reglas importantes:**

- Define el manejador por separado
- Pásalo **sin paréntesis** (`handleClick`, no `handleClick()`). Si añades paréntesis, la función se ejecutará al renderizar, no al hacer clic

---

## 02. El objeto de evento

Cada manejador recibe un objeto de evento `e` (o `event`). React lo pasa automáticamente. Puedes usarlo para acceder al elemento que desencadenó el evento con `e.target`.

### Misión: Cambiar color al hacer clic

```javascript
function handleClick(e) {
  e.target.style.backgroundColor = "yellow";
}

function App() {
  return <button onClick={handleClick}>Púlsame</button>;
}

export default App;
```

> [!WARNING]
> **Error común**
> Los estilos en línea en JSX usan **camelCase**. En lugar de `background-color`, usa `backgroundColor`. En lugar de `font-size`, usa `fontSize`.

---

## 03. Eventos del ratón: hover

Los eventos `onMouseOver` y `onMouseLeave` te permiten mostrar información cuando el usuario pasa el ratón sobre un elemento.

### Misión: Tooltip en la Arena

```javascript
import React, { useState } from "react";

function ArenaBanner() {
  const [showTooltip, setShowTooltip] = useState(false);

  return (
    <div>
      <h1
        onMouseOver={() => setShowTooltip(true)}
        onMouseLeave={() => setShowTooltip(false)}
      >
        Estandarte de la Arena de Emberfall
      </h1>
      {showTooltip && <div className="tooltip">¡Inscripciones abiertas hasta el anochecer!</div>}
    </div>
  );
}

export default ArenaBanner;
```

---

## 04. Focus y Blur

`onFocus` se activa cuando un elemento recibe el foco (se selecciona o se hace clic en él). `onBlur` se activa cuando el elemento pierde el foco (se hace clic fuera o se pulsa Tab para salir).

### Misión: Resaltar el campo de gremio

```javascript
function handleFocus(e) {
  e.target.style.backgroundColor = "lightblue";
}

function handleBlur(e) {
  e.target.style.backgroundColor = "white";
}

function GuildForm() {
  return (
    <div>
      <label htmlFor="guildName">Nombre del Gremio:</label>
      <input
        type="text"
        id="guildName"
        onFocus={handleFocus}
        onBlur={handleBlur}
      />
    </div>
  );
}

export default GuildForm;
```

Los elementos que no son de formulario (`<div>`, `<img>`) no pueden recibir foco por defecto. Para habilitarlo, añade `tabIndex={0}`.

### Misión: Ampliar un emblema con enfoque

```javascript
function handleZoomIn(e) {
  e.target.style.transform = "scale(1.2)";
}

function handleZoomOut(e) {
  e.target.style.transform = "scale(1)";
}

function Emblem() {
  return (
    <img
      src="/emblem.png"
      alt="Emblema de Emberfall"
      tabIndex={0}
      onFocus={handleZoomIn}
      onBlur={handleZoomOut}
      style={{ transition: "transform 0.2s" }}
    />
  );
}

export default Emblem;
```

---

## 05. Eventos de teclado

`onKeyDown` se activa cuando se pulsa una tecla. `onKeyUp` se activa cuando se suelta. Usa `e.key` para identificar qué tecla se ha pulsado.

### Misión: Atajos del HUD

```javascript
function handleKeyDown(e) {
  if (e.key === "h" || e.key === "H") {
    e.target.style.backgroundColor = "gold";
  }
}

function HUD() {
  return <div onKeyDown={handleKeyDown} tabIndex={0}>Pulsa H para resaltar el HUD</div>;
}

export default HUD;
```

Patrones comunes para accesibilidad:

- `e.key === "ArrowUp"` / `e.key === "ArrowDown"` para controles de volumen
- `e.key === " "` o `e.key === "Enter"` para activar botones con teclado

---

## 06. Composición de eventos para accesibilidad

Los mejores componentes del HUD responden tanto al ratón como al teclado. Un botón de "Asistir" en la Arena debe funcionar con clic, pasar el ratón, enfocar con Tab y activarse con Enter o Espacio.

### Misión: Botón "Asistir" accesible

```javascript
import React, { useState } from "react";

function AttendButton() {
  const [goingCount, setGoingCount] = useState(0);
  const [isHovering, setIsHovering] = useState(false);

  function handleAttend() {
    setGoingCount(goingCount + 1);
    alert("¡Te has registrado para la Noche de la Arena!");
  }

  function handleKeyDown(e) {
    if (e.key === " " || e.key === "Enter") {
      e.preventDefault();
      handleAttend();
    }
  }

  return (
    <button
      tabIndex="0"
      onClick={handleAttend}
      onMouseEnter={() => setIsHovering(true)}
      onMouseLeave={() => setIsHovering(false)}
      onFocus={() => setIsHovering(true)}
      onBlur={() => setIsHovering(false)}
      onKeyDown={handleKeyDown}
      onKeyUp={() => {}}
      style={{
        backgroundColor: isHovering ? "#61DAFB" : "#e0e0e0",
        padding: "10px 20px",
        cursor: "pointer"
      }}
    >
      Asistir ({goingCount})
    </button>
  );
}

export default AttendButton;
```

> [!TIP]
> **Versión para game dev**
> Todo HUD de juego combina estos eventos. Los menús deben ser navegables con teclado (tabIndex + onKeyDown), los iconos deben mostrar tooltips al pasar el ratón (onMouseOver/onMouseLeave) y los botones deben dar feedback visual al enfocar (onFocus). La accesibilidad no es opcional: es lo que hace jugable tu HUD para todos los aventureros.

---

## ⚡ XP Ganados: Ideas Clave

- 🎮 **Eventos sintéticos:** React envuelve eventos nativos para mayor consistencia entre navegadores
- 🖱️ **onClick:** Define manejadores por separado y pásalos sin paréntesis
- 🎯 **e.target:** Accede al elemento que desencadenó el evento
- 🎨 **Estilos en línea:** Usa camelCase (`backgroundColor`, no `background-color`)
- 🖱️ **Ratón:** `onMouseOver`/`onMouseLeave` para tooltips y efectos hover
- 👁️ **Foco:** `onFocus`/`onBlur` para validación y resaltado; usa `tabIndex={0}` en elementos no enfocables
- ⌨️ **Teclado:** `onKeyDown`/`onKeyUp` con `e.key` para atajos; gestiona Espacio/Enter para accesibilidad
- ♿ **Composición:** Combina eventos para soportar ratón y teclado por igual

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🎯 Botones interactivos en el HUD del gremio
- 💬 Tooltips informativos al pasar el ratón
- 📝 Resaltado de campos de formulario al enfocar
- ⌨️ Atajos de teclado en paneles de administración
- ♿ Interfaces accesibles para todos los usuarios

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. **Misión básica:** Crea un botón que muestre una alerta con el mensaje "¡Has forjado una Espada de Emberfall!" al hacer clic.
2. **Misión intermedia:** Implementa un tooltip que aparezca solo cuando el ratón esté sobre el nombre de un objeto.
3. **Misión avanzada:** Crea un campo de entrada que cambie de color al enfocar y vuelva al original al perder el foco.
4. **Misión de teclado:** Añade un div con `tabIndex={0}` que cambie su color al pulsar las teclas "R", "G" o "B".
5. **Pelea de jefe:** Construye un botón "Unirse al Gremio" completamente accesible que funcione con clic, hover, foco y las teclas Espacio/Enter, mostrando un contador de miembros.

---

## 🔗 Ver También

- [[10 - La Fragua]] — Formularios que combinan eventos con estado
- [[11 - El Sistema de Reliquias]] — Ciclo de vida y efectos secundarios
- [[12 - El Libro del Gremio]] — Estado global para interacciones compartidas

---
