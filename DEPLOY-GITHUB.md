# GitHub -> Dreamhost automated deployment

Push to `main`, and GitHub Actions builds the site with Hugo and rsyncs it to
Dreamhost. The workflow is in `.github/workflows/deploy.yml`.

## One-time setup

### 1. Put this project in a GitHub repo
Create a repo (private is fine — the built site is public regardless), then from
the `YJP-Hugo` folder:

```bash
git init
git add .
git commit -m "Initial Hugo site"
git branch -M main
git remote add origin git@github.com:<owner>/<repo>.git
git push -u origin main
```

### 2. Make a dedicated deploy key
A separate key just for deployment (don't reuse your personal one):

```bash
ssh-keygen -t ed25519 -f ~/.ssh/yjp_deploy -N "" -C "yjp-github-deploy"
```

This creates `~/.ssh/yjp_deploy` (private) and `~/.ssh/yjp_deploy.pub` (public).

### 3. Put the PUBLIC key on Dreamhost
So the Action can log in:

```bash
ssh-copy-id -i ~/.ssh/yjp_deploy.pub dh_cj98j5@iad1-shared-e1-19.dreamhost.com
```

(The user needs the shell/SSH toggle enabled in the panel first.)

### 4. Put the PRIVATE key in GitHub as a secret
In the repo: Settings -> Secrets and variables -> Actions -> New repository secret.

- Name: `DREAMHOST_SSH_KEY`
- Value: the full contents of `~/.ssh/yjp_deploy` (the private file, including the
  `-----BEGIN...` and `-----END...` lines)

GitHub encrypts it; the workflow is the only thing that can read it, at run time.

### 5. Push
Any push to `main` now builds and deploys. Watch it under the repo's Actions tab.
You can also trigger a deploy by hand there (the "Run workflow" button).

## Editing from now on
Edit files (add testimony to `data/policy.yaml`, etc.), commit, push. Done.
Nothing to build or upload locally.

## Notes
- `DH_HOST` / `DH_PATH` / `DH_USER` are plain config at the top of the workflow.
  Only the private key is secret.
- Shared-hosting hostnames can change if Dreamhost migrates the account. If deploys
  suddenly fail to connect, update `DH_HOST` in the workflow to the new server.
