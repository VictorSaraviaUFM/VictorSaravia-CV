# Victor Saravia | Portfolio

Static site (HTML/CSS/JS, no build step). Content lives in `data.js`.

## 1. Local preview
```bash
python3 -m http.server 8000   # then open http://localhost:8000
```
(Open it through a server, not by double-clicking, so the photo and scripts load consistently.)

## 2. Replace the photo
Save your photo as `assets/profile.jpg` (square, at least 600x600, JPG). Until the file exists the page shows a "Photo" placeholder. For the PDF, set `PHOTO` in `build_resume.py` to the same file and re-run it.

## 3. Replace the PDF
Overwrite `assets/resume.pdf` keeping the same name, or edit `build_resume.py` and run `python3 build_resume.py`.

## 4. Add a project
In `data.js`, copy an object inside `projects` and edit it. Use `status: "Private Academic Project"` with `repo: ""` and a `repoNote` for private repos. Keep 2-3 highlights and a few technologies.

## 5. Add a certification
In `data.js`, add `{ name, issuer, date, link }` to `certifications`. Leave `link: ""` to show a placeholder.

## 6. Deploy on Vercel
Push to GitHub, go to vercel.com > Add New Project > import the repo. Framework preset: "Other". No build command, output directory `./`. Deploy.

## 7. Deploy on GitHub Pages
Push to GitHub, then Settings > Pages > Source: "Deploy from a branch", branch `main`, folder `/ (root)`. The site appears at `https://<user>.github.io/<repo>/`.
