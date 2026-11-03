# Production workflow — v1

## Ownership

**Cursor / Ren'Py** — game code, interaction architecture, asset hooks, automated validation, engine smoke tests, desktop packaging.

**ChatGPT / Work** — narrative drafts, source-aware character/continuity reviews, content QA, design specifications, art handoff and Drive organization.

**Midjourney** — background concepts, location variants, environmental props and textures.

**ChatGPT image generation** — character portraits, expression sets, full-body sprites, scene illustrations.

## Source of truth

- GitHub: buildable game source and approved, release-safe artifacts.
- [Google Drive Chasing Quixote](https://drive.google.com/drive/folders/1LdQB99iNy0ZuOncVuX2g-VO_v0d2XkF1): manuscript and production documents; use appropriate access controls.
- All new dialogue is *provisional* until checked against the manuscript's exact chronology, evidence timing, and character relationships.

## Asset contract

Every asset should have: stable ID, source tool, approval state, original prompt/source, filename, usage rights, required pixel dimensions, crop, transparent padding (sprites), anchor, and intended Ren'Py scene.

Start with one Ashes Lounge background and one approved Fox character portrait. Check them together with the actual dialogue UI before batch-generating locations or expression sheets.

## Quality checkpoints

1. Character identity and scene composition match approved references.
2. Artwork does not bury dialogue or interactive elements.
3. Character assets are consistently anchored and expression variations do not jump.
4. No critical clue depends only on color, sound, or an unlabeled visual hotspot.
5. Unapproved or placeholder material is clearly distinguished from release-ready content.

## Build status

The repository is a Ren'Py 8.5.3 project with a source-only, spoiler-free *mechanical* scene. The first engine smoke test is the `cq_prototype` suite in `game/cq_smoke.rpy`. Run that, and lint, before expanding the scene.
