# https://leetcode.com/problems/two-sum/description/

class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    # Using hashmap : O(n), O(n)
    def solve1(self, nums, target):
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

if __name__ == "__main__":
    myObj = Solution()
    # arr = [2, 1, 7, 5, 9]
    arr = [2, 7, 11, 15]

    print(myObj.twoSum(arr, 9))
    print(myObj.solve1(arr, 9))