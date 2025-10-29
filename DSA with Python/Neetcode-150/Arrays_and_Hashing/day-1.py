# Day-1 of Neetcode-150 DSA Challenge
# https://leetcode.com/problems/contains-duplicate/  

# Contains Duplicates

class Solution:
    def __init__(self):
        pass
    
    # Brute Force Approach : O(n^2), O(1)
    def checkDuplicates(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
    # Using Sorting : O(nlogn), O(1)/O(n)
    def solve1(self, arr):
        arr.sort()
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return True
        return False
    
    # Using Hash set : O(n), O(n)
    def solve2(self, arr):
        seen = set()
        for num in arr:
            if num in seen:
                return True
            seen.add(num)
        return False

    # Using Hash set length : O(n), O(n)
    def solve3(self, nums):
        return len(set(nums)) < len(nums)

if __name__ == "__main__":
    nums = [1, 2, 3, 3]
    myObj = Solution()
    print(myObj.checkDuplicates(nums))
    print(myObj.solve1(nums))
    print(myObj.solve2(nums))
    print(myObj.solve3(nums))