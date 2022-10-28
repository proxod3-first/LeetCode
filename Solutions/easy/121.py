class Solution:
    
    # [7,1,5,3,6,4]: 5
    # 1 - currentMin
    # 6 - price
    # 6-1=5 - maxProfit (maxSell - minBuy = maxProfit)
    
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currentMin = prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            maxProfit = max(maxProfit, price-currentMin)
            currentMin = min(currentMin, price)
        return maxProfit