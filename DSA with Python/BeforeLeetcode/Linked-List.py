# Linked List Implementation

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
    
# Create Linked List using array  
def createList(arr):
  if not arr: return None
  head = Node(arr[0])
  curr = head
  
  for i in arr[1:]:
    curr.next = Node(i)
    curr = curr.next
  
  return head
  
# Traverse Linked List iterative
def traverseList(head):
  curr = head
  while curr:
    print(curr.data, end="->")
    curr = curr.next
  print("null")
  
def traverseListRec(head):
  if head is None: return
  print(head.data, end="->")
  traverseListRec(head.next)

# Searching in Singly Linked List
def searchVal(head, key):
  curr = head
  while curr:
    if curr.data == key:
      return True
    curr = curr.next
  
  return False

# Insertion at beginning
def insertAtBegin(head, val):
  newNode = Node(val)
  newNode.next = head
  return newNode

# Insertion at end
def insertAtEnd(head, val):
  newNode = Node(val)
  if not head: return newNode
  
  curr = head
  while curr.next:
    curr = curr.next
  curr.next = newNode
  return head

# Deletion at beginning
def deleteAtBegin(head):
  if not head: return None
  newHead = head.next
  return newHead

# Deletion at end
def deleteAtEnd(head):
  if not head: return None
  if not head.next: return None
  
  curr = head
  while curr.next.next:
    curr = curr.next
  curr.next = None
  return head

# Middle of Linked List || Two Pointer
def middleOfList(head):
  slowptr = head
  fastptr = head
  
  while fastptr is not None and fastptr.next is not None:
    fastptr = fastptr.next.next
    slowptr = slowptr.next
  return slowptr.data

# Detect a cycle
def cycleDetect(head):
  slow = head
  fast = head
  while slow and fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast: return True
    
  return False
  
  
if __name__ == "__main__":
  
  arr = [1, 2, 4, 2, 7, 0]
  createList(arr)
  head = createList(arr)
  
  traverseList(head)
  
  # Normal creation
  print('\n')
  node1 = Node(9)
  node2 = Node(8)
  node3 = Node(7)
  node4 = Node(6)
  node5 = Node(5)
  node1.next = node2
  node2.next = node3
  node3.next = node4
  node4.next = node5
  
  traverseListRec(node1)
  
  
  # Basic Linked List Operations 
  print('\n')
  print(searchVal(node1, 6))
  
  newHead = insertAtBegin(head, 3)
  traverseList(newHead)
  
  newHead1 = insertAtEnd(newHead, 5)
  traverseList(newHead1)
  
  newHead2 = deleteAtBegin(newHead1)
  traverseList(newHead2)
  
  newHead3 = deleteAtEnd(newHead2)
  traverseList(newHead3)
  
  print(middleOfList(node1))
  print(cycleDetect(node1))
  