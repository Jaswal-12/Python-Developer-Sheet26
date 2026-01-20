"""
variables_demo.py

This file explains the difference between **global** and **local** variables in Python.

- **Global Variable**: A variable defined outside any function, accessible throughout the file.
- **Local Variable**: A variable defined inside a function, accessible only within that function.
"""

# ---------------------------
# 1. Global Variable
# ---------------------------
x = 4  # Global variable
print("Global x before function call:", x)

# ---------------------------
# 2. Function with Local Variable
# ---------------------------
def hello():
    x = 5  # Local variable
    print(f"Local x inside hello() function: {x}")
    print("Hello from the function!")

# ---------------------------
# 3. Checking Variables
# ---------------------------
print(f"Global x before calling hello(): {x}")  # Accessing global variable

hello()  # Call function which has local x

print(f"Global x after calling hello(): {x}")  # Global x is unchanged

# ---------------------------
# 4. Using global keyword
# ---------------------------
def change_global():
    global x  # This tells Python to use the global x, not create a local x
    x = 10
    print(f"Global x inside change_global() after modification: {x}")

change_global()  # Modifies the global x
print(f"Global x after calling change_global(): {x}")

# ---------------------------
# Summary
# ---------------------------
"""
1. Local variables exist only inside the function where they are defined.
2. Global variables exist throughout the program.
3. If a local variable has the same name as a global variable, the local one takes priority inside the function.
4. Use 'global' keyword inside a function to modify a global variable.
"""
