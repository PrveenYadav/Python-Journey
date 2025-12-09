# https://leetcode.com/problems/reorder-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Brute force : O(n), O(n)
    def solve(self, head: Optional[ListNode]) -> None:
        if not head: return
        
        nodes = []
        curr = head
        while curr:
            nodes.append(curr) # instead of curr.val appending obj/node
            curr = curr.next

        i, j = 0, len(nodes)-1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            # if i == j: break
            if i >= j: break # if reach middle then break
            nodes[j].next = nodes[i]
            j -= 1
        
        nodes[i].next = None # terminate the list

# ----------- Helper functions for Optimal Solution --------------------
    # middle : O(n), O(1)
    def middle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # reverse : O(n), O(1)
    def reverse(self, head):
        if not head or not head.next: return head

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    # merge : O(n), O(1)
    def merge(self, l1, l2) -> None:
        while l2.next: 
            # Temporary store next pointers
            tmp1 = l1.next
            tmp2 = l2.next
            
            # Re-link
            l1.next = l2
            l2.next = tmp1
            
            # Move forward
            l1 = tmp1
            l2 = tmp2

    # Optimal : O(n), O(1)
    def solve1(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return

        # step-1: split the list
        mid = self.middle(head)
        
        # step-2: reverse the second half
        rev_head = self.reverse(mid)
        
        # step-3: Merge the two halves
        self.merge(head, rev_head)


    # Optimal and clear: O(n), O(1) 
    def solve2(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return

        # step-1: middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # step-2: reverse second half
        second = slow.next
        slow.next = None # cut the list
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # step-3: merge both halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

    def reorderList(self, head: Optional[ListNode]) -> None:
        # return self.solve(head)
        # return self.solve1(head)
        return self.solve2(head)
        
