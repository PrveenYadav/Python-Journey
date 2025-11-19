# https://leetcode.com/problems/car-fleet/

class Solution:
    def __init__(self):
        pass

    # Problem - Car Fleet (Leetcode-853) : O(nlogn), O(n)
    def carFleet(self, target, position, speed):
        stack = []
        pair = [(p, s) for p, s in zip(position, speed)] # pairing the position with speed
        pair.sort(reverse=True) # sorting the paired array in reverse order

        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

if __name__ == "__main__":
    myObj = Solution()
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]

    print(myObj.carFleet(target, position, speed))