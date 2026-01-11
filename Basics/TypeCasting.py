# 🔄 TYPECASTING IN PYTHON
# ----------------------
# Typecasting means converting one data type into another.
# Python supports two types:
# 1. Explicit Typecasting (done by the programmer)
# 2. Implicit Typecasting (done automatically by Python)

# ---------------------------------------
# Example from your original code
# ---------------------------------------

a = "1"
b = "1"

print(a + b)            # String concatenation
print(int(a) + int(b))  # Numeric addition

# Output:
# 11
# 2

# Explanation:
# "1" + "1"  -> "11"  (strings join)
# int("1") + int("1") -> 2 (numbers add)


# ---------------------------------------
# 1. Explicit Typecasting
# ---------------------------------------
# When we manually convert one data type into another

x = "10"
y = int(x)
print(y + 5)   # Output: 15

a = 5
b = float(a)
print(b)        # Output: 5.0
print(type(b))  # <class 'float'>

num = 100
text = str(num)
print(text)       # Output: 100
print(type(text)) # <class 'str'>


# ---------------------------------------
# 2. Implicit Typecasting
# ---------------------------------------
# When Python automatically converts one data type

m = 10     # int
n = 2.5    # float

result = m + n
print(result)       # Output: 12.5
print(type(result)) # <class 'float'>

# Python converted int to float automatically
# to avoid data loss.


# ---------------------------------------
# Summary
# ---------------------------------------
# Explicit Typecasting -> Done by programmer (int(), float(), str())
# Implicit Typecasting -> Done by Python automatically
