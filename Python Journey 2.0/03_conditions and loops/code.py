# Conditions in Python
name = "Hello"

for c in name:
    print(c, end=" ")

print("\n")

# Problem-1
# age = int(input("Enter your age: "))
age = 12

if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
else:
    print("Senior")


# Problem-2
age_one = 22
day = "Wednesday"

price = 12 if age_one >= 18 else 8

if day == "Wednesday":
    price = price-2
    # price -= 2

print("Price is: ", price)


# Problem-3
fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")


# Problem-5
weather = "Sunny"

if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":
    activity = "Build a snowman"

print(activity)


# Problem-6
order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order: ", coffee)


# Problem-7
password = "Secure3P@ss"
password_length = len(password)

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is: ", strength)


# Problem-8
year = 2023

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print( year, " is a leap year")
else:
    print(year, "is NOT a leap year")

