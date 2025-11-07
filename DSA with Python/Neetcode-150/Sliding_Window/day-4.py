# https://leetcode.com/problems/permutation-in-string/description/

from collections import Counter

class Solution:
    # Brute Force : O(n^3logn), O(n)
    def solve(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1) # sorting the s1 string
        for i in range(len(s2)):
            for j in range(len(s2)):
                subStr = s2[i : j + 1] # calculating substr of s2 string
                subStr = sorted(subStr) # then sorting the substring
                if subStr == s1: # then comparing sorted substring of s2 with sorted s1 string
                    return True
        return False

    # Brute Force : O(n^3), O(k)/O(1) because of only 26 characters in lowercase 
    def solve1(self, s1: str, s2: str) -> bool:
        # search the s1 string's length of window in s2 where the freq of charater are same as are in the s1
        freqS1 = Counter(s1)
        for i in range(len(s2)):
            for j in range(i, len(s2)):
                windowS2 = s2[i : j + 1]
                if Counter(windowS2) == freqS1:
                    return True
        return False

    # optimized : O(n*m), O(1)
    def solve2(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2: return False

        s1_freq = Counter(s1)

        for i in range(len2 - len1+1):
            window_freq = Counter(s2[i: i+len1])
            if window_freq == s1_freq:
                return True
        return False

    # Optimal : O(n + m), O(1)
    def solve3(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2: return False

        s1_freq = Counter(s1)
        window_freq = Counter(s2[:len1]) # initial window chars freq of s1 size

        if window_freq == s1_freq: return True

        for i in range(len1, len2):
            # moving the window by adding a char on end and removing from start
            window_freq[s2[i]] += 1 
            window_freq[s2[i - len1]] -= 1

            # Remove characters with count 0
            if window_freq[s2[i - len1]] == 0:
                del window_freq[s2[i - len1]]

            if window_freq == s1_freq:
                return True
        return False


    # Problem - Permutation in String
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # return self.solve(s1, s2)
        # return self.solve1(s1, s2)
        # return self.solve2(s1, s2)
        return self.solve3(s1, s2)

if __name__ == "__main__":
    myObj = Solution()
    s1 = "ab"
    s2 = "eidbaooo"

    print(myObj.checkInclusion(s1, s2))