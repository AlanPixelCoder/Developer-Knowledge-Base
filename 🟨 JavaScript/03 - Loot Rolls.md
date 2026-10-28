# 03. Loot Rolls

**Spanish version:** [03 - Tiradas de Botín.md](03%20-%20Tiradas%20de%20Bot%C3%ADn.md)

**Course:** JavaScript
**Chapter:** 3 — The Breaker Gate
**Topic:** if/else, comparisons, logical operators, Math.random()
**Tags:** `#javascript` `#conditionals` `#logic` `#random` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-3-7C5CFF?style=for-the-badge" alt="Chapter 3">
  <img src="https://img.shields.io/badge/Lore-Cabinet%20Guild-FF6B35?style=for-the-badge" alt="Cabinet Guild">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

After boot, the cabinet does not run every line blindly. The Breaker Gate blocks access until a check passes: enough credits, ticket valid, or the daily override. Conditionals let the script branch, and `Math.random()` lets it roll.

## One Fork

An `if` tests a boolean expression. If it is `true`, its block runs. If not, nothing happens unless there is an `else`.

```js
let credits = 2;
if (credits >= 1) {
  console.log("GATE: ACCEPTED - CREDITS OK");
} else {
  console.log("GATE: LOCKED - INSERT COIN");
}
```

## Output

```text
GATE: ACCEPTED - CREDITS OK
```

> [!IMPORTANT]
> A condition must evaluate to `true` or `false`. Comparisons like `>=`, `===`, `!==` produce booleans; using `=` is assignment, not comparison — that is a very common mixup.

## More Than Two Choices

When more than two outcomes exist, `else if` forms a chain. Only the first branch whose condition is true runs; the rest are skipped.

```js
let ticketClass = "crew";
if (ticketClass === "guild") {
  console.log("GATE: PRIORITY ACCESS");
} else if (ticketClass === "crew") {
  console.log("GATE: CREW ACCESS");
} else if (ticketClass === "guest") {
  console.log("GATE: GUEST ACCESS");
} else {
  console.log("GATE: UNKNOWN TICKET");
}
```

## Output

```text
GATE: CREW ACCESS
```

> [!TIP]
> Put the most specific or most restrictive rule first only if you need short-circuiting by order, but for a simple classification like this order by priority if the cases could overlap. If cases are mutually exclusive, order is less fragile if conditions are precise.

## Logic Without Guesswork

Sometimes one check is not enough. `&&` means both must be true, `||` means at least one must be true, `!` inverts a boolean.

```js
let hasTicket = true;
let bypassKey = false;
if (hasTicket && !bypassKey) {
  console.log("CHECK: STANDARD ENTRY");
}
if (bypassKey || hasTicket) {
  console.log("CHECK: ENTRY ALLOWED");
}
```

## Output

```text
CHECK: STANDARD ENTRY
CHECK: ENTRY ALLOWED
```

> [!WARNING]
> `&&` has higher precedence than `||`. When mixing them, parentheses prevent reading mistakes: `(a && b) || c` is different in intent from `a && (b || c)`.

## Rolling the Breaker

To test the gate unpredictably, use `Math.random()`. It returns a number in `[0, 1)` (0 included, 1 excluded). Scale and floor it to get a range.

```js
let roll = Math.floor(Math.random() * 6) + 1; // 1..6
if (roll >= 5) {
  console.log("BREAKER: JOLT - RARE SURGE");
} else if (roll >= 3) {
  console.log("BREAKER: HUM - STABLE");
} else {
  console.log("BREAKER: FLICKER - MILD");
}
```

## Output

```text
BREAKER: FLICKER - MILD
```
(The exact line depends on the roll value; the branching is what matters.)

The key: `Math.random()` gives no upper bound by itself. Multiply by the count of outcomes, floor to integer indices, and add an offset if you need to start at 1. That is the same trick used for dice in any cabinet game.

**Next:** [[04 - The Farm]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Yellow footer" />
</p>
