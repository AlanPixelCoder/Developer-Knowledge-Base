# 15. The Final Boss

**Spanish version:** [15 - El Jefe Final.md](15%20-%20El%20Jefe%20Final.md)

**Course:** React
**Topic:** Assembling the full Armory Console
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-ADVANCED-F0AD4E?style=for-the-badge" alt="Advanced">
  <img src="https://img.shields.io/badge/Lessons-01_--_07-7C5CFF?style=for-the-badge" alt="Lessons 01 to 07">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Cyan wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

Every tool forged along the way comes together now. The **Armory Operations Console** must show the duty roster, track repair orders, consult the relic catalog, and allow filing new orders — all from one application. No single chapter taught this assembly; it requires deciding where state lives, what gets shared through context, which routes exist, and how data is fetched. This is less about learning new APIs and more about architecture.

> [!NOTE]
> A capstone is an exercise in composition: reuse the patterns you've already practiced and connect them deliberately to solve a coherent problem.

## Blueprint of the console

| Area | Pattern used | Purpose |
| :--- | :--- | :--- |
| Navigation | `BrowserRouter`, `Routes`, `Link` | Move between views without reloads |
| Session info | Context API (`GuildProvider`) | Share active warden and alerts across views |
| Duty roster | Props + `.map()` | Display team data as a list |
| Repair orders | `useState`, controlled forms, `useNavigate` | File and view orders interactively |
| Relic catalog | `useEffect`, `fetch()`, loading/error states | Pull live data from the vault API |
| Reusable UI | Component composition | Keep panels small and testable |

## Why this matters

The console comes together by composition, not by bloating a single file. Each pattern does its job: props flow down, state stays local where possible, context shares truly global values, effects reach outside, and routing organizes views. The result is coherent and maintainable.

> [!TIP]
> Ask for each piece of data: "Does this need to be shared across many views?" If yes, context. If only to direct children, props. If only this component needs it and it changes, state.

## Output

```text
[App] Mounted with GuildProvider + BrowserRouter
[Nav] Routes: /, /triage, /orders, /relics
[Triage] Rendered 3 duty cards from props
[Orders] Form controlled -> navigate to list on submit
[Relics] Fetching... -> 4 relics loaded
```

## Victory and what's next

The Armory Operations Console is complete — not because it's huge, but because it's coherent. Every chapter's lesson has a place in it. The skills learned here transfer directly to real projects: breaking UIs into components, managing state and events, handling forms and effects, sharing data, fetching APIs, and routing between views.

**End of module:** [[00b - React Cheatsheet]]
