"""Generate index.html from PRIVACY_POLICY.md for GitHub Pages."""
import markdown
from pathlib import Path

md = Path("PRIVACY_POLICY.md").read_text(encoding="utf-8")
body = markdown.markdown(md, extensions=["tables", "fenced_code"])

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Privacy Policy for Carryoo — logistics and on-demand delivery platform.">
  <title>Carryoo — Privacy Policy</title>
  <style>
    :root {{ color-scheme: light dark; --bg: #f8fafc; --fg: #0f172a; --muted: #475569; --accent: #0d9488; --card: #fff; --border: #e2e8f0; }}
    @media (prefers-color-scheme: dark) {{
      :root {{ --bg: #0f172a; --fg: #f1f5f9; --muted: #94a3b8; --card: #1e293b; --border: #334155; }}
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; background: var(--bg); color: var(--fg); line-height: 1.65; }}
    header {{ background: linear-gradient(135deg, #0d9488 0%, #0f766e 100%); color: #fff; padding: 2rem 1.25rem; text-align: center; }}
    header h1 {{ margin: 0 0 0.25rem; font-size: 1.75rem; font-weight: 700; }}
    header p {{ margin: 0; opacity: 0.9; font-size: 0.95rem; }}
    main {{ max-width: 48rem; margin: 0 auto; padding: 1.5rem 1.25rem 3rem; }}
    article {{ background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 1.5rem 1.25rem; box-shadow: 0 1px 3px rgba(0,0,0,.06); }}
    article h1 {{ font-size: 1.35rem; margin-top: 0; }}
    article h2 {{ font-size: 1.15rem; margin-top: 2rem; padding-top: 0.5rem; border-top: 1px solid var(--border); color: var(--accent); }}
    article h3 {{ font-size: 1rem; margin-top: 1.25rem; }}
    article blockquote {{ margin: 1rem 0; padding: 0.75rem 1rem; border-left: 4px solid var(--accent); background: var(--bg); color: var(--muted); font-size: 0.9rem; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 0.85rem; margin: 1rem 0; display: block; overflow-x: auto; }}
    th, td {{ border: 1px solid var(--border); padding: 0.5rem 0.6rem; text-align: left; }}
    th {{ background: var(--bg); font-weight: 600; }}
    hr {{ border: none; border-top: 1px solid var(--border); margin: 1.5rem 0; }}
    footer {{ text-align: center; padding: 1rem; font-size: 0.85rem; color: var(--muted); }}
    a {{ color: var(--accent); }}
  </style>
</head>
<body>
  <header>
    <h1>Carryoo</h1>
    <p>Privacy Policy</p>
  </header>
  <main>
    <article>
{body}
    </article>
  </main>
  <footer>
    <p>&copy; Carryoo. Hosted for Google Play Store compliance.</p>
  </footer>
</body>
</html>"""

Path("index.html").write_text(html, encoding="utf-8")
print(f"Wrote index.html ({len(html)} bytes)")
