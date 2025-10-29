# https://leetcode.com/problems/valid-sudoku/
# https://leetcode.com/problems/longest-consecutive-sequence/

from collections import defaultdict

class Solution:
    def __init__(self):
        pass

    # Time Complexity: O(1) — Fixed 9×9 board
    # Space Complexity: O(1) — Maximum 27 sets with 9 elements each
    def isValidSudoku(self, board):
        cols = defaultdict(set) # For tracking digits in each column
        rows = defaultdict(set)
        squares = defaultdict(set) # Track digits in each 3x3 subgrid

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue # Skip empty cells

                # Check if digit already exists in row, column, or subgrid
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False # Duplicate found -> invalid

                # Add digit to all three sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True # No duplicates found -> valid
    

    # Brute force : Time - O(n^2), Space - O(n)
    def longestConsecutive(self, nums):
        ans = 0
        mySet = set(nums)

        for num in nums:
            count = 0
            curr = num
            while curr in mySet:
                count += 1
                curr += 1
            ans = max(ans, count)
        return ans
    
    # Using sorting : Time -> O(nlogn), Space -> O(1) or O(n)
    def solve(self, nums):
        if not nums:
            return 0
        res = 0
        nums.sort()

        curr, streak = nums[0], 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        return res

    # Using set : Time -> O(n), Space -> O(n)
    def solve1(self, nums):
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

    # Using Hashmap : Time -> O(n), Space -> O(n)
    def solve2(self, nums):
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res


if __name__ == "__main__":
    myObj = Solution()

    # Valid Sudoku Problem
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]

    print(myObj.isValidSudoku(board))

    # Longest Consecutive Problem
    # nums = [0,3,7,2,5,8,4,6,0,1]
    # nums = [100,4,200,1,3,2]
    nums = [1,0,1,2]

    print(myObj.longestConsecutive(nums))