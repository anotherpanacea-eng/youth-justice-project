#!/usr/bin/env bash
# Build the site and push it to Dreamhost over SSH.
# Prereqs: Hugo installed, SSH key added to Dreamhost (ssh-copy-id), rsync available.
set -euo pipefail

USER="dh_cj98j5"
HOST="iad1-shared-e1-19.dreamhost.com"
# The web directory Dreamhost serves this domain from. Confirm in the panel
# (Websites -> Manage; it's usually ~/<domain>/). Trailing slash matters.
REMOTE="~/youthjusticeproject.org/"

echo "Building with Hugo..."
hugo --cleanDestinationDir

echo "Deploying public/ -> ${USER}@${HOST}:${REMOTE}"
# --delete makes the server mirror public/ exactly (removes files no longer built).
# Drop --delete on the first run if you want to be cautious.
rsync -avz --delete public/ "${USER}@${HOST}:${REMOTE}"
echo "Done."
