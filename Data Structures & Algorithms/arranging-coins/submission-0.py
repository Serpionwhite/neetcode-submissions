class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        total_coins = n

        for index in range(1,n+1):
            if index <= total_coins:
                count += 1
                total_coins -= index
            else:
                break

        return count

        
        