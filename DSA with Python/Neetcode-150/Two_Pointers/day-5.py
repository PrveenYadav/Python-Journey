# https://leetcode.com/problems/trapping-rain-water/description/

class Solution:
    def __init__(self):
        pass

    # Brute Force : O(n^2), O(1)
    def trappingRainWater(self, height):
        if not height: return 0
        ans = 0
        n = len(height)

        for i in range(n):
            leftMax = rightMax = height[i]
            
            # This loop is checking all the heights to the left of index i to find the maximum height (leftMax) up to that point.
            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i+1, n):
                rightMax = max(rightMax, height[j])
            
            currTrappedRain = min(leftMax, rightMax) - height[i]
            ans += currTrappedRain

        return ans

    # Prefix-Sum : O(n), O(n)
    def trappingRainWater1(self, height):
        if not height: return 0
        n = len(height)
        ans = 0

        # initializing leftMax and rightMax with Array of zeros
        leftMax = [0] * n
        rightMax = [0] * n

        # updating the leftMax boundary
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])

        # updating the rightMax boundary
        rightMax[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        
        # calculating trapped rain or ans
        for i in range(n):
            currTrappedWater = min(leftMax[i], rightMax[i]) - height[i]
            ans += currTrappedWater
    
        return ans

    # Two Pointer : O(n), O(1)
    def trappingRainWater2(self, height):
        if not height: return 0
        ans = 0
        left, right = 0, len(height)-1
        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                ans += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                ans += rightMax - height[right]
        
        return ans

if __name__ == "__main__":
    myObj = Solution()

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(myObj.trappingRainWater(height))
    print(myObj.trappingRainWater1(height))
    print(myObj.trappingRainWater2(height))