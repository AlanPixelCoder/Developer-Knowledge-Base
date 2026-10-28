# 01. Insert Coin

**Spanish version:** [01 - Inserta la Moneda.md](01%20-%20Inserta%20la%20Moneda.md)

**Course:** JavaScript
**Chapter:** 1 — Cabinet Boot
**Topic:** Console output, line order, comments
**Tags:** `#javascript` `#console` `#comments` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-1-7C5CFF?style=for-the-badge" alt="Chapter 1">
  <img src="https://img.shields.io/badge/Lore-Cabinet%20Guild-FF6B35?style=for-the-badge" alt="Cabinet Guild">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

The Cabinet Guild keeps a row of beat-up browser arcade cabinets in its backroom. Each cabinet boots from a cold start: no menu, just a coin slot and a tiny service log. To wake one up, you talk to its log through the browser console, one instruction at a time.

## Talking to the Service Log

A cabinet does not guess. When you feed it an instruction, the engine runs it in strict order from top to bottom. `console.log()` is how you write to that service log without changing the cabinet art.

```js
console.log("CABINET-7: BOOT SEQUENCE START");
console.log("CABINET-7: COIN SLOT IDLE");
console.log("CABINET-7: AWAITING INSERT");
```

## Output

```text
CABINET-7: BOOT SEQUENCE START
CABINET-7: COIN SLOT IDLE
CABINET-7: AWAITING INSERT
```

The order is the point. Swap two lines and the log tells a different story. The engine never reorders them for convenience; it reads each statement exactly as written.

> [!IMPORTANT]
> Execution is sequential. If line 1 defines the state you read on line 2, line 2 must come after line 1. A flipped order is a logic bug even if every individual line is syntactically correct.

## Leaving Notes in the Script

Service techs scribble notes so they do not forget why a line exists. JavaScript has comments for that purpose: the engine ignores them.

```js
// Preheat the attract loop before players arrive
console.log("CABINET-7: ATTRACT LOOP ENABLED");

/*
   Do NOT re-enable the legacy payout counter.
   The guild disabled it after cabinet 3 jammed.
*/
console.log("CABINET-7: PAYOUT COUNTER: OFFLINE");
```

## Output

```text
CABINET-7: ATTRACT LOOP ENABLED
CABINET-7: PAYOUT COUNTER: OFFLINE
```

> [!TIP]
> A comment that says *what* the next line does is often redundant. A comment that says *why* a strange line exists will save you an hour next week.

## Why the Console First

The browser console is a live interpreter: you can test a single instruction without writing a full HTML page. For a cabinet log, that is perfect — one line fixes a guess. More importantly, errors appear in the same place: unclosed quotes or missing parentheses tend to fail at parse time, so the log points to the exact line to inspect.

> [!WARNING]
> Quotes must match. `"AWAITING` with no closing quote is a syntax error: the parser keeps scanning until it finds one or gives up. Parentheses follow the same rule.

**Next:** [[02 - Player Stats]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Yellow footer" />
</p>
