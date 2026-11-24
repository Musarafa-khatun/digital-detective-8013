# Mission 0 — Repository and Workspace Setup

## 1. Task / objective
The objective of this mission was to verify the installed versions of Python 3 and Git on my macOS system, establish the local project directory structure named `digital-detective-8013`, initialize a Git repository on branch `main`, link it to a public GitHub repository, and prepare the foundational workspace for all upcoming missions.

## 2. Work completed
- Checked and recorded the exact versions of Python 3 and Git.
- Created the local repository folder `digital-detective-8013`.
- Initialized a local Git repository with the default branch set to `main`.
- Created all required mission folders (`mission-00-setup` through `mission-08-final-report`) and the `evidence` folder.
- Configured Git user identity safely for this repository.
- Connected the local repository to remote origin `https://github.com/Musarafa-khatun/digital-detective-8013.git`.
- Created the root `README.md` containing the project overview and mission index.

## 3. Commands / tools used
- `python3 --version`: Verified the installed Python runtime (`Python 3.14.7`).
- `git --version`: Verified the installed version of Git (`git version 2.50.1 (Apple Git-155)`).
- `mkdir -p <folders>`: Created the mission directories and evidence folder.
- `git init -b main`: Initialized the Git repository with the primary branch named `main`.
- `git config user.name "Musarafa-khatun"`: Set local Git author name.
- `git config user.email "musarafakhatun@users.noreply.github.com"`: Set local Git author email using GitHub's privacy-safe noreply format.
- `git remote add origin https://github.com/Musarafa-khatun/digital-detective-8013.git`: Linked the local repository to GitHub.

## 4. My understanding
- **What is a repository?**: A repository (or "repo") is a storage space managed by Git that tracks files, directories, and the complete history of changes made over time. It allows developers to revert mistakes, review changes, and collaborate without losing work.
- **Why organize folders by mission?**: Keeping a dedicated folder for each mission separates the learning modules cleanly. It allows the instructor and anyone reviewing the project to inspect each topic independently, see the associated code and notes in one place, and verify that the assignment was tackled step-by-step.

## 5. Difficulties faced
- No major difficulties. Initially, Git was not configured with a local username and email in this specific folder, so commits would have used default system settings.

## 6. How I resolved them
- Configured `user.name` and `user.email` locally within the repository configuration so commits are correctly attributed to my GitHub profile while keeping my personal email address private.

## 7. Evidence / files
- Root README: [README.md](file:///Users/musarafakhatun/Desktop/S$AI%20assignment/digital-detective-8013/README.md)
- Mission 0 README: [mission-00-setup/README.md](file:///Users/musarafakhatun/Desktop/S$AI%20assignment/digital-detective-8013/mission-00-setup/README.md)
- Directory structure: 9 mission folders and 1 evidence folder.

## 8. Commit details
- **Commit message**: `Set up Digital Detective mission structure`
- **Branch**: `main`
- **Remote status**: Pushed to `https://github.com/Musarafa-khatun/digital-detective-8013.git` (pending GitHub repository creation).
