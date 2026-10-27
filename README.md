<div align="center">

# 🧠 Developer Knowledge Base

![Architecture](https://img.shields.io/badge/Architecture-Modular-blue?style=for-the-badge&logo=structure)
![Obsidian](https://img.shields.io/badge/Obsidian-Vault-7F6DF2?style=for-the-badge&logo=obsidian&logoColor=white)
![Environment](https://img.shields.io/badge/Environment-macOS_M4-000000?style=for-the-badge&logo=apple&logoColor=white)
![Version Control](https://img.shields.io/badge/Git-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

<p>A structured, multi-language technical repository for computer science foundations, software architecture patterns, and engineering workflows — with every exercise framed around building video games.</p>

</div>

**Español:** [README-ES.md](README-ES.md)

<img src="https://capsule-render.vercel.app/api?type=waving&color=7C5CFF&height=60&section=header" width="100%" alt="Slow Neon Wave" />

> **Note**
> This knowledge base acts as a central repository for documentation, reference architectures, and code notes authored in **Obsidian** and rendered directly on **GitHub**.

## 🗺️ Knowledge Domains & MOCs

Every domain is self-contained and opens with a **MOC** (Map of Content): an index note that lists each topic with a one-line description, so you enter through the map instead of scrolling a folder.

| Domain | Description | Notes | Status | Map of Content |
| :--- | :--- | :--- | :--- | :--- |
| 🐍 **Python** | Core syntax, control flow, data structures, OOP & ecosystems | 11 EN · 11 ES | 🟢 Active | [EN](%F0%9F%90%8D%20Python/README.md) · [ES](%F0%9F%90%8D%20Python/README-ES.md) |
| 🚀 **Git & GitHub** | Version control, branching strategies, collaboration & PR workflows | 4 EN · 4 ES | 🟢 Active | [EN](%F0%9F%9A%80%20Git%20&%20GitHub/README.md) · [ES](%F0%9F%9A%80%20Git%20&%20GitHub/README-ES.md) |
| 🟣 **CSharp** | Strongly typed, OOP, .NET ecosystem & Unity engine architecture | 8 EN · 8 ES | 🟢 Active | [EN](%F0%9F%9F%A3%20CSharp/README.md) · [ES](%F0%9F%9F%A3%20CSharp/README-ES.md) |
| 🧮 **Data Structures & Algorithms** | Core data structures, algorithm efficiency & problem solving | 5 EN · 5 ES | 🟢 Active | [EN](%F0%9F%A7%AE%20Data%20Structures%20&%20Algorithms/README.md) · [ES](%F0%9F%A7%AE%20Data%20Structures%20&%20Algorithms/README-ES.md) |
| 🖥️ **Command Line** | Terminal navigation, file management, permissions & shell workflow | 13 EN · 13 ES | 🟢 Active | [EN](%F0%9F%96%A5%EF%B8%8F%20Command%20Line/README.md) · [ES](%F0%9F%96%A5%EF%B8%8F%20Command%20Line/README-ES.md) |
| 🤖 **GenAI** | How LLMs work, prompt engineering, embeddings & AI failure modes | 6 EN · 6 ES | 🟢 Active | [EN](%F0%9F%A4%96%20GenAI/README.md) · [ES](%F0%9F%A4%96%20GenAI/README-ES.md) |
| 🌐 **HTML** | Web page structure, elements, attributes, styles, forms & semantic regions | 6 EN · 6 ES | 🟢 Active | [EN](%F0%9F%8C%90%20HTML/README.md) · [ES](%F0%9F%8C%90%20HTML/README-ES.md) |
| 🎨 **CSS** | Styling, selectors, colors, the box model, positioning & flexbox layouts | 14 EN · 14 ES | 🟢 Active | [EN](%F0%9F%8E%A8%20CSS/README.md) · [ES](%F0%9F%8E%A8%20CSS/README-ES.md) |
| 🟨 **JavaScript** | Variables, control flow, arrays, functions, objects, the DOM & events | 10 EN · 10 ES | 🟢 Active | [EN](%F0%9F%9F%A8%20JavaScript/README.md) · [ES](%F0%9F%9F%A8%20JavaScript/README-ES.md) |
| ⚛️ **React** | Components, JSX, props & state, hooks, context, fetching & routing | 17 EN · 17 ES | 🟢 Active | [EN](%E2%9A%9B%EF%B8%8F%20React/README.md) · [ES](%E2%9A%9B%EF%B8%8F%20React/README-ES.md) |
| ⚙️ **C++** | Systems programming, manual memory, classes, pointers & references | 53 EN · 53 ES | 🟢 Active | [EN](%E2%9A%99%EF%B8%8F%20C%2B%2B/README.md) · [ES](%E2%9A%99%EF%B8%8F%20C%2B%2B/README-ES.md) |
| 🏗️ **Software Engineering** | Design patterns, algorithms & system architecture | — | 🟡 Planned | *Coming soon* |
| 🎮 **Game Architecture** | Interactive mechanics, engine patterns & physics | — | 🟡 Planned | *Coming soon* |

**Topic numbering.** Notes are prefixed so a domain reads in learning order — `01`, `02`,
`03`… Cheatsheets use a `00b` / `00c` prefix and sit *before* the numbered sequence,
because they are meant to be consulted while working rather than read front to back.

**The modules that build on others.** 🤖 **GenAI** is the AI layer of this vault: it
starts from the Python of 🐍 **Python** and builds a next-token predictor, a prompt library
and a semantic search engine in pure Python, so the AI tooling is understood from the
inside rather than borrowed from an API. ⚛️ **React** is its web counterpart: it starts
from the 🟨 **JavaScript**, 🌐 **HTML** and 🎨 **CSS** modules and turns their static
pages into a living single-page application. ⚙️ **C++** is the low-level counterpart of
that stack: the same logic, the same loops and objects, but with the memory and the types
in your hands — the step between writing a game and understanding the machine it runs on.

**How to read a note.** Each one is a self-contained lesson: a concept, a runnable
example, its printed output, and the traps worth knowing. Code blocks are executable as
written — the comments state the output you should actually get.

**The Spanish mirror.** Every topic exists in both languages. English is the reference
version; the Spanish note carries a `**Versión original en inglés:**` line at the top
linking back to it. Inside Spanish code blocks, variables and string literals are
localized, while language keywords, API names and class names stay in English.

## 🌍 Languages

| Version | Entry point | Status |
| :--- | :--- | :--- |
| 🇬🇧 English (original) | [README.md](README.md) | 🟢 Reference base |
| 🇪🇸 Spanish (translation) | [README-ES.md](README-ES.md) | 🟢 In sync |

Every note exists in both languages. The Spanish note includes a
`**Versión original en inglés:**` line at the top linking back to its English original.
English is the reference version; the Spanish one is kept as a mirror of it.

## 🛠️ Repository Architecture

Notes are stored as **filename pairs** on the same line: the English note first, its
Spanish translation after the `·` separator.

```text
Developer-Knowledge-Base/
├── README.md                              <-- English homepage (reference)
├── README-ES.md                           <-- Spanish homepage (mirror)
├── LICENSE
├── .gitignore
│
├── tools/                                 <-- vault verifiers (see below)
├── .github/workflows/                      <-- runs them on every push
│
├── 🐍 Python/                             <-- 11 topics · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 00b - Python Cheatsheet.md         ·  00b - Chuleta de Python.md
│   ├── 00c - Python Cheatsheet II.md      ·  00c - Chuleta de Python II.md
│   ├── 01 - Setup & Data Types.md         ·  01 - Configuración y Tipos de Datos.md
│   ├── 02 - Control Flow.md               ·  02 - Control de Flujo.md
│   ├── 03 - Loops.md                      ·  03 - Bucles.md
│   ├── 04 - Terminal Dungeon Crawl.md     ·  04 - Mazmorra por Terminal.md
│   ├── 05 - Lists.md                      ·  05 - Listas.md
│   ├── 06 - Built-in Functions & List Methods.md  ·  06 - Funciones Integradas y Métodos de Lista.md
│   ├── 07 - Functions.md                  ·  07 - Funciones.md
│   ├── 08 - Object-Oriented Programming.md  ·  08 - Programación Orientada a Objetos.md
│   ├── 09 - Modules.md                    ·  09 - Módulos.md
│   └── z_attachments/                     <-- local assets (empty, untracked)
│
├── 🚀 Git & GitHub/                       <-- 4 topics · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 01 - Introduction & Setup.md        ·  01 - Introducción y Configuración.md
│   ├── 02 - Core Workflow.md               ·  02 - Flujo de Trabajo Principal.md
│   ├── 03 - Collaboration & Branching.md   ·  03 - Colaboración y Ramas.md
│   └── 04 - Advanced Workflow & PRs.md     ·  04 - Flujo Avanzado y PRs.md
│
├── 🟣 CSharp/                             <-- 8 topics · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 00b - CSharp Cheatsheet.md         ·  00b - Chuleta de CSharp.md
│   ├── 01 - Press Start.md                ·  01 - Pulsa Start.md
│   ├── 02 - Typecast.md                   ·  02 - Conversión de Tipos.md
│   ├── 03 - Control Flow.md               ·  03 - Control de Flujo.md
│   ├── 04 - Loops.md                      ·  04 - Bucles.md
│   ├── 05 - Arrays.md                     ·  05 - Arreglos.md
│   ├── 06 - Methods.md                    ·  06 - Métodos.md
│   └── Mad Dungeon Master - Checkpoint Project.md  ·  Mad Dungeon Master - Proyecto de Hito.md
│
├── 🧮 Data Structures & Algorithms/       <-- 5 topics · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 01 - Introduction to DSA.md        ·  01 - Introducción a Estructuras de Datos y Algoritmos.md
│   ├── 02 - Algorithms & Efficiency.md    ·  02 - Algoritmos y Eficiencia.md
│   ├── 03 - Lists & Linear Search.md      ·  03 - Listas y Búsqueda Lineal.md
│   ├── 04 - Binary Search.md              ·  04 - Búsqueda Binaria.md
│   └── 05 - Selection Sort.md             ·  05 - Ordenamiento por Selección.md
│
├── 🖥️ Command Line/                       <-- 13 topics · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 00b - Command Line Cheatsheet.md   ·  00b - Chuleta de Línea de Comandos.md
│   ├── 01 - The Shell.md                  ·  01 - La Terminal.md
│   ├── 02 - The Project Tree.md           ·  02 - El Árbol del Proyecto.md
│   ├── 03 - Dungeon Navigation.md         ·  03 - Navegando la Mazmorra.md
│   ├── 04 - Reading the Keep.md           ·  04 - Leyendo la Mazmorra.md
│   ├── 05 - Clearing the Fog.md           ·  05 - Despejando la Niebla.md
│   ├── 06 - Treasure Hunt.md              ·  06 - Caza del Tesoro.md
│   ├── 07 - Project Blueprints.md         ·  07 - Planos del Proyecto.md
│   ├── 08 - Forging Files.md              ·  08 - Forjando Archivos.md
│   ├── 09 - Writing the Lore.md           ·  09 - Escribiendo el Lore.md
│   ├── 10 - Managing Loot.md              ·  10 - Gestionando el Botín.md
│   ├── 11 - Cloning Relics.md             ·  11 - Clonando Reliquias.md
│   └── 12 - Dungeon Build.md              ·  12 - Construyendo la Mazmorra.md
│
├── 🌐 HTML/                           <-- 6 topics · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 00b - HTML Cheatsheet.md          ·  00b - Chuleta de HTML.md
│   ├── 00c - HTML Cheatsheet II.md       ·  00c - Chuleta de HTML II.md
│   ├── 01 - HTML Basics.md               ·  01 - Fundamentos de HTML.md
│   ├── 02 - Structure & Attributes.md    ·  02 - Estructura y Atributos.md
│   ├── 03 - Forms.md                     ·  03 - Formularios.md
│   └── 04 - Semantic HTML.md             ·  04 - HTML Semántico.md
│
├── 🎨 CSS/                                <-- 14 topics · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 00b - CSS Cheatsheet.md           ·  00b - Chuleta de CSS.md
│   ├── 00c - CSS Cheatsheet II.md        ·  00c - Chuleta de CSS II.md
│   ├── 01 - CSS Basics.md                ·  01 - Fundamentos de CSS.md
│   ├── 02 - Colors & Measurements.md     ·  02 - Colores y Medidas.md
│   ├── 03 - Selectors Pt. 1.md           ·  03 - Selectores Pt. 1.md
│   ├── 04 - Selectors Pt. 2.md           ·  04 - Selectores Pt. 2.md
│   ├── 05 - Pseudo-elements.md           ·  05 - Pseudoelementos.md
│   ├── 06 - Pseudo-classes.md            ·  06 - Pseudoclases.md
│   ├── 07 - Fonts & Text.md              ·  07 - Fuentes y Texto.md
│   ├── 08 - Backgrounds & Shorthands.md  ·  08 - Fondos y Shorthands.md
│   ├── 09 - Box Model & Borders.md       ·  09 - Modelo de Caja y Bordes.md
│   ├── 10 - Spacing & Box Sizing.md      ·  10 - Espaciado y Box Sizing.md
│   ├── 11 - Display & Positioning.md     ·  11 - Display y Posicionamiento.md
│   ├── 12 - Flexbox.md                   ·  12 - Flexbox ES.md
│
├── 🟨 JavaScript/                         <-- 10 topics · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 00b - JavaScript Cheatsheet.md    ·  00b - Chuleta de JavaScript.md
│   ├── 00c - JavaScript Cheatsheet II.md ·  00c - Chuleta de JavaScript II.md
│   ├── 01 - Insert Coin.md               ·  01 - Inserta la Moneda.md
│   ├── 02 - Player Stats.md              ·  02 - Atributos del Jugador.md
│   ├── 03 - Loot Rolls.md                ·  03 - Tiradas de Botín.md
│   ├── 04 - The Farm.md                  ·  04 - El Farmeo.md
│   ├── 05 - Inventory.md                 ·  05 - Inventario.md
│   ├── 06 - Skill Functions.md           ·  06 - Funciones de Habilidad.md
│   ├── 07 - Character Sheet.md           ·  07 - Ficha de Personaje.md
│   └── 08 - Living HUD.md                ·  08 - HUD Vivo.md
│
├── ⚛️ React/                              <-- 17 topics · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 00b - React Cheatsheet.md         ·  00b - Chuleta de React.md
│   ├── 00c - React Cheatsheet II.md      ·  00c - Chuleta de React II.md
│   ├── 01 - The Rebirth.md               ·  01 - El Renacimiento.md
│   ├── 02 - Spawn Point.md               ·  02 - Punto de Aparición.md
│   ├── 03 - Glyph Workshop.md            ·  03 - Taller de Glifos.md
│   ├── 04 - Living Markup.md             ·  04 - Marcado Vivo.md
│   ├── 05 - Building Blocks.md           ·  05 - Bloques de Construcción.md
│   ├── 06 - The Skill Tree.md            ·  06 - El Árbol de Habilidades.md
│   ├── 07 - Trade Routes.md              ·  07 - Rutas Comerciales.md
│   ├── 08 - The Health Bar.md            ·  08 - La Barra de Vida.md
│   ├── 09 - The Controller.md            ·  09 - El Mando.md
│   ├── 10 - The Forge.md                 ·  10 - La Fragua.md
│   ├── 11 - The Relic System.md          ·  11 - El Sistema de Reliquias.md
│   ├── 12 - The Guild Ledger.md          ·  12 - El Libro del Gremio.md
│   ├── 13 - The Courier.md               ·  13 - El Mensajero.md
│   ├── 14 - The World Map.md             ·  14 - El Mapa del Mundo.md
│   └── 15 - The Final Boss.md            ·  15 - El Jefe Final.md
│
├── ⚙️ C++/                                <-- 53 topics · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 00b - C++ Cheatsheet.md            ·  00b - Chuleta de C++.md
│   ├── 00c - C++ Cheatsheet II.md         ·  00c - Chuleta de C++ II.md
│   ├── 01 - The Program.md                ·  01 - El Programa.md
│   ├── 02 - Howdy!.md                     ·  02 - ¡Howdy!.md
│   ├── 03 - See Ya Later Alligator.md     ·  03 - Nos Vemos Más Tarde, Cocodrilo.md
│   ├── 04 - Ouija Board.md                ·  04 - Tabla Ouija.md
│   ├── 05 - Sign Bunny.md                 ·  05 - Conejito de Señalización.md
│   ├── Compile & Execute.md               ·  Compilar y Ejecutar.md
│   ├── 06 - Data Types.md                 ·  06 - Tipos de Datos.md
│   ├── 07 - Declaration of Independence.md  ·  07 - Declaración de Independencia.md
│   ├── 08 - IPO.md                        ·  08 - IPO (Entrada, Proceso, Salida).md
│   ├── 09 - Temperature.md                ·  09 - Temperatura.md
│   ├── 10 - Knighthood.md                 ·  10 - Caballería.md
│   ├── 11 - Month-over-Month (MoM).md     ·  11 - Mes a Mes (MoM).md
│   ├── 12 - Cat Years.md                  ·  12 - Años Gato.md
│   ├── 13 - Coin Flip.md                  ·  13 - Lanzamiento de Moneda.md
│   ├── 14 - Fever.md                      ·  14 - Fiebre.md
│   ├── 15 - Levels & Ranks.md             ·  15 - Niveles y Rangos.md
│   ├── 16 - Fortune Cookie.md             ·  16 - Galleta de la Fortuna.md
│   ├── 17 - Voting.md                     ·  17 - Votación.md
│   ├── 18 - Trivia Quiz.md                ·  18 - Trivial Quiz.md
│   ├── 19 - Enter PIN.md                  ·  19 - Introducir PIN.md
│   ├── 20 - Guess the Number.md           ·  20 - Adivina el Número.md
│   ├── 21 - Counting Sheep.md             ·  21 - Contando Ovejas.md
│   ├── 22 - 99 Bottles.md                 ·  22 - 99 Botellas.md
│   ├── 23 - Fizz Buzz.md                  ·  23 - Fizz Buzz (Reto).md
│   ├── 24 - Survival Gear.md              ·  24 - Equipo de Supervivencia.md
│   ├── 25 - Lemonade Stand.md             ·  25 - Puesto de Limonada.md
│   ├── 26 - Order Cart.md                 ·  26 - Carrito de Compras.md
│   ├── 27 - Roadtrip Playlist.md          ·  27 - Lista de Reproducción de Viaje.md
│   ├── 28 - Sum of Even - Product of Odd.md  ·  28 - Suma de Pares - Producto de Impares.md
│   ├── Arrays.md                          ·  Arrays en C++.md
│   ├── 29 - D.R.Y..md                     ·  29 - D.R.Y. (No te repitas).md
│   ├── 30 - Food Menu.md                  ·  30 - Menú de Comida.md
│   ├── 31 - OOO.md                        ·  31 - Fuera de Oficina.md
│   ├── 32 - Conversions.md                ·  32 - Conversiones.md
│   ├── 32 - Conversions (Continuation).md ·  32 - Conversiones (Continuación).md
│   ├── 33 - Tips Calculator.md            ·  33 - Calculadora de Propinas.md
│   ├── Scope in C++.md                    ·  Ámbito en C++.md
│   ├── 34 - Restaurants.md                ·  34 - Restaurantes.md
│   ├── 35 - Public vs. Private.md         ·  35 - Público vs Privado.md
│   ├── 36 - Bank Accounts.md              ·  36 - Cuentas Bancarias.md
│   ├── 37 - Bank Accounts (Continuation).md  ·  37 - Cuentas Bancarias (Continuación).md
│   ├── 38 - Classic Cars.md               ·  38 - Coches Clásicos.md
│   ├── 39 - Pet Rescue.md                 ·  39 - Rescate de Mascotas.md
│   ├── 39 - Pet Rescue (Continuation).md  ·  39 - Rescate de Mascotas (Continuación).md
│   ├── 40 - Memories.md                   ·  40 - Recuerdos.md
│   ├── 40 - Memories (Continuation).md    ·  40 - Recuerdos (Continuación).md
│   ├── 41 - A Few Pointers.md             ·  41 - Unos Punteros.md
│   ├── 42 - Dereference.md                ·  42 - Desreferenciación.md
│   ├── 43 - References vs. Pointers.md    ·  43 - Referencias vs Punteros.md
│   ├── 44 - Nullptr.md                    ·  44 - Puntero Nulo.md
│   └── 45 - The End.md                    ·  45 - El Fin.md
│
└── 🤖 GenAI/                              <-- 6 topics · EN + ES
    ├── README.md          ·  README-ES.md
    ├── 00b - GenAI Cheatsheet.md          ·  00b - Chuleta de GenAI.md
    ├── 00c - GenAI Cheatsheet II.md       ·  00c - Chuleta de GenAI II.md
    ├── 01 - How AI Thinks.md              ·  01 - Cómo Piensa la IA.md
    ├── 02 - Prompt Engineering.md         ·  02 - Ingeniería de Prompts.md
    ├── 03 - Embeddings & Semantic Search.md  ·  03 - Embeddings y Búsqueda Semántica.md
    ├── 04 - Limits & Risks.md             ·  04 - Límites y Riesgos.md
    └── z_attachments/                     <-- local assets (empty, untracked)
```

> The tree above shows the real structure of the repository. Every module ships both a
> `README.md` (English) and a `README-ES.md` (Spanish), and every note exists in both languages.

**Conventions worth knowing**

| Convention | Meaning |
| :--- | :--- |
| `README.md` / `README-ES.md` | The MOC of a domain. Start here. |
| `NN - Title.md` | A topic note. `NN` encodes the learning order. |
| `00b` / `00c` | Cheatsheets, consulted on demand. |
| `z_attachments/` | Local scratch folder for diagrams. Not versioned. |
| Pairing | Every `.md` has an English original; the Spanish translation sits next to it. |

**Not versioned on purpose** — listed in `.gitignore` so the vault stays portable:
`.obsidian/` (local vault state), `.DS_Store`, and the assistant tooling folders
`.copilot/`, `.opencode/`, `copilot/`.

## ✅ Automatic Verification

The vault drifts quietly: a note gets a new section, a code block stops matching
its documented output, the Spanish mirror falls a step behind. These four
verifiers catch that on every push, without anyone having to remember to look.

| Verifier | What it proves | Runs on |
| :--- | :--- | :--- |
| `.check_readme_index.py` | Every note is reachable from a README; no broken links; EN/ES totals match per module. | Linux |
| `tools/check_notes.py` | Fences close, tables keep their column count, wikilinks resolve, alerts use the five types GitHub renders. | Linux |
| `tools/check_parity.py` | Every note has a mirror in the other language, with the same commands in the same order. | Linux |
| `tools/check_transcripts.py` | Every documented bash block actually produces the output it claims, executed for real against a real file tree. | macOS |

```bash
python3 .check_readme_index.py     # index
python3 tools/check_notes.py       # structure
python3 tools/check_parity.py      # EN/ES mirror
python3 tools/check_transcripts.py # run the transcripts (macOS, zsh)
python3 tools/selftest.py          # prove the verifiers still catch faults
```

`tools/selftest.py` is the one worth knowing about. A verifier nobody has ever
seen fail proves nothing: it may be checking the wrong condition and still
report `OK` forever. The selftest breaks the notes on purpose in a throwaway
copy and fails if any verifier fails to notice.

**A red check does not block anything.** The workflow is not a required status
check, so a pull request merges regardless. That is deliberate: one person
writes this vault, and a gate that gets in the way of saving work eventually
gets switched off. To close that door later it is a single checkbox under
*Settings → Branches → Branch protection rules* — no change to the workflow,
since the verifiers already exit non-zero on failure.

Two jobs, because the costs differ: the three Linux verifiers take seconds and
cover the whole vault, while the transcript runner needs macOS (zsh and the BSD
tools) and only covers the modules whose transcripts have been audited. To add a
module to it, append its folder to `MODS` in `tools/check_transcripts.py` and
document the file tree its notes start from.

## ⚙️ Engineering Workflow

- **Vault Management:** Written and interlinked in [Obsidian](https://obsidian.md).
- **Layout & Rendering:** Designed and formatted using **Visual Studio Code / Trae** + **GitHub Copilot**.
- **Version Control:** Sourced, tracked, and hosted via **Git** & **GitHub**.
- **Translation:** the Spanish version is kept as a mirror of the English one. Variables, string literals and comments are translated; language keywords, API names and class names stay in English. Code blocks run with the same result as their originals.

```mermaid
gitGraph
   commit id: "Initial commit"
   commit id: "Vault Setup: Obsidian & Structure"
   branch feature/python
   checkout feature/python
   commit id: "Docs: Python Core & MOC"
   checkout main
   merge feature/python
   branch feature/csharp
   checkout feature/csharp
   commit id: "Docs: C# Architecture & Unity"
   checkout main
   merge feature/csharp
   commit id: "Release: Knowledge Base v1.0"
```
