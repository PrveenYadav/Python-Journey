# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def __init__(self):
        pass
    
    # Problem says without using devision, this solution is with devision
    def productOfArray(self, arr):
        ans = []
        prod = 1
        for i in range(len(arr)):
            prod *= arr[i]
        for i in range(len(arr)):
            ans.append(prod//arr[i]) #here
        return ans


    # Brute force : O(n^2), O(n)
    def solve(self, arr):
        n = len(arr)
        ans = [0] * n

        for i in range(n):
            product = 1
            for j in range(n):
                if i != j: # here we are excepting/avoiding the self by checking if they are not at same index then calculate
                    product *= arr[j]
            ans[i] = product
        return ans

    # Optimized : Time O(n), Space O(n)
    def solve1(self, nums):
        n = len(nums)
        res = [0] * n  # ans array initiallize with zeros, ans = [0, 0, 0, 0]
        pref = [0] * n # prefix array to calculte prefix product of every index
        suff = [0] * n # suffix array same for suffix

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i] # now will get ans by just calculating the prefix[i] with suffix[i]
        return res
    

    # Optimal using prefix, suffix => Time: O(n), Space: O(1) and O(n) for output array
    def solve2(self, nums):
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
    
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # backward/reverse loop for suffix
            res[i] *= postfix
            postfix *= nums[i]

        return res


if __name__ == "__main__":
    myObj = Solution()
    nums = [1,2,3,4]

    print(myObj.productOfArray(nums))
    print(myObj.solve(nums))
    print(myObj.solve1(nums))
    