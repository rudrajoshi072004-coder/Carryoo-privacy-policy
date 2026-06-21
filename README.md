# Carryoo — Privacy Policy (static HTML)

**100% static HTML** for [Google Play](https://play.google.com/console) privacy policy URL. Deploy on [Railway](https://railway.app/) or [GitHub Pages](https://pages.github.com/).

No JavaScript in the page itself. Railway runs a tiny Python static file server (`server.py`).

## Deploy on Railway (recommended)

1. Push this repo to GitHub (or connect the repo in Railway).
2. [Railway](https://railway.app/) → **New Project** → **Deploy from GitHub repo** → select this repository.
3. Railway auto-detects Python via `requirements.txt` and starts `python server.py` (see `Procfile` / `railway.toml`).
4. After deploy, open **Settings → Networking → Generate Domain** to get a public URL like `https://your-app.up.railway.app`.
5. Paste that URL (or `https://your-app.up.railway.app/privacy-policy.html`) in **Play Console → App content → Privacy policy**.

| Page | URL |
|------|-----|
| Home | `https://<your-railway-domain>/` |
| Same policy | `https://<your-railway-domain>/privacy-policy.html` |

**Local test (same as Railway):**

```bash
python server.py
# Open http://localhost:8080
```

Railway sets the `PORT` environment variable automatically; locally it defaults to `8080`.

## Public URLs (GitHub Pages)

| Page | URL |
|------|-----|
| Home | https://rudrajoshi072004-coder.github.io/Carryoo-privacy-policy/ |
| Same policy | https://rudrajoshi072004-coder.github.io/Carryoo-privacy-policy/privacy-policy.html |

## Deploy on GitHub

1. Push this repo to `main` (already connected to GitHub).
2. Repo → **Settings** → **Pages** → **Source**: **GitHub Actions**.
3. Wait for the **Deploy GitHub Pages** workflow to finish.

## Files that are deployed

| File | Role |
|------|------|
| `index.html` | Main static page (`lang="en"`) |
| `privacy-policy.html` | Same content, alternate URL |
| `server.py` | Static file server for Railway (reads `$PORT`) |
| `Procfile` / `railway.toml` | Railway start command and health check |
| `.nojekyll` | Lets GitHub serve the site as plain static files (Pages only) |

`PRIVACY_POLICY.md` and `build_index.py` are only for editing locally — **GitHub serves the HTML files directly**.

## Edit the policy

1. Change `PRIVACY_POLICY.md` (or edit `index.html` directly).
2. If you edited Markdown, regenerate HTML locally:

```bash
pip install markdown
python build_index.py
```

3. Commit and push `index.html` and `privacy-policy.html`.

## Play Store checklist

- [ ] Replace `[Legal Entity Name]`, address, and Grievance Officer in the HTML or Markdown, then regenerate.
- [ ] Open the live URL on your phone — page must load without login.
- [ ] Paste URL in Play Console.

## Contact

- support@nashikflow.app
- business@nashikflow.app
