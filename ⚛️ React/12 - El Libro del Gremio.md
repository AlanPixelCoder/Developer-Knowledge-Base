# 12. El Libro del Gremio

**Versión original en inglés:** [12 - The Guild Ledger.md](12%20-%20The%20Guild%20Ledger.md)

**Curso:** React
**Tema:** prop drilling, createContext, Provider, useContext, componentes proveedor personalizados, patrones de estado global
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO_AVANZADO-FF6B35?style=for-the-badge" alt="Intermedio Avanzado">
  <img src="https://img.shields.io/badge/Lecciones-01_--_06-7C5CFF?style=for-the-badge" alt="Lecciones">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

Todo Maestro de Gremio conoce el dolor: los registros importantes deben estar al alcance de todas las salas, cámaras del consejo y puestos avanzados del reino. El Libro del Gremio es el registro central de Emberfall con miembros, contratos y oro. Pero pasar pergaminos desde la Gran Sala hasta el puesto más lejano a través de una cadena de mensajeros es ineficiente y propenso a errores. Esto es exactamente el problema que enfrenta React con el **prop drilling** (paso de props a través de múltiples niveles). La solución es la **API de Contexto**: un conducto mágico que permite que los datos fluyan directamente a cualquier componente del árbol, sin importar lo profundo que esté anidado.

> [!NOTE]
> **Todo el capítulo en una frase**
> La API de Contexto (`createContext`, `Provider`, `useContext`) elimina el prop drilling al proporcionar un estado de tipo global accesible para cualquier componente del árbol, y los componentes proveedor personalizados hacen que este patrón sea reutilizable y limpio.

---

## 01. La carga del prop drilling

El **prop drilling** ocurre cuando pasas props a través de múltiples capas de componentes solo para llegar a un hijo profundamente anidado. Esto crea un acoplamiento fuerte, dificulta la refactorización y sobrecarga los componentes intermedios.

### Ejemplo de prop drilling

Imagina pasar el tema actual del gremio desde `App` hasta un botón `ThemeButton` profundamente anidado:

```javascript
function App() {
  const tema = "ember";
  return <Sala tema={tema} />;
}

function Sala({ tema }) {
  return <Consejo tema={tema} />;
}

function Consejo({ tema }) {
  return <BotonTema tema={tema} />;
}

function BotonTema({ tema }) {
  return <button>Cambiar tema: {tema}</button>;
}
```

`Sala` y `Consejo` no necesitan `tema`, pero deben pasarlo hacia abajo. Esto es prop drilling.

---

## 02. Crear un Contexto

La API de Contexto comienza con `createContext()`. Esto crea un objeto de Contexto que puede usarse para proporcionar y consumir datos.

```javascript
import { createContext } from "react";

export const ContextoTema = createContext();
```

Por defecto, `createContext()` puede recibir un valor opcional, pero es más común proporcionar valores a través de un Provider.

---

## 03. Proporcionar contexto con Provider

Envuelve el árbol de componentes que necesita acceder a los datos con el `Provider` del Contexto. Usa la prop `value` para pasar cualquier cosa: cadenas, objetos, funciones o estado.

### Misión: Proveedor del tema del gremio

```javascript
import React, { useState, createContext } from "react";
import CambiadorTema from "./CambiadorTema";
import Inicio from "./Inicio";

export const ContextoTema = createContext();

function App() {
  const [tema, setTema] = useState("oscuro");

  function alternarTema() {
    setTema(tema === "oscuro" ? "claro" : "oscuro");
  }

  return (
    <ContextoTema.Provider value={{ tema, alternarTema }}>
      <Inicio />
      <CambiadorTema />
    </ContextoTema.Provider>
  );
}

export default App;
```

---

## 04. Consumir contexto con useContext

En lugar de pasar props por todos los niveles, usa el hook `useContext` para acceder al valor del contexto directamente.

### Misión: Usar el tema

```javascript
import React, { useContext } from "react";
import { ContextoTema } from "./App";

function CambiadorTema() {
  const { tema, alternarTema } = useContext(ContextoTema);

  return (
    <button onClick={alternarTema}>
      Tema actual: {tema} | Cambiar
    </button>
  );
}

export default CambiadorTema;
```

---

## 05. Componentes proveedor personalizados - Arquitectura limpia

Para una mejor organización y reutilización, extrae la lógica del contexto a un componente proveedor personalizado. Esto mantiene `App.js` limpio y facilita las pruebas del proveedor.

### Misión: UserContext con proveedor personalizado

```javascript
import React, { createContext, useState } from "react";

export const ContextoUsuario = createContext();

export function ProveedorUsuario({ children }) {
  const [nombre, setNombre] = useState("");

  return (
    <ContextoUsuario.Provider value={{ nombre, setNombre }}>
      {children}
    </ContextoUsuario.Provider>
  );
}
```

### Envolver la aplicación

```javascript
import React from "react";
import { ProveedorUsuario } from "./ContextoUsuario";
import FormularioUsuario from "./FormularioUsuario";
import Resultados from "./Resultados";

function App() {
  return (
    <ProveedorUsuario>
      <FormularioUsuario />
      <Resultados />
    </ProveedorUsuario>
  );
}

export default App;
```

### Consumir en componentes hijos

```javascript
import React, { useContext } from "react";
import { ContextoUsuario } from "./ContextoUsuario";

function FormularioUsuario() {
  const { nombre, setNombre } = useContext(ContextoUsuario);

  return (
    <input
      type="text"
      value={nombre}
      onChange={(e) => setNombre(e.target.value)}
      placeholder="Introduce el nombre de tu aventurero"
    />
  );
}

export default FormularioUsuario;
```

```javascript
import React, { useContext } from "react";
import { ContextoUsuario } from "./ContextoUsuario";

function Resultados() {
  const { nombre } = useContext(ContextoUsuario);

  return <h1>¡Bienvenido al Gremio, {nombre}!</h1>;
}

export default Resultados;
```

---

## 06. Cuándo usar Contexto

El Contexto es potente, pero no es un reemplazo para toda la gestión de estado. Úsalo con sabiduría.

| Caso de Uso | ¿Usar Contexto? | Notas |
| :-- | :-- | :-- |
| Tema (modo oscuro/claro) | Sí | Preferencia global de la interfaz |
| Autenticación/Datos de usuario | Sí | Usuario actual en toda la app |
| Idioma/Localización | Sí | Configuración global de la app |
| Datos de un único formulario | No | Mejor usar estado local |
| Actualizaciones frecuentes (animaciones) | No | Puede causar problemas de rendimiento por re-renderizados |
| Lógica de estado compleja con muchas acciones | Tal vez | Considera reducers (useReducer) o librerías externas |

> [!TIP]
> **Versión para game dev**
> El Libro del Gremio es la única fuente de verdad de Emberfall. El Contexto es como la red mágica de adivinación de los Archivos del Gremio: una vez que inscribes los datos en el Libro, cualquier aventurero (componente) del reino puede acceder a ellos directamente, sin importar lo lejos que esté de la Gran Sala.

---

## ⚡ XP Ganados: Ideas Clave

- 🚧 **Prop drilling:** Pasar props por capas innecesarias es difícil de mantener
- 📦 **createContext:** Crea un objeto de contexto para compartir datos
- 🎁 **Provider:** Envuelve componentes y proporciona datos mediante la prop `value`
- 🔍 **useContext:** Consume datos del contexto sin prop drilling
- 🛠️ **Proveedores personalizados:** Encapsulan la lógica del contexto para un código más limpio y reutilizable
- 🌍 **Patrones globales:** Perfectos para temas, autenticación, idioma y datos globales de la app
- ⚖️ **Usar con sabiduría:** No todo el estado debe ir en el contexto

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🌓 Cambio de tema oscuro/claro en toda la app
- 👤 Autenticación y datos de perfil de usuario
- 🌐 Localización multiidioma
- 🛒 Estado del carrito de compras entre páginas
- 🔔 Sistemas de notificaciones
- ⚙️ Configuración global de la aplicación

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. **Misión básica:** Crea un contexto para un lema del gremio y consúmelo en dos componentes diferentes sin prop drilling.
2. **Misión intermedia:** Construye un contexto de tema con alternancia entre modo oscuro y claro, aplicando estilos dinámicamente a los componentes.
3. **Misión avanzada:** Crea un `ProveedorUsuario` personalizado que gestione el estado de inicio de sesión (conectado/desconectado), compartiéndolo entre múltiples componentes.
4. **Misión compleja:** Construye un contexto de carrito de compras con `añadirAlCarrito`, `eliminarDelCarrito` y `articulosCarrito` accesibles en todo el mercado de Emberfall.
5. **Pelea de jefe:** Forja un sistema completo "Sala del Gremio" usando Contexto: gestiona el nombre del gremio, el número de miembros y los fondos en un proveedor personalizado, con múltiples componentes leyendo y actualizando estos valores.

---

## 🔗 Ver También

- [[11 - El Sistema de Reliquias]] — Hooks como useEffect y useRef
- [[10 - La Fragua]] — Formularios que pueden usar contexto para compartir datos
- [[09 - El Mando]] — Eventos que actualizan el estado del contexto
- [[08 - La Barra de Vida]] — Fundamentos de la gestión del estado
- [[13 - El Mensajero]] — Obtención de datos que puede poblar el contexto

---
