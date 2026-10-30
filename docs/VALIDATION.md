# Delivery and validation · 30 October 2026

## Files created and intended repository changes

- Replace the existing root `README.md` with the complete new profile.
- Add 14 artwork files under `assets/glitch-garden/`: one PNG and 13 SVGs. See `ARTWORK.md` for the individual list.
- Optional supporting files: `scripts/build-garden.py`, `scripts/preview-garden.py`, `scripts/validate-garden.py`; `docs/ARTWORK.md`, `docs/SOURCES.md`, `docs/PUBLISHING.md`, `docs/VALIDATION.md`; `preview/index.html`, `preview/mobile.html`, `preview/atlas.html`.
- Local package: `glitch-garden-deliverables.zip` includes the above files. It excludes `.git`, the original remote assets, and itself.

No remote file has been changed. No existing mascot asset has been copied, edited, or deleted. No unrelated project was modified.

## Automated validation

`python3 scripts/validate-garden.py` passed:

- 10 README image references resolve to local files and contain nonempty alt text.
- All 13 SVGs parse as XML, have a viewBox and title, and are below 20 KB each.
- SVGs contain no scripts, embedded raster images, foreignObject, event handlers, or external references.
- All internal navigation links resolve to one of 8 explicit anchors.
- All four details/summary blocks are balanced.
- No old mascot filenames or script/style/iframe embeds appear in the README.
- Nine unique external GitHub links use the intended account. Repository targets were confirmed through repository discovery; linked code/document targets were successfully fetched through the GitHub connector.

## Actual visual inspection

The generated PNG was opened and inspected. A browser displayed the local HTML approximation of the complete README. Screenshots were inspected for the desktop opening, a 342-pixel content column, the ORQESTRA project presentation, and the top of the SVG atlas. The opening, navigation wrapping, artwork, specimen card, and SVG character rendered correctly in those views.

This was a local preview, not a screenshot of the published GitHub profile. The narrow content column approximates mobile wrapping; no physical mobile device test was performed. The preview renderer is specific to this README and is not a full GitHub-flavored Markdown implementation. GitHub's own Preview remains the final publishing check. No claim is made that every section was visually checked at every viewport.

The project applications were inspected as source and documentation only; their runtime suites were not rerun. No animation, external asset service, companion site, or workflow is required.

## Publish status

The GitHub connector reported read-only access (`push: false`) to the profile repository. The local deliverables and ZIP are complete; upload/push remains a user action with write access. See `PUBLISHING.md`.
