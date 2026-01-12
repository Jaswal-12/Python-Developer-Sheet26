# 🧵 STRINGS IN PYTHON
# ------------------
# A string is a sequence of characters.
# Anything enclosed in single quotes (' ') or double quotes (" ") is a string.
# Strings in Python are IMMUTABLE (they cannot be changed after creation).

# ---------------------------------------
# Creating Strings
# ---------------------------------------

name = "Karan"
age = "21"
friend = 'Abhay'

print(name)
print(age)
print(friend)

# ---------------------------------------
# String Concatenation
# ---------------------------------------

print(name + friend)      # Joining two strings
print(name + " " + friend)

# ---------------------------------------
# Multiline Strings
# ---------------------------------------
# We use triple quotes (''' or """) to write multiple lines

message = '''Hello,
How are you?
Welcome to Python Strings!'''

print(message)

# ---------------------------------------
# Accessing Characters using Index
# ---------------------------------------

print(name[0])   # K
print(name[1])   # a
print(name[2])   # r
print(name[3])   # a
print(name[4])   # n

# ---------------------------------------
# Looping through a String
# ---------------------------------------

for character in name:
    print(character)

# ---------------------------------------
# String Length
# ---------------------------------------

print("Length of name:", len(name))

# ---------------------------------------
# String Methods
# ---------------------------------------

text = "python programming"

print(text.upper())      # PYTHON PROGRAMMING
print(text.lower())      # python programming
print(text.capitalize())# Python programming
print(text.replace("python", "Java"))
print(text.split())      # ['python', 'programming']

# ---------------------------------------
# Checking if a word exists
# ---------------------------------------

sentence = "I am learning Python"

print("Python" in sentence)   # True
print("Java" in sentence)     # False

# ---------------------------------------
# Strings are Immutable
# ---------------------------------------

# name[0] = "R"   ❌ This will give an error
# Strings cannot be changed directly

# Instead:
new_name = "R" + name[1:]
print(new_name)
