class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_days = len(prices)
        if total_days < 2:
            return 0

        profit = 0
        for index in range(1,total_days):
            if prices[index] > prices[index-1]:
                profit += prices[index] - prices[index-1]

        return profit

        
        