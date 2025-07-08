# In python communicty mostly file name written with underscore (first_program.py)
# Programming: Creating a set of instructions - that tells a computer how to perform a task
# Program: set of instructions
# compiler: Converts High level language(C++, Python, java, etc) into Low level language(Machine code(in the form of 0 and 1))
# Source code -> Byte code -> machine code
# compiler converts source code into byte code then interpreter converts byte code into machine code : because interpreter cheks the program that it is working perfectly or not


print("Hello World")

a = 20
b = 40
sum = a+b
print("Sum is: ", sum)

name = input("Enter your name: ")
print("Your name is:", name)
print("Length of name: ", len(name))


# age = input("Enter your age: ")
# age = int(age) # converting into integer
# Or Directly 
age = int(input("Enter your age: "))

if(age >= 18):
    print("You can vote")
else:
    print("You are underage")


arr = [1, 2, 3]
print("Array is: ", arr)
print("Length of Array is: ", len(arr))

def solve(des):
    print("I am a function in python")

des = "Get job in Atlassian"
print(des)
print("Length of des: ", len(des))
print("Type of des: ", type(des))

solve(des)
