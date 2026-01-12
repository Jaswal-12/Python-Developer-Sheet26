# ✂️ STRING SLICING IN PYTHON
# -------------------------
# String slicing is used to get a part (substring) of a string.
# Syntax:
# string[start : end]
# start -> starting index (included)
# end   -> ending index (excluded)

name = "karan,jaswal"

# ---------------------------------------
# Basic Slicing
# ---------------------------------------

print(name[0:3])   # kar
print(len(name))  # length of string
print(name[:3])   # same as name[0:3]
print(name[1:])   # from index 1 to end

# ---------------------------------------
# Negative Slicing
# ---------------------------------------
# Negative index counts from the end of the string

print(name[0:-3])   # removes last 3 characters
print(name[-4:-1])  # extracts characters from back

# ---------------------------------------
# More Examples
# ---------------------------------------

text = "PythonProgramming"

print(text[0:6])     # Python
print(text[6:])      # Programming
print(text[-11:])   # Programming
print(text[:6])     # Python
print(text[-11:-1]) # Programmin

# ---------------------------------------
# Using Step Value
# Syntax: string[start : end : step]
# ---------------------------------------

word = "abcdefg"

print(word[0:7:2])   # a c e g
print(word[1:7:2])   # b d f
print(word[::-1])   # reverse the string

# ---------------------------------------
# Real-life Example
# ---------------------------------------

email = "karan@gmail.com"

username = email[:5]
domain = email[6:]

print("Username:", username)
print("Domain:", domain)
