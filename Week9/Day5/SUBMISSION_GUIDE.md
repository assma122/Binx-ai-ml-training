# Day 5 — Safe Submission Guide

## 1. Copy the final folder

Create this directory in the local repository:

```text
D:\Main_Folder_main\Week9\Day5
```

Copy **the contents** of `Week9_Day5_Final` into that `Day5` folder.

## 2. Open the repository root

```powershell
cd D:\Main_Folder_main
conda activate binx-ai
```

## 3. Review only the Day 5 files

```powershell
git status --short Week9/Day5
```

## 4. Stage only Day 5

```powershell
git add Week9/Day5/
git status
```

Confirm that files from `.vscode`, Week7, datasets, or the team project are not
listed under **Changes to be committed**.

## 5. Commit and push

```powershell
git commit -m "Complete Week 9 Day 5 project close-out"
git push origin main
```

## 6. Final checks

- Open the GitHub repository and confirm `Week9/Day5/` is visible.
- Open the README and confirm the tables, links, and screenshot render.
- Open the public app in an incognito window.
- Test one positive and one negative review.

These commands stage only `Week9/Day5/`; they do not add unrelated untracked
files elsewhere in the repository.
