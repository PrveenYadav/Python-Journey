# https://leetcode.com/problems/valid-anagram/

from collections import Counter

class Solution: 
    def __init__(self):
        pass

    # Using Sorting : Time -> O(nlogn + mlogm), Space -> O(1) to O(n+m)
    def validAnagram(self, s, t):
        if len(s) != len(t): return False
        return sorted(s) == sorted(t)

    # using hash map : O(n+m), O(1) -> since we have at most 26 different characters
    def solve(self, s, t):
        if len(s) != len(t): return False
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
    # Easy with counter
    def solve2(self, s, t):
        return len(s) == len(t) and Counter(s) == Counter(t)

    # Using Array : O(n+m), O(1)
    def solve1(self, s, t):
        if len(s) != len(t): return False
        count = [0] * 26
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
    

    def countFreq(self, s, c):
        mapIs = {}
        count = 0
        for i in range(len(s)):
            if s[i] == c:
                count += 1
        return count

if __name__ == "__main__":
    myObj = Solution()
    s = "racecar"
    t = "carrace"
    # s = "jar"
    # t = "jam"

    print(myObj.countFreq(s, 'r'))
    print(myObj.validAnagram(s, t))
    print(myObj.solve(s, t))
    print(myObj.solve1(s, t))
    print(myObj.solve2(s, t))
    
