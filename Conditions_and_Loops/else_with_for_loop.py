"""
Topic: else with loops in Python
Author: Explanation Script

IMPORTANT IDEA:
---------------
In Python, a loop's `else` block runs ONLY if the loop
finishes normally (i.e., WITHOUT hitting a `break`).

If `break` is executed → else will NOT run.
"""

print("========== Example 1: for loop with empty list ==========")

for i in []:
    print(i)
else:
    print("Sorry no i")   # Runs because loop never started but ended normally


"""
Explanation:
- The list is empty
- Loop body never executes
- No break occurred
- So `else` runs
"""


print("\n========== Example 2: for loop with break ==========")

for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("Sorry no i")   # This will NOT run


"""
Explanation:
- Loop starts printing numbers
- When i == 4 → break executes
- Loop terminates abruptly
- else is skipped
"""


print("\n========== Example 3: for loop without break ==========")

for i in range(3):
    print(i)
else:
    print("Loop completed successfully!")


"""
Explanation:
- Loop runs fully (0,1,2)
- No break occurred
- else executes
"""


print("\n========== Example 4: Searching an element ==========")

numbers = [10, 20, 30, 40]
target = 25

for n in numbers:
    if n == target:
        print("Found", target)
        break
else:
    print("Target not found")


"""
Explanation:
- Loop searches for target
- If found → break → else skipped
- If not found → loop completes → else runs
THIS IS A VERY COMMON USE CASE
"""


print("\n========== Example 5: while loop with else ==========")

i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("While loop finished normally")


"""
Explanation:
- while loop completed without break
- else runs
"""


print("\n========== Example 6: while loop with break ==========")

i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("This will NOT print")


"""
Explanation:
- break executed at i == 3
- loop did not finish normally
- else skipped
"""


print("\n========== Summary ==========")

print("""
RULE TO REMEMBER:
-----------------
Loop else executes ONLY when:
✔ Loop finishes naturally
✘ No break statement executed

Common Use:
-----------
✔ Searching problems
✔ Validation checks
✔ Knowing if loop exited early or not
""")
