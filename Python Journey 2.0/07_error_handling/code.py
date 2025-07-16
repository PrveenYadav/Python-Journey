# Error handling in Python
'''
Common Exception Types:
ValueError: When a function receives an argument of correct type but inappropriate value
TypeError: When an operation is performed on an object of inappropriate type
IndexError: When a sequence subscript is out of range
KeyError: When a dictionary key is not found
FileNotFoundError: When a file or directory is requested but doesn't exist
ZeroDivisionError: When dividing by zero
Exception: Catches all exceptions (use sparingly)
'''


file = open('new.txt', 'w')

try:
    file.write("Learning Error handling")
finally:
    file.close()

# both syntax are doing same thing, and it depends on preference which syntax you choose
with open('new.txt', 'w') as file:
    file.write('Recently learning error handling in python')


#Another Example
try:
    with open("test.txt", "w") as file:
        content = file.write("Python Journey Ongoing")
        print(content)
except FileNotFoundError as e:
    print(f"Error: {e}")


try:
    file = open("test.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully!")
    print(f"File content length: {len(data)}")
    print("Data in file: ", data)
finally:
    if 'file' in locals():
        file.close()
