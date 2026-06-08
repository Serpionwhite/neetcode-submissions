class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_length = 0
        count = 0
        for index in range(len(nums)):
            if nums[index] == 1:
                count += 1
                max_length = max(count, max_length)

            else:
                count = 0


        return max_length

        