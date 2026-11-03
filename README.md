# Chasing Quixote

A character-driven mystery visual novel for Ren'Py. Follow Fox Hawthorne, a former television detective actor, aboard a fan cruise where an apparent staged mystery becomes very real.

**Status:** Preproduction. The repository is a launchable Ren'Py 8.5.3 project with a short non-canonical prototype. No complete playable episode is claimed.

## Game direction

- **Engine:** Ren'Py, desktop-first.
- **Presentation:** Illustrated 2D environments, expressive character sprites, selective cinematic CGs.
- **Gameplay:** Explore locations, talk to people, collect observations, and reconstruct scenes using Fox's notebook.
- **Tone:** Wry and character-led, with a serious mystery and no forced one-liner after every emotional moment.
- **Design boundary:** No courtroom, Press/Present loop, credibility meter, or punitive disability-based status mechanic. There is one canonical mystery ending; optional discoveries change context and dialogue.
- **Narrative:** Manuscript and private canon ledger take priority over prototype dialogue.

## Where files live

- `game/`: Ren'Py project generated with the 8.5.3 launcher (`gui.rpy`, `screens.rpy`, `options.rpy`, and `game/gui/`), plus the custom prototype in `script.rpy` and `cq_notebook.rpy`.
- `docs/`: production workflow and asset standards.
- `AGENTS.md`: guardrails for Cursor and coding agents.
- **Google Drive:** [Chasing Quixote project folder](https://drive.google.com/drive/folders/1LdQB99iNy0ZuOncVuX2g-VO_v0d2XkF1), containing the private canon, production roadmap, dialogue drafts, and asset specifications.

## Launch

Use Ren'Py **8.5.3** (the current stable SDK when this project was generated): [https://www.renpy.org/release/8.5.3](https://www.renpy.org/release/8.5.3). A newer 8.x SDK should also open the project. The game window title is **Chasing Quixote**. The launcher lists the repository folder by its directory name.

The launcher only shows a project when that project's parent folder is the Projects Directory. This repository root is the project, because it contains `game/`.

### Windows

1. Install `renpy-8.5.3-sdk.zip` (or the SDK installer) and extract it.
2. Clone this repository.
3. Start `renpy.exe`.
4. If the project is missing from the list, open **preferences**, set **Projects Directory** to the folder that *contains* this repository, and return to the project list.
5. Select the project and click **Launch Project**.

From a command prompt in the SDK directory, with `<project>` as the full path to this repository:

```bat
lib\py3-windows-x86_64\python.exe renpy.py <project>
lib\py3-windows-x86_64\python.exe renpy.py <project> lint --error-code
lib\py3-windows-x86_64\python.exe renpy.py <project> test cq_prototype
```

### Linux and macOS

From the SDK directory:

```bash
./renpy.sh <project>
./renpy.sh <project> lint --error-code
./renpy.sh <project> test cq_prototype
```

`lint` checks the script. `test cq_prototype` plays the placeholder from the main menu: either clue order, the notebook, both reconstruction choices, save/load, rollback, and **End prototype** back to the main menu.

### What the prototype does

The sample content is **non-canonical placeholder material**, for testing mechanics only. It is deliberately spoiler-free.

- **Start** enters the hub.
- **Inspect the event schedule** and **Check the noticeboard** can be done in either order. Each observation is kept.
- **Open Fox's notebook** reviews those observations. **Close notebook** or Escape dismisses it.
- **Compare the records** stays closed until both observations exist. One choice records a working theory. The other leaves the theory unset. Neither deletes an observation.
- **End prototype** returns to the main menu.
- Save, load, and rollback use the standard launcher screens. They keep the clue list and theory flag that belong to that point in the script.

## Production approach

Cursor implements and tests Ren'Py. ChatGPT/Work develops scripts, character guidance and art specifications. Midjourney handles environment and prop concepts; ChatGPT generates character portraits and scene illustrations. GitHub is the code source of truth; Drive holds story canon and references.

**Public-repository caution:** This repository is public as of initial setup. Do not commit manuscript chapters, unreleased story twists, personal sensitive details, credentials, or unapproved artwork. Keep those assets in restricted storage until deliberately cleared for publication.
