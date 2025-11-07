# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def __init__(self):
        pass

    def characterReplacement(self, s, k):
        ans = 0
        for i in range(len(s)):
            freq = {}
            maxFreq = 0
            for j in range(i, len(s)):
                freq[s[j]] = 1 + freq.get(s[j], 0) # counting the freq of chars
                maxFreq = max(maxFreq, freq[s[j]])
                if (j-i + 1) - maxFreq <= k:
                    ans = max(ans, j-i+1)
        return ans

    def characterReplacement1(self, s, k):
        ans = 0
        freq = {}

        i = maxFreq = 0
        for j in range(len(s)):
            freq[s[j]] = 1 + freq.get(s[j], 0)
            maxFreq = max(maxFreq, freq[s[j]])

            while (j-i+1) - maxFreq > k:
                freq[s[i]] -= 1
                i += 1
            ans = max(ans, j-i+1)
        return ans
    
if __name__ == "__main__":
    myObj = Solution()
    s = "ABAB"
    k = 2

    print(myObj.characterReplacement(s, k))
    print(myObj.characterReplacement1(s, k))