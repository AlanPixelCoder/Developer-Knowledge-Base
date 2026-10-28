# 01. Wayfarer Cache

**Spanish version:** [01 - Alijo del Caminante](./01%20-%20Alijo%20del%20Caminante.md)

**Course:** Git & GitHub
**Topic:** Wayfarer expedition log — version control, setup, repo initialization
**Tags:** `#git` `#github` `#setup` `#wayfarer`

<p align="left">
  <img src="https://img.shields.io/badge/TOOL-GIT-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git Badge">
  <img src="https://img.shields.io/badge/PLATFORM-GITHUB-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge">
  <img src="https://img.shields.io/badge/Lore-Wayfarer-8D7358?style=for-the-badge" alt="Wayfarer">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7A3EE8?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=8D7358&height=70&section=header" width="100%" alt="Wayfarer wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #8D7358, #C9B7A3, #8D7358, transparent); margin: 24px 0;" />

Two wayfarers, Finch and Mora, set out to chart Greyharbor Pass. At first they scrawled notes on loose parchment in different packs. A lost map here, a revised route there — nothing matched. To avoid retracing the same mistake twice, they need a single cache of expedition notes that keeps history: every change recorded, every revision traceable. That cache is a Git repository.

> [!NOTE]
> **History is the point**
> Git is a distributed version control system. It does not back up your files by copying the folder over and over; it records snapshots of the project at points in time. GitHub hosts a shared copy so two wayfarers can sync without mailing parchment.

## Why a cache, not a stack of copies

Before Git, Finch kept `route_v1.txt`, `route_v2_final.txt`, `route_v2_final_REAL.txt`. No one could tell which one was current or why it changed. With Git, the "why" goes in a commit message, and the history shows exactly what changed between snapshots. That history is the expedition log.

## Preparing the pack

First, confirm Git is installed on the trail terminal.

```bash
git --version
```

The output should look something like this:

```text
git version 2.39.3
```

> [!WARNING]
> If the command is not found, Git must be installed before anything else. The exact version matters less than having a working `git` command in the shell.

## Stashing notes into a cache

The wayfarers start with a new folder for the pass charts: `wayfarer-pass`. To turn it into a cache (repository), they initialize Git in that folder.

```bash
pwd
git init
```

Expected output (plausible):

```text
/Users/wayfarer/wayfarer-pass
Initialized empty Git repository in /Users/wayfarer/wayfarer-pass/.git/
```

Running `git init` creates a hidden `.git` directory. That directory holds the entire history of the cache — without it, there is no Git repository.

## Linking to the shared campfire

To sync with the shared camp (GitHub), the cache needs a remote. They create an empty repository on GitHub called `wayfarer-pass` and link it as `origin`.

```bash
git remote add origin https://github.com/finch-mora/wayfarer-pass.git
git branch -M main
```

The second command renames the default branch to `main` — the trail name used going forward. To confirm the link is set up:

```bash
git branch
```

Expected output:

```text
* main
```

> [!TIP]
> `origin` is just a name for the remote URL. The wayfarers could call it something else, but `origin` is the convention every trail uses. Keep it unless there's a strong reason not to.

## Output

After initialization and linking, the local cache knows its history location (`.git`) and knows where to push and pull from (`origin`). The branch is `main`. Nothing has been committed yet — the cache is empty, waiting for the first trail marker.

## Task 1: Lay the First Cache

Create a folder `wayfarer-pass`, run `git init` inside it, add a remote pointing to `https://github.com/finch-mora/wayfarer-pass.git`, rename the branch to `main`, and verify with `git branch`. Write down the exact commands in order and the plausible outputs you would expect to see at each step.

**Why this order:** history must exist locally before anything can be snapped into a commit. Linking the remote before the first push just means the address is known when it's time to share the cache.

**Next:** [[02 - Trail Markers]]
