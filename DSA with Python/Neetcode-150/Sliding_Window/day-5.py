# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter

class Solution:

    # check validity
    def check_validity(self, window_str, target_str):
        # 1. Create a frequency map (Counter) for the target string 't'.
        # This tells us exactly how many of each character we need to find.
        target_counts = Counter(target_str)

        # 2. Iterate through the characters in the current substring (window_str).
        # For every character, we decrease the required count if it exists in our map.
        for char in window_str:
            if char in target_counts:
                # We found one of the required characters, so we decrement the count.
                target_counts[char] -= 1

        # 3. Check if all required counts have been satisfied (i.e., are zero or less).
        # If any count is still positive, it means we didn't find enough of that character.
        for count in target_counts.values():
            if count > 0:
                # Not valid: Missing one or more required characters.
                return False

        # Valid: All required characters have been found in the window.
        return True

    # Brute force : O(n^3), O(n)
    def solve(self, s, t):
        # We use infinity for min_len so the first valid window will always be the shortest.
        min_len = float('inf')
        # This stores the shortest valid substring found so far.
        result_window = ""

        # Two nested loops generate every possible substring.
        for i in range(len(s)):

            for j in range(i, len(s)):

                # Get the current substring/window.
                current_window = s[i:j+1]

                # Step 3: Check Validity and Update Result
                # WHAT: Calls the helper function to see if the current window is valid.
                # WHY: If it's valid, it's a potential answer, and we check if it's the new minimum.
                if self.check_validity(current_window, t):
                    current_len = len(current_window)
                    
                    # Check if this valid window is shorter than the shortest one found so far.
                    if current_len < min_len:
                        # Update the minimum length and store the new shortest window.
                        min_len = current_len
                        result_window = current_window
                        
        # Step 4: Return the Result
        # If min_len is still infinity, no valid window was found, so we return "".
        # Otherwise, we return the shortest valid window found.
        return result_window

    # Optimal : O(n+m), O(m)
    def solve1(self, s, t):
        if t == "": return ""

        countT = Counter(t)
        window = Counter()
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] += 1 # expanding the window

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # Update result if this window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # Remove left character from window / Shrinking the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]: # if the removed char is one that was required then we are decreasing the have -= 1, cause we need one char more because we removed one from left
                    have -= 1
                l += 1 # otherwise shrinking
        
        left, right = res # unpacking the result indices, because res contains [left_index, right_index]
        return s[left : right + 1] if resLen != float("infinity") else ""
    

    # Problem - Minimum window substring
    def minWindow(self, s, t):
        # return self.solve(s, t)
        return self.solve1(s, t)
    
if __name__ == "__main__":
    myObj = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(myObj.minWindow(s, t))