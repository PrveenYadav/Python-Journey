### **Object-Oriented Programming (OOP) in Python - Brief Explanation**

**OOP** is a programming paradigm that organizes code into *objects* (real-world entities with **data** and **behavior**) instead of just functions. Python fully supports OOP with classes and objects.

---

### **4 Core Concepts of OOP:**
1. **Class**  
   - Blueprint/template for creating objects.  
   - Example:  
     ```python
     class Dog:  # Class
         pass
     ```

2. **Object (Instance)**  
   - A specific instance of a class.  
   - Example:  
     ```python
     my_dog = Dog()  # Object
     ```

3. **Attributes (Data)**  
   - Variables that belong to an object (e.g., name, age).  
   - Example:  
     ```python
     class Dog:
         def __init__(self, name):  # Constructor
             self.name = name  # Attribute

     my_dog = Dog("Buddy")
     print(my_dog.name)  # Output: "Buddy"
     ```

4. **Methods (Behavior)**  
   - Functions that belong to an object.  
   - Example:  
     ```python
     class Dog:
         def bark(self):  # Method
             print("Woof!")

     my_dog = Dog()
     my_dog.bark()  # Output: "Woof!"
     ```

---

### **Key OOP Principles:**
1. **Encapsulation**  
   - Bundling data (attributes) and methods into a single unit (class).  
   - Use `_` or `__` for private members (convention).  

2. **Inheritance**  
   - Child classes inherit attributes/methods from a parent class.  
   - Example:  
     ```python
     class Labrador(Dog):  # Inherits from Dog
         def fetch(self):
             print("Fetching ball!")
     ```

3. **Polymorphism**  
   - Same method behaves differently for different classes.  
   - Example:  
     ```python
     class Cat:
         def speak(self):
             print("Meow!")

     class Dog:
         def speak(self):
             print("Woof!")

     animals = [Cat(), Dog()]
     for animal in animals:
         animal.speak()  # Output: "Meow!", "Woof!"
     ```

4. **Abstraction**  
   - Hiding complex logic, exposing only essential features.  
   - Example: Using abstract classes (via `abc` module).  

---

### **Why Use OOP in Python?**
- **Modularity**: Break code into reusable objects.  
- **Reusability**: Inherit/extend existing classes.  
- **Scalability**: Easier to manage large projects.  

---

### **Example: Full OOP Program**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model

    def drive(self):  # Method
        print(f"{self.brand} {self.model} is driving!")

my_car = Car("Tesla", "Model S")
my_car.drive()  # Output: "Tesla Model S is driving!"
```

---

### **When to Use OOP?**
- Building complex systems (e.g., games, GUI apps).  
- When data and behavior are naturally linked (e.g., `User`, `Product` classes).  

---

Here’s another **fun and easy polymorphism example with emojis**—this time using **smartphone notifications** where different apps make different sounds/vibrations:

---

## **Example: Polymorphism**

```python
class App:
    def notify(self):
        pass  # Base method (to override)

class WhatsApp(App):
    def notify(self):
        print("💬 *Ding!* New WhatsApp message!")

class Instagram(App):
    def notify(self):
        print("📸 *Boop!* Instagram like received!")

class Email(App):
    def notify(self):
        print("✉️ *Bling!* You’ve got mail!")

# Polymorphic function
def trigger_notification(app: App):
    app.notify()  # Same call, different notifications!

# Usage
apps = [WhatsApp(), Instagram(), Email()]

for app in apps:
    trigger_notification(app)  # One function, many behaviors!
```

**Output:**
```
💬 *Ding!* New WhatsApp message!  
📸 *Boop!* Instagram like received!  
✉️ *Bling!* You’ve got mail!  
```

---

### **Why This is Polymorphism?**  
1. **Same Interface**: All apps use `.notify()`.  
2. **Different Actions**: Each app customizes its notification sound/emoji.  
3. **Extendable**: Add `Linkedin` or `Twitter` later without changing `trigger_notification()`.  

---

### **Real-World Analogy:**  
Like your phone’s **volume button** — it works universally, but each app "decides" what sound to make

---
## Example of `@staticmethod` Decorator or Decorators in Python

### **Example: A Simple Math Utility Class**
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b

    @staticmethod
    def multiply(a, b):
        """Static method to multiply two numbers."""
        return a * b

# Usage (no need to create an instance!)
print(MathUtils.add(5, 3))       # Output: 8
print(MathUtils.multiply(5, 3))   # Output: 15
```

---

### **Key Points:**
1. **`@staticmethod` Decorator**:  
   - Marks the method as static (no `self` or `cls` parameter needed).  
2. **No Instance Required**:  
   - Call it directly on the class (`MathUtils.add()`).  
3. **Use Cases**:  
   - Utility functions (e.g., math operations, data formatting).  
   - Grouping related functions in a class (without needing object state).  

---

### **Static Method vs. Regular Method:**
| Feature          | Static Method (`@staticmethod`) | Regular Method (`self`) |
|------------------|--------------------------------|------------------------|
| **Instance Needed?** | ❌ No | ✅ Yes |
| **Access to Instance/Class** | ❌ No | ✅ Yes (`self`, `cls`) |
| **Usage** | `Class.method()` | `obj.method()` |

---

### **Another Example: String Formatter**
```python
class StringUtils:
    @staticmethod
    def reverse(text):
        return text[::-1]

    @staticmethod
    def capitalize(text):
        return text.upper()

# Usage
print(StringUtils.reverse("hello"))     # Output: "olleh"
print(StringUtils.capitalize("world"))  # Output: "WORLD"
```

---

### **When to Use Static Methods?**
- When the method **doesn't depend on object state**.  
- For **organizing code** logically (e.g., grouping helper functions in a class).  

**Real-world analogy** Think of static methods like **tools in a toolbox**—you use them directly without needing to "activate" the toolbox first