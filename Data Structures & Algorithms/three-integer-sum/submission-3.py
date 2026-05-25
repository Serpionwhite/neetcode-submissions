class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        start_pointer = 0
        end_pointer = len(nums) - 1

        res = []

        while start_pointer < len(nums)-2:
            if start_pointer > 0 and nums[start_pointer] == nums[start_pointer-1]:
                start_pointer += 1
                continue
            end_pointer = len(nums) - 1
            middle_pointer = start_pointer + 1
            while middle_pointer < end_pointer:
                if nums[start_pointer] + nums[middle_pointer] + nums[end_pointer] == 0:
                    res.append([nums[start_pointer], nums[middle_pointer], nums[end_pointer]])

                    while middle_pointer < end_pointer and nums[middle_pointer] == nums[middle_pointer+1]:
                        middle_pointer += 1

                    while end_pointer > middle_pointer and nums[end_pointer] == nums[end_pointer-1]:
                        end_pointer -= 1

                    middle_pointer += 1
                    end_pointer -= 1

                elif nums[start_pointer] + nums[middle_pointer] + nums[end_pointer] > 0:
                    end_pointer -= 1
                else:
                    middle_pointer += 1

            start_pointer += 1

        return res

            




        