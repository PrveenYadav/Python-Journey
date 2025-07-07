#Basic input and output
name = input("What is your name: ")
print("My name is " + name) #concatination

#type conversion : str to int
old_age = input("Enter your age: ")
new_age = int(old_age) + 2
print(new_age)

#Printing sum
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

sum = int(num1) + int(num2)
print("Sum is : " + str(sum))

#String
name = "Tony Stark"
print(name.find('t')) #returns index
print(name.replace("Tony", "Ironman")) #we can replace char or string like replace T from M
print("Stark" in name) #Tells this string exist or not in the variable name

#Operators
print(2 + 5)
print(2 < 5)

#Conditional statements
age = 88

if age >= 18: 
    print("You are adult")
    print("You can vote")
elif age < 18 and age > 3:
    print("You are in school")
else:
    print("Not a valid age")


#Basic Calculator in Python
first = input("Enter first number: ")
operator = input("Enter operator(+, -, *, /, %): ")
second = input("Enter second number: ")

first = int(first) #Type conversion str to int
second = int(second)

if operator == '+': 
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    print(first / second)
elif operator == '%':
    print(first % second)
else:
    print("Invalid operator")


#Range function
numbers = range(5)
print(numbers)

#while loop
i = 1
while i <= 5: 
    print(i * "hello ") #we can print stars at the place of hello 
    i = i+1

#for loop
for i in range(5):
    #print(i) #it will print 0 to 4
    print(i + 1) #it will print 1 to 5


#lists in python 
marks = [95, 97, 94]
print(marks)
print(marks[1])
print(marks[-3])
print(marks[1:3])

for score in marks:
    print(score)

marks.append(99)
print(marks)

marks.insert(0, 99)
print(marks)

print(len(marks))

marks.clear()
print(marks)

#Doubles in python
marks2 = (95, 97, 94, 98, 96)

print(marks2.count(94))
print(marks2.index(98))

#sets in python
marks3 = {95, 97, 97, 97, 85}
print(marks3) #only print unique values

#Functions in Python
def print_sum(num1, num2):
    print(num1 + num2)

print_sum(2, 5) #Function call and passing parameters
