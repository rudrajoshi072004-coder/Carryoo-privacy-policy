"""Regenerate static HTML from PRIVACY_POLICY.md — Carryoo privacy policy layout."""
import re
import markdown
from pathlib import Path

md = Path("PRIVACY_POLICY.md").read_text(encoding="utf-8")
body = markdown.markdown(md, extensions=["tables", "fenced_code"])

for email in ("support@nashikflow.app", "business@nashikflow.app"):
    body = body.replace(email, f'<a href="mailto:{email}">{email}</a>')

# Remove duplicate title/dates — shown in page hero / content title
body = re.sub(r"<h1>Privacy Policy</h1>\s*", "", body, count=1)
body = re.sub(
    r"<p><strong>Last updated:</strong>.*?</p>\s*<hr\s*/>\s*",
    "",
    body,
    count=1,
    flags=re.DOTALL,
)


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"^\d+\.\s*", "", text)
    slug = re.sub(r"[^\w\s-]", "", text.lower()).strip().replace(" ", "-")
    return slug or "section"


def add_section_ids(html: str) -> str:
    def repl(m):
        title = m.group(1)
        sid = slugify(title)
        return f'<h2 id="{sid}" class="section-title">{title}</h2>'

    return re.sub(r"<h2>(.*?)</h2>", repl, html)


body = add_section_ids(body)

body = body.replace(
    '<h2 id="account-and-data-deletion-carryoo" class="section-title">2. Account and data deletion (Carryoo)</h2>',
    '<section class="deletion-highlight" id="account-deletion">'
    '<h2 id="account-and-data-deletion-carryoo" class="section-title">2. Account and data deletion (Carryoo)</h2>',
    1,
)
body = body.replace(
    '<h2 id="who-this-policy-applies-to" class="section-title">3. Who This Policy Applies To</h2>',
    "</section>"
    '<h2 id="who-this-policy-applies-to" class="section-title">3. Who This Policy Applies To</h2>',
    1,
)

body = body.replace("<h3>", '<h3 class="subsection-title">')

# Carryoo privacy policy visual system
STATIC_CSS = """
    :root {
      --bg: #f0f3ff;
      --ink: #040a1a;
      --text: #3a3a3a;
      --link: #2962ff;
      --blue: #0a57ff;
      --footer-bg: #0b1220;
      --footer-muted: #bdbdbd;
      --border: #ddd;
      --card-shadow: 0 0 4px 0 rgba(0, 0, 0, 0.5);
      --page-shadow: 0 0 4px 0 rgba(0, 0, 0, 0.54);
    }
    *, *::before, *::after { box-sizing: border-box; }
    html {
      font-size: 62.5%;
      scroll-behavior: smooth;
      -webkit-text-size-adjust: 100%;
    }
    body {
      margin: 0;
      font-family: "Titillium Web", "Segoe UI", system-ui, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }
    a { color: var(--link); text-decoration: none; }
    a:hover { text-decoration: underline; }

    /* Header */
    .site-header {
      background: #fff;
      padding: 1.6rem 4rem;
      box-shadow: 0 0 1.2rem 0.3rem rgba(0, 0, 0, 0.12);
      position: sticky;
      top: 0;
      z-index: 100;
    }
    .site-header__inner {
      max-width: 150rem;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 2rem;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 0.8rem;
      text-decoration: none;
      color: var(--ink);
      font-weight: 700;
      font-size: 2rem;
      letter-spacing: -0.02em;
    }
    .brand:hover { text-decoration: none; }
    .brand-mark {
      width: 3.2rem;
      height: 3.2rem;
      border-radius: 0.6rem;
      background: linear-gradient(135deg, #0a57ff 0%, #00c2a8 100%);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.4rem;
      font-weight: 700;
    }
    .nav-links {
      display: flex;
      align-items: center;
      gap: 2.4rem;
      list-style: none;
      margin: 0;
      padding: 0;
      flex-wrap: wrap;
    }
    .nav-links a {
      color: #000;
      font-size: 1.6rem;
      line-height: 2.4rem;
      font-weight: 600;
    }
    .nav-links a:hover { color: var(--blue); text-decoration: none; }
    .nav-links .active { color: var(--blue); }

    /* Page shell */
    .page-shell {
      background: #fff;
      max-width: 1500px;
      margin: 0 auto;
      box-shadow: var(--page-shadow);
    }

    /* Dark hero banner */
    .hero-banner {
      background-image: linear-gradient(154.48deg, #000, #040a1a);
      min-height: 25rem;
      text-align: center;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .hero-banner h1 {
      color: #fff;
      font-size: clamp(2.8rem, 5vw, 3.6rem);
      line-height: 1.15;
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.04em;
      margin: 0;
      padding: 6rem 2rem;
    }

    /* Overlapping white content card */
    .main-wrap {
      position: relative;
    }
    .policy-card {
      margin: 0 8rem;
      background: #fff;
      box-shadow: var(--card-shadow);
      transform: translateY(-80px);
      border-radius: 0.5rem;
      padding: 4rem;
    }

    .content-title {
      font-weight: 800;
      color: var(--ink);
      font-size: 1.6rem;
      margin: 0 0 1rem;
    }
    .meta-line {
      font-size: 1.3rem;
      color: #818181;
      margin: 0 0 2rem;
    }

    .jump-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 0.8rem;
      margin: 0 0 2.4rem;
      padding-bottom: 1.6rem;
      border-bottom: 1px solid #eee;
    }
    .jump-bar a {
      font-size: 1.2rem;
      font-weight: 600;
      color: var(--blue);
      padding: 0.4rem 1rem;
      border: 1px solid #c5d4ff;
      border-radius: 999px;
      background: #f5f8ff;
      white-space: nowrap;
    }
    .jump-bar a:hover {
      background: var(--blue);
      color: #fff;
      text-decoration: none;
    }

    .legal-body {
      font-size: 1.4rem;
      line-height: 2.4rem;
      color: var(--text);
      text-align: justify;
    }
    .legal-body p {
      margin: 1rem 0;
      line-height: 1.7;
      font-size: 1.4rem;
      text-align: justify;
    }
    .legal-body ul, .legal-body ol {
      margin: 1rem 0;
      padding-left: 2rem;
    }
    .legal-body li {
      margin-bottom: 0.8rem;
      line-height: 1.7;
      font-size: 1.4rem;
    }
    .legal-body strong, .legal-body b {
      font-weight: 600;
      color: #333;
    }
    .legal-body a { color: var(--link); text-decoration: none; }
    .legal-body a:hover { text-decoration: underline; }

    .section-title {
      font-weight: 800;
      color: var(--ink);
      font-size: 1.6rem;
      margin: 2.8rem 0 1rem;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      line-height: 1.4;
    }
    .subsection-title {
      font-size: 1.5rem;
      font-weight: 700;
      color: #333;
      margin: 2rem 0 0.8rem;
    }

    .info-box {
      margin: 1.25rem 0;
      padding: 1.2rem 1.4rem;
      background: #fffbeb;
      border: 1px solid #fde68a;
      border-radius: 0.5rem;
      font-size: 1.3rem;
      color: #92400e;
      text-align: left;
    }
    .info-box p { margin: 0; text-align: left; }

    .deletion-highlight {
      margin: 1.5rem 0;
      padding: 1.5rem 1.5rem 0.5rem;
      border: 2px solid #0d9488;
      border-radius: 0.5rem;
      background: linear-gradient(135deg, #f0fdfa 0%, #ecfdf5 100%);
    }
    .deletion-highlight .section-title { color: #0f766e; margin-top: 0; }

    .table-wrap {
      overflow-x: auto;
      margin: 1.2rem 0 1.6rem;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 0.8rem 0;
      text-align: left;
    }
    th, td {
      padding: 0.8rem;
      border: 0.1rem solid var(--border);
      vertical-align: top;
    }
    th {
      background-color: #f5f5f5;
      color: #2d2f34;
      font-weight: 600;
      font-size: 1.3rem;
      line-height: 2rem;
    }
    td {
      background: #fff;
      font-size: 1.3rem;
      line-height: 2rem;
      font-weight: 400;
    }
    tr:nth-child(even) td { background-color: #f9f9f9; }

    hr {
      border: none;
      border-top: 1px solid #eee;
      margin: 2.4rem 0;
    }

    .contact-card {
      margin-top: 2rem;
      padding: 1.6rem;
      background: #f7f8fc;
      border: 1px solid #e5e7eb;
      border-left: 4px solid var(--blue);
      border-radius: 0.5rem;
      text-align: left;
    }
    .contact-card h3 {
      margin: 0 0 0.8rem;
      font-size: 1.4rem;
      font-weight: 800;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: var(--ink);
    }
    .contact-card p { margin: 0.4rem 0; font-size: 1.4rem; text-align: left; }

    /* Footer */
    .site-footer {
      background: var(--footer-bg);
      color: #fff;
      padding: 4rem 4rem 2.4rem;
    }
    .footer-inner {
      max-width: 1500px;
      margin: 0 auto;
    }
    .footer-brand {
      display: flex;
      align-items: center;
      gap: 0.8rem;
      font-size: 2rem;
      font-weight: 700;
      color: #fff;
      text-decoration: none;
      margin-bottom: 2.4rem;
    }
    .footer-brand:hover { text-decoration: none; color: #fff; }

    /* Footer download app + demo QR */
    .footer-download {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 2.4rem;
      flex-wrap: wrap;
      margin: 0 0 3.2rem;
      padding: 2.4rem;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 1.2rem;
    }
    .footer-download__info h4 {
      margin: 0 0 0.6rem;
      font-size: 1.8rem;
      font-weight: 800;
      color: #fff;
    }
    .footer-download__info p {
      margin: 0 0 1.6rem;
      font-size: 1.35rem;
      color: var(--footer-muted);
      line-height: 1.6;
      max-width: 42rem;
    }
    .footer-download__badges {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
    }
    .store-badge {
      display: inline-flex;
      align-items: center;
      gap: 1rem;
      background: #000;
      border: 1px solid rgba(255, 255, 255, 0.25);
      border-radius: 0.8rem;
      padding: 0.8rem 1.4rem;
      color: #fff;
      text-decoration: none;
      min-width: 15.5rem;
      cursor: pointer;
      font-family: inherit;
    }
    .store-badge:hover { border-color: #fff; color: #fff; text-decoration: none; }
    .store-badge__icon {
      font-size: 2.2rem;
      line-height: 1;
    }
    .store-badge__text {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      line-height: 1.2;
    }
    .store-badge__text small {
      font-size: 1rem;
      opacity: 0.85;
    }
    .store-badge__text strong {
      font-size: 1.45rem;
      font-weight: 700;
    }
    .footer-download__qr {
      text-align: center;
      flex-shrink: 0;
    }
    .footer-download__qr img {
      width: 12.5rem;
      height: 12.5rem;
      background: #fff;
      border-radius: 0.8rem;
      padding: 0.6rem;
      margin: 0 auto 0.8rem;
    }
    .footer-download__qr span {
      display: block;
      font-size: 1.2rem;
      color: var(--footer-muted);
      font-weight: 600;
    }
    .footer-download__qr .demo-pill {
      display: inline-block;
      margin-top: 0.5rem;
      padding: 0.2rem 0.7rem;
      border-radius: 999px;
      background: rgba(10, 87, 255, 0.35);
      color: #c5d4ff;
      font-size: 1.05rem;
      font-weight: 700;
    }

    .footer-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 4rem;
      margin-bottom: 3rem;
    }
    .footer-col h4 {
      margin: 0 0 1.2rem;
      font-size: 1.6rem;
      font-weight: 700;
      line-height: 140%;
      color: #fff;
    }
    .footer-col ul {
      list-style: none;
      margin: 0;
      padding: 0;
    }
    .footer-col li { margin-bottom: 0.8rem; }
    .footer-col a {
      color: #fff;
      font-size: 1.4rem;
      text-decoration: none;
    }
    .footer-col a:hover { color: #c5d4ff; text-decoration: none; }
    .footer-legal {
      border-top: 1px solid rgba(255, 255, 255, 0.12);
      padding-top: 2rem;
      color: var(--footer-muted);
      font-size: 1.3rem;
      line-height: 1.7;
    }
    .footer-legal h5 {
      margin: 0 0 0.8rem;
      color: #fff;
      font-size: 1.4rem;
      font-weight: 700;
    }
    .footer-legal p { margin: 0 0 0.6rem; }
    .footer-legal a { color: #c5d4ff; }

    /* Install Carryoo — sticky top banner (demo) */
    .install-banner {
      background: #0b1220;
      color: #fff;
      padding: 1rem 2rem;
      position: sticky;
      top: 0;
      z-index: 120;
    }
    .install-banner__inner {
      max-width: 1500px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.6rem;
      flex-wrap: wrap;
    }
    .install-banner__left {
      display: flex;
      align-items: center;
      gap: 1.2rem;
      min-width: 0;
    }
    .install-banner__icon {
      width: 4rem;
      height: 4rem;
      border-radius: 0.9rem;
      flex-shrink: 0;
    }
    .install-banner__copy strong {
      display: block;
      font-size: 1.5rem;
      font-weight: 700;
      line-height: 1.3;
    }
    .install-banner__copy span {
      display: block;
      font-size: 1.25rem;
      color: #94a3b8;
      margin-top: 0.2rem;
    }
    .install-banner__actions {
      display: flex;
      align-items: center;
      gap: 1rem;
    }
    .btn-open-app {
      background: var(--blue);
      color: #fff;
      border: none;
      border-radius: 0.5rem;
      padding: 0.9rem 1.8rem;
      font-size: 1.4rem;
      font-weight: 700;
      cursor: pointer;
      font-family: inherit;
      text-decoration: none;
      display: inline-block;
    }
    .btn-open-app:hover { background: #0846d6; color: #fff; text-decoration: none; }
    .install-banner__close {
      background: transparent;
      border: none;
      color: #94a3b8;
      font-size: 2rem;
      line-height: 1;
      cursor: pointer;
      padding: 0.4rem 0.6rem;
    }
    .install-banner__close:hover { color: #fff; }
    .install-banner[hidden] { display: none !important; }

    /* Mid-page download card */
    .download-card {
      margin: 3.2rem 0 1rem;
      padding: 2.4rem;
      border-radius: 1.2rem;
      background: linear-gradient(135deg, #0a1a4a 0%, #0a57ff 100%);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 2rem;
      flex-wrap: wrap;
      text-align: left;
    }
    .download-card h3 {
      margin: 0 0 0.6rem;
      font-size: 1.8rem;
      font-weight: 800;
      color: #fff;
      text-transform: none;
      letter-spacing: 0;
    }
    .download-card p {
      margin: 0;
      font-size: 1.4rem;
      color: #dbe4ff;
      text-align: left;
      line-height: 1.6;
    }
    .download-card .btn-open-app {
      background: #fff;
      color: var(--blue);
      white-space: nowrap;
    }
    .download-card .btn-open-app:hover { background: #eef2ff; color: var(--blue); }
    .demo-badge {
      display: inline-block;
      margin-left: 0.6rem;
      padding: 0.2rem 0.7rem;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.18);
      color: #fff;
      font-size: 1.1rem;
      font-weight: 700;
      vertical-align: middle;
    }

    /* Demo modal */
    .demo-modal {
      position: fixed;
      inset: 0;
      z-index: 200;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 2rem;
    }
    .demo-modal.is-open { display: flex; }
    .demo-modal__backdrop {
      position: absolute;
      inset: 0;
      background: rgba(4, 10, 26, 0.55);
    }
    .demo-modal__panel {
      position: relative;
      background: #fff;
      border-radius: 1.2rem;
      max-width: 42rem;
      width: 100%;
      padding: 2.8rem 2.4rem 2.4rem;
      box-shadow: 0 1.6rem 4rem rgba(0, 0, 0, 0.25);
      text-align: center;
    }
    .demo-modal__panel img {
      width: 6.4rem;
      height: 6.4rem;
      margin: 0 auto 1.6rem;
      border-radius: 1.4rem;
    }
    .demo-modal__panel h3 {
      margin: 0 0 0.8rem;
      font-size: 2rem;
      color: var(--ink);
      font-weight: 800;
    }
    .demo-modal__panel p {
      margin: 0 0 2rem;
      font-size: 1.45rem;
      color: #5a5a5a;
      line-height: 1.6;
      text-align: center;
    }
    .demo-modal__actions {
      display: flex;
      gap: 1rem;
      justify-content: center;
      flex-wrap: wrap;
    }
    .btn-secondary {
      background: #eef2ff;
      color: var(--blue);
      border: none;
      border-radius: 0.5rem;
      padding: 0.9rem 1.6rem;
      font-size: 1.4rem;
      font-weight: 700;
      cursor: pointer;
      font-family: inherit;
      text-decoration: none;
      display: inline-block;
    }
    .btn-secondary:hover { background: #dbe4ff; text-decoration: none; }

    body.has-install-banner .site-header { top: 6.2rem; }

    @media (max-width: 900px) {
      .site-header { padding: 1.2rem 2rem; }
      .nav-links { gap: 1.4rem; }
      .nav-links a { font-size: 1.4rem; }
      .policy-card {
        margin: 1.5rem;
        padding: 2.4rem 1.6rem;
        transform: translateY(-48px);
      }
      .footer-grid { grid-template-columns: repeat(2, 1fr); gap: 2.4rem; }
      .site-footer { padding: 3rem 2rem 2rem; }
      .install-banner { padding: 1rem 1.6rem; }
      .download-card { padding: 2rem; }
      .footer-download { padding: 2rem; }
    }
    @media (max-width: 560px) {
      .nav-links { display: none; }
      .footer-grid { grid-template-columns: 1fr 1fr; }
      .hero-banner { min-height: 18rem; }
      .hero-banner h1 { padding: 4rem 1.5rem; }
      .install-banner__copy span { display: none; }
      body.has-install-banner .site-header { top: 5.6rem; }
      .footer-download { justify-content: center; text-align: center; }
      .footer-download__info p { margin-left: auto; margin-right: auto; }
      .footer-download__badges { justify-content: center; }
    }
"""

JUMP_LINKS = [
    ("Introduction", "introduction"),
    ("Account deletion", "account-deletion"),
    ("What we collect", "personal-data-we-collect"),
    ("How we use data", "how-we-use-your-personal-data"),
    ("Sharing & disclosure", "how-we-share-personal-data"),
    ("Your rights", "your-rights-and-choices"),
    ("Grievance Officer", "grievance-officer-and-contact"),
    ("Cookies", "cookies-and-similar-technologies-web"),
]


def wrap_html(body: str) -> str:
    jump_html = "".join(
        f'<a href="#{anchor}">{label}</a>' for label, anchor in JUMP_LINKS
    )
    download_card = """
        <aside class="download-card" aria-label="Install Carryoo app">
          <div>
            <h3>We are better on the app! <span class="demo-badge">Demo</span></h3>
            <p>Install Carryoo for faster bookings, live trip tracking, and driver partner tools. Play Store listing coming soon — this is a demo prompt for now.</p>
          </div>
          <button type="button" class="btn-open-app js-open-app">Install Carryoo</button>
        </aside>
"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="Content-Language" content="en">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Privacy Policy for Carryoo — logistics and on-demand delivery platform for customers and driver partners. Google Play compliant.">
  <meta name="robots" content="index, follow">
  <title>Privacy Policy | Carryoo</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Titillium+Web:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>{STATIC_CSS}</style>
</head>
<body class="has-install-banner">
  <div class="install-banner" id="installBanner" role="region" aria-label="Install Carryoo">
    <div class="install-banner__inner">
      <div class="install-banner__left">
        <img class="install-banner__icon" src="assets/app-icon.svg" alt="" width="40" height="40">
        <div class="install-banner__copy">
          <strong>Install Carryoo</strong>
          <span>for efficient goods transportation</span>
        </div>
      </div>
      <div class="install-banner__actions">
        <button type="button" class="btn-open-app js-open-app">OPEN APP</button>
        <button type="button" class="install-banner__close" id="closeInstallBanner" aria-label="Dismiss install banner">&times;</button>
      </div>
    </div>
  </div>

  <header class="site-header">
    <div class="site-header__inner">
      <a class="brand" href="index.html">
        <span class="brand-mark" aria-hidden="true">C</span>
        Carryoo
      </a>
      <ul class="nav-links">
        <li><a href="enterprise.html">For Enterprise</a></li>
        <li><a href="driver-partner.html">Driver Partner</a></li>
        <li><a href="support.html">Support</a></li>
        <li><a href="index.html" class="active">Privacy Policy</a></li>
      </ul>
    </div>
  </header>

  <div class="page-shell">
    <div class="hero-banner">
      <h1>Privacy Policy</h1>
    </div>

    <div class="main-wrap">
      <article class="policy-card legal-body" lang="en">
        <p class="content-title">Privacy Policy</p>
        <p class="meta-line">Last updated: 29 May 2026 &nbsp;|&nbsp; Effective: 29 May 2026</p>
        <nav class="jump-bar" aria-label="Quick section links">{jump_html}</nav>
{body}
{download_card}
      </article>
    </div>
  </div>

  <footer class="site-footer">
    <div class="footer-inner">
      <a class="footer-brand" href="index.html">
        <span class="brand-mark" aria-hidden="true">C</span>
        Carryoo
      </a>

      <div class="footer-download">
        <div class="footer-download__info">
          <h4>Download our app</h4>
          <p>Scan the demo QR or tap a store button. Play Store / App Store links will go live when Carryoo is published — this is a demo for now.</p>
          <div class="footer-download__badges">
            <button type="button" class="store-badge js-open-app" aria-label="Get it on Google Play (demo)">
              <span class="store-badge__icon" aria-hidden="true">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M3 20.5v-17c0-.8.9-1.3 1.5-.9l14.2 8.5c.7.4.7 1.4 0 1.8L4.5 21.4c-.6.4-1.5-.1-1.5-.9z"/></svg>
              </span>
              <span class="store-badge__text">
                <small>GET IT ON</small>
                <strong>Google Play</strong>
              </span>
            </button>
            <button type="button" class="store-badge js-open-app" aria-label="Download on the App Store (demo)">
              <span class="store-badge__icon" aria-hidden="true">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M16.4 12.3c0-2.1 1.7-3.1 1.8-3.2-1-1.4-2.5-1.6-3-1.7-1.3-.1-2.5.8-3.1.8-.7 0-1.7-.7-2.8-.7-1.4 0-2.8.9-3.5 2.2-1.5 2.6-.4 6.5 1.1 8.6.7 1 1.6 2.2 2.7 2.1 1.1 0 1.5-.7 2.8-.7s1.6.7 2.8.7c1.2 0 1.9-1 2.6-2 .8-1.2 1.1-2.3 1.1-2.4-.1 0-2.2-.8-2.2-3.7zm-2-6.2c.6-.7 1-1.7.9-2.7-1 .1-2.1.6-2.7 1.4-.6.7-1.1 1.7-.9 2.7 1 0 2-.6 2.7-1.4z"/></svg>
              </span>
              <span class="store-badge__text">
                <small>Download on the</small>
                <strong>App Store</strong>
              </span>
            </button>
          </div>
        </div>
        <div class="footer-download__qr">
          <img src="assets/qr-demo.svg" alt="Demo QR code to download Carryoo" width="146" height="146">
          <span>Scan to download</span>
          <span class="demo-pill">Demo QR</span>
        </div>
      </div>

      <div class="footer-grid">
        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="#">About Carryoo</a></li>
            <li><a href="#">Careers</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="enterprise.html#vehicles">Two Wheelers</a></li>
            <li><a href="enterprise.html#vehicles">Trucks</a></li>
            <li><a href="enterprise.html">Carryoo Business</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Support</h4>
          <ul>
            <li><a href="mailto:support@nashikflow.app">Contact Us</a></li>
            <li><a href="privacy-policy.html">Privacy Policy</a></li>
            <li><a href="#account-deletion">Account Deletion</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Contact</h4>
          <ul>
            <li><a href="mailto:support@nashikflow.app">support@nashikflow.app</a></li>
            <li><a href="mailto:business@nashikflow.app">business@nashikflow.app</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-legal">
        <h5>Registered Office:</h5>
        <p>&copy; 2026 Carryoo / [Legal Entity Name]. [Registered Office Address, Nashik, Maharashtra, India]</p>
        <p>Email: <a href="mailto:support@nashikflow.app">support@nashikflow.app</a></p>
        <p>Privacy policy for Google Play Store and web.</p>
      </div>
    </div>
  </footer>

  <div class="demo-modal" id="demoModal" aria-hidden="true">
    <div class="demo-modal__backdrop" data-close-modal></div>
    <div class="demo-modal__panel" role="dialog" aria-modal="true" aria-labelledby="demoModalTitle">
      <img src="assets/app-icon.svg" alt="" width="64" height="64">
      <h3 id="demoModalTitle">Carryoo app — coming soon</h3>
      <p>This is a demo install prompt. The Carryoo app is not on the Play Store yet. Leave your email with support and we will notify you when downloads go live.</p>
      <div class="demo-modal__actions">
        <a class="btn-open-app" href="mailto:support@nashikflow.app?subject=Notify%20me%20when%20Carryoo%20app%20launches">Notify me</a>
        <button type="button" class="btn-secondary" data-close-modal>Close</button>
      </div>
    </div>
  </div>

  <script>
    (function () {{
      var banner = document.getElementById("installBanner");
      var closeBtn = document.getElementById("closeInstallBanner");
      var modal = document.getElementById("demoModal");
      if (sessionStorage.getItem("carryooInstallBannerDismissed") === "1" && banner) {{
        banner.hidden = true;
        document.body.classList.remove("has-install-banner");
      }}
      if (closeBtn && banner) {{
        closeBtn.addEventListener("click", function () {{
          banner.hidden = true;
          document.body.classList.remove("has-install-banner");
          sessionStorage.setItem("carryooInstallBannerDismissed", "1");
        }});
      }}
      function openModal() {{
        if (!modal) return;
        modal.classList.add("is-open");
        modal.setAttribute("aria-hidden", "false");
      }}
      function closeModal() {{
        if (!modal) return;
        modal.classList.remove("is-open");
        modal.setAttribute("aria-hidden", "true");
      }}
      document.querySelectorAll(".js-open-app").forEach(function (btn) {{
        btn.addEventListener("click", openModal);
      }});
      document.querySelectorAll("[data-close-modal]").forEach(function (el) {{
        el.addEventListener("click", closeModal);
      }});
      document.addEventListener("keydown", function (e) {{
        if (e.key === "Escape") closeModal();
      }});
    }})();
  </script>
</body>
</html>
"""


# Post-process: wrap tables, style blockquotes as info boxes
body = body.replace("<blockquote>", '<div class="info-box">').replace("</blockquote>", "</div>")
body = re.sub(r"(<table>)", r'<div class="table-wrap">\1', body)
body = re.sub(r"(</table>)", r"\1</div>", body)

html = wrap_html(body)
Path("index.html").write_text(html, encoding="utf-8")
Path("privacy-policy.html").write_text(html, encoding="utf-8")
print(f"Wrote index.html and privacy-policy.html ({len(html)} bytes each)")
