# function definition in python

# Problem-1
def calculate_square(num): #parameter = reference of val
    return num**2

print(calculate_square(9)) #argument = actual val

# Problem-2
def add_two(x, y):
    return x+y

print(add_two(2, 9))


# Problem-3
def multiply(a, b):
    return a * b

print(multiply(12, 5))
print(multiply('V', 5))


# Problem-4
def circle_calculation(radius):
    area = 2 * 3.14 * radius
    circumference = 3.14 * (radius*radius)
    return area, circumference

# print(circle_calculation(5))
a, c = circle_calculation(5)
print("Area is: ", round(a, 2), "and Circumference is: ", round(c, 2)) #round(31.400000000000002, 2) it will convert into 31.40


# Problem-5
def greet_user(name):
    if name:
        print("Nice to meet you", name)
    else:
        print("Nice to meet you sir")

greet_user("Vicky")

# or another way
def greet(name = "Sir"):
    return "Hello, " + name

print(greet())


# Problem-6 : cube of a number
# using lambda function : we use lambda for one-time-operation
cube = lambda x: x**3
print(cube(3))

# using normal function
def cube_is(x):
    return x**3
print(cube(5))


# Problem-7
def sum_all(*args): #will handle all(*) arguments
    return sum(args)

print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4))
print(sum_all(1, 2, 3, 4, 5, 6))

# Problem-8 : kwargs = for handling multiple key, val pairs aguments
def print_kvargs(**kwargs):
    for key, val in kwargs.items():
        print(f"{key} : {val}") # f = for formating

print_kvargs(name="Anuj", age=25, city="delhi")


# Problem-9
# using of yield
def even_generator(n):
    for i in range(2, n+1, 2): # range(start, stop, step)
        yield i

for num in even_generator(10):
    print(num)

# without using yield
def even_nums(n):
    for i in range(2, n+1, 2):
        print(i)
even_nums(9)


# Problem-10
def factorial(n):
    #base case
    if(n == 0):
        return 1 # 0! = 1
    else:
        #recursive call
        return n * factorial(n-1)

print("Factorial is: ", factorial(5))

# Dry Run: 5! = 5*4*3*2*1 = 120
# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1 * 0!
# 0 ---> base case reached(return 1, because 0! = 1), exit now
