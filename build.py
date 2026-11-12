#!/usr/bin/env python3
"""Build the portfolio website into docs/ (the folder GitHub Pages serves).

Edit project text in src/projects/<slug>.html, edit the list below to
change titles, summaries or order, then run:  python3 build.py

The order of PROJECTS is the order of the site. The first project is the
one featured at the top of the home page, so moving a project to the top
of the list makes it the lead.
"""
import re
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
SRC = ROOT / "src" / "projects"
OUT = ROOT / "docs"

NAME = "Derek (Ziheng) Zhuang"
SHORT_NAME = "Derek Zhuang"
EMAIL = "derekzhuang12345@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/derek-zhuang-6246352b1"
PDF = "https://drive.google.com/file/d/1knBHxL6q7wfWigkeNkA8Oi-ZfvWAPpQj/view"
UPDATED = "Nov 2026"
# Set this once the site is live (for example "https://username.github.io/portfolio")
# so shared links show a preview image. Leave empty until then.
SITE_URL = "https://derekzhuang.github.io"

PROJECTS = [
    {
        "slug": "robot-electrical",
        "title": "2026 robot electrical system",
        "where": "FRC Team 6560, 2026 season",
        "byline": "FRC Team 6560, 2026 season. I designed the lattice belly pan and wired the entire robot.",
        "summary": "I wired the whole robot on 12 AWG copper-clad aluminum after checking the rules, and split CAN into two buses so a mechanism fault cannot take down the drivetrain. That split kept us playing defense when a crushed wire took out the mechanism bus.",
        "thumb": "p1_wiring.jpg", "thumb_size": (1520, 1430), "thumb_pos": "58% 50%",
        "thumb_alt": "Underside of the 2026 robot with its wiring, power distribution hub and fuse panels",
    },
    {
        "slug": "bolt-underglow",
        "title": "BOLT under-glow controller board",
        "where": "BOLT at Virginia Tech, started October 2026",
        "byline": "BOLT Controls, Virginia Tech's electric motorcycle team. Project started in October 2026, with the schematic and PCB layout done in Altium Designer.",
        "summary": "An LED controller board on the bike's CAN bus: two schematic revisions, a design review that found three problems, and a four-layer layout routed to zero design rule violations. Fabrication is planned for the end of November.",
        "thumb": "b_layout.jpg", "thumb_size": (1390, 1389), "thumb_pos": "50% 50%",
        "thumb_alt": "Routed four-layer PCB layout of the under-glow board",
        "sections": [("schematic", "Schematic"), ("review", "Design review"), ("layout", "PCB layout")],
    },
    {
        "slug": "turret",
        "title": "Turret wire management",
        "where": "FRC Team 6560, fall 2025 through the 2026 season",
        "byline": "FRC Team 6560, fall 2025 research through the 2026 competition robot. I designed and built the wire routing. The turret structure and shooter belong to the team.",
        "summary": "Every power and CAN wire has to follow a turret that turns about 400°. The printed V1 cracked in collision practice, so V2 went the opposite way and ran all 28 official 2026 matches without a repair.",
        "thumb": "p2_v2.jpg", "thumb_size": (1500, 1141), "thumb_pos": "38% 50%",
        "thumb_alt": "Turret on the 2026 robot with the V2 wire routing channel and cable sleeve",
        "sections": [("concept", "Concept"), ("v1", "V1"), ("v2", "Why V2 replaced V1")],
    },
    {
        "slug": "belly-pans",
        "title": "Belly pans: where the electronics live",
        "where": "FRC Team 6560, 2025 offseason",
        "byline": "FRC Team 6560, 2025 offseason robot, July to August 2025. My first belly pan, designed in SolidWorks, with the electronics layout planned around the wiring.",
        "summary": "My first belly pan: a half-width lattice pan laid out around the wiring, cut on the team CNC the same night I finished the design.",
        "thumb": "p3_robot.jpg", "thumb_size": (1000, 910), "thumb_pos": "50% 50%",
        "thumb_alt": "Belly pan with electronics in the full robot CAD model",
    },
    {
        "slug": "hatch",
        "title": "Hatch, a full-stack marketplace",
        "where": "A friend's startup, July to August 2026",
        "byline": "A friend's startup MVP, July to August 2026. I took over development and wrote 91 of the 93 commits on main. "
                  '<a href="https://github.com/tobyzijin925-web/projectHatch">github.com/tobyzijin925-web/projectHatch</a>',
        "summary": "A Node.js and SQLite backend with no npm dependencies, a 14-table schema with the task lifecycle enforced in the database, and a server-side AI intake assistant.",
        "thumb": "h_intake.jpg", "thumb_size": (1600, 887), "thumb_pos": "50% 0%", "thumb_line": True,
        "thumb_alt": "Hatch intake page",
    },
]

INTRO = (
    "I work on the electrical side of competition machines: power distribution, wiring, and deciding where the "
    "electronics go. I was Electrical Lead on FRC Team 6560 for 2025-26 and now mentor the team. I also drive and "
    "run electrical and battery systems for an H2GP hydrogen fuel-cell race car. On the Controls subteam at BOLT, "
    "Virginia Tech's electric motorcycle team, I am designing an "
    '<a href="projects/bolt-underglow.html">LED controller board</a>, and I am working toward PCB and chip design.'
)


def page(title, body, depth, description, block_label, image=None, home=False):
    up = "../" * depth
    full_title = NAME if home else f"{escape(title)} | {NAME}"
    og = ""
    if SITE_URL and image:
        og = f'\n<meta property="og:image" content="{SITE_URL.rstrip("/")}/assets/img/{image}">'
    brand = "" if home else f'\n  <a class="brand" href="{up}index.html">{NAME}</a>'
    all_projects = "" if home else f'\n    <a href="{up}index.html">All projects</a>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{escape(description)}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{escape(description)}">{og}
<link rel="icon" href="{up}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{up}assets/css/site.css">
</head>
<body>
<header class="site-head{' home' if home else ''}"><div class="in">{brand}
  <nav aria-label="Site">{all_projects}
    <a href="{PDF}">Portfolio PDF</a>
    <a href="{LINKEDIN}">LinkedIn</a>
    <a href="mailto:{EMAIL}">Email</a>
  </nav>
</div></header>
<main>
{body}
</main>
<footer class="tb{' home-tb' if home else ''}"><div class="cells">
  <span><b>{SHORT_NAME}</b>Engineering portfolio</span>
  <span>{escape(block_label)}</span>
  <span>Updated {UPDATED}. <a href="{PDF}">PDF version</a></span>
</div></footer>
<script src="{up}assets/js/site.js" defer></script>
</body>
</html>
"""


def card(p, feature=False):
    w, h = p["thumb_size"]
    cls = "thumb line" if p.get("thumb_line") else "thumb"
    pos = f' style="object-position:{p["thumb_pos"]};"' if feature else ""
    lazy = "" if feature else ' loading="lazy"'
    extra = " feature" if feature else ""
    return f"""<a class="project{extra}" href="projects/{p['slug']}.html">
    <div class="{cls}"><img src="assets/img/{p['thumb']}" width="{w}" height="{h}" alt="{escape(p['thumb_alt'])}"{pos}{lazy}></div>
    <div class="words">
      <h2>{escape(p['title'])}</h2>
      <div class="where">{escape(p['where'])}</div>
      <p class="sum">{escape(p['summary'])}</p>
    </div>
  </a>"""


def build_home():
    lead, rest = PROJECTS[0], PROJECTS[1:]
    items = "\n".join(f"  <li>{card(p)}</li>" for p in rest)
    body = f"""<div class="wrap">
<section class="hero">
  <div class="who">
    <h1 class="display">{NAME}</h1>
    <p class="byline">Electrical engineering student at Virginia Tech, class of 2029</p>
    <div class="prose"><p class="lead">{INTRO}</p></div>
    <div class="contact">
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="{LINKEDIN}">linkedin.com/in/derek-zhuang-6246352b1</a>
    </div>
  </div>
  {card(lead, feature=True)}
</section>
<section class="more" id="projects">
  <h2>More projects</h2>
  <ul class="work">
{items}
  </ul>
</section>
</div>"""
    desc = ("Engineering portfolio of Derek Zhuang, electrical engineering student at Virginia Tech: "
            "robot electrical systems, PCB design, and wire management.")
    html = page(NAME, body, 0, desc, "Index of projects", image=lead["thumb"], home=True)
    (OUT / "index.html").write_text(html, encoding="utf-8")


def link_figures(content):
    """Give each figure an id (fig-N) and turn 'Fig. N' references into links to it."""
    parts = content.split("<figure")
    out = [parts[0]]
    for part in parts[1:]:
        m = re.search(r"<b>Fig\. (\d+)</b>", part)
        out.append(f'<figure id="fig-{m.group(1)}"' + part if m else "<figure" + part)
    content = "".join(out)
    return re.sub(r'<span class="ref">Fig\. (\d+)([^<]*)</span>',
                  r'<a class="ref" href="#fig-\1">Fig. \1\2</a>', content)


def build_projects():
    (OUT / "projects").mkdir(parents=True, exist_ok=True)
    n = len(PROJECTS)
    for i, p in enumerate(PROJECTS):
        content = link_figures((SRC / f"{p['slug']}.html").read_text(encoding="utf-8"))
        onpage = ""
        if p.get("sections"):
            links = "".join(f'<a href="#{sid}">{escape(label)}</a>' for sid, label in p["sections"])
            onpage = f'\n  <nav class="onpage" aria-label="On this page"><span>On this page</span>{links}</nav>'
        head = f"""<header class="page-head">
  <h1 class="display">{escape(p['title'])}</h1>
  <p class="byline">{p['byline']}</p>{onpage}
</header>"""
        # A page can place its own title with <!--head--> (beside its lead figure).
        if "<!--head-->" in content:
            content = content.replace("<!--head-->", head)
        else:
            content = head + "\n" + content
        prev_p = PROJECTS[i - 1] if i > 0 else None
        next_p = PROJECTS[i + 1] if i < n - 1 else None
        nav = '<nav class="next" aria-label="More projects">'
        if prev_p:
            nav += f'<div><span>Previous</span><a href="{prev_p["slug"]}.html">{escape(prev_p["title"])}</a></div>'
        if next_p:
            nav += f'<div class="fwd"><span>Next</span><a href="{next_p["slug"]}.html">{escape(next_p["title"])}</a></div>'
        nav += "</nav>"
        body = f"""<article class="wrap">
{content}
{nav}
</article>"""
        html = page(p["title"], body, 1, p["summary"], p["title"], image=p["thumb"])
        (OUT / "projects" / f"{p['slug']}.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    build_home()
    build_projects()
    (OUT / ".nojekyll").write_text("")
    print(f"Built {len(PROJECTS) + 1} pages into {OUT}")
