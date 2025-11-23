# https://leetcode.com/problems/koko-eating-bananas/

import math

class Solution:

    # Hour/Time calculation : O(N)
    def totalHour(self, piles, k):
        total = 0
        for pile in piles:
            total += math.ceil(pile/k) # time/hour is taking on each pile
        return total


    # Brute force : O(m*n), O(1)
    def solve(self, piles, h, k):
        speed = 1
        while True:
            totalTime = self.totalHour(piles, speed) # O(N) Time
            if totalTime <= h:
                return speed
            speed += 1
        return speed

    # Optimal using Binary Search : O(n*logm), O(1)
    def solve1(self, piles, h):
        start, end = 1, max(piles)
        ans = end # In worse case koko can eat max(piles) each hour

        while start <= end:
            mid = start + ((end-start)//2)
            currHour = self.totalHour(piles, mid) # O(N) Time

            if currHour <= h:
                # This speed works, try smaller speed
                ans = mid
                end = mid-1
            else:
                start = mid+1
        return ans


    def minEatingSpeed(self, piles, h):
        # return self.solve(piles, h)
        return self.solve1(piles, h)
        

if __name__ == "__main__":
    myObj = Solution()
    piles = [3, 7, 11, 4, 8]
    h = 8

    print(myObj.minEatingSpeed(piles, h))