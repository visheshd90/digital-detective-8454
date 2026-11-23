# Mission 6 - Version Control with Git Notes

## Task 6.1 — Understand the basic Git workflow

### Git Operations Table:
| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status** | Inspects the working directory and staging area to show which files are modified, untracked, or staged and ready for commit. |
| **Stage selected changes** | Adds specific modified or new files to the staging area (`git add`), preparing them to be included in the next snapshot. |
| **Create a commit** | Permanently records the staged snapshot into the repository history (`git commit`) with a unique ID and descriptive message. |
| **View commit history** | Displays the chronological timeline of previous commits (`git log`), showing commit hashes, author details, timestamps, and messages. |

### Difference Between Staging and Committing:
* **Staging (`git add`):** Acts as a staging dock or workspace preparation step. It groups specific changes you want to include in your next save without permanently locking them into the project history yet.
* **Committing (`git commit`):** Takes everything currently in the staging area and permanently saves it as an official, version-controlled checkpoint in your repository's history graph.

## Task 6.2 — Create and use a branch
* **Branch created:** `update-about` (`git checkout -b update-about`)
* **File modified:** Root `README.md` (Added "My Learning" section detailing OS, Python, and Git milestones).
* **Commands used:** `git status`, `git add README.md`, `git commit -m "..."`, `git push -u origin update-about`
* **Verification:** Successfully pushed the new branch to GitHub and verified branch tracking.

## Task 6.3 — Create a Pull Request

### GitHub Actions Performed:
* Opened a Pull Request from `update-about` into `main` on GitHub.
* Added a descriptive title and summary of changes.
* Reviewed and merged the PR into `main`, then synchronized local changes using `git checkout main` and `git pull`.

### Conceptual Explanations:
* **What is a branch?**
  A branch is an independent, isolated line of development separate from the main codebase (`main`). It allows developers to implement new features, fix bugs, or test changes without altering or breaking the stable production code.
* **What is a Pull Request (PR)?**
  A Pull Request is a collaborative feature on platforms like GitHub where developers propose changes made in a branch to be merged into another branch (such as `main`). It serves as a workspace for code review, discussion, automated testing, and feedback before integration.
* **Why are they useful when people work on the same project?**
  Branches and Pull Requests prevent team members from stepping on each other's toes by keeping individual work isolated. PRs facilitate peer code review, catch bugs early through automated checks, ensure code quality standards, and maintain an organized history of decisions and changes made across the project.

## Task 6.4 — Build your Git command glossary

### Git Command Glossary Table:
| Git Operation | Command Example | One-line explanation in your own words |
| :--- | :--- | :--- |
| **Initialise a repository** | `git init` | Creates a new hidden `.git` directory to start tracking a project folder with version control. |
| **Check status** | `git status` | Inspects the current state of the working directory to see untracked, modified, or staged files. |
| **Stage changes** | `git add <file>` | Prepares specific modified or new files by adding them to the staging area before saving. |
| **Commit changes** | `git commit -m "..."` | Permanently records all staged changes as a new snapshot in the project's commit history. |
| **View history** | `git log` | Displays a chronological list of previous commits with their unique hashes, authors, and messages. |
| **Create or list branches** | `git branch` | Lists all existing local branches or creates a new independent branch line of development. |
| **Switch branches** | `git switch <branch>` | Moves your working environment from one branch to another. |
| **Publish changes** | `git push` | Uploads your local commits and branches up to a remote repository like GitHub. |
| **Retrieve remote changes** | `git pull` | Downloads and merges the latest updates from a remote repository down to your local machine. |
