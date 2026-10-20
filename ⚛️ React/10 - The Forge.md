# 10. The Forge

**Spanish version:** [10 - La Fragua.md](10%20-%20La%20Fragua.md)

**Course:** React
**Topic:** forms, htmlFor, onChange, e.target.value, onSubmit, preventDefault, complex state objects, controlled components, select, textarea, form checklist
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-01_--_07-7C5CFF?style=for-the-badge" alt="Lessons">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Cyan wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

The embers of The Forge glow hot enough to melt Relic steel. Every day, adventurers come to commission gear, sign up for guild contracts, leave reviews for the Blacksmith, and submit quest reports. All of these require collecting user input. In React, forms are the crucible where state and events meet. By mastering controlled components, you'll learn to forge airtight forms that capture every keystroke, validate data, and submit cleanly without losing a single ember of state.

> [!NOTE]
> **The whole chapter in one sentence**
> React forms use controlled components where state owns the data — bind `value` to state, update with `onChange`, and handle submission with `onSubmit` + `preventDefault()` to keep full control over every field.

---

## 01. Labels and htmlFor

In HTML, the `for` attribute connects a label to an input. In JavaScript, `for` is a reserved keyword for loops, so React uses `htmlFor`.

### Mission: Guild Registration Label

```javascript
function GuildRegistration() {
  return (
    <form>
      <label htmlFor="guildName">Guild Name:</label>
      <input type="text" id="guildName" />
    </form>
  );
}

export default GuildRegistration;
```

---

## 02. Capturing Input with onChange

The `onChange` event fires on every keystroke, allowing you to capture and track input in real time.

### Mission: Live Guild Name Preview

```javascript
import React, { useState } from "react";

function GuildNameInput() {
  const [name, setName] = useState("");

  function handleChange(e) {
    setName(e.target.value);
  }

  return (
    <div>
      <input type="text" id="name" onChange={handleChange} value={name} />
      <p>Your guild will be known as: {name}</p>
    </div>
  );
}

export default GuildNameInput;
```

---

## 03. Handling Form Submission

By default, submitting a form reloads the page. Use `e.preventDefault()` to stop this behavior and handle submission with React state.

### Mission: Submit a Contract

```javascript
import React, { useState } from "react";

function QuestContract() {
  const [contractName, setContractName] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    if (contractName.length > 3) {
      console.log("Contract submitted to the Guild Ledger:", contractName);
      setContractName("");
    } else {
      alert("Contract name must be longer than 3 characters.");
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="contract">Quest Contract:</label>
      <input
        type="text"
        id="contract"
        value={contractName}
        onChange={(e) => setContractName(e.target.value)}
      />
      <button type="submit">Forge Contract</button>
    </form>
  );
}

export default QuestContract;
```

---

## 04. Complex State Objects

When dealing with multiple fields, it's cleaner to use a single state object with computed property names.

### Mission: Adventurer Login

```javascript
import React, { useState } from "react";

function AdventurerLogin() {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    age: 0
  });

  function handleFormData(e) {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  }

  function handleSubmit(e) {
    e.preventDefault();
    console.log("Adventurer credentials:", formData);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="email">Guild Email:</label>
      <input
        type="email"
        id="email"
        name="email"
        value={formData.email}
        onChange={handleFormData}
      />

      <label htmlFor="password">Password:</label>
      <input
        type="password"
        id="password"
        name="password"
        value={formData.password}
        onChange={handleFormData}
      />

      <label htmlFor="age">Age:</label>
      <input
        type="number"
        id="age"
        name="age"
        value={formData.age}
        onChange={handleFormData}
      />

      <button type="submit">Enter the Guild</button>
    </form>
  );
}

export default AdventurerLogin;
```

> [!WARNING]
> **Critical Rule**
> Always use the spread operator `...formData` when updating a state object. If you omit it, you'll overwrite all other fields.

---

## 05. Select Dropdowns

For dropdowns, bind the `value` to the `<select>` element (not the individual `<option>` elements). No `selected` attribute is needed.

### Mission: Choose Your Quest

```javascript
import React, { useState } from "react";

function QuestSelector() {
  const [adventure, setAdventure] = useState("");

  function handleChange(e) {
    setAdventure(e.target.value);
  }

  function handleSubmit(e) {
    e.preventDefault();
    alert("You have selected: " + adventure);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="adventure">Select a Quest:</label>
      <select id="adventure" value={adventure} onChange={handleChange}>
        <option value="">-- Choose your fate --</option>
        <option value="Deep Halls">Deep Halls Expedition</option>
        <option value="Cinderpeak">Cinderpeak Volcano</option>
        <option value="Frostspire">Frostspire Ruins</option>
        <option value="Shadowfen">Shadowfen Hunt</option>
      </select>
      <button type="submit">Embark</button>
    </form>
  );
}

export default QuestSelector;
```

---

## 06. Textarea

`<textarea>` is also a controlled component in React. Use `value` and `onChange`, just like inputs.

### Mission: Quest Report

```javascript
import React, { useState } from "react";

function QuestReport() {
  const [report, setReport] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    console.log("Quest Report filed:", report);
    setReport("");
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="report">Field Report:</label>
      <textarea
        id="report"
        name="report"
        value={report}
        onChange={(e) => setReport(e.target.value)}
        placeholder="Describe the horrors you witnessed..."
        rows="5"
        cols="40"
      />
      <button type="submit">File Report</button>
    </form>
  );
}

export default QuestReport;
```

---

## 07. Form Checklist

Follow these steps to forge a bulletproof controlled form:

1. **State Initialization** - Create state for each field (or a single object)
2. **Controlled Elements** - Bind `value` to state on every input, select, and textarea
3. **Change Handlers** - Use `onChange` to update state on every keystroke/selection
4. **Submit Handler** - Use `onSubmit` on the form to handle submission
5. **Prevent Default** - Call `e.preventDefault()` to avoid page reload

> [!TIP]
> **Game dev version**
> Every guild registration page, loot submission form, or quest board in Emberfall follows this exact pattern. The Forge doesn't just shape steel — it shapes the data that drives the entire companion site.

---

## ⚡ XP Earned: Key Takeaways

- 📝 **htmlFor:** Use `htmlFor` instead of `for` to link labels and inputs
- 🔄 **onChange:** Fires on every change, perfect for real-time capture
- 🎯 **Controlled components:** React state owns all form data via `value`
- 🚫 **preventDefault:** Stop the browser's default form submission behavior
- 🗃️ **Complex state:** Use a single object + computed properties `[e.target.name]` for multiple fields
- 📋 **select & textarea:** Both work as controlled components with `value` and `onChange`
- ✅ **Validation:** Check data before submission and reset state after success

---

## 🎁 Loot Table: Real-World Use Cases

- 🛡️ Guild registration and authentication forms
- 📜 Quest contracts and adventure sign-ups
- 💬 Player reviews and feedback forms
- 🛒 Store checkout forms on the Emberfall marketplace
- 📝 Bug reports and support tickets

---

## 🎮 Side Quests: Practice Exercises

1. **Misión básica:** Create a simple name input that displays "Welcome, [name], to Emberfall!" in real time.
2. **Misión intermedia:** Build a login form with email and password, validating that both fields are filled before submission.
3. **Misión avanzada:** Create a multi-field form using a single state object with computed property names.
4. **Misión compleja:** Build a quest application form with inputs, a select dropdown for class, and a textarea for backstory.
5. **Pelea de jefe:** Forge a complete guild charter submission form with validation, preventing submission if required fields are empty, and logging all data to the console on success.

---

## 🔗 See Also

- [[09 - The Controller]] — Events that power form interactions
- [[11 - The Relic System]] — Hooks and side effects for form validation
- [[12 - The Guild Ledger]] — Share form data globally with Context

---
