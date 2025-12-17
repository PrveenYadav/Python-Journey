# https://leetcode.com/problems/find-the-duplicate-number/


from typing import List

class Solution:
    # Brute force using sorting : O(nlogn), O(1)/O(n)
    def solve(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return nums[i]
        return -1

    # Optimized using set : O(n), O(n)
    def solve1(self, nums: List[int]) -> int:
        mySet = set()
        for num in nums:
            if num in mySet:
                return num
            mySet.add(num)
        return -1
        
    # Optimized using list : O(n), O(n)
    def solve2(self, nums: List[int]) -> int:
        seen = [0] * len(nums)
        for num in nums:
            if seen[num - 1]:
                return num
            seen[num - 1] = 1
        return -1

    # Optimized : O(n), O(1)
    def solve3(self, nums: List[int]) -> int:
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0 :
                return abs(num)
            nums[idx] *= -1
        return -1
    
    # Optimal - using two pointer : O(n), O(1)
    def solve4(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


    def findDuplicate(self, nums: List[int]) -> int:
        # return self.solve(nums)
        # return self.solve1(nums)
        # return self.solve2(nums)
        # return self.solve3(nums)
        return self.solve4(nums)