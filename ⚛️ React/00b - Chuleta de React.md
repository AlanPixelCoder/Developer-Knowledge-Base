# 00b. Chuleta de React

**Versión original en inglés:** [00b - Chuleta de React.md](00b%20-%20Chuleta%20de%20React.md)

**Course:** React
**Topic:** Quick reference for the Armory Console toolkit
**Tags:** `#react` `#cheatsheet` `#reference` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER_TO_INTERMEDIATE-6CC24A?style=for-the-badge" alt="Principiante a intermedio">
  <img src="https://img.shields.io/badge/Covers-Chapters_01_--_09-7C5CFF?style=for-the-badge" alt="Chapters 01 to 09">
  <img src="https://img.shields.io/badge/Type-Cheatsheet-00C2A8?style=for-the-badge" alt="Cheatsheet">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

A compact field reference for rebuilding the Emberfall Armory Console: JSX, components, composition, props, state, and events.

> [!TIP]
> When in doubt, ask: is this data coming from above (props) or owned here (state)? That one question resolves most design choices.

## Core mindset

| Idea | Meaning |
| :--- | :--- |
| **Declarative** | Describe what the UI should look like for given data; React updates the DOM. |
| **Component-based** | Split the console into reusable functions that compose into a tree. |
| **One-way flow** | Data flows parent → child via props; state changes trigger re-renders. |

## Quick traps

| Trap | Fix |
| :--- | :--- |
| Using `class` in JSX | Use `className` |
| Missing key in lists | Add a stable unique `key` |
| Mutating state directly | Use the setter |
| Wrong component case | Use PascalCase for custom components |

---

**See also:** [[00c - React Cheatsheet II]] | [[01 - The Rebirth]]
