# https://leetcode.com/problems/reverse-linked-list/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Print the Linked List
def printData(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" -> ")
        curr = curr.next
    print(None)

# Insert a node at beginning
def insertAtBeginning(head, data):
    newNode = Node(data)
    newNode.next = head
    head = newNode
    return head

# Insert at End
def insertAtEnd(head, data):
    newNode = Node(data)
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = newNode
    newNode.next = None
    return head

# search middle using fast and slow pointer
def middleElement(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.data

# ----------------------------------------------------------

# Helper function for brute force solution
def arrToLinkedList(arr):
    head = Node(arr[-1]) # the last element of the array 
    curr = head

    for i in range(len(arr)-2, -1, -1):
        newNode = Node(arr[i])
        curr.next = newNode
        curr = newNode
    return head

# Reverse the linked list : Brute Force : O(n), O(n)
def reverseLinkedList(head):
    if not head or not head.next: return head

    arr = []
    curr = head
    while curr is not None:
        arr.append(curr.data)
        curr = curr.next
    
    newHead = arrToLinkedList(arr)
    return newHead

# Optimal : O(n), O(1)
def reverseOptimal(head):
    if not head or not head.next: return head

    prev = None
    curr = head

    while curr: # while curr is not None/Null
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    head = node1
    printData(head)

    newHead = insertAtBeginning(head, 8)
    printData(newHead)
    
    newHead1 = insertAtEnd(head, 3)
    printData(newHead1)

    print("middle is: ", middleElement(newHead1))

    # --------------------- Reverse Linked List ------------------------
    reversedListHead = reverseLinkedList(head)
    print("Reverse Linked List - Brute force: ", end="")
    printData(reversedListHead)

    reverseHead = reverseOptimal(head)
    print("Reverse Linked List - Optimal: ", end="")
    printData(reverseHead)
