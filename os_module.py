"""
os_module_demo.py

This file demonstrates the use of the 'os' module in Python.

The 'os' module provides a way of using operating system dependent functionality like:
- Reading or writing to the file system
- Managing directories
- Getting environment variables
- Working with file paths
"""

import os

# ---------------------------
# 1. Getting Current Working Directory
# ---------------------------
current_dir = os.getcwd()  # Returns the current working directory
print("Current Working Directory:", current_dir)

# ---------------------------
# 2. Changing Directory
# ---------------------------
# os.chdir(path) can change the current working directory
# Uncomment the next lines to test changing directory
# new_path = "C:\\Users\\Karan\\Documents"  # Change this path as per your system
# os.chdir(new_path)
# print("Directory changed to:", os.getcwd())

# ---------------------------
# 3. Listing Files and Directories
# ---------------------------
files_and_dirs = os.listdir(current_dir)  # List all files and directories in current_dir
print("Files and Directories in Current Directory:", files_and_dirs)

# ---------------------------
# 4. Creating Directories
# ---------------------------
# os.mkdir(path) creates a single directory
# os.makedirs(path) creates multiple nested directories
new_folder = "TestFolder"
if not os.path.exists(new_folder):  # Check if folder exists
    os.mkdir(new_folder)
    print(f"Directory '{new_folder}' created successfully.")
else:
    print(f"Directory '{new_folder}' already exists.")

# ---------------------------
# 5. Removing Directories
# ---------------------------
# os.rmdir(path) removes a single empty directory
# os.removedirs(path) removes nested directories
# Uncomment to remove the directory we just created
# os.rmdir(new_folder)
# print(f"Directory '{new_folder}' removed successfully.")

# ---------------------------
# 6. Checking if Path Exists
# ---------------------------
path_check = os.path.exists(new_folder)
print(f"Does '{new_folder}' exist? ->", path_check)

# ---------------------------
# 7. File Operations
# ---------------------------
# Checking if a file exists
file_name = "example.txt"
if not os.path.exists(file_name):
    # Creating a file
    with open(file_name, 'w') as f:
        f.write("Hello, this is an example file using os module.\n")
    print(f"File '{file_name}' created successfully.")

# Removing a file
# Uncomment below to delete the file
# os.remove(file_name)
# print(f"File '{file_name}' removed successfully.")

# ---------------------------
# 8. Environment Variables
# ---------------------------
# Get environment variables
user = os.getenv("USERNAME")  # On Windows, it gives the current username
home = os.getenv("HOME")      # On Linux/Mac, gives the home directory
print("Current User:", user)
print("Home Directory:", home)

# Set environment variables (temporary for session)
os.environ["MY_VAR"] = "12345"
print("Custom Environment Variable:", os.environ.get("MY_VAR"))

# ---------------------------
# 9. File Path Operations
# ---------------------------
file_path = os.path.join(current_dir, "example.txt")  # Join paths safely
print("File Path using os.path.join:", file_path)

# Split path into directory and file
dir_name, base_name = os.path.split(file_path)
print("Directory:", dir_name)
print("File Name:", base_name)

# Get file extension
file_name_only, file_ext = os.path.splitext(base_name)
print("File Name without Extension:", file_name_only)
print("File Extension:", file_ext)

# ---------------------------
# 10. Miscellaneous
# ---------------------------
# Get the OS name
print("OS Name:", os.name)  # 'nt' for Windows, 'posix' for Linux/Mac

# Get absolute path
abs_path = os.path.abspath("example.txt")
print("Absolute Path of example.txt:", abs_path)

# Check if it is a file or directory
print("Is 'example.txt' a file?", os.path.isfile("example.txt"))
print("Is 'TestFolder' a directory?", os.path.isdir("TestFolder"))

# End of os_module_demo.py
