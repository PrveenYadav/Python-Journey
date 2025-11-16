# https://leetcode.com/problems/evaluate-reverse-polish-notation/


class Solution:
    def __init__(self):
        pass

    # Brute force : O(n^2), O(n)
    def evalRPN(self, tokens):
        while len(tokens) > 1: # runs until the token has only one element
            for i, c in enumerate(tokens):
                if c in "+-*/":
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    if c == "+":
                        ans = a + b
                    elif c == "-":
                        ans = a - b
                    elif c == "*":
                        ans = a * b
                    elif c == "/":
                        ans = int(a / b)
                    
                    tokens = tokens[:i-2] + [str(ans)] + tokens[i+1:]
                    break
        return int(tokens[0])
    
    # Optimal using recursion : O(n), O(n)
    def solve1(self, tokens):
        def dfs():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)

            right = dfs()
            left = dfs()

            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            elif token == '/':
                return int(left / right)

        return dfs()
    
    # Optimal using stack: O(n), O(n)
    def solve2(self, tokens):
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                # res = float(b) / a
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]

            
if __name__ == "__main__":
    myObj = Solution()
    tokens = ["2","1","+","3","*"]

    print(myObj.evalRPN(tokens))
    print(myObj.solve1(tokens))
    print(myObj.solve2(tokens))