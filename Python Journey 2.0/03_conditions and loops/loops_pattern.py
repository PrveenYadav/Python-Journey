# Pattern printing in python 

n = int(input("Enter the number: "))

# Pattern-1
for i in range(1, n+1):
    print(5*'*')

# Pattern-2
for i in range(1, n+1): # for rows
    for j in range(1, i+1): # for columns
        print(j, end="")  # we can print(i) or j for another pattern
    print() #adds a newline after each row is complete.

# Pattern-3
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(64+j), end="") # ASCII val of 65 = 'A'
    print()

# Pattern-4
for i in range(1, n+1):
    # printing spaces
    print(" " * (n-i), end="")

    # printing digits
    for j in range(1, 2*i):
        print(j, end="")
    print()