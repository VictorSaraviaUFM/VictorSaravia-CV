# Victor Saravia — Portfolio

Plain HTML/CSS/JS, no build step, no framework (a single content-driven page doesn't need one).
Content lives in `content.js`; `script.js` renders it; `styles.css` holds the dark/light themes.

```
index.html   semantic structure + SEO/Open Graph metadata
content.js   ALL content: profile, projects, skills, education, certificates, interests
script.js    renders content, theme toggle (localStorage + prefers-color-scheme)
styles.css   design tokens for dark and light themes (top of file)
assets/      profile.jpg (your photo), resume.pdf, favicon.svg
scripts/build_cv.py   regenerates assets/resume.pdf (ATS-friendly text PDF with photo)
```

## 1. Local preview
Open `index.html` in a browser, or run `python -m http.server 8000` and visit http://localhost:8000

## 2. Replace the photo
Save your photo as `assets/profile.jpg` (square or portrait, face centered, ≥ 600 px; no filters). Until it exists the page shows a "VS" badge. Re-run the PDF script (below) so the PDF gets the same photo.

## 3. Replace / rebuild the PDF
`pip install reportlab pillow && python scripts/build_cv.py` → writes `assets/resume.pdf`.
Edit the text in that script, or overwrite `assets/resume.pdf` with your own file (keep the name). After deploying, set `PORTFOLIO_URL` in the script and rebuild to add a Portfolio link.

## 4. Add a project
In `content.js`, copy a block inside `projects` and edit it: `name, type, area, status` ("Public" or "Private Academic Project"), `team, summary, flow` (3 architecture steps), `highlights` (2–3), `tags`, `repo` (leave `""` for private repos and use `note`). Optional: add real screenshots later.

## 5. Add a certificate
In `content.js` → `certifications`, add `{ name, issuer, date, link }`. Empty `link` shows `[CREDENTIAL LINK]`; fill `[ISSUER]` and `[DATE]`.

## Skills / experience
Skills: edit `skills` in `content.js`. Experience: add an `experience` array in `content.js` and a matching render block + section in `index.html`/`script.js` (copy the Education pattern).

## 6. Deploy on Vercel
Push to GitHub → vercel.com → Add New → Project → import repo → Framework Preset "Other" → Deploy. Free tier is enough.

## 7. Deploy on GitHub Pages
Repo → Settings → Pages → Source: "Deploy from a branch" → `main` / `/ (root)` → Save.

## Before publishing
- Confirm `https://github.com/VictorSaraviaUFM` is your public profile.
- Add the real tech stack for the football project; fill certificate issuers/dates/links.
- Solar Pulso is private: do not link it. Publish a separate, authorized, recreated repo only if your course and teammates allow it (never fork-and-make-public).
- Add `og:url` / `og:image` after deploying.
