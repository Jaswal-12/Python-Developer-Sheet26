"""
Python Dictionary – Complete Explanation with Examples
====================================================

This file explains:
1. What dictionaries are in Python
2. Key properties of dictionaries
3. Common dictionary methods
4. Iteration techniques
5. Real-world use cases

Author: Karan I
"""

# --------------------------------------------------
# 1. WHAT IS A DICTIONARY?
# --------------------------------------------------

"""
A dictionary in Python is a collection of key-value pairs.

Key characteristics:
- Ordered (Python 3.7+)
- Mutable (can be changed)
- Keys must be unique and immutable
- Values can be of any data type
"""


# Example dictionary
dic = {
    "Karan": "Jaswal",
    "hello": "world"
}

print("Dictionary:", dic)


# --------------------------------------------------
# 2. ACCESSING VALUES
# --------------------------------------------------

# Using square brackets
print("Value using key:", dic["Karan"])

# Using get() method (safe access)
print("Value using get():", dic.get("Karan"))

# get() does not raise error if key is missing
print("Missing key using get():", dic.get("age"))


# --------------------------------------------------
# 3. ITERATING OVER A DICTIONARY
# --------------------------------------------------

# Iterating over keys
print("Keys:")
for key in dic.keys():
    print(key)

# Iterating over values
print("Values:")
for value in dic.values():
    print(value)

# Iterating over key-value pairs
print("Items:")
for key, value in dic.items():
    print(key, "->", value)


# --------------------------------------------------
# 4. ADDING AND UPDATING VALUES
# --------------------------------------------------

# Adding a new key-value pair
dic["age"] = 21
print("After adding age:", dic)

# Updating an existing value
dic["hello"] = "Python"
print("After updating value:", dic)


# --------------------------------------------------
# 5. REMOVING ELEMENTS
# --------------------------------------------------

# pop(): removes a key-value pair
removed_value = dic.pop("age")
print("Removed value:", removed_value)
print("After pop:", dic)

# popitem(): removes last inserted item
last_item = dic.popitem()
print("Popped item:", last_item)
print("After popitem:", dic)


# --------------------------------------------------
# 6. DICTIONARY METHODS
# --------------------------------------------------

print("All keys:", dic.keys())
print("All values:", dic.values())
print("All items:", dic.items())


# --------------------------------------------------
# 7. REAL-WORLD USE CASES
# --------------------------------------------------

"""
Dictionaries are widely used in real-world applications such as:
- Storing user profiles
- Configuration settings
- JSON data handling
- Database-like structures
"""

# Example: Student record
student = {
    "name": "Karan",
    "roll_no": 101,
    "course": "B.Tech",
    "skills": ["Python", "AWS", "Web Development"]
}

print("Student Name:", student["name"])
print("Student Skills:", student["skills"])


# --------------------------------------------------
# 8. SUMMARY
# --------------------------------------------------

"""
Key Takeaways:
- Dictionaries store data in key-value pairs
- Keys must be unique and immutable
- Fast data access using keys
- Very useful for structured and real-world data
- Commonly asked topic in Python interviews
"""
