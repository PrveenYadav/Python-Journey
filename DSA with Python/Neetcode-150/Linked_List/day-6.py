 # https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # Approach-1: O(n), O(n)
    def solve(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #step-1: clone the list
        #step-2: set the pointers
        mp = { None : None } # if value is Null then set None

        #step-1
        curr = head
        while curr:
            newNode = Node(curr.val) # val
            mp[curr] = newNode
            curr = curr.next
        
        #step-2
        curr = head
        while curr:
            copy = mp[curr]
            copy.next = mp[curr.next]
            copy.random = mp[curr.random]
            curr = curr.next
        
        return mp[head]

    # Approach-2 : Optimal - O(n), O(1) and O(n) for output
    def solve1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        # Pass-1: Interweave Copy Nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Pass-2: Set Random Pointers for Copy Nodes
        curr = head
        while curr:
            copy = curr.next
            if curr.random: copy.random = curr.random.next
            curr = curr.next.next

        # Pass-3: Separate the Lists 
        cloned_head = head.next
        curr = head
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next: copy.next = copy.next.next
            curr = curr.next

        return cloned_head


    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # return self.solve(head)
        return self.solve1(head)