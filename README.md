# Derek Zhuang engineering portfolio (website)

Static site for GitHub Pages. The published site is everything in `docs/`.

## Layout
- `src/projects/<slug>.html`: the text and figures for each project page.
- `build.py`: the project list (titles, bylines, home page summaries, order), the home page, and the shared header and footer.
- `src/img/`: the original figures (JPEG and PNG) and `manifest.json`, the list of sizes that `make_images.py` writes.
- `make_images.py`: turns the originals into WebP files in `docs/assets/img/`, at full size plus 800 and 1200 px wide versions for phones. Needs Pillow.
- `docs/`: the built site that GitHub Pages serves. `docs/assets/` holds the CSS, the figure viewer script, fonts and the WebP images.

## Editing
1. Change text in `src/projects/<slug>.html`, or titles, summaries and order in `PROJECTS` inside `build.py`.
2. Run `python3 build.py` (no packages needed).
3. Commit and push. GitHub Pages republishes in about a minute.

To add or replace a figure: put the original in `src/img/`, run `python3 make_images.py` (needs `pip install pillow`), then `python3 build.py`. Pages keep naming the original file, such as `../assets/img/p1_wiring.jpg`, and the build points them at the WebP versions. A figure shown wider than half the window needs its own `sizes="..."` on the `<img>` (see `b_buck.png` on the BOLT page).

The graduation year on the home page is `CLASS_YEAR` in `build.py`.

The first entry in `PROJECTS` is the lead project: it gets the large photo at the top of the home page. To make BOLT the lead once the board is fabricated, move its entry to the top and rebuild.

In a project file, `<!--head-->` marks where the title goes when it sits beside the page's main figure. Figures get their link targets automatically from the `Fig. N` in each caption.

## Publishing on GitHub Pages
1. The repo is `DerekZhuang/DerekZhuang.github.io` (public). Push to `main`.
2. On GitHub: Settings, Pages, Source "Deploy from a branch", Branch `main`, folder `/docs`, Save.
3. The site is served at `https://derekzhuang.github.io/`.
4. `SITE_URL` in `build.py` holds that address so links shared on LinkedIn or in messages show a preview image.

## Rules carried over from the PDF
- No fabricated or embellished claims. Every number on the site comes from the PDF portfolio, which was checked against primary sources.
- No em dashes.
- Credit the team for team work (turret structure, shooter, robot CAD).
- No other teams' images. No phone number on the public site.
- Design: Barlow Condensed, Source Serif 4 and Barlow; one ink color and one green accent used only for figure numbers, links and review rings. No Inter, no orange, no tinted callout boxes, no all-caps labels, no 01/02/03 numbering.
- Links inside running text are underlined, standalone links are about 44 px tall on phones, and tables have a header row. Keep these when adding content.
- Figures are numbered per page and the text refers to them. If you add or move a figure, renumber the captions and the `Fig. N` references on that page.

## Not done yet
- Turret video loop (5 to 8 s, compressed to a few MB) once the clip is available.
- H2GP page.
- Photo of the fabricated under-glow board.
