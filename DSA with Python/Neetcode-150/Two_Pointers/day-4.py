# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def __init__(self):
        pass
    
    # Container with most water
    def mostWater(self, nums): # Brute force : O(n^2), O(1)
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                ht = min(nums[i], nums[j])
                area = j - i
                currWater = ht * area
                ans = max(ans, currWater)
        return ans
    
    # Two Pointer : O(n), O(1)
    def mostWater1(self, height):
        ans = 0
        i, j = 0, len(height)-1

        while i < j:
            ht = min(height[i], height[j])
            area = j - i
            currWater = ht * area
            ans = max(ans, currWater)

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        
        return ans

if __name__ == "__main__":
    myObj = Solution()
    height = [1,8,6,2,5,4,8,3,7]

    print(myObj.mostWater(height))
    print(myObj.mostWater1(height))