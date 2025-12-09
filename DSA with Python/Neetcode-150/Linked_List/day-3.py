# https://leetcode.com/problems/linked-list-cycle/description/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Brute force : O(n), O(n)
    def solve(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False

    # Optimal : O(n), O(1)
    def solve1(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False


    # Problem - Linked List Cycle
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # return self.solve(head)
        return self.solve1(head)

