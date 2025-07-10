# Loops in Python

# Problem-1
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count = 0

for i in numbers:
    if i >= 0:
        count += 1
    
print("Positive numbers:", count)

# Problem-2
n = 10
sum_is = 0

for i in range(n+1):
    if i%2 == 0:
        sum_is += i

print("Sum is:", sum_is)

# Problem-3
num = 7

for i in range(1, 11):
    if(i == 5):
        continue
    print(num, 'x', i, '=', num*i)


# Problem-4
my_str = "Vicky"
reversed_str = ""

for i in my_str:
    reversed_str = i + reversed_str

# Dry Run in which iteration -------->
# 1 -> rev_str = V + ""   = V
# 2 -> rev_str = i + V    = iV
# 3 -> rev_str = c + iV   = ciV
# 4 -> rev_str = k + ciV  = kciV
# 5 -> rev_str = y + kciV = ykciV
 
print(reversed_str)


# Problem-5
name = "teekter"
count_is = 0

for c in name:
    if name.count(c) == 1:
        print(c)
        break


# Problem-6
nums_is = 5
fact = 1

for i in range(1, nums_is+1):
    fact = fact * nums_is
    nums_is -= 1

print("Factorial is:",fact)

# Using while loop
while nums_is > 0:
    fact *= nums_is
    nums_is -= 1
print(fact)


# Problem-7
while True:
    num = int(input("Enter number between 1 to 10: "))
    if num >= 1 and num <= 10:
        print("Ya, You get it!")
        break
    else:
        print("Oho, Try again bro")

# Problem-8
nums_is = 8
is_prime = True

if nums_is > 1:
    for i in range(2, nums_is):
        if(nums_is % i == 0):
            is_prime = False
            break

print(is_prime)


# Problem-9
items = ["apple", "banana", "orange", "apple", "mango"]

my_set = set()

for item in items:
    if item in my_set:
        print("Duplicate item is: ", item)
        break
    else:
        my_set.add(item)

# Problem-10
import time

wait_time = 1
attempts = 0
max_retries = 4

while attempts < max_retries:
    print("Attempt", attempts + 1, "- wait time", wait_time, )
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
