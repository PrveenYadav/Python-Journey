import math
import random

print(math.floor(-2.8))
print(math.trunc(-2.8))
print((2 + 1j) * 3) #python can do calculation with imaginary numbers

# Python can handle all type of numbers like: decimal(base 10, values(0 - 9)), octal(base 8, values(0 - 7)), hexa(base 16), binary(base 2)

print(hex(10))
print(oct(10))
print(bin(10))
print(int(3.14))

print(int('64', 8)) # 8 means converting in octal octal(base 8)
print(int('64', 16))
print(int('10000', 2))


# playing with random
print(random.random())
print(math.floor(random.random()*100)) #generating random number from 0 to 100

print(random.randint(1, 10)) #integer random number 1 to 10

chai_list = ["Ginger tea", "Lemon tea", "Milk tea", "Mint tea", "Masala tea"]
print(random.choice(chai_list))

random.shuffle(chai_list)
print(chai_list)


# sets in python : sets stores only unique values
set_one = {1, 3, 3, 4, 6}

print(set_one)
print(set_one & {1, 3, 8}) #Intersection
print(set_one | {1, 3, 7}) #Union

# Boolean
print(True == 1)
print(True + 4)

first = 10
print(first is 10)