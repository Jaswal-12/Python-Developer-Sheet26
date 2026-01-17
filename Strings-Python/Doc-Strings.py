"""
Python Docstrings, Comments, and PEP 8 Style Guide
=================================================

This file explains:
1. What docstrings are and how they are used
2. Difference between comments and docstrings
3. What PEP 8 is and why it is important
4. Professional examples following best practices

Author: Karan I
"""

# --------------------------------------------------
# 1. DOCSTRINGS
# --------------------------------------------------

"""
A docstring is a string literal that appears immediately after the
definition of a module, function, class, or method.

Docstrings are used to:
- Explain what the code does
- Describe parameters and return values
- Help tools like help(), IDEs, and documentation generators
"""


def square(n):
    """
    Calculate the square of a number.

    Parameters:
        n (int or float): The number whose square is required

    Returns:
        int or float: Square of the input number
    """
    return n ** 2


print(square(5))
print(square.__doc__)


# --------------------------------------------------
# 2. DOCSTRING FOR A CLASS
# --------------------------------------------------

class Calculator:
    """
    A simple calculator class to perform basic operations.
    """

    def add(self, a, b):
        """
        Add two numbers.

        Parameters:
            a (int or float): First number
            b (int or float): Second number

        Returns:
            int or float: Sum of a and b
        """
        return a + b


calc = Calculator()
print(calc.add(10, 20))


# --------------------------------------------------
# 3. COMMENTS vs DOCSTRINGS
# --------------------------------------------------

# COMMENTS:
# - Used to explain specific lines of code
# - Ignored by Python interpreter
# - Written using #

# Example comment
x = 10  # storing integer value


"""
DOCSTRINGS:
- Used for documentation
- Can be accessed at runtime
- Written using triple quotes
- Meant for users and developers
"""


# --------------------------------------------------
# 4. WHAT IS PEP 8?
# --------------------------------------------------

"""
PEP 8 stands for Python Enhancement Proposal 8.

It is an official style guide that provides guidelines and best practices
on how to write clean, readable, and professional Python code.

Why PEP 8 matters:
- Improves code readability
- Makes collaboration easier
- Helps maintain consistency
- Used in interviews and production code
"""


# --------------------------------------------------
# 5. IMPORTANT PEP 8 RULES WITH EXAMPLES
# --------------------------------------------------

# 1. Function and variable naming: use snake_case

def calculate_area(radius):
    """Return area of a circle."""
    pi = 3.14159
    return pi * radius * radius


# 2. Class naming: use PascalCase

class StudentRecord:
    """Represents a student record."""

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no


# 3. Line length: maximum 79 characters

long_text = (
    "This is an example of breaking long strings "
    "into multiple lines according to PEP 8."
)


# 4. Proper spacing

a = 5
b = 10
result = a + b


# 5. Blank lines for readability


def multiply(a, b):
    """Return multiplication of two numbers."""
    return a * b


# --------------------------------------------------
# 6. PROFESSIONAL DOCSTRING STYLE (GOOGLE STYLE)
# --------------------------------------------------


def divide(a, b):
    """
    Divide two numbers.

    Args:
        a (int or float): Numerator
        b (int or float): Denominator

    Returns:
        float: Result of division

    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


# --------------------------------------------------
# 7. SUMMARY
# --------------------------------------------------

"""
Key Takeaways:
- Use docstrings to document functions, classes, and modules
- Use comments for short explanations of logic
- Follow PEP 8 for clean and professional Python code
- Writing good documentation improves interview and real-world coding
"""
