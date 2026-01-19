"""
virtual_environment_guide.py
=================================

This file provides a complete and professional explanation of
Python Virtual Environments with examples and real-world use cases.

-------------------------------------------------
🔹 What is a Virtual Environment?
-------------------------------------------------

A virtual environment is an isolated Python environment that allows
each project to have its own Python interpreter and installed packages
(dependencies), independent of other projects and the system-wide Python.

In simple words:
A virtual environment keeps your project dependencies separate and safe.

-------------------------------------------------
🔹 Why Virtual Environments Are Needed
-------------------------------------------------

Problem without virtual environments:

- Project A requires: Django 2.2
- Project B requires: Django 4.0

Installing both globally causes:
❌ Version conflicts
❌ Application crashes
❌ Hard-to-debug errors

Solution:
✅ Create separate virtual environments for each project.

-------------------------------------------------
🔹 What a Virtual Environment Contains
-------------------------------------------------

Each virtual environment includes:
- A private Python interpreter
- Its own site-packages directory
- Independent installed libraries

It DOES NOT affect:
- System Python
- Other virtual environments
- Other projects

-------------------------------------------------
🔹 How Virtual Environments Work (Concept)
-------------------------------------------------

System Python
   |
   ├── Project_A (venv_A)
   │      └── Django 2.2
   |
   ├── Project_B (venv_B)
          └── Django 4.0

Both projects run independently without conflicts.
"""

# -------------------------------------------------
# Example 1: Creating a Virtual Environment
# -------------------------------------------------

"""
Command to create a virtual environment:

    python -m venv venv

Explanation:
- python  -> system Python
- -m venv -> uses built-in venv module
- venv    -> name of the virtual environment folder
"""

# -------------------------------------------------
# Example 2: Activating a Virtual Environment
# -------------------------------------------------

"""
Windows (CMD / PowerShell / Git Bash):

    venv\\Scripts\\activate

macOS / Linux:

    source venv/bin/activate

After activation, terminal shows:

    (venv)

This confirms the virtual environment is active.
"""

# -------------------------------------------------
# Example 3: Installing Packages Inside Virtual Environment
# -------------------------------------------------

"""
Once activated, install packages:

    pip install flask
    pip install django

These packages are installed ONLY inside the virtual environment.
They are not available globally.
"""

# -------------------------------------------------
# Example 4: Checking Installed Packages
# -------------------------------------------------

"""
To see installed packages:

    pip list

This command shows only packages installed inside the active venv.
"""

# -------------------------------------------------
# Example 5: requirements.txt (Very Important)
# -------------------------------------------------

"""
Save installed dependencies:

    pip freeze > requirements.txt

Install dependencies later:

    pip install -r requirements.txt

Used for:
✔ Deployment
✔ Team collaboration
✔ CI/CD pipelines
"""

# -------------------------------------------------
# Example 6: Deactivating the Virtual Environment
# -------------------------------------------------

"""
To deactivate the environment:

    deactivate

This returns you to system Python.
"""

# -------------------------------------------------
# Real-World Project Structure
# -------------------------------------------------

"""
Typical Python project using virtual environment:

Project/
│── venv/
│── app.py
│── requirements.txt
│── README.md

Note:
- venv/ folder is NOT pushed to GitHub
- requirements.txt IS pushed to GitHub
"""

# -------------------------------------------------
# Common Mistakes Beginners Make
# -------------------------------------------------

"""
❌ Installing packages without activating venv
❌ Pushing venv folder to GitHub
❌ Forgetting requirements.txt
❌ Using global Python for projects
"""

# -------------------------------------------------
# Interview-Oriented Definition ⭐
# -------------------------------------------------

"""
A virtual environment is an isolated Python environment that allows
developers to manage project-specific dependencies without interfering
with other projects or the system-wide Python installation.
"""

# -------------------------------------------------
# When to Use Virtual Environments
# -------------------------------------------------

"""
✔ Every Python project
✔ Web development (Django, Flask)
✔ Data science projects
✔ Backend APIs
✔ Production & deployment
"""

print("This file explains Python Virtual Environments in detail.")
print("Use it for learning, interviews, and GitHub documentation.")
