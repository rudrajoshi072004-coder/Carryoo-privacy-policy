"""Optional: regenerate static HTML from PRIVACY_POLICY.md. GitHub deploys index.html as-is."""
import markdown
from pathlib import Path

md = Path("PRIVACY_POLICY.md").read_text(encoding="utf-8")
body = markdown.markdown(md, extensions=["tables", "fenced_code"])

for email in ("support@nashikflow.app", "business@nashikflow.app"):
    body = body.replace(email, f'<a href="mailto:{email}">{email}</a>')

body = body.replace(
    "<h2>2. Account and data deletion (Carryoo)</h2>",
    '<section class="deletion-highlight" id="account-deletion">'
    "<h2>2. Account and data deletion (Carryoo)</h2>",
    1,
)
body = body.replace(
    "<h2>3. Who This Policy Applies To</h2>",
    "</section><h2>3. Who This Policy Applies To</h2>",
    1,
)

STATIC_CSS = """
    :root {
      color-scheme: light dark;
      --bg: #f8fafc;
      --fg: #0f172a;
      --muted: #475569;
      --accent: #0d9488;
      --card: #ffffff;
      --border: #e2e8f0;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --bg: #0f172a;
        --fg: #f1f5f9;
        --muted: #94a3b8;
        --card: #1e293b;
        --border: #334155;
      }
    }
    *, *::before, *::after { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      background: var(--bg);
      color: var(--fg);
      line-height: 1.65;
    }
    .site-header {
      background: linear-gradient(135deg, #0d9488 0%, #0f766e 100%);
      color: #fff;
      padding: 2rem 1.25rem;
      text-align: center;
    }
    .site-header h1 { margin: 0 0 0.25rem; font-size: 1.75rem; font-weight: 700; }
    .site-header p { margin: 0; opacity: 0.92; font-size: 0.95rem; }
    .site-header .dates { margin-top: 0.75rem; font-size: 0.85rem; opacity: 0.9; }
    .site-header .nav { margin-top: 1rem; }
    .site-header .nav a {
      color: #fff;
      font-weight: 600;
      text-decoration: underline;
      text-underline-offset: 3px;
    }
    .deletion-highlight {
      margin: 0 -0.25rem 1.5rem;
      padding: 1rem 1rem 0.25rem;
      border: 2px solid var(--accent);
      border-radius: 10px;
      background: color-mix(in srgb, var(--accent) 8%, var(--card));
    }
    .deletion-highlight h2 {
      margin-top: 0;
      padding-top: 0;
      border-top: none;
      font-size: 1.2rem;
    }
    .deletion-highlight h3 { color: var(--fg); }
    main { max-width: 48rem; margin: 0 auto; padding: 1.5rem 1.25rem 3rem; }
    article {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.5rem 1.25rem;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
    }
    article h1 { font-size: 1.35rem; margin-top: 0; }
    article h2 {
      font-size: 1.12rem;
      margin-top: 2rem;
      padding-top: 0.75rem;
      border-top: 1px solid var(--border);
      color: var(--accent);
    }
    article h3 { font-size: 1rem; margin-top: 1.25rem; }
    article ul { padding-left: 1.25rem; }
    article blockquote {
      margin: 1rem 0;
      padding: 0.75rem 1rem;
      border-left: 4px solid var(--accent);
      background: var(--bg);
      color: var(--muted);
      font-size: 0.9rem;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
      margin: 1rem 0;
      display: block;
      overflow-x: auto;
    }
    th, td {
      border: 1px solid var(--border);
      padding: 0.5rem 0.65rem;
      text-align: left;
      vertical-align: top;
    }
    th { background: var(--bg); font-weight: 600; }
    hr { border: none; border-top: 1px solid var(--border); margin: 1.5rem 0; }
    a { color: var(--accent); }
    .site-footer {
      text-align: center;
      padding: 1rem 1.25rem 2rem;
      font-size: 0.85rem;
      color: var(--muted);
    }
"""

def wrap_html(body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="Content-Language" content="en">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Privacy Policy for Carryoo — logistics and on-demand delivery. Static page for Google Play Store.">
  <meta name="robots" content="index, follow">
  <title>Carryoo — Privacy Policy</title>
  <style>{STATIC_CSS}</style>
</head>
<body>
  <header class="site-header">
    <h1>Carryoo</h1>
    <p>Privacy Policy</p>
    <p class="dates">Last updated: 29 May 2026 · Effective: 29 May 2026</p>
    <p class="nav"><a href="#account-deletion">Account &amp; data deletion (Google Play)</a></p>
  </header>
  <main>
    <article lang="en">
{body}
    </article>
  </main>
  <footer class="site-footer">
    <p>&copy; Carryoo. Static privacy policy for Google Play Store.</p>
    <p><a href="mailto:support@nashikflow.app">support@nashikflow.app</a></p>
  </footer>
</body>
</html>
"""

html = wrap_html(body)
Path("index.html").write_text(html, encoding="utf-8")
Path("privacy-policy.html").write_text(html, encoding="utf-8")
print(f"Wrote index.html and privacy-policy.html ({len(html)} bytes each)")
