# https://leetcode.com/problems/add-two-numbers/description/


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # Using Recursion : O(n+m), (n+m)
    def solve(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if not l1 and not l2 and carry == 0: return None

        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        carry, val = divmod(v1 + v2 + carry, 10)

        next_node = self.solve(l1.next if l1 else None, l2.next if l2 else None, carry)
        return ListNode(val, next_node)

    # Optimal : O(n), O(1) and O(max(n, m)) for output list
    def solve1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry: 
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # new digit
            value = v1 + v2 + carry
            carry = value // 10
            value = value % 10
            curr.next = ListNode(value)

            # update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # return self.solve(l1, l2, 0) # 0 is carry
        return self.solve1(l1, l2)