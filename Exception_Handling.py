"""
=========================================
Topic: Exception (Error) Handling in Python
File : exception_handling_demo.py
=========================================

Exception Handling allows a program to handle runtime errors
without crashing.

KEYWORDS:
---------
try     -> code that may cause error
except  -> handles error
else    -> runs if no error occurs
finally -> always runs
"""

print("========== Example 1: Basic Exception Handling ==========")

try:
    a = int(input("ENTER A NUMBER: "))

    for i in range(1, 11):
        print(f"{a} X {i} = {a*i}")

except ValueError:
    # Raised when input is not an integer
    print("ValueError: Please enter a valid number")

except Exception as e:
    # Handles any other unexpected error
    print("Some error occurred:", e)

else:
    # Runs only if NO exception occurred
    print("Multiplication table printed successfully")

finally:
    # Always runs
    print("Program execution completed")


"""
IMPORTANT NOTE ABOUT EXCEPT ORDER
---------------------------------
❌ WRONG:
except Exception:
except IndexError:

✔ CORRECT:
except IndexError:
except Exception:

Reason:
--------
Exception is the parent class of all errors.
If it comes first, specific errors will never execute.
"""

print("\n========== Example 2: IndexError Demonstration ==========")

try:
    lst = [10, 20, 30]
    print(lst[5])   # Invalid index

except IndexError:
    print("IndexError: List index out of range")

except Exception as e:
    print("Other error:", e)


print("\n========== Example 3: ZeroDivisionError ==========")

try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Result:", x / y)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Only numbers are allowed")

except Exception as e:
    print("Unexpected error:", e)


print("\n========== Example 4: Using else without error ==========")

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", num)


print("\n========== SUMMARY ==========")

print("""
RULES TO REMEMBER:
-----------------
✔ Always put risky code inside try
✔ Catch specific exceptions first
✔ Exception should be LAST
✔ else runs only when no error
✔ finally always runs

COMMON ERRORS:
--------------
- Wrong indentation
- Putting Exception before specific errors
- Writing risky code outside try

INTERVIEW ONE-LINER:
-------------------
Exception handling prevents program termination
and allows graceful error recovery.
""")
