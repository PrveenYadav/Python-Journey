# https://leetcode.com/problems/sliding-window-maximum/description/

import heapq
from collections import deque

class Solution:
    def __init__(self):
        pass

    # Brute force : O(n*k), O(n)
    def solve(self, nums, k):
        ans = []
        for i in range(len(nums) - k+1): # starting index of window always will go till len(arr) - window_size
            curr_window = nums[i : i+k]
            maxi = max(curr_window) # time : O(n+k) , built in funtion in python to calculate max of array in one line
            ans.append(maxi)
        return ans
    
    # same brute force, but using loop instead of max
    def solve1(self, nums, k):
        ans = []
        for i in range(len(nums) - k+1):
            maxi = 0
            for j in range(i, i+k):
                maxi = max(maxi, nums[j])
            ans.append(maxi)
        return ans

    
    # Optimized using Heaps/Priority queue : O(nlogn), O(n)
    # Python version 3.13 -> by default only create 'min heap' and manually making 'max heap' by negate values
    def solve2(self, nums, k):
        heap = []
        ans = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                ans.append(-heap[0][0])
        return ans
    
    # Python new version 3.14 -> max heap functions available
    def solve3(self, nums, k):
        ans = []
        maxHeap = []

        for i in range(len(nums)):
            heapq.heappush_max(maxHeap, (nums[i], i))
            if i >= k-1:
                while maxHeap[0][1] <= i-k:
                    heapq.heappop_max(maxHeap)
            ans.append(maxHeap[0][0])
        return ans


    # Optimal using deque : O(n), O(n)
    def solve4(self, nums, k):
        ans = []
        q = deque() # storing indeces in decreasing order corresponding to values. This way, the index of the largest element in the current relevant window will always be at q[0].
        
        for i, num in enumerate(nums):
            # Remove elements smaller than current element num
            while q and nums[q[-1]] <= num:  # avoiding smaller elements
                q.pop()
            
            # Add the current index to the back of the deque.
            q.append(i)

            # Remove the index from the front if it is outside the curr window
            if q[0] == i-k:
                q.popleft()

            if i >= k-1: # Start recording maximums only after the first window
                ans.append(nums[q[0]])
        return ans


if __name__ == "__main__":
    myObj = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

    print(myObj.solve(nums, k))
    print(myObj.solve1(nums, k))

    print(myObj.solve2(nums, k))
    # print(myObj.solve3(nums, k))

    print(myObj.solve4(nums, k))
