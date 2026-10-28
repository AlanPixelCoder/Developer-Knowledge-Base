# 02. Trail Markers

**Spanish version:** [02 - Marcas del Sendero](./02%20-%20Marcas%20del%20Sendero.md)

**Course:** Git & GitHub
**Topic:** Wayfarer workflow — working tree, staging, commits, status, push
**Tags:** `#git` `#workflow` `#commits` `#wayfarer`

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

With the cache ready, Finch lays down the first trail marker: a map of Greyharbor Pass. Instead of carving it in stone, he writes `pass-map.md`. Mora adds `supply-manifest.md`. Every time they want to save a meaningful change to the history of the expedition, they leave a trail marker in the form of a commit. The trick is knowing where notes sit before they become markers.

> [!NOTE]
> **Three places for notes**
> Git tracks changes across three areas: the **working directory** (files being edited), the **staging area** (files marked to go into the next snapshot), and the **local repository** (committed snapshots stored in `.git`).

## Marking the map

Finch creates `pass-map.md` with the first rough sketch of the pass. At this point it's just a file on disk — Git sees it as untracked. To choose what goes into the next snapshot, he stages it.

```bash
git add pass-map.md
```

To stage everything changed in the current folder:

```bash
git add .
```

To stage only certain file types:

```bash
git add *.md
```

Staging is selective on purpose. If Finch fixes a typo in one file but is mid-edit on another, he can stage just the finished change.

## Leaving a trail marker

Once the staged changes form a coherent marker — "first pass map" — he commits them with a message explaining why.

```bash
git commit -m "trail: add first sketch of Greyharbor Pass"
```

A commit is a snapshot with an ID, author, timestamp, and message. It becomes part of the expedition history. Good messages say *what* and *why* in a short form; vague messages like "update" are hard to follow three bends down the trail.

> [!TIP]
> The staging area is like packing the saddlebag for this leg of the journey. You don't have to pack everything you touched today — only what belongs together in this marker.

## Checking the trail

Before committing or pushing, it's worth checking the state of the pack. `git status` shows untracked files, staged changes, and unstaged changes.

```bash
git status
```

Plausible output at this point:

```text
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to remove from index)
	new file:   pass-map.md
```

Or after edits:

```text
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
	modified:   supply-manifest.md

no changes added to commit (use "git add" and/or "git commit")
```

## Sending markers to the shared camp

The markers exist locally in `.git`. To share them with the campfire on GitHub, they push. The first time on a new branch they set the upstream.

```bash
git push -u origin main
```

After that, pushing new markers is simpler:

```bash
git push
```

Plausible push output (abbreviated):

```text
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 245 bytes | 245.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/finch-mora/wayfarer-pass.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main' by default.
```

> [!WARNING]
> Only push what has been committed. `git add` moves to staging; `git commit` creates the snapshot; `git push` sends snapshots to the remote. If you forgot to commit, nothing new will go to the campfire.

## Output

The workflow becomes a loop: edit in the working directory → `git add` to stage → `git commit` to leave a trail marker → `git push` to share with the camp. `git status` is the compass for knowing which step comes next. Each marker is small and explains its purpose.

## Task 2: Leave Two Markers

Create `pass-map.md` and `supply-manifest.md` in `wayfarer-pass`. Stage both with `git add .`, commit with the message `"trail: add pass map and initial supply manifest"`, push to `origin/main` with `-u` on first push. Show the plausible sequence of commands and plausible outputs for `git status` before staging and after committing.

**Why this order:** stage what belongs together, commit with a clear message, then share. Small, purposeful markers are easier to read in history than giant commits that change everything at once.

**Next:** [[03 - Forks in the Trail]]
