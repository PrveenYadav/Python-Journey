# https://leetcode.com/problems/group-anagrams/description/

from collections import Counter
from collections import defaultdict

class Solution:
    def __init__(self):
        pass

    # Brute force using sorting : O(m * nlogn), O(m*n)
    def groupAnagrams(self, strs):
        res = defaultdict(list) # creating a dict/hashmap
        for s in strs: # iterating through the loop
            sortedS = ''.join(sorted(s)) # converting strings into characters and then sorting them and then again creating string with sorted orders: like "eat" -> ['e', 'a', 't'] then ['e', 'a', 't'] -> ['a', 'e', 't'], then ['a', 'e', 't'] -> "aet"
            res[sortedS].append(s) # inserting the string s as a val("eat") in the hashmap with the key("aet") of sortedS
        return list(res.values()) # returning the list of only values from hashmaps
    
        """How we are Mapping in the hashmap"""
        # "aet" -> ["eat", "tea", "ate"]
        # "ant" -> ["tan", "nat"]
        # "abt" -> ["bat"]
        """Returning the list of values only"""
        # [["eat", "tea", "ate"],["tan", "nat"],["bat"]]

        

    # Optimal with Hashmap : O(m*n), O(m*n)
    def solve(self, strs):
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())


if __name__ == "__main__":
    myObj = Solution()
    # strs = ["act","pots","tops","cat","stop","hat"]
    strs = ["eat","tea","tan","ate","nat","bat"]
    
    print(myObj.groupAnagrams(strs))
    print(myObj.solve(strs))
    
