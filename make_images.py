#!/usr/bin/env python3
"""Turn the original figures in src/img/ into web images in docs/assets/img/.

Run this only when a figure is added or replaced:  python3 make_images.py
It needs Pillow (pip install pillow). build.py itself needs no packages.

For each original it writes NAME.webp at full size (what the figure viewer
opens), plus NAME-800.webp and NAME-1200.webp when the original is large
enough, so phones download a smaller file. It also writes
src/img/manifest.json, which build.py reads for the sizes.
Schematic PNGs stay lossless at full size so thin lines and small text
stay sharp in the viewer.
"""
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
SRC = ROOT / "src" / "img"
OUT = ROOT / "docs" / "assets" / "img"
STEPS = [(800, 1000), (1200, 1500)]   # (variant width, smallest original that gets it)
# Link previews (og:image) need a JPEG, so the home page thumbnails are also copied as they are.
KEEP_ORIGINAL = {"p1_wiring.jpg", "b_layout.jpg", "p2_v2.jpg", "p3_robot.jpg", "h_intake.jpg"}

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for f in sorted(SRC.iterdir()):
        if f.suffix.lower() not in (".jpg", ".jpeg", ".png"):
            continue
        im = Image.open(f)
        im = im.convert("RGBA" if "A" in im.getbands() else "RGB")
        w, h = im.size
        line_art = f.suffix.lower() == ".png"
        if line_art:
            im.save(OUT / f"{f.stem}.webp", "WEBP", lossless=True, method=6)
        else:
            im.save(OUT / f"{f.stem}.webp", "WEBP", quality=82, method=6)
        widths = []
        for vw, min_w in STEPS:
            if w >= min_w:
                small = im.resize((vw, round(h * vw / w)), Image.LANCZOS)
                small.save(OUT / f"{f.stem}-{vw}.webp", "WEBP", quality=90 if line_art else 82, method=6)
                widths.append(vw)
        if f.name in KEEP_ORIGINAL:
            (OUT / f.name).write_bytes(f.read_bytes())
        manifest[f.stem] = {"w": w, "h": h, "widths": widths}
    (SRC / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    print(f"Wrote {len(manifest)} figures into {OUT}")

if __name__ == "__main__":
    main()
