<div align="center">

# 🐍 Python: Verdant Relay (MOC)

[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Obsidian](https://img.shields.io/badge/Obsidian-483699?logo=obsidian&logoColor=white)](https://obsidian.md/)
[![macOS](https://img.shields.io/badge/macOS-000000?logo=apple&logoColor=white)](https://www.apple.com/macos/)

_A telemetry field guide for maintaining a network of remote sensor beacons along a storm-battered coastal reserve._

</div>

**Español:** [README-ES.md](./README-ES.md)

---

**Note:**
This page is the central map for the Python notes in this Obsidian vault. The running example follows **Verdant Relay**, a field-operations studio maintaining remote sensor beacons — parsing logs, summarising readings, and automating reports.

**Tip:**
Start with Beacon Boot Sequence and work through the tide cycles toward the Storm Window capstone.

---

## 🗺️ Map of Content

### 📑 Reference & Cheatsheets

* **Cheatsheets:**
  * [00b - Verdant Relay Field Card](./00b%20-%20Verdant%20Relay%20Field%20Card.md) — Syntax, control flow, loops, data structures, functions, classes, and imports.

### 🧠 1. Telemetry Foundations

* **Beacon Boot Sequence:** [01 - Beacon Boot Sequence](./01%20-%20Beacon%20Boot%20Sequence.md) — Output, variables, data types, and arithmetic for boot-time readings.
* **Threshold Gates:** [02 - Threshold Gates](./02%20-%20Threshold%20Gates.md) — Errors, conditionals, relational and logical operators for alarm logic.
* **Tide Cycles:** [03 - Tide Cycles](./03%20-%20Tide%20Cycles.md) — `while`/`for` loops, `range()`, iteration control and retries.

### 📦 2. Data & State

* **Relay Drift:** [04 - Relay Drift](./04%20-%20Relay%20Drift.md) — Lists, indexing, slicing, built-ins, methods, and batch iteration.
* **Storm Stack:** [05 - Storm Stack](./05%20-%20Storm%20Stack.md) — Nested lists/matrices, dictionaries, and sets for stacked telemetry.

### ⚙️ 3. Automation & Integration

* **Relay Routines:** [06 - Relay Routines](./06%20-%20Relay%20Routines.md) — Functions, parameters, return values, scope, and lambdas.
* **Beacon Class:** [07 - Beacon Class](./07%20-%20Beacon%20Class.md) — Classes, objects, `__init__()`, and instance methods.
* **Relay Modules:** [08 - Relay Modules](./08%20-%20Relay%20Modules.md) — Imports, standard library, and custom modules.
* **Storm Window:** [09 - Storm Window](./09%20-%20Storm%20Window.md) — Capstone telemetry console bringing the pieces together.

```mermaid
flowchart LR
    A[Telemetry Foundations] --> B[Data & State]
    B --> C[Automation & Integration]
    C --> D[Storm Window Capstone]
```
