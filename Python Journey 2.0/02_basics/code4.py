# Tuples in Python are immutable sequences, typically used to store collections of heterogeneous data.
# They are defined by enclosing elements in parentheses, separated by commas.
# Tuples vs Lists: Tuples are immutable, meaning once created, their elements cannot be changed, while lists are mutable and can be modified.
# Example of a tuple
my_tuple = (1, 2, 3, "hello", True)

# Accessing elements in a tuple
print(my_tuple)
print(len(my_tuple))
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: hello

tuple_two = ("Tony Stark", 88, "Vicky", False, "Spider Man", "Vicky")
print(tuple_two)
print(tuple_two.count("Vicky"))

add_tuples = my_tuple + tuple_two
print(add_tuples)
print(len(add_tuples))

if "Vicky" in tuple_two:
    print("Yes")
