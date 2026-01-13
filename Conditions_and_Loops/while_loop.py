# Python While Loop Examples with Full Explanation

# ------------------------------
# What is a while loop?
# A while loop is used to repeatedly execute a block of code as long as a condition is True.
# Syntax:
# while condition:
#     # code to execute

# Important Points:
# 1. The condition is checked before each iteration.
# 2. Make sure the condition will eventually become False, otherwise you get an infinite loop.
# 3. You can use 'break' to exit the loop or 'continue' to skip an iteration.

# ------------------------------
# Example 1: Basic while loop
x = int(input("Enter a number: "))  # User input
i = 0
while i < x:
    print(i)
    i += 1  # Increment i to avoid infinite loop

print("\n")

# ------------------------------
# Example 2: Using break in a while loop
# Stops the loop when i equals 3
x = int(input("Enter a number: "))
i = 0
while i < x:
    if i == 3:
        print("Breaking the loop at i=3")
        break
    print(i)
    i += 1

print("\n")

# ------------------------------
# Example 3: Using continue in a while loop
# Skips printing even numbers
x = int(input("Enter a number: "))
i = 0
while i < x:
    i += 1  # Increment at start to avoid infinite loop
    if i % 2 == 0:
        continue
    print(i)

print("\n")

# ------------------------------
# Example 4: Using while loop with else
# The else block runs when the condition becomes False
x = 5
i = 0
while i < x:
    print(i)
    i += 1
else:
    print("Loop finished successfully!")

print("\n")

# ------------------------------
# Example 5: Nested while loops
# Outer loop counts rows, inner loop counts columns
rows = 3
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()  # Newline after each row
    i += 1
