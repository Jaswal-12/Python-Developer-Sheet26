"""
python_import_guide.py
=================================

This file explains how the `import` statement works in Python.
It covers different types of imports with clear explanations
and practical examples.

-------------------------------------------------
🔹 What is import in Python?
-------------------------------------------------

The `import` statement is used to bring code from another module
(file) or library into the current Python program.

A module can contain:
- Functions
- Variables
- Classes

Using import helps in:
✔ Code reusability
✔ Better organization
✔ Cleaner and modular programs
"""

# -------------------------------------------------
# Example 1: Importing a built-in module
# -------------------------------------------------

import math

print("Example 1: Using math module")
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)

print("\n" + "-" * 40 + "\n")

# -------------------------------------------------
# Example 2: Importing specific items from a module
# -------------------------------------------------

from math import sqrt, pi

print("Example 2: Import specific items")
print("Square root of 25:", sqrt(25))
print("Pi value:", pi)

print("\n" + "-" * 40 + "\n")

# -------------------------------------------------
# Example 3: Importing everything from a module
# -------------------------------------------------

from math import *

print("Example 3: Import everything from math")
print("Square root of 36:", sqrt(36))
print("Ceiling of 4.2:", ceil(4.2))

"""
⚠ Warning:
Using `from module import *` is not recommended in large projects
because it:
- Pollutes the namespace
- Makes code harder to read and debug
"""

print("\n" + "-" * 40 + "\n")

# -------------------------------------------------
# Example 4: Import with alias (as keyword)
# -------------------------------------------------

import math as m

print("Example 4: Import with alias")
print("Square root of 49:", m.sqrt(49))

print("\n" + "-" * 40 + "\n")

# -------------------------------------------------
# Example 5: Importing your own module
# -------------------------------------------------

"""
Suppose you have a file named: my_module.py

Content of my_module.py:
-----------------------
def greet(name):
    return f"Hello, {name}"

pi_value = 3.14
-----------------------

Usage in another file:
"""

# from my_module import greet, pi_value
# print(greet("Karan"))
# print(pi_value)

"""
✔ Python searches for modules in:
1. Current directory
2. PYTHONPATH
3. Python installation directories
"""

print("\n" + "-" * 40 + "\n")

# -------------------------------------------------
# Example 6: import vs from import
# -------------------------------------------------

"""
import math
✔ Access using math.sqrt()

from math import sqrt
✔ Access using sqrt()
"""

print("Example 6: import vs from import")
print("Using import math:", math.sqrt(64))
print("Using from math import sqrt:", sqrt(64))

print("\n" + "-" * 40 + "\n")

# -------------------------------------------------
# Example 7: How Python import works internally
# -------------------------------------------------

"""
When Python sees an import statement:
1. Checks if the module is already loaded
2. Searches for the module in directories
3. Executes the module code
4. Creates a module object
5. Makes it available in the namespace
"""

# -------------------------------------------------
# Common Mistakes
# -------------------------------------------------

"""
❌ Importing unused modules
❌ Circular imports
❌ Using import * in big projects
❌ Wrong file/module name
"""

# -------------------------------------------------
# Interview-Oriented Definition ⭐
# -------------------------------------------------

"""
The import statement in Python is used to load modules and their
definitions into the current namespace, enabling code reuse,
modularity, and better program organization.
"""

print("This file explains how Python import works with examples.")
print("Use it for learning, exams, and GitHub documentation.")

s
