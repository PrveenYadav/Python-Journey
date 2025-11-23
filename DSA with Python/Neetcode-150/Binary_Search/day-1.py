# https://leetcode.com/problems/binary-search/
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def __init__(self):
        pass

    # Problem - Binary Search
    def binarySearch(self, arr, target): # O(log n), O(1)
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + ((end-start)//2)
            if nums[mid] < target: start = mid+1
            elif nums[mid] > target: end = mid-1
            else: return mid
        return -1


    # Problem - Search a 2D Matrix
    def searchMatrix(self, matrix, target): # Brute Force : O(m*n), O(1)
        m = len(matrix) # row length
        n = len(matrix[0]) # col length

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target: return True
        return False

    # Optimized : O(m+n), O(1)
    def searchMatrix1(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1

        while row < m and col >= 0:
            if matrix[row][col] > target: 
                col -= 1
            elif matrix[row][col] < target: 
                row += 1
            else: 
                return True
        return False

    # Optimal : Time -> O(logm + logn) || O(log(m*n)), Space -> O(1)
    def searchMatrix2(self, matrix, target):
        m, n = len(matrix), len(matrix[0]) # row and column length
        start = 0
        end = (m*n) - 1

        while start <= end:
            mid = start + ((end-start)//2)
            row = mid // n # row
            col = mid % n # column

            if target < matrix[row][col]: 
                end = mid - 1
            elif target > matrix[row][col]: 
                start = mid + 1
            else: 
                return True
        return False
            

if __name__ == "__main__":
    myObj = Solution()

    nums = [-1,0,3,5,9,12]
    t = 9
    print(myObj.binarySearch(nums, t))

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(myObj.searchMatrix(matrix, target))
    print(myObj.searchMatrix1(matrix, target))
    print(myObj.searchMatrix2(matrix, target))
