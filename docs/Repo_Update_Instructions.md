# Repo Update Instructions

These commands assume your Git remote is set to `origin` and you have access to `https://github.com/nastradam/DIY-Dillon1050-Autodrive`.

```bash
# 1) Get the latest
git pull --rebase origin main

# 2) Create a release branch
git checkout -b release/v0.1.0

# 3) Copy new files from the update pack into your repo working directory, then stage
git add .
git commit -m "chore(release): bootstrap repo v0.1.0 with docs, BOM, and code skeleton"

# 4) Merge to main
git checkout main
git merge --no-ff release/v0.1.0 -m "merge: release v0.1.0"

# 5) Tag & push
git tag v0.1.0
git push origin main --tags
```

> If you previously saw `rejected (fetch first)`: run `git pull --rebase origin main` before pushing.
