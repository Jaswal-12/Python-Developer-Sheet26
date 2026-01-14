# 🔧 FUNCTIONS IN PYTHON
# --------------------
# A function is a block of reusable code that performs a specific task.
# Functions help make programs:
# - Clean
# - Reusable
# - Easy to understand and maintain
#
# In large programs, functions reduce repetition and improve readability.

# ---------------------------------------
# Types of Functions
# ---------------------------------------

# 1. Built-in Functions
# Python already provides many useful functions.
# Examples: print(), len(), max(), min(), sum(), type()

numbers = [10, 20, 30, 40]

print(len(numbers))   # Length of list
print(max(numbers))   # Maximum value
print(sum(numbers))   # Sum of elements
print(type(numbers)) # Data type

# ---------------------------------------
# 2. User-Defined Functions
# ---------------------------------------
# We create our own functions using the 'def' keyword.

# Example 1: Geometric Mean Function
def gmean(a, b):
    """
    This function calculates the geometric mean
    of two numbers.
    """
    mean = (a * b) / (a + b)
    print("Geometric Mean:", mean)

gmean(2, 5)

# ---------------------------------------
# Example 2: Function to Add Two Numbers
# ---------------------------------------

def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)

# ---------------------------------------
# Example 3: Function with Default Argument
# ---------------------------------------

def greet(name="User"):
    print("Hello", name)

greet("Karan")
greet()

# ---------------------------------------
# Example 4: Function to Check Even or Odd
# ---------------------------------------

def check_even_odd(n):
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")

check_even_odd(10)
check_even_odd(7)

# ---------------------------------------
# Example 5: Function with Multiple Values
# ---------------------------------------

def calculate(a, b):
    return a + b, a - b, a * b

add, sub, mul = calculate(8, 4)
print("Add:", add)
print("Subtract:", sub)
print("Multiply:", mul)

# ---------------------------------------
# Summary
# ---------------------------------------
# - Functions are defined using 'def'
# - They can take parameters and return values
# - Built-in and user-defined functions make coding efficient
