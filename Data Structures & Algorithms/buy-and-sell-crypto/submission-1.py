class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        n = len(prices)
        for right in range(left+1, n):
            difference = prices[right] - prices[left]
            if difference < 0:
                left = right
                continue
            max_profit = max(max_profit, difference)
        return max_profit
        