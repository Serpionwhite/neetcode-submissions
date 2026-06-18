class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min1 = min2 = float("inf")
        max1 = max2 = 0

        for val in nums:
            if val > max1:
                max2 = max1
                max1 = val
            elif val > max2:
                max2 = val

            if val < min1:
                min2 = min1
                min1 = val

            elif val < min2:
                min2 = val

        return (max1*max2) - (min1 * min2)

        