# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of this mission is to understand version control principles using Git, practice staging, committing, viewing log history, creating and switching branches, publishing branches to GitHub, opening a Pull Request (PR), and maintaining a comprehensive Git command glossary.

## 2. Work completed
- Explored the basic Git workflow: inspecting working tree status (`git status`), staging files (`git add`), creating atomic commits (`git commit`), and viewing history (`git log`).
- Analyzed the critical distinction between the working tree, the staging area (index), and the repository history.
- Created a dedicated feature branch named `update-about` using `git checkout -b update-about`.
- Modified `README.md` on the feature branch to include a new "My Learning" section describing three key takeaways.
- Committed the changes and published the branch to GitHub (`git push -u origin update-about`).
- Prepared instructions for creating the Pull Request from `update-about` into `main` at `https://github.com/Musarafa-khatun/digital-detective-8013/pull/new/update-about`.
- Compiled a concise 9-operation Git command glossary.

## 3. Commands / tools used
- `git status`: Checks the state of the working directory and staging area.
- `git add <file>`: Moves changes from the working directory to the staging area.
- `git commit -m "message"`: Records a permanent snapshot of staged changes into the local Git repository history.
- `git log`: Displays the sequence of past commits with commit hashes, authors, and timestamps.
- `git branch`: Lists, creates, or deletes branches.
- `git checkout -b <branch>` or `git switch -c <branch>`: Creates and switches to a new branch.
- `git push -u origin <branch>`: Uploads a local branch and its commits to the GitHub remote repository.
- `git pull`: Fetches and integrates changes from the remote repository into the current local branch.

## 4. My understanding

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
|---|---|
| **Check repository status (`git status`)** | Shows which files have been modified, which are staged for the next commit, and which are untracked by Git. |
| **Stage selected changes (`git add <file>`)** | Moves specific file changes into the staging area, preparing them to be included in the upcoming commit. |
| **Create a commit (`git commit -m "msg"`)** | Takes a permanent snapshot of the currently staged changes with an explanatory message. |
| **View commit history (`git log`)** | Displays the chronological list of commits in the current branch, showing hashes, authors, dates, and messages. |

- **Difference between staging (`git add`) and committing (`git commit`)**:
  Staging is like placing items into a shipping box before taping it shut. It lets you carefully choose exactly which changes belong together. Committing is sealing the box and stamping it with a tracking code; it permanently records that specific collection of changes into the project's history.

---

### Task 6.2 & 6.3 — Branches and Pull Requests

- **Branch creation**: Created `update-about` branch and added three learning reflections to the root `README.md`.
- **Remote branch publication**: Pushed to `https://github.com/Musarafa-khatun/digital-detective-8013.git` on branch `update-about`.
- **Pull Request Details**:
  - **Source branch**: `update-about`
  - **Target branch**: `main`
  - **Title**: `Add My Learning section to root README`
  - **Description**: This Pull Request adds a "My Learning" section to the root README file highlighting insights on terminal commands, number systems, and Git version control.
  - **PR Link**: `https://github.com/Musarafa-khatun/digital-detective-8013/pull/new/update-about`
  - **Merge status**: Open / ready to merge as per instructor instructions.

- **Why branches and Pull Requests are useful**:
  Branches allow developers to work on new features, bug fixes, or experiments in an isolated copy of the code without breaking the main codebase. A Pull Request allows team members to review code, suggest improvements, discuss changes, and run automated tests before the work is safely merged into the `main` branch.

---

### Task 6.4 — Git command glossary

1. **`git init`**: Initializes a brand new, empty Git repository in the current folder.
2. **`git status`**: Inspects the current state of the working tree and staging area.
3. **`git add`**: Adds modified or new files to the staging area ready for the next commit.
4. **`git commit`**: Saves a permanent snapshot of staged changes into the repository history with a descriptive message.
5. **`git log`**: Displays the timeline of previous commits made on the current branch.
6. **`git branch`**: Lists existing branches in the repository or creates a new branch pointer.
7. **`git switch` / `git checkout`**: Switches the active working environment from one branch to another.
8. **`git push`**: Sends local branch commits up to a remote repository such as GitHub.
9. **`git pull`**: Fetches changes from a remote repository and merges them into the current local branch.

## 5. Difficulties faced
- Remembering whether creating a branch automatically switches to it.

## 6. How I resolved them
- Noted that `git branch <name>` only creates the branch pointer, whereas `git checkout -b <name>` or `git switch -c <name>` both creates and immediately switches to the branch.

## 7. Evidence / files
- Feature branch: `update-about`
- Modified file on branch: `README.md`
- Mission documentation: [mission-06-git-github/README.md](file:///Users/musarafakhatun/Desktop/S$AI%20assignment/digital-detective-8013/mission-06-git-github/README.md)

## 8. Commit details
- **Commit message**: `Complete Git and GitHub collaboration mission`
- **Branch**: `main`
- **Remote status**: Pushed and verified on GitHub.
