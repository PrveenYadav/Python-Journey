# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/


# Problem - Find Minimum in Rotated Sorted Array
class Solution:
    # Brute force : O(n), O(1)
    def solve(self, nums):
        return min(nums)

    # Optimal : O(logn), O(1)
    def solve1(self, nums):
        start, end = 0, len(nums)-1
        
        while start < end:
            mid = start + (end-start)//2

            if nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid
        return nums[start]


    def findMin(self, nums):
        # return self.solve(nums)
        return self.solve1(nums)

# Problem - Search in Rotated Sorted Array  
class Solution1:
    # Brute force : O(n), O(1)
    def solve(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

    # Optimal : O(logn), O(1)
    def solve1(self, arr, target):
        left, right = 0, len(arr)-1

        while left <= right:
            mid = left + (right-left)//2
            if arr[mid] == target: return mid

            # left sorted portion
            if arr[left] <= arr[mid]:
                if target > arr[mid] or target < arr[left]: 
                    left = mid+1
                else:
                    right = mid-1

            # right sorted portion
            else:
                if target < arr[mid] or target > arr[right]: 
                    right = mid-1
                else:
                    left = mid+1
        return -1


    def search(self, nums, target):
        # return self.solve(nums, target)
        return self.solve1(nums, target)


if __name__ == "__main__":
    myObj = Solution()
    arr = [3, 4, 5, -45, 1, 2]
    print(myObj.findMin(arr))

    myObj1 = Solution1()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(myObj1.search(nums, target))