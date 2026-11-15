# AH Wallpaper Gallery

Interactive designs for AH Wallpaper. The app reads `index.json` from this repository and shows the designs in its **Discover** tab.

## Adding a design
1. Create a folder inside `designs/` with a short English name and no spaces, e.g. `neon-city`.
2. Put these files in it:
   - `design.ahwp` — exported with the **Share** button in the app.
   - `thumb.jpg` — about 640×360, under 150 KB.
   - `meta.json` — copy it from `designs/example/` and edit the name and author.
3. Run `python tools/make_index.py`.
4. Commit and push.

## Limits
- `design.ahwp` can be up to 20 MB. Larger designs go in GitHub Releases.
- Review every design before adding it.
