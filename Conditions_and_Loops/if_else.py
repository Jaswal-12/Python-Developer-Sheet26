# 🔀 CONDITIONAL STATEMENTS IN PYTHON
# ---------------------------------
# Conditional statements are used to make decisions in a program.
# Python uses:
# if
# elif
# else

# ---------------------------------------
# Example 1: Voting Eligibility
# ---------------------------------------

age = int(input("Enter Your Age: "))

if age > 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# ---------------------------------------
# Example 2: Using if-elif-else
# ---------------------------------------

apple_price = 10
budget = 200

if budget - apple_price > 50:
    print("Alexa, add 1 kg apples to the cart.")
elif budget - apple_price > 70:
    print("It's okay, you can buy.")
else:
    print("Alexa, do not add apples to the cart.")

# ---------------------------------------
# Example 3: Checking a Number
# ---------------------------------------

n = int(input("Enter a number: "))

if n < 0:
    print("The number is Negative.")
elif n > 0:
    print("The number is Positive.")
else:
    print("The number is Zero.")

# ---------------------------------------
# Summary
# ---------------------------------------
# if   -> checks the first condition
# elif -> checks another condition if the previous is false
# else -> runs when all conditions are false
