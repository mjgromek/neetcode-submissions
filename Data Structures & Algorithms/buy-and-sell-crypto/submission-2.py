class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1
        maxProfit = 0

        while right < len(prices):
            maxProfit = max(maxProfit, prices[right] - prices[left])
            if prices[right] < prices[left]:
                prices[left] = prices[right] 

            right += 1
            
        return maxProfit
        