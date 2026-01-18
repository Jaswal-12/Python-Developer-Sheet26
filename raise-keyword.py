# custom_error_examples.py

# Example 1: ValueError for numbers out of range
try:
    a = int(input("Enter any number between 5 and 9: "))
    if a < 5 or a > 9:
        raise ValueError("Value should be between 5 and 9")
    print(f"You entered a valid number: {a}")
except ValueError as ve:
    print(f"Error: {ve}")


# Example 2: TypeError for non-string input
try:
    name = input("Enter your name: ")
    if not isinstance(name, str) or name.strip() == "":
        raise TypeError("Name must be a non-empty string")
    print(f"Hello, {name}!")
except TypeError as te:
    print(f"Error: {te}")


# Example 3: ZeroDivisionError manually
try:
    num = int(input("Enter a number to divide 10: "))
    if num == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    print("Result:", 10 / num)
except ZeroDivisionError as zde:
    print(f"Error: {zde}")


# Example 4: Custom exception class
class MyCustomError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise MyCustomError("You must be at least 18 years old to register")
    print("Age accepted!")
except MyCustomError as mce:
    print(f"Error: {mce}")
