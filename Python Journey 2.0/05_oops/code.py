# Object Oriented Programming in Python

# creating a class
class Obj:
    # constructor: A constructor in Python is a special method __init__() that automatically initializes an object's attributes when it is created.
    def __init__(self, brand, model): #self is like this keyword in c++ or javascript
        self.brand = brand # self.brand = class's attribute/variable, and brand = parameter passed here
        self.model = model

my_obj = Obj("Mercedes Benz", "s-class") # creating an object
print(my_obj.brand, end=" - ")
print(my_obj.model)

new_obj = Obj("Toyota", "Fortuner Legender")
print(new_obj.brand)
print(new_obj.model)


# Another class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    # By declaring self it can access any attributes of class, But in c++ we keep empty, because it automatically access parrent attributes in child functions
    def fullname(self):
        return f"{self.brand} {self.model}"
    

my_car = Car("BMW", "7-series")
print(my_car.fullname())


# Example of Inheritance
# Inheriting attributes(brand, model) from another class(Car class)
class CarOne(Car):
    def __init__(self, brand, model, price):
        # self.brand = brand
        # self.model = model
        super().__init__(brand, model)
        self.price = price
    
    def car_details(self):
        return f"{self.brand} {self.model} - {self.price}"


my_obj2 = CarOne("Lamborgini", "Urus", "5 crore")
print(my_obj2.car_details())
print(my_obj2.model) # we have the access of attributes
print(my_obj2.fullname()) # we also have the access of functions

# checking the instance of class
print(isinstance(my_car, Car))
print(isinstance(my_obj2, Car))
print(isinstance(my_obj2, CarOne))
print(isinstance(my_car, CarOne))



# Example of Encapsulation
class Students:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # now we can't access age attribute outside of the class

    # getter function
    def get_age(self):
        return self.__age # __age
    
student1 = Students("Vicky", 19)
print(student1.name, end=" - ")
# print(student1.age) #we don't have access of age - it's private
print(student1.get_age())


# Example of Polymorphism
class App:
    def notify(self):
        pass  # Placeholder/do nothing and we can override it whenever we want

class WhatsApp(App):
    def notify(self):
        print("💬 Ding! New WhatsApp message")

class Instagram(App):
    def notify(self):
        print("📸 Boop! Instagram like received")

class Email(App):
    def notify(self):
        print("✉️  Bling! You’ve got mail")

# Polymorphic function
def trigger_notification(app: App):
    app.notify()  # Same call, different notifications!

# Usage
apps = [WhatsApp(), Instagram(), Email()]

for app in apps:
    trigger_notification(app)  # One function, many behaviors!


'''
Why This is Polymorphism?
Same Interface: All apps use .notify().

Different Actions: Each app customizes its notification sound/emoji.

Extendable: We can add Linkedin or Twitter later without changing trigger_notification().

Real-World Analogy:
Like your phone’s volume button — it works universally, but each app "decides" what sound to make! 
'''


# Example of @staticmethod Decorators
class MathUtils:
    #Static method to add two numbers
    @staticmethod
    def add(a, b):
        return a + b

    #Static method to multiply two numbers
    @staticmethod
    def multiply(a, b):
        return a * b

# Usage (no need to create an instance/object)
print(MathUtils.add(5, 3))       
print(MathUtils.multiply(5, 3))
