# Carryoo — Privacy Policy (GitHub Pages)

Public privacy policy for the **Carryoo** mobile apps, hosted on GitHub Pages for [Google Play](https://play.google.com/console) compliance.

## Live URL (after deployment)

Once GitHub Pages is enabled, use this URL in Play Console → **App content** → **Privacy policy**:

**https://rudrajoshi072004-coder.github.io/Carryoo-privacy-policy/**

## Repository

https://github.com/rudrajoshi072004-coder/Carryoo-privacy-policy

## Files

| File | Description |
|------|-------------|
| [`index.html`](./index.html) | Play Store–ready public page (static HTML) |
| [`PRIVACY_POLICY.md`](./PRIVACY_POLICY.md) | Source policy (Markdown) |
| [`.github/workflows/pages.yml`](./.github/workflows/pages.yml) | Auto-deploy on push to `main` |

## Enable GitHub Pages (one-time)

1. Open the repo on GitHub → **Settings** → **Pages**
2. Under **Build and deployment**, set **Source** to **GitHub Actions**
3. Push to `main` — the workflow deploys the site automatically

## Regenerate `index.html`

After editing `PRIVACY_POLICY.md`:

```bash
pip install markdown
python build_index.py
git add index.html PRIVACY_POLICY.md
git commit -m "Update privacy policy"
git push
```

## Before Play Store submission

1. Replace placeholders in `PRIVACY_POLICY.md` (`[Legal Entity Name]`, address, Grievance Officer), then run `build_index.py`
2. Confirm the live URL loads in a mobile browser
3. Paste the URL in Play Console

## Contact

- Support: support@nashikflow.app
- Business: business@nashikflow.app
