"""
Python Set Methods – Detailed Explanation with Examples
======================================================

This file explains the most commonly used set methods in Python
with clear examples and professional explanations.

Author: Karan I
"""

# --------------------------------------------------
# 1. CREATING SETS
# --------------------------------------------------

s1 = {1, 4, 3, 4, 45}
s2 = {1, 13, 3}

print("Set s1:", s1)
print("Set s2:", s2)


# --------------------------------------------------
# 2. UNION
# --------------------------------------------------

"""
union() returns a new set containing all unique elements
from both sets.
"""

print("Union:", s1.union(s2))

# s1.update(s2)  # Uncomment to modify s1 permanently
# print("After update:", s1)


# --------------------------------------------------
# 3. INTERSECTION
# --------------------------------------------------

"""
intersection() returns elements that are common
in both sets.
"""

print("Intersection:", s1.intersection(s2))


# --------------------------------------------------
# 4. SYMMETRIC DIFFERENCE
# --------------------------------------------------

"""
symmetric_difference() returns elements that are
present in either set, but not in both.
"""

print("Symmetric Difference:", s1.symmetric_difference(s2))


# --------------------------------------------------
# 5. ISDISJOINT
# --------------------------------------------------

"""
isdisjoint() returns True if two sets have no
common elements.
"""

print("Is Disjoint:", s1.isdisjoint(s2))


# --------------------------------------------------
# 6. ISSUPERSET
# --------------------------------------------------

"""
issuperset() returns True if the set contains
all elements of another set.
"""

print("Is Superset:", s1.issuperset(s2))


# --------------------------------------------------
# 7. ISSUBSET
# --------------------------------------------------

"""
issubset() returns True if all elements of the set
are present in another set.
"""

print("Is Subset:", s1.issubset(s2))


# --------------------------------------------------
# 8. REMOVE METHOD
# --------------------------------------------------

"""
remove() deletes a specific element from the set.
Raises KeyError if the element does not exist.
"""

s1.remove(45)
print("After remove(45):", s1)


# --------------------------------------------------
# 9. POP METHOD
# --------------------------------------------------

"""
pop() removes and returns a random element
from the set because sets are unordered.
"""

s1.pop()
print("After pop:", s1)


# --------------------------------------------------
# 10. DEL KEYWORD
# --------------------------------------------------

"""
del deletes the entire set object from memory.
After deletion, accessing it causes NameError.
"""

del s2

# Uncommenting the next line will raise an error
# print(s2)


# --------------------------------------------------
# 11. SUMMARY
# --------------------------------------------------

"""
Key Takeaways:
- union() combines elements
- intersection() finds common elements
- symmetric_difference() finds unique elements
- isdisjoint(), issubset(), issuperset() compare sets
- remove() deletes a specific element
- pop() removes a random element
- del deletes the set completely

These methods are commonly asked in interviews
and widely used in real-world Python applications.
"""
