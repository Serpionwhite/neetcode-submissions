class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        total_days = len(prices)

        if total_days < 2:
            return 0


        
        for index in range(total_days-1):
            for second_index in range(index+1, total_days):
                profit = max(profit, prices[second_index] - prices[index])
        
        return profit
        