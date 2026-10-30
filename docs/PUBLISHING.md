# Preview and publish the Glitch Garden

The profile is ready locally. The GitHub connector reported `push: false` for `anshiiii-hub/anshiiii-hub`, so no remote files were changed.

## Preview

Open `preview/index.html` in a browser for the desktop layout, `preview/mobile.html` for a narrow content-column approximation, and `preview/atlas.html` for the vector artwork. These pages use only local assets and work without a server. The preview renderer is deliberately small and specific to this README; it is not GitHub's Markdown engine.

For GitHub's actual rendering, open `README.md` in a Markdown editor with GitHub-flavored Markdown support, or use GitHub's **Preview** tab after uploading. The custom styles in the HTML previews are preview-only; the actual README uses supported Markdown and HTML.

## Publish through GitHub

1. Sign in as an account that can write to [anshiiii-hub/anshiiii-hub](https://github.com/anshiiii-hub/anshiiii-hub).
2. Extract `glitch-garden-deliverables.zip`.
3. Use **Add file → Upload files** in the repository. Upload `README.md` and the `assets/glitch-garden` folder, preserving that folder path. Replace the root README.
4. Keep all existing assets and other files. The old `assets/anshita-*` files are not used by the new README and do not need to be removed.
5. Commit the change to `main` (or open a pull request if preferred). Confirm the images appear in the repository README, then view [the profile](https://github.com/anshiiii-hub).

Only `README.md` and `assets/glitch-garden/` are required on GitHub. The scripts, documentation, and previews are optional maintenance files. Do not upload the ZIP itself as a substitute for extracting the files. No GitHub Action, third-party badge service, paid API, or animation service is required.

## Publish from a local clone

Clone the existing repository into a separate directory, copy the new root README and the whole `assets/glitch-garden` folder into it, and review `git diff` and `git status`. Stage only the new README and new art directory, commit, and push through your normal authenticated Git workflow. Do not replace the entire existing assets directory.

## Rebuild and validate

From the deliverables directory:

```sh
python3 scripts/build-garden.py
python3 scripts/preview-garden.py
python3 scripts/validate-garden.py
```

These scripts use Python's standard library. The generated PNG hero is a separate image asset; the vector builder does not overwrite it. To use the fully vector opening instead, change the hero image extension in `README.md` from `.png` to `.svg` and rebuild the previews.
