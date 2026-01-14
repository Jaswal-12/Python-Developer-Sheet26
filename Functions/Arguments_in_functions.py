# 🔧 FUNCTION ARGUMENTS & RETURN STATEMENT IN PYTHON
# ------------------------------------------------
# Functions can accept different types of arguments
# and can return values using the return keyword.
#
# This file covers:
# 1. Default Arguments
# 2. Required Arguments
# 3. Variable-Length Arguments (*args)
# 4. Return Statement

# ==================================================
# 1️⃣ DEFAULT ARGUMENT FUNCTIONS
# ==================================================
# Default arguments take a value automatically
# if no argument is passed during function call.

def avg(a=9, b=1):
    """
    Calculates the average of two numbers.
    Uses default values if arguments are not provided.
    """
    print("Average:", (a + b) / 2)


# Function calls
avg(2, 2)   # overrides default values
avg()       # uses default values a=9, b=1


# ==================================================
# 2️⃣ REQUIRED ARGUMENTS
# ==================================================
# Required arguments must be provided while calling the function.

def avg_required(a, b=9):
    """
    'a' is a required argument
    'b' has a default value
    """
    print("Average:", (a + b) / 2)


avg_required(2)      # valid (b uses default value)
avg_required(2, 6)   # valid


# ==================================================
# 3️⃣ VARIABLE-LENGTH ARGUMENTS (*args)
# ==================================================
# *args allows a function to accept any number of arguments.
# All values are received as a tuple.

def av(*num):
    """
    Calculates average of multiple numbers.
    """
    total = 0
    for i in num:
        total += i

    print("Average is:", total / len(num))


av(5, 6, 7, 8, 9)
av(10, 20, 30)


# ==================================================
# 4️⃣ RETURN STATEMENT
# ==================================================
# The return statement sends a value back to the caller.
# Code after return does not execute.

def square(a):
    """
    Returns square of a number.
    """
    return a * a


result = square(2)
print("Square:", result)


# ==================================================
# SUMMARY
# ==================================================
# - Default arguments provide flexibility
# - Required arguments must be passed
# - *args allows variable number of inputs
# - return sends data back from a function
