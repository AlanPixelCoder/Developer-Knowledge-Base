# 02. Punto de Aparición

**Versión original en inglés:** [02 - Spawn Point](./02%20-%20Spawn%20Point.md)

**Course:** React
**Capítulo:** I. El Renacer de la Interfaz
**Tema:** Encender la fragua para la Consola del Arsenal
**Etiquetas:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Lessons-01_--_07-7C5CFF?style=for-the-badge" alt="Lessons 01 to 07">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

With the plan laid out, the Armory's forge must be brought online. The console cannot be sketched on a blank page in the browser alone — it needs a workspace that compiles JSX, serves files quickly, and refreshes as changes are made. This chapter traces that setup from verifying the tools, to scaffolding with Vite, to finding the single anchor point where React takes control of the page.

> [!NOTE]
> The key is not memorizing every file, but understanding the path: a container in HTML, a root created by `createRoot`, and a component tree rendered into it.

## Checking the anvil

Before striking metal, the bench must be ready. Node.js runs JavaScript outside the browser, and npm pulls the packages the forge needs. Both come together in the LTS build.

```bash
node -v
npm -v
```

If versions report back (Node 18+ is a safe baseline), the anvil is stable. If the shell says *command not found*, the install needs to happen first before going any further.

> [!TIP]
> The version numbers matter less than that both commands respond. Focus on having them available in the terminal you'll use to run the dev server.

## Striking up the forge with Vite

Vite acts like a bellows for the workshop: it starts a local server almost instantly and hot-reloads changes without a full page refresh. Scaffolding a fresh React project only takes a few prompts.

```bash
npm create vite@latest armory-console
cd armory-console
npm install
npm run dev
```

When prompted, choose **React** as the framework and **JavaScript** as the variant. After `npm run dev`, the console will be available at `http://localhost:5173/`. Editing a file and saving will update the view almost immediately — that feedback loop is what keeps the rebuild moving quickly.

## Tracing the skeleton

A freshly scaffolded Vite project has a tight layout. Each piece has a job, and only a couple need attention at first.

| File | Purpose |
| :--- | :--- |
| `index.html` | The only HTML page loaded. It holds the mount point `<div id="root"></div>`. |
| `src/main.jsx` | The entry script: finds the root, calls `createRoot`, and renders `<App />`. |
| `src/App.jsx` | The top component of the console tree — the first place to sketch panels. |
| `package.json` | Lists dependencies (`react`, `react-dom`) and scripts like `dev`, `build`. |

> [!WARNING]
> The dev server must run from inside the project folder. If `npm run dev` is started from the wrong directory, it won't see `package.json` and will fail to start.

## The single anchor

Everything begins at one empty div. React doesn't take over the whole page — it takes over a designated container. The entry script makes that explicit.

```javascript
import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";

const root = createRoot(document.getElementById("root"));
root.render(<App />);
```

The flow is deliberate: grab the anchor by id, create a root for it, render the component tree. From that moment on, updates flow through React. If that div is missing or the id is mistyped, `createRoot` has nowhere to mount — the app won't start.

## Output

```text
Dev server running at http://localhost:5173/
Mount point ready: <div id="root"></div>
First render: <App /> anchored to root
```

## Why the anchor matters

Reconciliation works because React knows the boundary of its territory. By limiting control to a single container, the Armory Console can live alongside other scripts if needed, but more importantly the library can track what it owns. The dependency split also plays a role: `react` holds the component model and hooks, while `react-dom` knows how to write to the browser's DOM via `createRoot`. Keeping that separation is what allows React's ideas to reach different platforms. With the forge lit and the anchor set, the next task is learning the glyphs that will fill the console: JSX.

**Siguiente:** [[03 - Taller de Glifos]]
