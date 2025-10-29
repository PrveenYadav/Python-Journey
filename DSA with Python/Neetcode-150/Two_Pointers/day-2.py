# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

from collections import defaultdict

class Solution:
    def __init__(self):
        pass

    # Problem : Two Sum II - Input Array Is Sorted
    def twoSumSorted(self, numbers, target): # O(n^2), O(1)
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return []

    def twoSumSorted1(self, nums, target): # O(n), O(n)
        mp = defaultdict(int) # hashmap initialized with default val 0
        for i in range(len(nums)):
            diff = target - nums[i]
            if mp[diff]:
                return [mp[diff], i+1]
            mp[nums[i]] = i+1
        return []

    # Two pointer will work on sorted array
    def twoSumSorted2(self, nums, target): # O(n), O(1)
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                return [i+1, j+1]
            elif nums[i] + nums[j] < target:
                i += 1
            else:  # if nums[i] + nums[j] > target then 100% we need to eluminate the nums[j] because the array is sorted
                j -= 1
        return []


if __name__ == "__main__":
    myObj = Solution()
    numbers = [2,7,11,15]
    target = 9

    print(myObj.twoSumSorted(numbers, target))
    print(myObj.twoSumSorted1(numbers, target))
    print(myObj.twoSumSorted2(numbers, target))