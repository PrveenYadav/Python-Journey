# https://leetcode.com/problems/top-k-frequent-elements/description/

import heapq
from collections import Counter

class Solution:
    def __init__(self):
        pass

    # Brute force using sorting : Time O(n log n), Space O(n) 
    def topKFrequent1(self, nums, k):
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

    # Using min heap / heapq : Time O(nlogk), Space O(n+k) 
    def topKFrequentElements(self, nums, k):
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

    # Using heapq -> Time: O(nlogk), Space: O(n) 
    def topKFrequent(self, nums, k):
        if k == len(nums):
            return nums

        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        return heapq.nlargest(k, count.keys(), key=count.get)   
    
    # Time: O(nlogk), Space: O(n) 
    def solve(self, nums, k):
        freqCounter = Counter(nums)
        
        resArray = [ num for num,count in freqCounter.most_common(k)]
        return resArray

    # Optimal using Bucket sort -> Time: O(n), Space: O(n) 
    def solve1(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
    
if __name__ == "__main__":
    myObj = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    print(myObj.topKFrequent1(nums, k))
    print(myObj.topKFrequentElements(nums, k))
    print(myObj.topKFrequent(nums, k))
    print(myObj.solve(nums, k))
    print(myObj.solve1(nums, k))