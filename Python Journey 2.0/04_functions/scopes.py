# scopes/namespaces in python

# globel variable : we can use this x = 46 whereever we want
x = 46

def func():
    x = 73
    def func2():
        print(x)
    return func2

result = func()
result()

# Example of closure
def first(x):
    def second(y):
        return x**y
    return second

f = first(2) # x = 2
g = first(3) # x = 3

print(f(3)) # y = 2 , it will print x**y = 2**3 = 2^3 = 2*2*2 = 8
print(g(2)) # y = 2 , it x**y = 3**2 = 3^2 = 3*3 = 9

