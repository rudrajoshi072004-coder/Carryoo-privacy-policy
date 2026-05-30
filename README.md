# Carryoo — Privacy Policy (static HTML)

**100% static HTML** for [GitHub Pages](https://pages.github.com/) and [Google Play](https://play.google.com/console) privacy policy URL.

No JavaScript. No build step on GitHub — only upload and serve HTML.

## Public URLs (after Pages is enabled)

| Page | URL |
|------|-----|
| Home | https://rudrajoshi072004-coder.github.io/Carryoo-privacy-policy/ |
| Same policy | https://rudrajoshi072004-coder.github.io/Carryoo-privacy-policy/privacy-policy.html |

Use either URL in **Play Console → App content → Privacy policy**.

## Deploy on GitHub

1. Push this repo to `main` (already connected to GitHub).
2. Repo → **Settings** → **Pages** → **Source**: **GitHub Actions**.
3. Wait for the **Deploy GitHub Pages** workflow to finish.

## Files that are deployed

| File | Role |
|------|------|
| `index.html` | Main static page (`lang="en"`) |
| `privacy-policy.html` | Same content, alternate URL |
| `.nojekyll` | Lets GitHub serve the site as plain static files |

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
