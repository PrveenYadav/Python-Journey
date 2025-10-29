"""
----------- Stacks Data Structure -------------
empty() -> Time complexity O(1)
size() -> O(1)
top()/peek() -> O(1)
push(a)/append(a) -> O(1)
pop() -> O(1)

"""

# Stack Implementation using array or list[]
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)


# Stack Implementation using collections.deque
from collections import deque

class Stack1:
    def stackImplementation(self):
        stack = deque()

        stack.append(1)
        stack.append(2)
        stack.append(3)
        stack.append(4)
        stack.append(5)
        print("Initial stack: ", stack)

        print("poped element: ", stack.pop())
        print("poped element: ", stack.pop())
        print("stack after pop(): ", stack)


# Stack Implementation using Linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack2:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    
    def isEmpty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size


# Problem : Check for balanced parentheses
def isBalanced(s):
    # Stack to store opening brackets
    st = deque() 
    for c in s:
        if c == '(' or c == '{' or c == '[':
            st.append(c)
        # Process closing brackets
        elif c == ')' or c == '}' or c == ']':
            # No opening bracket
            if not st: return False 
            top = st[-1]
            if (c == ')' and top != '(') or (c == '}' and top != '{') or (c == ']' and top != '['):
                return False
            # Pop matching opening bracket
            st.pop() 
    # Balanced if stack is empty
    return not st 


def main():
    print("\n----- Stack Implementaion using list -----")
    # Create a stack
    myStack = Stack()

    myStack.push('A')
    myStack.push('B')
    myStack.push('C')
    print("Stack: ", myStack.stack)
    print("Pop: ", myStack.pop())
    print("Peek: ", myStack.peek())
    print("isEmpty: ", myStack.isEmpty())
    print("Size: ", myStack.size())

    print("\n----- Stack Implementaion using collections.deque() -----")
    obj2 = Stack1()
    obj2.stackImplementation()

    print("\n----- Stack Implementation using Linked list -----")
    myStack2 = Stack2()
    myStack2.push('A')
    myStack2.push('B')
    myStack2.push('C')

    print("Pop: ", myStack2.pop())
    print("Peek: ", myStack2.peek())
    print("isEmpty: ", myStack2.isEmpty())
    print("Size: ", myStack2.stackSize())


    print("\n ------- DSA Problem | Check for balanced parentheses -----")
    testCases = ["[{()}]", "[()()]{}", "(]", "([{]})"]
    for s in testCases:
        print(f'Input: {s} -> Output: {str(isBalanced(s)).lower()}')


if __name__ == "__main__":
    main()