# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def __init__(self):
        pass

    # Problem - Best time to buy and sell stocks
    def maxProfit(self, prices): # Brute force : O(n^2), O(1)
        ans = 0
        for i in range(len(prices)):
            buyPrice = prices[i]
            for j in range(i+1, len(prices)):
                sellPrice = prices[j]
                profit = sellPrice - buyPrice
                ans = max(ans, profit)
        return ans
    
    # Two Pointer : O(n), O(1)
    def maxProfit1(self, prices):
        ans = 0
        i, j = 0, 1

        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                ans = max(ans, profit)
            else:
                i = j
            
            j += 1

        return ans

    # Dynamic Programming : O(n), O(1)
    def maxProfit2(self, prices):
        ans = 0
        buyPrice = prices[0]

        for sell in prices:
            ans = max(ans, sell - buyPrice)
            buyPrice = min(buyPrice, sell)
        
        return ans

if __name__ == "__main__":
    myObj = Solution()
    prices = [7,1,5,3,6,4]

    print(myObj.maxProfit(prices))
    print(myObj.maxProfit1(prices))
    print(myObj.maxProfit2(prices))