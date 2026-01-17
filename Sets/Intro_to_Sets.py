"""
Python Sets – Complete Explanation with Examples
===============================================

This file explains:
1. What sets are in Python
2. Why we use sets
3. Important properties of sets
4. Common set operations with examples
5. Professional use-cases

Author: Karan I
"""

# --------------------------------------------------
# 1. WHAT IS A SET?
# --------------------------------------------------

"""
A set in Python is an unordered collection of unique elements.

Key characteristics:
- Sets do NOT allow duplicate values
- Sets are unordered (no fixed index)
- Sets are mutable (can be changed)
- Elements must be immutable (int, float, string, tuple)
"""


# Example: Creating a set
s = {6, 1, 2, 3, 4, 2, 4, 5}
print("Set s:", s)

# Duplicate values (2 and 4) are automatically removed


# --------------------------------------------------
# 2. EMPTY SET vs EMPTY DICTIONARY
# --------------------------------------------------

# This creates an empty dictionary, NOT a set
k = {}
print("Type of k:", type(k))

# Correct way to create an empty set
empty_set = set()
print("Type of empty_set:", type(empty_set))


# --------------------------------------------------
# 3. ITERATING OVER A SET
# --------------------------------------------------

print("Elements in set s:")
for i in s:
    print(i, end=" ")
print("\n")

# Order may change every time because sets are unordered


# --------------------------------------------------
# 4. WHY DO WE USE SETS?
# --------------------------------------------------

"""
Sets are mainly used when:
- You want unique elements only
- You want fast membership testing
- You want to remove duplicates from data
- You want to perform mathematical set operations
"""


# Example 1: Removing duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)


# Example 2: Fast membership checking
students = {"Aman", "Ravi", "Karan", "Neha"}
print("Is Karan present?", "Karan" in students)
print("Is Rahul present?", "Rahul" in students)


# --------------------------------------------------
# 5. ADDING AND REMOVING ELEMENTS
# --------------------------------------------------

fruits = {"apple", "banana", "orange"}

# Add an element
fruits.add("mango")
print("After add:", fruits)

# Remove an element (raises error if not present)
fruits.remove("banana")
print("After remove:", fruits)

# Discard an element (no error if not present)
fruits.discard("grapes")
print("After discard:", fruits)


# --------------------------------------------------
# 6. IMPORTANT SET OPERATIONS
# --------------------------------------------------

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union: all unique elements
print("Union:", A | B)

# Intersection: common elements
print("Intersection:", A & B)

# Difference: elements in A but not in B
print("Difference (A - B):", A - B)

# Symmetric Difference: elements in either set but not both
print("Symmetric Difference:", A ^ B)


# --------------------------------------------------
# 7. SET METHODS
# --------------------------------------------------

sample_set = {10, 20, 30}

sample_set.pop()  # Removes a random element
print("After pop:", sample_set)

sample_set.clear()  # Removes all elements
print("After clear:", sample_set)


# --------------------------------------------------
# 8. REAL-WORLD USE CASES
# --------------------------------------------------

"""
Real-world examples of using sets:
- Removing duplicate user IDs
- Finding common skills between candidates
- Checking unique visitors on a website
- Performing mathematical operations
"""

# Example: Common skills
candidate1_skills = {"Python", "AWS", "Docker"}
candidate2_skills = {"Python", "React", "AWS"}

common_skills = candidate1_skills & candidate2_skills
print("Common skills:", common_skills)


# --------------------------------------------------
# 9. SUMMARY
# --------------------------------------------------

"""
Key Points:
- Sets store only unique values
- Sets are unordered and mutable
- Use sets for fast lookups and duplicate removal
- Supports powerful mathematical operations
- Widely used in real-world Python applications
"""
