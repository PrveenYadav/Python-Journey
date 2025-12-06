# https://leetcode.com/problems/merge-two-sorted-lists/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def arrToLinkedList(arr):
    tempHead = Node(None)
    curr = tempHead

    for num in arr:
        newNode = Node(num)
        curr.next = newNode
        curr = newNode # update current further

    head = tempHead.next
    return head

# Merge two sorted list : Brute Force
def solve(head1, head2): # O(nlogn), O(n)
    ans = [] # O(n) space
    curr = head1
    while curr is not None:
        ans.append(curr.val)
        curr = curr.next
    curr1 = head2
    while curr1 is not None:
        ans.append(curr1.val)
        curr1 = curr1.next
    
    ans.sort()
    head = arrToLinkedList(ans) # O(n) time
    return head

# Optimized using recursion: O(n+m), O(n+m)
def solve1(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.val <= head2.val:
        head1.next = solve1(head1.next, head2)
        return head1
    else:
        head2.next = solve1(head1, head2.next)
        return head2

# Optimal : O(n), O(1)
def solve2(head1, head2):
    dummy = Node(None)
    curr = dummy

    while head1 and head2:
        if head1.val < head2.val:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next

        curr = curr.next

    # curr.next = head1 or head2
    if head1: curr.next = head1
    if head2: curr.next = head2

    return dummy.next

 
# Print the Linked List values
def printData(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print(None)

if __name__ == "__main__":
   list1 = [1,2,4]
   list2 = [1,3,4] 

   head1 = arrToLinkedList(list1)
   head2 = arrToLinkedList(list2)

   newHead = solve(head1, head2)
   printData(newHead)

   newHead1 = solve1(head1, head2)
   printData(newHead1)

   newHead2 = solve2(head1, head2)
   printData(newHead2)