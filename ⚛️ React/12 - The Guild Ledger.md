# 12. The Guild Ledger

**Spanish version:** [[12 - El Libro del Gremio.md](12%20-%20El%20Libro%20del%20Gremio.md)

**Course:** React
**Topic:** Forging the next piece of the Armory Console
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER_TO_INTERMEDIATE-6CC24A?style=for-the-badge" alt="Beginner to Intermediate">
  <img src="https://img.shields.io/badge/Lessons-01_--_06-7C5CFF?style=for-the-badge" alt="Lessons 01 to 06">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Cyan wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

The Armory Console rebuild continues. This chapter adds the next panel to the growing system, following the same discipline: describe the interface from data, keep boundaries clear, and compose small pieces into something reliable.

> [!NOTE]
> Each addition must reinforce one-way data flow. If a value belongs to this component and changes, it belongs in state. If it comes from above, it belongs in props.

## Building the piece

The pattern stays consistent. Components remain small, focused, and reusable. Expressions, conditions, and the right hooks keep the behavior predictable without reaching into the DOM directly.

```javascript
function ConsolePanel() {
  return (
    <section className="console-panel">
      <h3>Armory Panel</h3>
      <p>Forged to fit the console's architecture.</p>
    </section>
  );
}
```

> [!TIP]
> Before adding logic, ask whether an existing pattern from earlier chapters already solves the problem. Reuse over reinvention.

## Why it fits the rebuild

Every panel in the console must cooperate with the others. Keeping state local where possible, passing data explicitly, and avoiding unnecessary side effects makes the whole tree easier to reason about and debug.

> [!WARNING]
> Don't duplicate data or break the flow. If multiple components need the same changing value, lift it up or use context only when props would become unworkable.

## Output

```text
ConsolePanel rendered
Boundaries respected: props down, events up
Pattern consistent with the Armory rebuild
```

**Next:** [[13 - The Courier]]
