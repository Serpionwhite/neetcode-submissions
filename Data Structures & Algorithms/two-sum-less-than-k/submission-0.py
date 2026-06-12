class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_sum = -1

        start = 0
        end = len(nums) - 1

        while start < end:
            if nums[start] + nums[end] < k:
                max_sum = max(max_sum, nums[start] + nums[end])
                start+= 1
            else:
                end-=1

        return max_sum
        