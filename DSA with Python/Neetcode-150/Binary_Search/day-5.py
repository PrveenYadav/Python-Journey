# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

from typing import List

class Solution:
    # Brute Force : O((m+n)log(m+n)), O(n+m)
    def solve(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArr = nums1 + nums2
        mergedArr.sort()
        n = len(mergedArr)

        if n % 2 == 1: # odd
            mid_index = n//2
            return float(mergedArr[mid_index])
        else: # even
            mid_right = n // 2
            mid_left = mid_right - 1
            return (mergedArr[mid_left] + mergedArr[mid_right]) / 2.0

    # Brute Force : O((m+n)log(m+n)), O(n+m)
    def solve1(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2) 
        length = len(nums)
        mid = length // 2
        return float(nums[mid] if length % 2 else (nums[mid-1] + nums[mid]) / 2.0)

    # Space optimized : O(m+n), O(1)
    def solve2(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        midIdx = n//2
        midLeftIdx = midIdx - 1

        i = j = 0
        count = 0
        mid = midLeft = -1 # mid elements

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                if count == midIdx: mid = nums1[i]
                if count == midLeftIdx: midLeft = nums1[i]
                count += 1
                i += 1
            else:
                if count == midIdx: mid = nums2[j]
                if count == midLeftIdx: midLeft = nums2[j]
                count += 1
                j += 1

        # if any elements are remain in nums1 or nums2
        while i < len(nums1):
            if count == midIdx: mid = nums1[i]
            if count == midLeftIdx: midLeft = nums1[i]
            count += 1
            i += 1
        while j < len(nums2):
            if count == midIdx: mid = nums2[j]
            if count == midLeftIdx: midLeft = nums2[j]
            count += 1
            j += 1

        if n % 2 == 1: # odd
            return float(mid)
        else:
            return (mid + midLeft) / 2.0

    # Optimal : Binary Search : O(log min(n, m)), O(1)
    def solve3(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

    
    # Problem : Median of two sorted array
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # return self.solve(nums1, nums2)
        # return self.solve1(nums1, nums2)
        # return self.solve2(nums1, nums2)
        return self.solve3(nums1, nums2)
    

if __name__ == "__main__":
    obj = Solution()
    nums1 = [1,2]
    nums2 = [3,4]

    print(obj.findMedianSortedArrays(nums1, nums2))