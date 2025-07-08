# Strings : Collection of characters
# Strings are Immutable in Python
name = "Ragnorok Thor"

print(type(name))
print(len(name))
print(name[2])
print(name[-1])
print(name[0:8])
print(name[:])
print(name[:8])
print(name[9:])
print(name[0:8:2])
print(name.find('h')) # we can even find or replace - words
print(name.replace('T', 'P'))
print("Thor" in name)
print("Phor" in name) # false: because string is Immutable
print(name.lower())
print(name.upper())

sirName = "           Thor   "
print(sirName.strip()) # Removes the extra spaces

tea = "ginger, lemon, milk, mint, masala, "
print(tea.split(", ")) #converting into list basis on comman and space(", ")

hero = "Iron man man man"
print(hero.count("man"))

chai_type = "Milk"
quantity = 2
order = "I ordered {} cup of {} tea"
print(order.format(quantity, chai_type))

# Converting list into string
heros_list = ["Iron man", "Thor", "Hulk", "Captain America", "Spider man"]
print(", ".join(heros_list))

for c in name:
    print(c)
