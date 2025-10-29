# String 

class Solution:

    def checkPalindrome(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def firstNonRepeatingChar(self, s):
        freq = {}

        # count the frequencies
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # find first non-repeating character
        for char in s:
            if freq[char] == 1:
                return char
            
        return None

        
def main():
    my_obj = Solution()
    # s = "Hellho world What is happening"
    s = "abcba"

    print(my_obj.checkPalindrome(s))
    print(my_obj.firstNonRepeatingChar(s))


if __name__ == "__main__":
    main()