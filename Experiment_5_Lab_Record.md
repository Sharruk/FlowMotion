# ICS1405 – Software Engineering Principles and Practices
## Experiment 5: Explore Git and GitHub Commands and Practice Source Code Management

**Student Name:** [Your Name]  
**Register Number:** [Your Register Number]  
**Date:** February 27, 2026  
**Project Name:** FlowMotion – Intelligent Habit & Routine Management System  

---

### 1. Introduction

#### 1.1 Experiment Overview
This experiment focuses on implementing robust Version Control System (VCS) practices using Git and GitHub. For the "FlowMotion" project, a Django-based intelligent habit tracker, maintaining a clean history of changes is critical as the codebase scales from simple CRUD operations to complex AI integrations.

#### 1.2 Importance of Version Control
In modern software engineering, version control is the backbone of collaboration and maintainability. It allows developers to:
- Track every change with a timestamp and author.
- Revert to previous stable states if a new feature breaks the system.
- Work on multiple features simultaneously using branching without interfering with the main production code.

#### 1.3 Relevance to FlowMotion Project
FlowMotion involves multiple modules: User Authentication, Habit Tracking Logic, AI Recommendation Engines, and Desktop Widget Integration. Git ensures that a bug in the AI module doesn't block the development of the UI or the database schema.

#### 1.4 Objectives
- To initialize a local Git repository and link it to a remote GitHub repository.
- To practice incremental commits and meaningful commit messaging.
- To implement a Feature Branch Workflow for modular development.
- To analyze the efficiency of merging strategies and conflict resolution.

#### 1.5 Scope and Assumptions
The scope covers the core FlowMotion repository. It is assumed that Git is installed on the local environment (Replit/Linux) and a GitHub account is available for remote hosting.

---

### 2. Tools and Environment
- **VCS Tool:** Git (Version 2.x+)
- **Hosting Platform:** GitHub
- **Development Environment:** Replit (Cloud IDE) / VS Code
- **Operating System:** Linux (NixOS distribution)
- **Language/Framework:** Python 3.11, Django 5.2

---

### 3. Repository Setup

#### 3.1 Initialization and Remote Linking
The following steps were executed to set up the FlowMotion repository:
1.  **Initialize Local Repo:** `git init`
2.  **Add Files:** `git add .`
3.  **Initial Commit:** `git commit -m "Initial commit: Setup Django project structure for FlowMotion"`
4.  **Create GitHub Repo:** Created `FlowMotion-App` on GitHub.
5.  **Link Remote:** `git remote add origin https://github.com/[username]/FlowMotion-App.git`
6.  **Push to Main:** `git push -u origin main`

#### 3.2 Branch Hierarchy and Naming Conventions
FlowMotion follows a **Feature Branch Workflow**:
- **`main`**: The production-ready branch. Only stable code resides here.
- **`develop`**: The integration branch for features.
- **`feature/ai-integration`**: Dedicated branch for Gemini AI tool recommendations.
- **`feature/habit-ui`**: Dedicated branch for dashboard and habit detail templates.
- **`bugfix/login-modal`**: Short-lived branch for fixing authentication UI issues.

#### 3.3 Repository Structure Diagram
```text
Root/
├── .git/                (VCS metadata)
├── .gitignore           (Files to ignore: pyc, sqlite3, .env)
├── flowmotion/          (Project Settings)
├── habits/              (Core App)
│   ├── ai_utils.py      (AI Logic)
│   └── views.py         (Business Logic)
├── templates/           (UI)
└── manage.py            (Entry point)
```

---

### 4. Version Control Operations

#### 4.1 Core Commands Explained
- **`git status`**: Checks the state of the working directory and staging area. Used before every commit to ensure no unwanted files (like `db.sqlite3`) are added.
- **`git log --oneline --graph`**: Visualizes the commit history and branch merges.
- **`git stash`**: Temporarily saves uncommitted changes when switching context (e.g., from `feature/ai` to a critical `bugfix`).

#### 4.2 Incremental Commit Strategy
Commits in FlowMotion are atomic. Instead of one giant commit, changes are broken down:
1.  `feat: add AIRecommendation model to habits`
2.  `feat: implement get_ai_recommendations using Gemini API`
3.  `fix: add retry logic for AI JSON parsing`

#### 4.3 Conflict Resolution Example
During a merge from `feature/ai-integration` to `develop`, a conflict occurred in `views.py`.
**Conflict Snippet:**
```python
<<<<<<< HEAD
    return render(request, 'dashboard.html', context)
=======
    recommendations = get_ai_recommendations(habit.name)
    return render(request, 'dashboard.html', {**context, 'ai': recommendations})
>>>>>>> feature/ai-integration
```
**Resolution:** The code was manually edited to include both the original context and the new AI recommendations, followed by `git add views.py` and `git commit`.

---

### 5. Git Workflow Implementation

#### 5.1 Chosen Workflow: Feature Branch Workflow
FlowMotion utilizes the **Feature Branch Workflow**. This ensures the `main` branch is always deployable. Every new capability (like the Desktop Widget) is developed in an isolated branch.

#### 5.2 Daily Development Cycle
1.  `git pull origin develop` (Sync latest changes)
2.  `git checkout -b feature/new-task` (Create workspace)
3.  *Code and incremental commits*
4.  `git push origin feature/new-task`
5.  *Create Pull Request (PR) on GitHub*
6.  *Merge PR after review*

---

### 6. Workflow Analysis

| Metric | Analysis |
| :--- | :--- |
| **Efficiency** | High. Parallel development of AI and UI modules without overlap. |
| **Maintainability** | Excellent. Commit history provides a clear audit trail of why logic changed. |
| **Risk** | Low. Isolated branches prevent "breaking the build" for others. |

**Observed Benefit:** When the Gemini API call format changed, the fix was isolated to the `feature/ai-integration` branch, tested, and then merged, ensuring zero downtime for the main application.

---

### 7. Comparison of Alternative Workflows

| Workflow | Pros | Cons | Suitability for FlowMotion |
| :--- | :--- | :--- | :--- |
| **Centralized** | Simple, no branches. | High conflict risk. | Low (too risky for AI updates). |
| **GitFlow** | Very structured (Release/Hotfix). | Complex for small teams. | Moderate (Good for future scaling). |
| **Feature Branch** | Clean, modular, isolated. | Requires discipline. | **High (Optimal choice).** |

---

### 8. Documentation and Evidence (Sample Logs)

**Commit History Log:**
```bash
* f49d8eb (HEAD -> main) feat: add fallback tools for AI recommendations
* 364697f feat: implement retry logic for Gemini API
* a2b1c3d fix: resolve merge conflict in habit_detail.html
* 1234567 feat: initial habit tracking models
```

---

### 9. Observations
1.  **Technical:** Using `.gitignore` is essential to prevent sensitive API keys (in `.env`) from leaking to GitHub.
2.  **Challenges:** Merging template changes often caused conflicts due to overlapping HTML div structures.
3.  **Solution:** Adopted a standard "div naming" convention to reduce line overlap in Git.

---

### 10. Conclusion
The implementation of Git and GitHub for FlowMotion has successfully transitioned the project from a local script to a professional-grade software product. The Feature Branch Workflow ensured that AI experimentation did not compromise the core habit-tracking stability.

---

### 11. Appendix: Sample .gitignore
```text
*.pyc
__pycache__/
db.sqlite3
.env
.replit
.local/
```