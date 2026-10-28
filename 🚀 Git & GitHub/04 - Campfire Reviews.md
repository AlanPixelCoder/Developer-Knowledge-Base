# 04. Campfire Reviews

**Spanish version:** [04 - Revisiones en la Hoguera](./04%20-%20Revisiones%20en%20la%20Hoguera.md)

**Course:** Git & GitHub
**Topic:** Wayfarer integration — merge, conflicts, Pull Requests, open source workflow
**Tags:** `#git` `#pull-requests` `#merging` `#wayfarer`

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

Finch returns from the shale cliffs with good news: the shortcut is passable. Before carving it into the official route map, the party sits by the campfire for a review. They need to merge `cliff-scout` into `main`, handle any disagreements in the notes, and propose changes formally through a Pull Request. The campfire is where rough notes become part of the official expedition log.

> [!NOTE]
> **Merging brings trails together**
> `git merge` takes commits from one branch and integrates them into another. If changes don't overlap, it's usually clean. If both sides edited the same lines, Git marks a conflict that must be resolved by hand.

## Bringing the shortcut home

The cleanest way: update `main` first, switch to it, make sure it's current, then merge the side trail in. Alternatively merge from the feature branch, but keeping `main` up to date is a safe habit.

```bash
git checkout main
git pull
git checkout cliff-scout
git merge main
```

Or from `main` directly:

```bash
git checkout main
git pull
git merge cliff-scout
```

If there are no conflicting changes, Git creates a merge commit (or fast-forwards) and the shortcut notes become part of `main`. Then push:

```bash
git push
```

## When notes clash

Sometimes Finch and Mora edit `pass-map.md` at the same time — one adds a bridge marker, the other adds a ford marker, in the same section. Git can't decide which to keep. It marks the conflict like this:

```text
<<<<<<< HEAD
Ford marker added by Mora on main
=======
Bridge marker added by Finch on cliff-scout
>>>>>>> cliff-scout
```

The wayfarers must edit the file to pick one, combine both, or write a new version. They remove the `<<<<<<<`, `=======`, `>>>>>>>` markers. After resolving, they stage and commit.

```bash
git add pass-map.md
git commit -m "trail: resolve pass-map merge conflict"
git push origin cliff-scout
```

> [!WARNING]
> Never leave conflict markers in committed files. If unsure, look at both sides carefully and make sure the final text is coherent. A bad merge creates a mess that's harder to undo than a delay.

## Pull Requests at the campfire

A **Pull Request (PR)** is a proposal to merge a branch into another. On GitHub it opens a space for discussion, review, and checks before integration. Even for a two-person party it's worth using: the PR becomes the record of "why we added the shortcut" with comments and the diff.

Typical flow:

1. Push the branch to origin.
2. Open a Pull Request on GitHub from `cliff-scout` to `main`.
3. Review the diff, discuss, and request changes if needed.
4. Once approved, merge the PR (GitHub can do a merge commit, squash, or rebase).
5. Pull the updated `main` locally.

> [!TIP]
> A good PR description says what the trail change is, why it's needed, and any notes for reviewers (e.g. "tested at low water, safe to cross").

## The trail map for wider expeditions

For contributing to someone else's cache with no write access, the flow is slightly different:

1. **Fork** the original repository on GitHub to your own account.
2. **Clone** your fork locally: `git clone <fork-url>`.
3. **Create a branch** for your change: `git switch -c trail-fix`.
4. **Commit and push** to your fork: `git add . && git commit -m "..." && git push -u origin trail-fix`.
5. **Open a Pull Request** from your fork's branch to the original repository's `main` branch.

## Output

Merging integrates side trails into the main route. Conflicts are expected when work overlaps — they just need careful resolution. Pull Requests formalize the review at the campfire, creating a paper trail of decisions. The open-source workflow scales the same pattern to larger parties of wayfarers.

## Task 4: Hold a Campfire Review

Simulate merging `cliff-scout` into `main`: give the commands to update `main`, merge the branch, and push. Show a plausible conflict in `pass-map.md` with `<<<<<<<`, `=======`, `>>>>>>>`, then show the resolution steps (`git add`, `git commit`, `git push`). Finally outline the five steps for contributing to an external repository via fork and PR, using plausible commands where possible.

**Why this order:** integration requires care. Review before merging, resolve conflicts deliberately, and document the proposal in a PR. Good habits prevent lost notes and keep the official route trustworthy.

**End of Wayfarer trail.**
