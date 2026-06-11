class Solution:
    def arrangeCoins(self, n: int) -> int:
        # count = 0
        # total_coins = n

        # for index in range(1,n+1):
        #     if index <= total_coins:
        #         count += 1
        #         total_coins -= index
        #     else:
        #         break

        # return count


        left = 1
        right = n
        res = 0

        while left <= right:
            mid = (left+right) // 2
            coins = (mid*(mid+1))//2

            if coins > n:
                right = mid-1
            else:
                left = mid+1
                res = max(res, mid)

        return res

        
        