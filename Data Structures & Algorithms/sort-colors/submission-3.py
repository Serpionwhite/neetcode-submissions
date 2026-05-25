class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)

        zero_index = 0
        two_index = length-1
        first_index = 0

        index = 0

        while index <= two_index:
            if nums[index] == 0:
                nums[index], nums[zero_index] = nums[zero_index], nums[index]
                zero_index += 1
                index += 1

            elif nums[index] == 2:
                nums[two_index], nums[index] = nums[index], nums[two_index]
                two_index -= 1

            else:
                index += 1

        return nums

