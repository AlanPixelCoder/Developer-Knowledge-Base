<div align="center">

# 🧠 Base de Conocimiento para Desarrolladores

![Architecture](https://img.shields.io/badge/Architecture-Modular-blue?style=for-the-badge&logo=structure)
![Obsidian](https://img.shields.io/badge/Obsidian-Vault-7F6DF2?style=for-the-badge&logo=obsidian&logoColor=white)
![Environment](https://img.shields.io/badge/Environment-macOS_M4-000000?style=for-the-badge&logo=apple&logoColor=white)
![Version Control](https://img.shields.io/badge/Git-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

<p>Un repositorio técnico estructurado y multilenguaje sobre fundamentos de ciencias de la computación, patrones de arquitectura de software y flujos de trabajo de ingeniería — con cada ejercicio planteado alrededor de la creación de videojuegos.</p>

</div>

**English:** [README.md](README.md)

<img src="https://capsule-render.vercel.app/api?type=waving&color=7C5CFF&height=60&section=header" width="100%" alt="Slow Neon Wave" />

> **Nota**
> Esta base de conocimiento funciona como un repositorio central de documentación, arquitecturas de referencia y notas de código escritas en **Obsidian** y renderizadas directamente en **GitHub**. Las notas en español son traducciones de las originales en inglés y se mantienen como un espejo: el inglés es la versión de referencia.

## 🗺️ Dominios de Conocimiento y MOCs

Cada dominio es autónomo y abre con un **MOC** (Mapa de Contenidos): una nota índice que
enumera cada tema con una descripción de una línea, para entrar por el mapa en lugar de
recorrer una carpeta.

| Dominio | Descripción | Notas | Estado | Mapa de Contenidos |
| :--- | :--- | :--- | :--- | :--- |
| 🐍 **Python** | Sintaxis básica, control de flujo, estructuras de datos, POO y ecosistemas | 11 EN · 11 ES | 🟢 Activo | [EN](%F0%9F%90%8D%20Python/README.md) · [ES](%F0%9F%90%8D%20Python/README-ES.md) |
| 🚀 **Git & GitHub** | Control de versiones, estrategias de ramificación, colaboración y flujos de PR | 4 EN · 4 ES | 🟢 Activo | [EN](%F0%9F%9A%80%20Git%20&%20GitHub/README.md) · [ES](%F0%9F%9A%80%20Git%20&%20GitHub/README-ES.md) |
| 🟣 **CSharp** | Tipado fuerte, POO, ecosistema .NET y arquitectura del motor Unity | 8 EN · 8 ES | 🟢 Activo | [EN](%F0%9F%9F%A3%20CSharp/README.md) · [ES](%F0%9F%9F%A3%20CSharp/README-ES.md) |
| 🧮 **Estructuras de Datos y Algoritmos** | Estructuras de datos fundamentales, eficiencia de algoritmos y resolución de problemas | 5 EN · 5 ES | 🟢 Activo | [EN](%F0%9F%A7%AE%20Data%20Structures%20&%20Algorithms/README.md) · [ES](%F0%9F%A7%AE%20Data%20Structures%20&%20Algorithms/README-ES.md) |
| 🖥️ **Línea de Comandos** | Navegación en la terminal, gestión de archivos, permisos y flujo de trabajo en la shell | 13 EN · 13 ES | 🟢 Activo | [EN](%F0%9F%96%A5%EF%B8%8F%20Command%20Line/README.md) · [ES](%F0%9F%96%A5%EF%B8%8F%20Command%20Line/README-ES.md) |
| 🤖 **GenAI** | Cómo funcionan los LLM, ingeniería de prompts, embeddings y modos de fallo de la IA | 6 EN · 6 ES | 🟢 Activo | [EN](%F0%9F%A4%96%20GenAI/README.md) · [ES](%F0%9F%A4%96%20GenAI/README-ES.md) |
| 🌐 **HTML** | Estructura de páginas web, elementos, atributos, estilos y formularios | 6 EN · 6 ES | 🟢 Activo | [EN](%F0%9F%8C%90%20HTML/README.md) · [ES](%F0%9F%8C%90%20HTML/README-ES.md) |
| 🎨 **CSS** | Estilos, selectores, colores, el modelo de caja, posicionamiento y maquetación flexbox | 14 EN · 14 ES | 🟢 Activo | [EN](%F0%9F%8E%A8%20CSS/README.md) · [ES](%F0%9F%8E%A8%20CSS/README-ES.md) |
| 🟨 **JavaScript** | Variables, control de flujo, arreglos, funciones, objetos, el DOM y eventos | 10 EN · 10 ES | 🟢 Activo | [EN](%F0%9F%9F%A8%20JavaScript/README.md) · [ES](%F0%9F%9F%A8%20JavaScript/README-ES.md) |
| ⚛️ **React** | Componentes, JSX, props y estado, hooks, contexto, obtención de datos y enrutamiento | 17 EN · 17 ES | 🟢 Activo | [EN](%E2%9A%9B%EF%B8%8F%20React/README.md) · [ES](%E2%9A%9B%EF%B8%8F%20React/README-ES.md) |
| ⚙️ **C++** | Programación de sistemas, memoria manual, clases, punteros y referencias | 53 EN · 53 ES | 🟢 Activo | [EN](%E2%9A%99%EF%B8%8F%20C%2B%2B/README.md) · [ES](%E2%9A%99%EF%B8%8F%20C%2B%2B/README-ES.md) |
| 🏗️ **Ingeniería de Software** | Patrones de diseño, algoritmos y arquitectura de sistemas | — | 🟡 Planificado | *Próximamente* |
| 🎮 **Arquitectura de Juegos** | Mecánicas interactivas, patrones de motor y física | — | 🟡 Planificado | *Próximamente* |

**Numeración de los temas.** Las notas llevan un prefijo para que el dominio se lea en orden
de aprendizaje — `01`, `02`, `03`… Las chuletas usan el prefijo `00b` / `00c` y se sitúan
*antes* de la secuencia numerada, porque están pensadas para consultarse mientras se trabaja
y no para leerse de principio a fin.

**Los módulos que se apoyan en otros.** 🤖 **GenAI** es la capa de IA de esta vault: parte
del Python de 🐍 **Python** y construye un predictor del siguiente token, una biblioteca de
prompts y un motor de búsqueda semántica en Python puro, de modo que las herramientas de IA
se entiendan por dentro en lugar de pedirlas prestadas a una API. ⚛️ **React** es su
equivalente web: parte de los módulos de 🟨 **JavaScript**, 🌐 **HTML** y 🎨 **CSS** y
convierte sus páginas estáticas en una aplicación de página única viva. ⚙️ **C++** es la
contraparte de bajo nivel de esa pila: la misma lógica, los mismos bucles y objetos, pero con
la memoria y los tipos en tus manos — el paso entre escribir un juego y entender la máquina
sobre la que corre.

**Cómo leer una nota.** Cada una es una lección autónoma: un concepto, un ejemplo ejecutable,
su salida por consola y las trampas que conviene conocer. Los bloques de código se ejecutan
tal cual — los comentarios indican la salida que deberías obtener realmente.

**El espejo en español.** Todos los temas existen en ambos idiomas. El inglés es la versión de
referencia; la nota en español incluye una línea `**Versión original en inglés:**` al principio
que enlaza a su original. Dentro de los bloques en español, las variables y las cadenas están
traducidas, mientras que las palabras clave del lenguaje, los nombres de API y los nombres de
clase permanecen en inglés.

## 🌍 Idiomas

| Versión | Ruta de entrada | Estado |
| :--- | :--- | :--- |
| 🇬🇧 Inglés (original) | [README.md](README.md) | 🟢 Base de referencia |
| 🇪🇸 Español (traducción) | [README-ES.md](README-ES.md) | 🟢 Sincronizado |

Cada nota existe en ambos idiomas. Las notas en español incluyen una línea
`**Versión original en inglés:**` en la parte superior que enlaza a su nota original. El inglés
es la versión de referencia y el español se mantiene como su espejo.

## 🛠️ Arquitectura del Repositorio

Las notas se guardan como **pares de nombres de archivo** en la misma línea: primero la nota
en inglés y, tras el separador `·`, su traducción al español.

```text
Developer-Knowledge-Base/
├── README.md                              <-- Portada en inglés (referencia)
├── README-ES.md                           <-- Portada en español (espejo)
├── LICENSE
├── .gitignore
│
├── tools/                                 <-- verificadores de la vault (ver abajo)
├── .github/workflows/                      <-- los ejecuta en cada push
│
├── 🐍 Python/                             <-- 11 temas · EN + ES
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
│   └── z_attachments/                     <-- recursos locales (vacía, sin versionar)
│
├── 🚀 Git & GitHub/                       <-- 4 temas · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 01 - Introduction & Setup.md        ·  01 - Introducción y Configuración.md
│   ├── 02 - Core Workflow.md               ·  02 - Flujo de Trabajo Principal.md
│   ├── 03 - Collaboration & Branching.md   ·  03 - Colaboración y Ramas.md
│   └── 04 - Advanced Workflow & PRs.md     ·  04 - Flujo Avanzado y PRs.md
│
├── 🟣 CSharp/                             <-- 8 temas · EN + ES
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
├── 🧮 Data Structures & Algorithms/       <-- 5 temas · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 01 - Introduction to DSA.md        ·  01 - Introducción a Estructuras de Datos y Algoritmos.md
│   ├── 02 - Algorithms & Efficiency.md    ·  02 - Algoritmos y Eficiencia.md
│   ├── 03 - Lists & Linear Search.md      ·  03 - Listas y Búsqueda Lineal.md
│   ├── 04 - Binary Search.md              ·  04 - Búsqueda Binaria.md
│   └── 05 - Selection Sort.md             ·  05 - Ordenamiento por Selección.md
│
├── 🖥️ Command Line/                       <-- 13 temas · EN + ES
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
├── 🌐 HTML/                           <-- 6 temas · EN + ES
│   ├── README.md          ·  README-ES.md
│   ├── 00b - HTML Cheatsheet.md          ·  00b - Chuleta de HTML.md
│   ├── 00c - HTML Cheatsheet II.md       ·  00c - Chuleta de HTML II.md
│   ├── 01 - HTML Basics.md               ·  01 - Fundamentos de HTML.md
│   ├── 02 - Structure & Attributes.md    ·  02 - Estructura y Atributos.md
│   ├── 03 - Forms.md                     ·  03 - Formularios.md
│   └── 04 - Semantic HTML.md             ·  04 - HTML Semántico.md
│
├── 🎨 CSS/                                <-- 14 temas · EN + ES
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
├── 🟨 JavaScript/                         <-- 10 temas · EN + ES
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
├── ⚛️ React/                              <-- 17 temas · EN + ES
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
├── ⚙️ C++/                                <-- 53 temas · EN + ES
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
└── 🤖 GenAI/                              <-- 6 temas · EN + ES
    ├── README.md          ·  README-ES.md
    ├── 00b - GenAI Cheatsheet.md          ·  00b - Chuleta de GenAI.md
    ├── 00c - GenAI Cheatsheet II.md       ·  00c - Chuleta de GenAI II.md
    ├── 01 - How AI Thinks.md              ·  01 - Cómo Piensa la IA.md
    ├── 02 - Prompt Engineering.md         ·  02 - Ingeniería de Prompts.md
    ├── 03 - Embeddings & Semantic Search.md  ·  03 - Embeddings y Búsqueda Semántica.md
    ├── 04 - Limits & Risks.md             ·  04 - Límites y Riesgos.md
    └── z_attachments/                     <-- recursos locales (vacía, sin versionar)
```

> El árbol anterior muestra la estructura real del repositorio. Cada módulo incluye su
> `README.md` (inglés) y su `README-ES.md` (español), y cada nota existe en ambos idiomas.

**Convenciones que conviene conocer**

| Convención | Significado |
| :--- | :--- |
| `README.md` / `README-ES.md` | El MOC de un dominio. Empieza por aquí. |
| `NN - Title.md` | Una nota de tema. `NN` indica el orden de aprendizaje. |
| `00b` / `00c` | Chuletas, para consultar bajo demanda. |
| `z_attachments/` | Carpeta local para diagramas. Sin versionar. |
| Emparejamiento | Cada `.md` tiene un original en inglés; la traducción va junto a él. |

**No se versiona a propósito** — figura en `.gitignore` para que la vault siga siendo portable:
`.obsidian/` (estado local de la vault), `.DS_Store` y las carpetas de herramientas del
asistente `.copilot/`, `.opencode/`, `copilot/`.

## ✅ Verificación Automática

La vault se descoloca en silencio: una nota gana una sección, un bloque de código deja de
coincidir con la salida que documenta, el espejo español se queda un paso atrás. Estos
cuatro verificadores lo detectan en cada push, sin que nadie tenga que acordarse de mirar.

| Verificador | Qué demuestra | Corre en |
| :--- | :--- | :--- |
| `.check_readme_index.py` | Que toda nota se alcanza desde algún README; que no hay enlaces rotos; que los totales EN/ES cuadran por módulo. | Linux |
| `tools/check_notes.py` | Que los ``` cierra, que las tablas conservan sus columnas, que los wikilinks resuelven y que las alertas usan los cinco tipos que GitHub dibuja. | Linux |
| `tools/check_parity.py` | Que cada nota tiene su espejo en el otro idioma, con los mismos comandos en el mismo orden. | Linux |
| `tools/check_transcripts.py` | Que cada bloque bash documentado produce de verdad la salida que dice, ejecutándolo contra un árbol de archivos real. | macOS |

```bash
python3 .check_readme_index.py     # índice
python3 tools/check_notes.py       # estructura
python3 tools/check_parity.py      # espejo EN/ES
python3 tools/check_transcripts.py # ejecutar las transcripciones (macOS, zsh)
python3 tools/selftest.py          # comprobar que los verificadores siguen detectando fallos
```

`tools/selftest.py` es el que conviene conocer. Un verificador al que nunca se le ha visto
fallar no demuestra nada: puede estar comprobando la condición equivocada y aun así
informar `OK` para siempre. La autoprueba rompe las notas a propósito en una copia
descartable y falla si algún verificador no se entera.

**Un check en rojo no bloquea nada.** El workflow no es un required status check, así que
un pull request se mergea igual. Es deliberado: escribe esta vault una sola persona, y una
puerta que se interpone a la hora de guardar el trabajo acaba desactivándose. Para cerrarla
más adelante basta una casilla en *Settings → Branches → Branch protection rules*, sin tocar
el workflow: los verificadores ya salen con código distinto de cero cuando algo falla.

Son dos jobs porque los costes son distintos: los tres verificadores de Linux tardan segundos
y cubren toda la vault, mientras que el de transcripciones necesita macOS (zsh y las
herramientas de BSD) y solo cubre los módulos cuyas transcripciones están auditadas. Para
sumar un módulo, añade su carpeta a `MODS` en `tools/check_transcripts.py` y documenta el
árbol de archivos del que parten sus notas.

## ⚙️ Flujo de Trabajo de Ingeniería

- **Gestión de la vault:** escrita y enlazada en [Obsidian](https://obsidian.md).
- **Maquetación y renderizado:** diseñada y formateada con **Visual Studio Code / Trae** + **GitHub Copilot**.
- **Control de versiones:** creado, rastreado y alojado con **Git** y **GitHub**.
- **Traducción:** la versión en español se mantiene como espejo de la inglesa. Las variables, las cadenas y los comentarios se traducen; las palabras clave, los nombres de API y los nombres de clase permanecen en inglés. Los bloques de código se ejecutan con el mismo resultado que sus originales.

```mermaid
gitGraph
   commit id: "Commit inicial"
   commit id: "Vault: Obsidian y estructura"
   branch feature/python
   checkout feature/python
   commit id: "Docs: núcleo de Python y MOC"
   checkout main
   merge feature/python
   branch feature/csharp
   checkout feature/csharp
   commit id: "Docs: arquitectura de C# y Unity"
   checkout main
   merge feature/csharp
   commit id: "Lanzamiento: base v1.0"
```
