# 10. La Fragua

**Versión original en inglés:** [10 - The Forge.md](10%20-%20The%20Forge.md)

**Curso:** React
**Tema:** formularios, htmlFor, onChange, e.target.value, onSubmit, preventDefault, objetos de estado complejos, componentes controlados, select, textarea, lista de verificación de formularios
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-01_--_07-7C5CFF?style=for-the-badge" alt="Lecciones">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

Las brasas de La Fragua brillan lo suficiente como para fundir acero de reliquia. Cada día, aventureros acuden para encargar equipo, inscribirse en contratos del gremio, dejar reseñas al Herrero y presentar informes de misión. Todo esto requiere recopilar datos del usuario. En React, los formularios son el crisol donde se encuentran el estado y los eventos. Al dominar los componentes controlados, aprenderás a forjar formularios herméticos que capturen cada pulsación, validen datos y se envíen limpiamente sin perder ni una brasa de estado.

> [!NOTE]
> **Todo el capítulo en una frase**
> Los formularios de React usan componentes controlados donde el estado es dueño de los datos: vincula `value` al estado, actualízalo con `onChange` y gestiona el envío con `onSubmit` + `preventDefault()` para tener control total sobre cada campo.

---

## 01. Etiquetas y htmlFor

En HTML, el atributo `for` conecta una etiqueta con un campo. En JavaScript, `for` es una palabra reservada para bucles, así que React usa `htmlFor`.

### Misión: Registro en el Gremio

```javascript
function RegistroGremio() {
  return (
    <form>
      <label htmlFor="nombreGremio">Nombre del Gremio:</label>
      <input type="text" id="nombreGremio" />
    </form>
  );
}

export default RegistroGremio;
```

---

## 02. Capturar entrada con onChange

El evento `onChange` se activa con cada pulsación, lo que te permite capturar y seguir la entrada en tiempo real.

### Misión: Vista previa del nombre del gremio

```javascript
import React, { useState } from "react";

function EntradaNombreGremio() {
  const [nombre, setNombre] = useState("");

  function manejarCambio(e) {
    setNombre(e.target.value);
  }

  return (
    <div>
      <input type="text" id="nombre" onChange={manejarCambio} value={nombre} />
      <p>Tu gremio se conocerá como: {nombre}</p>
    </div>
  );
}

export default EntradaNombreGremio;
```

---

## 03. Gestionar el envío del formulario

Por defecto, enviar un formulario recarga la página. Usa `e.preventDefault()` para detener este comportamiento y gestionar el envío con el estado de React.

### Misión: Enviar un contrato

```javascript
import React, { useState } from "react";

function ContratoMision() {
  const [nombreContrato, setNombreContrato] = useState("");

  function manejarEnvio(e) {
    e.preventDefault();
    if (nombreContrato.length > 3) {
      console.log("Contrato enviado al Libro del Gremio:", nombreContrato);
      setNombreContrato("");
    } else {
      alert("El nombre del contrato debe tener más de 3 caracteres.");
    }
  }

  return (
    <form onSubmit={manejarEnvio}>
      <label htmlFor="contrato">Contrato de Misión:</label>
      <input
        type="text"
        id="contrato"
        value={nombreContrato}
        onChange={(e) => setNombreContrato(e.target.value)}
      />
      <button type="submit">Forjar Contrato</button>
    </form>
  );
}

export default ContratoMision;
```

---

## 04. Objetos de estado complejos

Cuando hay múltiples campos, es más limpio usar un único objeto de estado con nombres de propiedad calculados.

### Misión: Inicio de sesión de aventurero

```javascript
import React, { useState } from "react";

function InicioSesionAventurero() {
  const [datosFormulario, setDatosFormulario] = useState({
    correo: "",
    contrasena: "",
    edad: 0
  });

  function manejarDatosFormulario(e) {
    setDatosFormulario({
      ...datosFormulario,
      [e.target.name]: e.target.value
    });
  }

  function manejarEnvio(e) {
    e.preventDefault();
    console.log("Credenciales del aventurero:", datosFormulario);
  }

  return (
    <form onSubmit={manejarEnvio}>
      <label htmlFor="correo">Correo del Gremio:</label>
      <input
        type="email"
        id="correo"
        name="correo"
        value={datosFormulario.correo}
        onChange={manejarDatosFormulario}
      />

      <label htmlFor="contrasena">Contraseña:</label>
      <input
        type="password"
        id="contrasena"
        name="contrasena"
        value={datosFormulario.contrasena}
        onChange={manejarDatosFormulario}
      />

      <label htmlFor="edad">Edad:</label>
      <input
        type="number"
        id="edad"
        name="edad"
        value={datosFormulario.edad}
        onChange={manejarDatosFormulario}
      />

      <button type="submit">Entrar al Gremio</button>
    </form>
  );
}

export default InicioSesionAventurero;
```

> [!WARNING]
> **Regla crítica**
> Usa siempre el operador de propagación `...datosFormulario` al actualizar un objeto de estado. Si lo omites, sobrescribirás todos los demás campos.

---

## 05. Listas desplegables

En las listas desplegables, vincula `value` al elemento `<select>` (no a los `<option>` individuales). No se necesita el atributo `selected`.

### Misión: Elegir tu misión

```javascript
import React, { useState } from "react";

function SelectorMision() {
  const [aventura, setAventura] = useState("");

  function manejarCambio(e) {
    setAventura(e.target.value);
  }

  function manejarEnvio(e) {
    e.preventDefault();
    alert("Has seleccionado: " + aventura);
  }

  return (
    <form onSubmit={manejarEnvio}>
      <label htmlFor="aventura">Selecciona una Misión:</label>
      <select id="aventura" value={aventura} onChange={manejarCambio}>
        <option value="">-- Elige tu destino --</option>
        <option value="Salas Profundas">Expedición a las Salas Profundas</option>
        <option value="Cumbre de Ceniza">Volcán Cumbre de Ceniza</option>
        <option value="Aguja Helada">Ruinas de Aguja Helada</option>
        <option value="Ciénaga Sombría">Caza en la Ciénaga Sombría</option>
      </select>
      <button type="submit">Emprender</button>
    </form>
  );
}

export default SelectorMision;
```

---

## 06. Área de texto

`<textarea>` también es un componente controlado en React. Usa `value` y `onChange`, igual que los campos de entrada.

### Misión: Informe de misión

```javascript
import React, { useState } from "react";

function InformeMision() {
  const [informe, setInforme] = useState("");

  function manejarEnvio(e) {
    e.preventDefault();
    console.log("Informe de misión presentado:", informe);
    setInforme("");
  }

  return (
    <form onSubmit={manejarEnvio}>
      <label htmlFor="informe">Informe de Campo:</label>
      <textarea
        id="informe"
        name="informe"
        value={informe}
        onChange={(e) => setInforme(e.target.value)}
        placeholder="Describe los horrores que presenciaste..."
        rows="5"
        cols="40"
      />
      <button type="submit">Presentar Informe</button>
    </form>
  );
}

export default InformeMision;
```

---

## 07. Lista de verificación de formularios

Sigue estos pasos para forjar un formulario controlado a prueba de fallos:

1. **Inicialización del estado** - Crea el estado para cada campo (o un único objeto)
2. **Elementos controlados** - Vincula `value` al estado en cada input, select y textarea
3. **Manejadores de cambio** - Usa `onChange` para actualizar el estado con cada pulsación o selección
4. **Manejador de envío** - Usa `onSubmit` en el formulario para gestionar el envío
5. **Prevenir comportamiento por defecto** - Llama a `e.preventDefault()` para evitar la recarga de la página

> [!TIP]
> **Versión para game dev**
> Cada página de registro del gremio, formulario de envío de botín o tablero de misiones en Emberfall sigue este mismo patrón. La Fragua no solo da forma al acero, también da forma a los datos que impulsan todo el sitio companion.

---

## ⚡ XP Ganados: Ideas Clave

- 📝 **htmlFor:** Usa `htmlFor` en lugar de `for` para vincular etiquetas y campos
- 🔄 **onChange:** Se activa con cada cambio, ideal para la captura en tiempo real
- 🎯 **Componentes controlados:** El estado de React controla todos los datos del formulario mediante `value`
- 🚫 **preventDefault:** Detiene el comportamiento por defecto del envío del formulario
- 🗃️ **Estado complejo:** Usa un único objeto + propiedades calculadas `[e.target.name]` para múltiples campos
- 📋 **select y textarea:** Ambos funcionan como componentes controlados con `value` y `onChange`
- ✅ **Validación:** Verifica los datos antes de enviar y restablece el estado tras el éxito

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🛡️ Formularios de registro y autenticación del gremio
- 📜 Contratos de misión y inscripciones a aventuras
- 💬 Reseñas de jugadores y formularios de comentarios
- 🛒 Formularios de compra en el mercado de Emberfall
- 📝 Informes de errores y tickets de soporte

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. **Misión básica:** Crea un campo de nombre que muestre "Bienvenido, [nombre], a Emberfall!" en tiempo real.
2. **Misión intermedia:** Construye un formulario de inicio de sesión con correo y contraseña, validando que ambos campos estén rellenos antes del envío.
3. **Misión avanzada:** Crea un formulario con múltiples campos usando un único objeto de estado con nombres de propiedad calculados.
4. **Misión compleja:** Construye un formulario de solicitud al gremio con campos de entrada, una lista desplegable para la clase y un área de texto para la biografía.
5. **Pelea de jefe:** Forja un formulario completo de presentación de carta del gremio con validación, evitando el envío si faltan campos obligatorios y registrando todos los datos en la consola al tener éxito.

---

## 🔗 Ver También

- [[09 - El Mando]] — Eventos que impulsan las interacciones de los formularios
- [[11 - El Sistema de Reliquias]] — Hooks y efectos secundarios para la validación de formularios
- [[12 - El Libro del Gremio]] — Compartir datos de formularios globalmente con Context

---
