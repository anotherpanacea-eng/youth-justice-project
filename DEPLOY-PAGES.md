# GitHub Pages deployment (active)

Push to `main` → GitHub Actions builds with Hugo and publishes to Pages.
Workflow: `.github/workflows/pages.yml`. No SSH key, no secrets.

## One-time setup

1. **Push the repo** to `github.com/anotherpanacea-eng/youth-justice-project`
   (public, so Pages is free).

2. **Turn on Pages with Actions:** repo → Settings → Pages → Build and deployment →
   Source = **GitHub Actions**. (You do NOT pick a branch; the workflow handles it.)

3. **Push to `main`.** Watch the run in the Actions tab. When it's green, the site
   is live at:

   `https://anotherpanacea-eng.github.io/youth-justice-project/`

   (Relative links in the templates work fine under that subpath.)

## Editing from now on
Edit files (add testimony to `data/policy.yaml`, etc.) in Claude Code, commit,
push. The Action rebuilds and redeploys automatically.

## Moving youthjusticeproject.org onto Pages (when you're ready)

Right now the domain still points at Dreamhost. To serve it from Pages instead:

1. Add a file `static/CNAME` containing one line: `youthjusticeproject.org`
   (Hugo copies it into the build so the custom domain sticks on every deploy.)
2. repo → Settings → Pages → Custom domain → enter `youthjusticeproject.org`, save,
   and let GitHub verify it.
3. In **Dreamhost DNS**, point the domain at GitHub Pages. For the apex domain,
   that's A records to GitHub's Pages IPs:
   `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   (and the `www` host as a CNAME to `anotherpanacea-eng.github.io` if you use www).
4. In the Dreamhost panel, set the domain's web hosting to **DNS only** so Dreamhost
   stops trying to serve it. Your Dreamhost **email is unaffected** — that's the MX
   records, which you leave alone.
5. Tick **Enforce HTTPS** in Settings → Pages once the cert is issued.

Until you do this, the Dreamhost-hosted site stays live and Pages serves the
`github.io` URL in parallel — handy for previewing before you cut over.

## The other workflow
`deploy.yml` (Dreamhost rsync) is now **manual-only** — it won't run on push. It's
there as a fallback if you ever want to push back to Dreamhost; it needs the
`DREAMHOST_SSH_KEY` secret (see DEPLOY-GITHUB.md).
