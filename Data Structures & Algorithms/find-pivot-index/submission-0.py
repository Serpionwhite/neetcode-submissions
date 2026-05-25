class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        total_sum = sum(nums)
        n = len(nums)

        index = 0

        while index < n:
            if leftsum == total_sum-nums[index]-leftsum:
                return index
            leftsum+= nums[index]
            index += 1

        return -1

        
        