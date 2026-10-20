# 15. The Final Boss

**Spanish version:** [15 - El Jefe Final.md](15%20-%20El%20Jefe%20Final.md)

**Course:** React
**Topic:** Capstone architecture, component hierarchy, routing, state management, data fetching, quiz logic, conditional rendering in routes, context providers and styling
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

The module finale. You started with `console.log()` in a browser tab; now you hold the full kit —
JSX, components, props, state, events, forms, hooks, context, fetching and routing. The **final boss**
is where it all fights together: the **"Which Emberfall class are you?"** quiz — a landing page, a name
form, a run of questions, and a result card whose portrait is fetched live from the guild archive.
Quick reference for every tool: [[00c - React Cheatsheet II]].

> [!NOTE]
> **The whole chapter in one sentence**
> One SPA, five components, one context provider, one router, one `useEffect` fetch and three layers of CSS — the architecture every mid-sized React project is built from.

---

## 01. The Final Boss

> [!NOTE]
> **Key information**
> Capstones are not about new APIs — they are about **architecture**: what is a component, where state lives, what is global, and which chapter's tool solves which problem.

Before writing a line, walk the four pillars of the build:

| Pillar | What it covers | Forged in |
| :--- | :--- | :--- |
| **Component Hierarchy** | Header, Home, Question, UserForm, Results | [[05 - Building Blocks]], [[06 - The Skill Tree]] |
| **Routing** | React Router between the landing page and the quiz | [[14 - The World Map]] |
| **State Management** | `useState` for selections/scores/result, `useContext` for the player's name | [[08 - The Health Bar]], [[12 - The Guild Ledger]] |
| **External Data Fetching** | `useEffect` + `fetch()` for the result portrait from the guild archive | [[11 - The Relic System]], [[13 - The Courier]] |

Read the table as a battle plan: every row is a chapter you already cleared, and the boss fight is
executing all four **at once, in one codebase**.

---

## 02. The Camp: File Layout

> [!NOTE]
> **Key information**
> Vite compiles `.jsx` by default. The **extension** signals JSX markup to the compiler and to the
> developer skimming the file list. The older `.js` works too; the convention is `.jsx` for anything
> that returns markup.

The quiz lives in a `components/` folder, one concern per file:

```text
src/
├── components/
│   ├── Header.jsx      ← title + <Link> navigation
│   ├── Home.jsx        ← landing page, the "take the quiz" call
│   ├── UserForm.jsx    ← pre-quiz name, writes to context
│   ├── Question.jsx    ← current question, options as buttons
│   └── Results.jsx     ← final class + fetched portrait
├── UserContext.jsx     ← global player name (Provider + hook)
├── App.jsx             ← quiz state, routing, provider wiring
└── index.jsx           ← createRoot + <BrowserRouter>
```

Each file owns exactly one job. `Question.jsx` never knows who the player is; `Results.jsx` never knows
how the quiz was scored — that isolation is the payoff of [[06 - The Skill Tree]].

---

## 03. The Quiz Engine

All quiz state lives in `App` so the router below can see it. Two `useState` calls hold the journey —
the **current question** and the **answers so far** — and two more hold the outcome: the class and its portrait.

```js
import React, { useState, useEffect } from "react";
import Question from "./components/Question.jsx";
import Results from "./components/Results.jsx";

const questions = [
  {
    text: "A torch gutters in the Deep Halls. You...",
    options: ["Push onward alone", "Fall back and regroup"],
  },
  {
    text: "A rival guild mocks your emblem. You...",
    options: ["Answer with steel", "Answer with satire"],
  },
];

function determineElement(answers) {
  // Score the route: mostly first options = Pyromancer, otherwise Warden
  const flames = answers.filter(function(a) { return a === 0; }).length;
  return flames > answers.length / 2 ? "Pyromancer" : "Warden";
}

function App() {
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState([]);
  const [element, setElement] = useState(null);
  const [artwork, setArtwork] = useState("");

  function handleAnswer(optionIndex) {
    // Save the answer, then advance — one click, two state updates
    setAnswers([...answers, optionIndex]);
    setCurrentQuestionIndex(currentQuestionIndex + 1);
  }

  useEffect(function() {
    // The last question was just answered: grade it and fetch the portrait
    if (currentQuestionIndex === questions.length && answers.length > 0) {
      const result = determineElement(answers);
      setElement(result);
      fetchArtwork(result);
    }
  }, [currentQuestionIndex]);
```

The `useEffect` comparison is the finish line detector: while `currentQuestionIndex < questions.length`
the quiz keeps asking; the moment the index **equals** the list length, `determineElement(answers)`
grades the run, `setElement` stores the class, and `fetchArtwork(...)` calls the guild archive.

```js
  async function fetchArtwork(query) {
    try {
      const response = await fetch(
        "https://collectionapi.metmuseum.org/public/collection/v1/search?q=" + query
      );
      const data = await response.json();
      const objectUrl =
        "https://collectionapi.metmuseum.org/public/collection/v1/objects/" +
        data.objectIDs[0];
      const objectResponse = await fetch(objectUrl);
      const artworkData = await objectResponse.json();
      setArtwork(artworkData.primaryImageSmall);
    } catch (err) {
      console.log("Guild archive unreachable: " + err.message);
    }
  }
```

The portrait pipeline is chapter [[13 - The Courier]] end to end — search endpoint, then object
endpoint, then the image URL parked in state — with the MET Museum API standing in as the guild archive.

### The Question Component

`Question.jsx` receives everything through props and turns the options into buttons with
`.map()`:

```js
function Question({ question, options, onAnswer }) {
  return (
    <div>
      <h2>{question.text}</h2>
      {options.map(function(option, index) {
        return (
          <button key={option} onClick={function() { onAnswer(index); }}>
            {option}
          </button>
        );
      })}
    </div>
  );
}
```

### Quest: Third Path

Add a third option to each question and a `"Trickster"` branch to `determineElement`.
Confirm the finish line still fires exactly once — no double `fetchArtwork` calls in the
Network tab.

---

## 04. Two Paths, One Door

The quiz route is not one component — it is a **conditional**, decided at render time:
questions while the run lasts, results when it ends.

```js
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/form" element={<UserForm />} />
  <Route path="/quiz" element={
    currentQuestionIndex < questions.length
      ? <Question
          question={questions[currentQuestionIndex]}
          options={questions[currentQuestionIndex].options}
          onAnswer={handleAnswer}
        />
      : <Results element={element} artwork={artwork} />
  } />
</Routes>
```

The ternary inside `element` is the same conditional rendering from [[04 - Living Markup]], promoted
to routing level: **one URL, two components**, swapped by state. The player never navigates between
questions — the URL stays `/quiz` while the content advances underneath it.

> [!WARNING]
> **The mistake everyone makes once**
> Forgetting that the branch re-renders on **every** state change. Put a
> `console.log("quiz route render")` inside the ternary's branch and watch it fire per answer — then
> move the heavy work (the fetch) into the `useEffect` guard, where it runs once per completion.

---

## 05. The Guild Scribe

The player's name is entered on one screen (`UserForm`) and read on another (`Results`). That is global
state — the job from [[12 - The Guild Ledger]]: `createContext()`, a Provider, `useContext`.

```js
import { createContext, useContext, useState } from "react";

export const UserContext = createContext();

export function UserProvider({ children }) {
  const [name, setName] = useState("");
  return (
    <UserContext.Provider value={{ name, setName }}>
      {children}
    </UserContext.Provider>
  );
}

export function useUser() {
  return useContext(UserContext);
}
```

Wire it around the routes, so every page can reach the name:

```js
import { UserProvider } from "./UserContext.jsx";

function App() {
  // ...quiz state from section 03...
  return (
    <UserProvider>
      <Header />
      <Routes>
        {/* the routes from section 04 live inside the provider */}
      </Routes>
    </UserProvider>
  );
}
```

Then each consumer does its one job: **`UserForm` sets** (`setName` from the input's `onChange`), **`Results` reads**:

```js
import { useContext } from "react";
import { UserContext } from "../UserContext.jsx";

function Results({ element, artwork }) {
  const { name } = useContext(UserContext);
  return (
    <div>
      <h1>{name}, you are the {element}!</h1>
      <div className="artwork">
        <img src={artwork} alt={"Portrait of the " + element} />
      </div>
    </div>
  );
}
```

One source of truth, zero prop drilling through the router.

---

## 06. Three Layers of Paint

The capstone styles itself in three layers, and knowing which layer a rule belongs to is half of CSS-in-React hygiene.

### Layer 1 — Global: `index.css`

```css
html {
  font-family: Arial;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #f0f0f0;
  min-height: 100vh;
}
```

`min-height: 100vh` makes the page **fill the viewport** even when the quiz has three lines of content.
`flex-direction: column` stacks children top to bottom — the default `row` would line them up sideways.

### Layer 2 — Component rules

```css
form {
  max-width: 400px;
  margin: 2rem auto;
}
form label {
  display: block;
}
form input {
  width: 400px;
  padding: 10px;
  border-radius: 5px;
}
nav a:hover {
  text-decoration: underline;
}
button:hover {
  background-color: #c4c4c4;
}
```

Plain CSS, one stylesheet, no libraries — `nav a:hover` and `button:hover` give every link and button on the site the same hover behavior without touching a single component.

### Layer 3 — Dynamic API content

```css
.artwork {
  text-align: center;
}
.artwork img {
  max-width: 30%;
  border-radius: 10px;
}
```

The portrait comes from an API you do not control — it may be 3000px wide. `max-width: 30%` is the
seatbelt: giant artwork **scales down** to the layout instead of shattering it.

---

## 07. The Victory Screen

### Checkpoint: The Whole Module in One List

- **[[01 - The Rebirth]] → [[04 - Living Markup]]**: React is declarative and component-based; JSX transpiles to `React.createElement`; markup embeds `{expressions}` and renders conditionally.
- **[[05 - Building Blocks]] → [[07 - Trade Routes]]**: components are PascalCase functions; props flow parent → child; `.map()` turns data into lists.
- **[[08 - The Health Bar]] → [[10 - The Forge]]**: `useState` drives re-renders; events are synthetic and camelCase; forms are controlled from state.
- **[[11 - The Relic System]] → [[12 - The Guild Ledger]]**: hooks bring effects, refs and cleanup; context kills prop drilling.
- **[[13 - The Courier]] → [[14 - The World Map]]**: `fetch` inside `useEffect` with loading and error states; the router swaps pages without reloads.

### Project Requirements: "Which Emberfall class are you?"

| Requirement | Built with |
| :--- | :--- |
| Header with `<Link>` navigation | Section 04 + [[14 - The World Map]] |
| Pre-quiz name screen | `UserForm` + context (section 05) |
| Question sequence with option buttons | `Question` + `.map()` (section 03) |
| Score → final class | `determineElement(answers)` (section 03) |
| Result portrait from an external API | `fetchArtwork` + `useEffect` (section 03) |
| One URL for the whole quiz run | Conditional `element` (section 04) |
| Consistent, non-breaking layout | Three CSS layers (section 06) |

> [!TIP]
> **Game dev version**
> This capstone is a vertical slice: the same architecture scales to a patch-notes reader, a guild
> roster, a storefront — swap `questions` for products and the quiz engine is a catalog. Every
> genre-defining SPA is this skeleton with a different dataset on the forge. The boss is dead; go build the expansion.

---

## ⚡ XP Earned: Key Takeaways

- 🏗️ Capstones are won on **architecture**: hierarchy, routing, state and fetching, decided before code.
- 🧩 One file, one job — `Question` never reads the name, `Results` never reads the score.
- 🔀 A ternary inside `element` gives one URL two components, swapped by state alone.
- 🗄️ Global data (the player's name) belongs in a context Provider — entered once, read anywhere.
- 🖼️ Artwork from an untrusted API needs `max-width` — never let remote pixels pick your layout size.
- 🏁 The finish-line `useEffect` compares `currentQuestionIndex` to `questions.length` and grades exactly once.

---

## 🎁 Loot Table: Real-World Use Cases

- 🧪 Personality quizzes and recommendation flows ("which plan fits you?")
- 📋 Multi-step forms: wizards, onboarding, job applications — same index-and-answers state
- 🏆 Result screens that fetch an external asset: certificates, report cards, generated art
- 🗂️ Any SPA where one URL hosts a stateful sequence instead of a single view
- 🎓 The template for a portfolio project: routing + context + fetch + forms, all in one

---

## 🎮 Side Quests: Practice Exercises

1. Persist `answers` in `localStorage` so a page refresh resumes the quiz at the same question.
2. Add a progress bar driven by `currentQuestionIndex / questions.length` inside `Header`.
3. Give the quiz a `/results` route and `navigate()` there when the run finishes — compare it with the conditional-`element` approach from section 04.
4. Extend `UserForm` with a controlled class-favorite dropdown (chapter [[10 - The Forge]]) stored in the same context.
5. **Boss fight:** turn the capstone into a patch-note reader — fetch the GitHub releases feed with the `useEffect` pattern from section 03, list entries with `.map()`, route them at `/news`, and keep the header, context and three CSS layers untouched.

---

## 🔗 See Also

- [[00c - React Cheatsheet II]] — every API this capstone uses, on one page
- [[14 - The World Map]] — the routing pack the quiz navigates with
- [[13 - The Courier]] — the fetch/loading/error pattern behind `fetchArtwork`
- [[12 - The Guild Ledger]] — the context pattern behind `UserProvider`
- [[01 - The Rebirth]] — where the whole journey started

---
