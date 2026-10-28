# 00c. Chuleta de React II

**Versión original en inglés:** [00c - Chuleta de React II.md](00c%20-%20Chuleta%20de%20React%20II.md)

**Course:** React
**Topic:** Forms, hooks, context, fetching, routing
**Tags:** `#react` `#cheatsheet` `#reference` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE_TO_ADVANCED-F0AD4E?style=for-the-badge" alt="Intermedio avanzado">
  <img src="https://img.shields.io/badge/Covers-Chapters_10_--_15-7C5CFF?style=for-the-badge" alt="Chapters 10 to 15">
  <img src="https://img.shields.io/badge/Type-Cheatsheet-00C2A8?style=for-the-badge" alt="Cheatsheet">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

Field reference for the second half of the Armory rebuild: controlled forms, `useEffect`, `useRef`, Context API, data fetching, and client-side routing.

> [!TIP]
> Keep side effects out of render. If it touches the outside world, it belongs in `useEffect`.

## Controlled forms

```javascript
import { useState } from "react";

function OrderForm() {
  const [name, setName] = useState("");
  function handleSubmit(e) {
    e.preventDefault();
    console.log(name);
  }
  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <button>Submit</button>
    </form>
  );
}
```

## useEffect

```javascript
import { useEffect, useState } from "react";

function VaultTimer() {
  const [sec, setSec] = useState(0);
  useEffect(() => {
    const id = setInterval(() => setSec(s => s + 1), 1000);
    return () => clearInterval(id);
  }, []);
  return <p>{sec}s</p>;
}
```

## Context API

```javascript
import { createContext, useContext, useState } from "react";

const GuildCtx = createContext();

export function GuildProvider({ children }) {
  const [warden, setWarden] = useState({ name: "Aelun" });
  return <GuildCtx.Provider value={{ warden, setWarden }}>{children}</GuildCtx.Provider>;
}

export function useGuild() {
  return useContext(GuildCtx);
}
```

## Data fetching

```javascript
import { useEffect, useState } from "react";

function Relics() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("/api/relics")
      .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(setData)
      .catch(e => setError(e.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;
  return <ul>{data.map(d => <li key={d.id}>{d.name}</li>)}</ul>;
}
```

## Routing

```javascript
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <nav><Link to="/">Home</Link></nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/orders" element={<Orders />} />
      </Routes>
    </BrowserRouter>
  );
}
```

---

**See also:** [[00b - React Cheatsheet]] | [[15 - The Final Boss]]
