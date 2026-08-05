class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l,r,maxProfit = 0,1,0

        while l < r and r < len(prices):
            maxProfit = max(maxProfit, prices[r]-prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return maxProfit

