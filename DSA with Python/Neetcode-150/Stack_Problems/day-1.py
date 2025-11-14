# https://leetcode.com/problems/valid-parentheses/description/

from collections import deque

class Solution:
    def __init__(self):
        pass

    # Brute force : O(n^2), O(n)
    def solve(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s: # time: O(n)
            # removing from string if matches pairs
            s = s.replace('()', '') # time: O(n), space: O(n)
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''

    # Optimal using deque based stack : O(n), O(n)
    def solve1(self, s: str) -> bool:
        st = deque()
        for c in s:
            if c == '(' or c == '{' or c == '[':
                st.append(c)
            elif c == ')' or c == '}' or c == ']':
                if not st: return False
                top = st[-1]
                if ( c == ')' and top != '(') or (c == '}' and top != '{') or (c == ']' and top != '['):
                    return False
                st.pop()
        return not st # if stack is empty -> return True

    # Optimal list based stack : O(n), O(n)
    def solve2(self, s: str) -> bool:
        st = []
        mapping = {')':'(', '}': '{', ']':'['}
        for c in s:
            if c in '({[':
                st.append(c)
            elif c in ')}]':
                if not st or st.pop() != mapping[c]:
                    return False
        return len(st) == 0

    # Optimal : O(n), O(n)
    def solve3(self, s: str) -> bool:
        # stack = []
        stack = deque() # better practice using deque()
        mapping = {')':'(', '}': '{', ']':'['}

        for c in s:
            if c in mapping.values(): # opening bracket - push in stack
                stack.append(c)
            elif c in mapping.keys(): # closing bracket - check for match
                if not stack: return False
                if stack.pop() != mapping[c]: return False
        
        return not stack
            
    
    # Problem - Valid Parentheses
    def isValid(self, s: str) -> bool:
        # return self.solve(s)
        # return self.solve1(s)
        # return self.solve2(s)
        return self.solve3(s)
    

if __name__ == "__main__":
    myObj = Solution()
    s = "()[]{}"

    print(myObj.isValid(s))