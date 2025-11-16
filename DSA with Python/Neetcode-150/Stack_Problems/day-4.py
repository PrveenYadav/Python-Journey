# https://leetcode.com/problems/daily-temperatures/description/


class Solution:
    def __init__(self):
        pass

    # Brute Force : O(n^2), O(n)
    def dailyTemperatures(self, arr):
        ans = []
        for i in range(len(arr)):
            waiting_days = 0 
            for j in range(i+1, len(arr)):
                if arr[j] > arr[i]:
                    waiting_days = j - i
                    break
            ans.append(waiting_days)
        return ans

    # Optimal using stack : O(n), O(n)
    def solve(self, arr):
        ans = [0] * len(arr)
        stack = [] # store pairs of [temp, index]
        # stack will look like: stack = [(73, 0), (74, 1), (75, 2), (71, 3)]
        
        for j, temp in enumerate(arr):
            while stack and temp > stack[-1][0]: # stack[-1] = top | [0] is 1st in (temp, index)
                stackT, i = stack.pop() # poped temp and index
                waiting_days = j - i
                ans[i] = waiting_days
            stack.append((temp, j)) # pushing the tuple of (temp, index)    
        return ans        

if __name__ == "__main__":
    myObj = Solution()
    arr = [73,74,75,71,69,72,76,73]
    # Output: [1,1,4,2,1,1,0,0]

    print(myObj.dailyTemperatures(arr))
    print(myObj.solve(arr))