# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Brute Force : O(n), O(n)    
    def solve(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        removeIdx = len(nodes) - n
        if removeIdx == 0:
            return head.next
        
        nodes[removeIdx - 1].next = nodes[removeIdx].next
        return head

    # reversing the list in O(n), O(1)
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        prev = None
        curr = head

        while curr: # while curr is not None/Null
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev    

    # Time and space : O(n), O(1)
    def solve1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rev_head = self.reverse(head)

        if n == 1: 
            rev_head = rev_head.next
        else:
            cnt = 1
            curr = rev_head
            while curr and cnt < n-1: # till prev node
                curr = curr.next
                cnt += 1
            
            # now curr is pointing the prev node from the node to be deleted: deleting the node
            if curr and curr.next:
                curr.next = curr.next.next
        
        newHead = self.reverse(rev_head)
        return newHead    

    # Using Length : O(n), O(1)
    def solve2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head
        while curr:
            curr = curr.next
            N += 1
        
        removeIdx = N - n
        if removeIdx == 0: return head.next

        prev = head
        for i in range(N-1):
            if (i+1) == removeIdx:
                prev.next = prev.next.next
                break
            prev = prev.next
        
        return head

    # Optimal and clear using two pointer in single pass : O(n), O(1)
    def solve3(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        # move the right pointer n steps further 
        while n > 0:
            curr = curr.next
            n -= 1

        # now updating both left and right pointer one - one step further till right -> None
        while curr:
            prev = prev.next
            curr = curr.next

        prev.next = prev.next.next
        return dummy.next

    
    # Problem - Remove nth node from end of the list
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # return self.solve(head, n)
        # return self.solve1(head, n)
        # return self.solve2(head, n)
        return self.solve3(head, n)
    
    