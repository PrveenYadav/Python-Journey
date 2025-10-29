# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def __init__(self):
        pass

    def validPalindrome(self, s): # O(n), O(n)
        newArr = [] # space => O(n)
        for char in s: # time => O(n)
            if char.isalnum(): # isalpha() only checks for alphabates and isalnum() checks for alphanumeric
                newArr.append(char.lower())

        i = 0
        j = len(newArr) - 1
        while i < j: # time O(n)
            if newArr[i] != newArr[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def validPalindrome1(self, s): # O(n), O(1)
        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
    

if __name__ == "__main__":
    myObj = Solution()
    s = "A man, a plan5, a ca5nal: Panama"

    # print(s[::-1])
    print(myObj.validPalindrome(s))
    print(myObj.validPalindrome1(s))
