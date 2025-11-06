# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def __init__(self):
        pass

    # Brute force : O(n), O(m) is len of unique chars
    def longestSubstring(self, s):
        ans = 0
        for i in range(len(s)):
            mySet = set()
            for j in range(i, len(s)):
                if s[j] in mySet:
                    break
                mySet.add(s[j])
            ans = max(ans, len(mySet))
        return ans

    # Optimized using set : O(n), O(m) is len of unique chars 
    def longestSubstring1(self, s):
        mySet = set()
        ans = 0
        i = 0

        for j in range(len(s)):
            while s[j] in mySet:
                mySet.remove(s[i])
                i += 1
            mySet.add(s[j])
            ans = max(ans, j-i + 1)
        return ans
    
    # Optimal using hashmap : O(n), O(m) is len of unique chars
    def longestSubstring2(self, s):
        mp = {}
        ans = 0
        i = 0

        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]] + 1, i)
            mp[s[j]] = j
            ans = max(ans, j-i + 1)
        return ans

if __name__ == "__main__":
    myObj = Solution()
    s = "pwwkew"

    print(myObj.longestSubstring(s))
    print(myObj.longestSubstring1(s))
    print(myObj.longestSubstring2(s))