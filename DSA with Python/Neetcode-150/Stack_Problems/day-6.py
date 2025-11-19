# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def __init__(self):
        pass

    # Problem - Largest area in Histogram
    def largestRectangleArea(self, heights): # Brute force : O(n^2), O(1)
        maxArea = 0
        for i in range(len(heights)):
            minHeight = float("inf")
            for j in range(i, len(heights)):
                minHeight = min(minHeight, heights[j])
                width = j - i+1
                currArea = width * minHeight
                maxArea = max(maxArea, currArea)
        return maxArea
    
        # Optimal : O(n), O(n)
    
    # Brute force : O(n^2), O(1)
    def solve(self, heights):
        n = len(heights)
        maxArea = 0
        
        for i in range(n):
            left = i
            right = i

            # extending the left while bars are >= curr height
            while left > 0 and heights[left - 1] >= heights[i]:
                left -= 1

            # extending the right while bars are >= curr height
            while right < n-1 and heights[right + 1] >= heights[i]:
                right += 1

            width = right - left + 1
            currArea = width * heights[i]
            maxArea = max(maxArea, currArea)
        return maxArea

    # Optimal using monotonic stack : O(n), O(n)
    def solve1(self, heights):
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n+1): # loop n-1 times (one extra iteration with height 0)
            currHeight = heights[i] if i < n else 0 # For last iteration (i == n), use height 0 to clear the stack
            while stack and currHeight < heights[stack[-1]]:
                ht = heights[stack.pop()] # pop the taller bar from stack
                width = i if not stack else i - stack[-1] - 1
                currArea = ht * width
                maxArea = max(maxArea, currArea)
            stack.append(i)
        return maxArea

if __name__ == "__main__":
    myObj = Solution()
    heights = [2, 1, 5, 6, 2, 3]

    print(myObj.largestRectangleArea(heights))
    print(myObj.solve(heights))
    print(myObj.solve1(heights))