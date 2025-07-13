# **Python Decorators Explained Briefly with Example**

A decorator in Python is a **function that modifies another function** (or method/class) without changing its source code. It "wraps" the original function to add extra behavior.

---

## **How Decorators Work**
1. **Take a function** as input.
2. **Add new functionality** before/after the original function runs.
3. **Return the modified function**.

---

## **Example 1: Basic Decorator**
```python
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
```

**Output:**
```
Before the function runs  
Hello!  
After the function runs  
```

---

## **Example 2: Decorator with Arguments**
```python
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
```

**Output:**
```
Hello, Alice!  
Hello, Alice!  
Hello, Alice!  
```

---

## **Example 3: Built-in Decorators**
Python has built-in decorators like:
- `@staticmethod` (for class-independent methods)
- `@classmethod` (for class methods)
- `@property` (for getter/setter methods)

```python
class MyClass:
    @staticmethod
    def static_method():
        print("I don't need 'self' or 'cls'!")
```

---

### **Key Takeaways**
✔ **Decorators modify functions** without changing their code.  
✔ They use `@decorator_name` syntax.  
✔ Common uses: logging, timing, access control, caching.  

**Real-world analogy :** Think of decorators like **"wrapping paper"** around a gift (function)—it adds something extra without changing the gift itself! 🎁