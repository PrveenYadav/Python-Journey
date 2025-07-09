# Dictionary in Python: Dictionaries are collections of key-value pairs.
# Dicionary is mutable, unordered, and indexed by keys

myDict = {
    "name": "Vicky",  
    "sir_name": "Choudhary",  
    "age": 19,
    "city": "Delhi",
    "is_student": False,
    "courses": ["Python", "Java", "C++"],
    "address": {
        "street": "123 Main St",
        "zip": "110001"
    }
}

print(myDict)
print(len(myDict))
print(myDict["name"])
print(myDict["age"])
print(myDict.get("city"))
print(myDict["courses"])
print(myDict["address"]["street"])
print(myDict.get("country", "Not Found"))  # Default value if key not found
print(myDict.get("city", "Not found"))
myDict["country"] = "India"
print(myDict)
myDict.pop("city")
print(myDict)
del myDict["sir_name"]
print(myDict)

print("\n")

print(myDict.keys())
print(myDict.values())
print(myDict.items())

print("\n")

for keys in myDict:
    print(keys, myDict[keys])

print("\n")

for key, value in myDict.items():
    print(key, value)


if "city" in myDict:
    print("city found")
else:
    print("Not found")

squared_num = {x:x**2 for x in range(11)}
print(squared_num)

squared_num.clear()
print(squared_num)
