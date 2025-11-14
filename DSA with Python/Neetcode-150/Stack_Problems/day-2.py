# https://leetcode.com/problems/min-stack/


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # to track min

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = self.minStack[-1] if self.minStack else float('inf')
        self.minStack.append(min(val, current_min))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    # Brute force : O(n), O(1)
    def getMin1(self) -> int:
        # return min(self.stack)

        # st = self.stack
        # mini = st[0]
        # for i in range(len(st)):
        #     mini = min(mini, st[i])
        # return mini
    
        st = self.stack
        mini = st[0]
        for i in range(len(st)):
            if st[i] <= mini:
                mini = st[i]
        return mini

    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    myObj = MinStack()
