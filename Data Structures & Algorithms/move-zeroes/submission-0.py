class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        non_zero_index = 0
        total_elements = len(nums)

        for index in range(total_elements):
            if nums[index] == 0:
                continue

            nums[index], nums[non_zero_index] = nums[non_zero_index], nums[index]
            non_zero_index += 1

        return nums
        