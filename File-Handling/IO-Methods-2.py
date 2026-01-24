"""
FILE POINTER OPERATIONS IN PYTHON
---------------------------------
This program explains:

1. tell()   -> Returns current file pointer position
2. seek()   -> Moves the file pointer to a specific position
3. read() with size
4. truncate()
5. readable(), writable(), seekable()
6. close() and closed attribute

Author: Karan
"""

# ==========================================================
# 1. tell() - Get current file pointer position
# ==========================================================

with open("pointer_demo.txt", "w+") as f:
    f.write("Hello Python File Handling")

    # tell() returns current cursor position
    position = f.tell()
    print("Current pointer position after write:", position)

# ==========================================================
# 2. seek() - Move file pointer
# ==========================================================
# seek(offset, reference_point)
# reference_point:
# 0 -> beginning of file (default)
# 1 -> current position
# 2 -> end of file

with open("pointer_demo.txt", "r") as f:
    # Move pointer to beginning
    f.seek(0)

    # Read first 5 characters
    print("\nFirst 5 characters:", f.read(5))

    # Show pointer position
    print("Pointer position:", f.tell())

    # Move pointer again
    f.seek(6)
    print("After seek(6):", f.read())

# ==========================================================
# 3. seek() with offset from end
# ==========================================================

with open("pointer_demo.txt", "r") as f:
    # Move pointer to 6 characters before end
    f.seek(-6, 2)
    print("\nLast 6 characters:", f.read())

# ==========================================================
# 4. read(size) - Read fixed number of characters
# ==========================================================

with open("pointer_demo.txt", "r") as f:
    print("\nRead 10 characters:", f.read(10))
    print("Pointer position after read:", f.tell())

# ==========================================================
# 5. truncate() - Resize the file
# ==========================================================
# truncate(size) cuts the file to given size

with open("truncate_demo.txt", "w+") as f:
    f.write("This content will be truncated")
    f.truncate(10)

with open("truncate_demo.txt", "r") as f:
    print("\nAfter truncate:", f.read())

# ==========================================================
# 6. File capability methods
# ==========================================================

with open("pointer_demo.txt", "r") as f:
    print("\nFile readable():", f.readable())
    print("File writable():", f.writable())
    print("File seekable():", f.seekable())

# ==========================================================
# 7. closed attribute
# ==========================================================

f = open("pointer_demo.txt", "r")
print("\nFile closed before close():", f.closed)
f.close()
print("File closed after close():", f.closed)

print("\nProgram finished successfully.")
