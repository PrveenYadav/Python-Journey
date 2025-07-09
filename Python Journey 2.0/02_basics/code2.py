# Lists in Python: Lists are ordered collections of items that can be of different types.
# Lists are mutable

myList = [1, 2, 4, 5, 6]
print(myList)
print(myList[1])
myList.append(7)
print(myList)

myList.insert(2, 3)
print(myList)

myList.remove(7)
print(myList)

myList.pop()
print(myList)

list2 = [14, 16, 12, 13, 11, 15]
list2.sort()
print(list2)
list2.reverse()
print(list2)
print(len(list2))

list2.clear()
print(list2)


list3 = ["Rahul", "Arvi", "Aman", "Ram", "Krishna"]
list3[2] = "Anuj"
print(list3)
list3[2:3] = ["Aman"]
print(list3)
list3.insert(1, "Ajay")
print(list3)

for i in list3:
    print(i, end=" ")

print('\n')

print(range(11))
squared_num = [x**2 for x in range(11)]
print(squared_num)

cube_num = [y**3 for y in range(6)]
print(cube_num)
