# Decorators in Python

# 1. Define a decorator
def my_decorator(func):
    def wrapper():
        print("Before the function runs")  # Added behavior
        func()  # Call the original function
        print("After the function runs")   # Added behavior
    return wrapper

# 2. Apply the decorator
@my_decorator
def say_hello():
    print("Hello!")

# 3. Call the decorated function
say_hello()


# Another Example
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()  # Run the original function
        end = time.time()
        print(f"⏱️ This took {end-start:.2f} seconds")
    return wrapper

@timer
def slow_function():
    print("Working...")
    time.sleep(2)  # Simulate slow work

slow_function()


# Another Example
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)  # Run the function 3 times
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
