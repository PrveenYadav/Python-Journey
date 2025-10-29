# Linked List

# Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__ == "__main__":
    print("\n ------- Singly Linked List Implementaion -------")
    node1 = Node(3)
    node2 = Node(5)
    node3 = Node(13)
    node4 = Node(2)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    currentNode = node1
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")


# Doubly Linked List
class Node1:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

if __name__ == "__main__":
    print("\n ------- Doubly Linked List Implementaion -------")
    node1 = Node1(3)
    node2 = Node1(5)
    node3 = Node1(13)
    node4 = Node1(2)

    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    node3.next = node4

    node4.prev = node3

    print("\nTraversing forward:")
    currentNode = node1
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

    print("\nTraversing backward:")
    currentNode = node4
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.prev
    print("null")


# Circular Singly Linked List
class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__ == "__main__":  
    print("\n ------- Circular Singly Linked List Implementaion -------")
    node1 = Node2(3)
    node2 = Node2(5)
    node3 = Node2(13)
    node4 = Node2(2)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1

    currentNode = node1
    startNode = node1
    print(currentNode.data, end=" -> ") 
    currentNode = currentNode.next 

    while currentNode != startNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next

    print("...")


# Circular Doubly Linked List
class Node3:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

if __name__ == "__main__":
    print("\n ------ Circular Doubly Linked List Implementation ------")
    node1 = Node3(3)
    node2 = Node3(5)
    node3 = Node3(13)
    node4 = Node3(2)

    node1.next = node2
    node1.prev = node4

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    node3.next = node4

    node4.prev = node3
    node4.next = node1

    print("\nTraversing forward:")
    currentNode = node1
    startNode = node1
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next

    while currentNode != startNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("...")

    print("\nTraversing backward:")
    currentNode = node4
    startNode = node4
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev

    while currentNode != startNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.prev
    print("...")



print("\n ******* Linked List Operations ******* ")

# Traversal of Singly Linked List
def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

# Find the lowest value in Singly Linked list
def findLowestValue(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue

# Delete a specific node in singly linked list
def deleteSpecificNode(head, nodeToDelete):

    if head == nodeToDelete:
        return head.next

    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next

    if currentNode.next is None:
        return head

    currentNode.next = currentNode.next.next

    return head

# Insert a node in singly linked list
def insertNodeAtPosition(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode
    
    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head


if __name__ == "__main__":
    node1 = Node(7)
    node2 = Node(11)
    node3 = Node(3)
    node4 = Node(2)
    node5 = Node(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("Traversal: ", end="")
    traverseAndPrint(node1)

    print("Lowest value:", findLowestValue(node1))

    # Delete node4
    node1 = deleteSpecificNode(node1, node4)
    print("After deletion node4: ", end="")
    traverseAndPrint(node1)

    # Insert a new node with value 97 at position 2
    newNode = Node(97)
    node1 = insertNodeAtPosition(node1, newNode, 2)

    print("After insertion: ", end="")
    traverseAndPrint(node1)
