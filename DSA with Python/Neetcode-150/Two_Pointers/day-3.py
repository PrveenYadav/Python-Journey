# https://leetcode.com/problems/3sum/

class Solution:
    def __init__(self):
        pass

    def threeSum(self, nums): # O(n^3), O(m)
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        temp = tuple([nums[i], nums[j], nums[k]])
                        ans.add(temp)
        return [list(i) for i in ans]

    def threeSum1(self, nums): # O(n^2), O(n)
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue # skipping the duplicates

            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0: k -= 1
                elif total < 0: j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]: j += 1 # skip duplicates
        return ans


if __name__ == "__main__":
    myObj = Solution()
    nums = [-1,0,1,2,-1,-4]
    # Output: [[-1,-1,2],[-1,0,1]]

    print(myObj.threeSum(nums))
    print(myObj.threeSum1(nums))