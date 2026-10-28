# 03. Forks in the Trail

**Spanish version:** [03 - Bifurcaciones del Camino](./03%20-%20Bifurcaciones%20del%20Camino.md)

**Course:** Git & GitHub
**Topic:** Wayfarer collaboration — clone, fork, branches, switch, pull
**Tags:** `#git` `#branching` `#collaboration` `#wayfarer`

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

The trail splits. Finch wants to scout a possible shortcut through the shale cliffs; Mora needs to keep charting the main pass. Neither wants to erase the other's work. On the trail they would split the party for a time — in Git, they create branches. To work together from afar, they clone, fork, and pull updates to keep their caches in sync.

> [!NOTE]
> **Branches are side trails**
> A branch is a parallel line of history. Changes on `shortcut-scout` don't affect `main` until they are deliberately merged. You can explore, mark the trail, and turn back without rewriting the main route.

## Joining the expedition from another pack

Mora is away from Finch's terminal. To get a full copy of the expedition cache, she clones it.

```bash
git clone https://github.com/finch-mora/wayfarer-pass.git
cd wayfarer-pass
```

Cloning downloads the entire repository — history, branches, and files — into a new folder. After cloning, `origin` is already set to point to that remote.

## Forks when permission is not there

Sometimes a wayfarer wants to contribute to someone else's cache but doesn't have write access. They **fork** the repository on GitHub: creating a personal copy under their own account. They clone their fork, make changes on a branch, and later propose merging back via a Pull Request (covered next).

For a two-person team with write access, forking isn't necessary — cloning and branching is enough. Knowing both is part of the trail.

## Permissions at camp

GitHub access levels affect what you can do:

- **Read** — can view and clone, cannot push.
- **Write** — can push branches and commits (standard for trusted wayfarers).
- **Admin** — can manage settings, collaborators, and protection rules.

> [!TIP]
> If `git push` is rejected with a permission error, check whether you cloned the original or your fork, and whether your account has write access.

## Blazing a side trail

To scout the shortcut safely, Finch creates and switches to a new branch.

```bash
git branch shortcut-scout
git switch shortcut-scout
```

Or in one command:

```bash
git checkout -b shortcut-scout
```

While on `shortcut-scout`, any commits he makes only affect that branch. `main` remains exactly as it was. To see all branches:

```bash
git branch -a
```

Plausible output:

```text
* shortcut-scout
  main
  remotes/origin/main
```

## Syncing with news from camp

Mora just pushed an updated `supply-manifest.md` to `main`. Finch wants to bring those updates into his current work so he knows what supplies are available. From his branch (or from `main`), he pulls.

```bash
git pull
```

`git pull` fetches changes from the tracked remote branch and merges them into the current local branch. If working on `main`, it updates `main`. If working on a feature branch and the upstream is set, it updates that branch — but it's often safer to pull `main` first, then merge `main` into the side trail, or rebase depending on the trail rules.

For now, the key is: pulling keeps the cache current with what others left at the campfire.

> [!WARNING]
> Pull often, especially before starting new work or before pushing. A stale cache is the easiest way to create avoidable conflicts down the trail.

## Output

Branches let the party split and explore without stepping on each other. Cloning brings the full history to a new pack. Forking creates a personal copy when write access isn't available. `git pull` keeps local caches in sync with the shared campfire. The main route stays intact until the side trail is ready to be reviewed and merged.

## Task 3: Split the Party

On the shared cache, create a branch called `cliff-scout`, switch to it, add `cliff-notes.md`, commit with `"trail: add cliff scout observations"`, push the branch to origin with `-u origin cliff-scout`. Also write the commands to clone the repo into a new folder and to pull latest changes while on `main`. Give plausible outputs where relevant.

**Why this order:** isolate risky exploration on a branch. Push the branch so others can see it, but don't touch `main`. Keep `main` up to date with `git pull` when syncing.

**Next:** [[04 - Campfire Reviews]]
