class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        total_days = len(prices)

        if total_days < 2:
            return 0


        
        start = 0
        end = 1

        while end < total_days:
            if prices[end] > prices[start]:
                profit = max(profit, prices[end] - prices[start])

            else:
                start = end

            end += 1

        return profit
        