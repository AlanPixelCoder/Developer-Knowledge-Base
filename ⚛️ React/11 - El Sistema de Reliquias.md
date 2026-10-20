# 11. El Sistema de Reliquias

**Versión original en inglés:** [11 - The Relic System.md](11%20-%20The%20Relic%20System.md)

**Curso:** React
**Tema:** hooks, transición clase→funcional, useEffect, efectos secundarios, array de dependencias, limpieza, useRef, estado vs referencias
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

En las profundidades de las bóvedas de Emberfall yacen reliquias antiguas, selladas durante siglos. Estos artefactos laten con un poder oculto que solo se despierta cuando se cumplen ciertas condiciones. Al igual que estas reliquias, los componentes de React tienen poderes más allá de renderizar la interfaz: pueden obtener datos de los Archivos del Gremio, interactuar directamente con el DOM, configurar temporizadores para eventos de la arena y limpiarse a sí mismos. Estos son los **efectos secundarios**, y el Sistema de Reliquias (Hooks) te proporciona las herramientas para controlarlos.

> [!NOTE]
> **Todo el capítulo en una frase**
> Los Hooks permiten a los componentes funcionales usar estado y características del ciclo de vida: `useEffect` gestiona los efectos secundarios con control preciso mediante el array de dependencias y las funciones de limpieza, mientras que `useRef` conserva valores mutables entre renders sin provocar nuevos renders.

---

## 01. El despertar de los Hooks

Los Hooks se introdujeron en **React 16.8** (febrero de 2019), permitiendo a los componentes funcionales usar estado y métodos del ciclo de vida sin escribir componentes de clase.

### De clases a funciones

Antes de los Hooks, los componentes de clase eran verbosos. Ahora, el enfoque funcional es el preferido.

**Componente de clase (heredado):**
```javascript
class Planeta extends React.Component {
  constructor(props) {
    super(props);
    this.state = { reino: "Caída de Ceniza" };
  }
  render() {
    return <h1>El reino de {this.state.reino}</h1>;
  }
}
```

**Componente funcional con useState (moderno):**
```javascript
import React, { useState } from "react";

function Planeta() {
  const [reino, setReino] = useState("Emberhold");
  return <h1>El reino de {reino}</h1>;
}
```

---

## 02. useEffect - Despertar las reliquias

`useEffect` te permite realizar **efectos secundarios**: operaciones que van más allá del ciclo de renderizado de React. Ejemplos: obtener datos, configurar suscripciones, temporizadores o manipular el DOM manualmente.

### Sintaxis básica

```javascript
useEffect(function() {
  // Lógica del efecto secundario
}, [arrayDependencias]);
```

### Momento de ejecución

- **Array de dependencias vacío `[]`**: Se ejecuta una vez, tras el renderizado inicial. Perfecto para obtener datos iniciales.
- **Sin array de dependencias**: Se ejecuta tras cada renderizado. ¡Usar con precaución!
- **Con dependencias `[contador]`**: Se ejecuta solo cuando `contador` cambia.

### Misión: Registrar entrada al reino

```javascript
import React, { useEffect, useState } from "react";

function PuertaReino() {
  const [visitantes, setVisitantes] = useState(0);

  useEffect(() => {
    console.log(`Ha entrado un nuevo aventurero. Total: ${visitantes}`);
  }, [visitantes]);

  return (
    <button onClick={() => setVisitantes(visitantes + 1)}>
      Entrar a Emberhold ({visitantes})
    </button>
  );
}

export default PuertaReino;
```

---

## 03. Limpieza - Sellar las reliquias

Algunos efectos (temporizadores, escuchadores de eventos, suscripciones) persisten después de que el componente se desmonte o se vuelva a renderizar. Esto puede causar fugas de memoria. Para evitarlo, **devuelve una función de limpieza** desde `useEffect`.

### Misión: Temporizador de la arena

```javascript
import React, { useState, useEffect } from "react";

function TemporizadorArena() {
  const [segundos, setSegundos] = useState(0);

  useEffect(function() {
    const idIntervalo = setInterval(function() {
      setSegundos(function(segundosPrevios) {
        return segundosPrevios + 1;
      });
    }, 1000);

    return function() {
      clearInterval(idIntervalo);
      console.log("Temporizador de la arena sellado - reliquia desactivada");
    };
  }, []);

  return <h1>Tiempo de Arena: {segundos}s</h1>;
}

export default TemporizadorArena;
```

> [!WARNING]
> **Regla crítica**
> Limpia siempre los efectos que creen recursos persistentes. React ejecuta la limpieza antes de desmontar el componente y antes de volver a ejecutar el efecto.

---

## 04. useRef - Preservar la esencia de las reliquias

`useRef` crea una referencia mutable que persiste entre renderizados. El valor se almacena en `.current`. **Modificar `.current` NO provoca un nuevo renderizado.**

### Almacenar valores mutables

```javascript
import React, { useRef } from "react";

function ContadorReliquias() {
  const refConteoReliquias = useRef(0);

  function recolectarReliquia() {
    refConteoReliquias.current += 1;
    console.log("Reliquias recolectadas:", refConteoReliquias.current);
  }

  return <button onClick={recolectarReliquia}>Recolectar Reliquia</button>;
}
```

Fíjate: al hacer clic no se actualiza la interfaz, pero el valor persiste internamente.

---

## 05. useRef - Acceso al DOM

Uno de los usos más potentes de `useRef` es acceder directamente a elementos del DOM. Esto es útil para enfocar campos, medir elementos o activar animaciones.

### Misión: Enfocar automáticamente el portal del gremio

```javascript
import React, { useRef, useEffect } from "react";

function PortalGremio() {
  const refPortal = useRef(null);

  useEffect(() => {
    refPortal.current.focus();
  }, []);

  return (
    <input
      ref={refPortal}
      type="text"
      placeholder="Introduce el nombre de tu aventurero..."
    />
  );
}

export default PortalGremio;
```

---

## 06. Estado vs Referencias - Conoce la diferencia

Entender cuándo usar `useState` frente a `useRef` es fundamental.

| Aspecto | `useState` | `useRef` |
| :-- | :-- | :-- |
| Provoca renderizado | Sí, al llamar al setter | No, modificar `.current` es silencioso |
| Propósito | Estado de la interfaz que debe mostrarse | Valores mutables, acceso al DOM, temporizadores |
| Persistencia | Persiste entre renderizados | Persiste entre renderizados |
| Uso | Contadores, valores de formulario, alternancias | IDs de temporizadores, valores anteriores, nodos DOM |

> [!TIP]
> **Versión para game dev**
> El Sistema de Reliquias refleja la magia de Emberfall. `useEffect` es el ritual que despierta las reliquias cuando cambian las condiciones (dependencias). La limpieza es el sello protector que evita la corrupción (fugas de memoria). `useRef` es la esencia de un artefacto: persiste incluso cuando el mundo se vuelve a renderizar a su alrededor.

---

## ⚡ XP Ganados: Ideas Clave

- 🪝 **Hooks:** Permiten a los componentes funcionales usar estado y ciclo de vida (React 16.8+)
- ⚡ **useEffect:** Gestiona efectos secundarios (obtención de datos, temporizadores, suscripciones, manipulación del DOM)
- 📋 **Array de dependencias:** Controla cuándo se ejecutan los efectos (`[]` una vez, sin array siempre, `[deps]` condicionalmente)
- 🧹 **Limpieza:** Devuelve una función de limpieza para evitar fugas de memoria
- 🔗 **useRef:** Conserva valores mutables en `.current` sin provocar nuevos renderizados
- 🎯 **Acceso al DOM:** `useRef` da acceso directo a elementos del DOM mediante la prop `ref`
- ⚖️ **Estado vs Ref:** Usa estado para datos visibles en la interfaz, referencias para datos internos o mutables no visibles

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🌐 Obtener datos de APIs (Archivos del Gremio, catálogo de reliquias)
- ⏱️ Temporizadores, cuentas atrás y relojes de la arena
- 🎯 Enfocar campos automáticamente y gestionar el foco del teclado
- 🎨 Animaciones y mediciones del DOM
- 🔌 Conexiones WebSocket con limpieza adecuada
- 💾 Almacenar valores anteriores sin provocar nuevos renderizados

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. **Misión básica:** Crea un componente que registre "¡Reliquia despertada!" en la consola solo una vez al montarse.
2. **Misión intermedia:** Construye una cuenta atrás de la arena que empiece en 10 y cuente hasta 0, limpiándose correctamente al desmontarse.
3. **Misión avanzada:** Crea un botón que incremente un contador en el estado y también registre clics totales en una referencia (sin efectos secundarios en el renderizado).
4. **Misión compleja:** Construye un campo de entrada que se enfoque automáticamente al montarse y cuente cuántas veces se ha escrito (usando una referencia para el contador).
5. **Pelea de jefe:** Forja un componente "Escáner de Reliquias" que obtenga datos ficticios tras 2 segundos (usando setTimeout en useEffect), muestre un estado de carga y limpie el temporizador si se desmonta antes de tiempo.

---

## 🔗 Ver También

- [[10 - La Fragua]] — Formularios que se benefician de la validación con useEffect
- [[12 - El Libro del Gremio]] — API de Contexto para estado global
- [[09 - El Mando]] — Eventos e interacciones del usuario
- [[08 - La Barra de Vida]] — Fundamentos de la gestión del estado

---
