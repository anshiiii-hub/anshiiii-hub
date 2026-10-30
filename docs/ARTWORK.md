# Original artwork and NOVA

NOVA's consistent identity is an asymmetrical mint crystal with a midnight inset facet, two square paper eyes, a lime diamond core, and three orbiting fragments: lime, mint, and periwinkle. It has no limbs, human traits, laptop, or robot hardware. The five vector scenes share the exact same drawing function in `scripts/build-garden.py`; only expression and surrounding objects change.

The README uses an imagegen-created panoramic PNG for its opening, then self-contained SVG illustrations for the ecosystem, task graph, toolkit, roadmap, character scenes, and closing garden. A fully vector alternate hero is included. The code-generated vector design follows the same character specification as the generated opening scene, with simplified facets for small sizes.

All essential wording stays in Markdown. SVGs contain only artwork, accessibility titles, and small specimen numbers. Nothing fetches an external font or image, and no script executes inside the README. The artwork is static, so it also works for reduced-motion preferences without an alternate asset. The PNG is approximately 2.4 MB; each SVG is below 20 KB.

## Hero generation

Created using the built-in `image_gen` tool, then copied into `assets/glitch-garden/hero-garden.png`. No CLI/API fallback was used. No image from the previous mascot system was provided as a reference. The result was visually inspected before integration.

Final prompt:

> Use case: illustration-story. Create one polished original panoramic 3:1 illustration for a GitHub profile titled The Glitch Garden, but ABSOLUTELY NO TEXT or typography inside the image. An indie botanical atlas inside a computer, original sophisticated editorial flat geometric illustration with tiny deliberate pixel fragments, not generic 3D AI art. Wide scene: dark deep forest ink #101A19 and midnight #142536 landscape, delicate fine-lined branching neural trees, mint crystalline reeds, periwinkle data constellations, lime glowing seeds, subtle coral fungi. Main character NOVA near center-right: a small floating irregular six-sided mint crystalline organism, distinct asymmetrical hexagon silhouette with one top corner cut, dark front inset facet, luminous lime diamond core in lower body, two tiny warm-paper square eyes above core, no mouth, arms, legs, robot hardware or humanoid body; three detached orbiting square fragments (lime top left, mint right, periwinkle lower left). NOVA curiously leans toward one small lime diamond seed sprouting from a plant. Restrained warm light on paper-textured faceted floating garden islands; fine scientific diagram lines without labels. Subtle atmosphere, beautiful graphic composition, crisp angular forms, generous dark negative space upper left, no dramatic excessive neon. Colors ONLY forest ink, midnight, acid lime #D7F56D, mint #9EE6C4, periwinkle #8B91FF, coral #FF8978, paper #F7F3E9, stone #83928C. No humans, no laptop, no desk, no robot, no badge, no stock imagery, no watermark. Delivery: illustration only, 3:1 wide banner.

## Files

- `hero-garden.png` — generated opening scene.
- `hero-garden.svg` — reproducible vector alternate.
- `nova-curious.svg` — observes a data pattern.
- `nova-growing.svg` — examines a digital plant.
- `nova-debugging.svg` — inspects a coral bug.
- `nova-discovery.svg` — celebrates a seed-shaped discovery.
- `nova-resting.svg` — rests among geometric stars.
- `idea-ecosystem.svg` — five connected regions.
- `project-orqestra.svg` — abstract task DAG and review/output nodes; not an architecture screenshot.
- `project-docdiff.svg` — document comparison motif.
- `project-upi.svg` — decorative chart motif; not actual financial data.
- `tool-garden.svg` — four botanical specimen sheets.
- `growth-paths.svg` — branching, unfinished learning paths.
- `garden-footer.svg` — the last seed and resting NOVA.
