class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        array_length = len(nums)

        if array_length < 4:
            return []

        res = []

        start = 0
        while start < array_length - 3:
            if start > 0 and nums[start] == nums[start-1]:
                start += 1
                continue
            end = array_length - 1

            while end > start + 2:
                if end < array_length - 1 and nums[end] == nums[end+1]:
                    end -= 1
                    continue
                
                second_start = start + 1
                second_end = end - 1

                while second_start < second_end:  # FIX: two-pointer loop was missing
                    total = nums[start] + nums[second_start] + nums[second_end] + nums[end]  # FIX: moved inside while

                    if total == target:
                        res.append([nums[start], nums[second_start], nums[second_end], nums[end]])
                        while second_start < second_end and nums[second_start+1] == nums[second_start]:
                            second_start += 1
                        while second_start < second_end and nums[second_end-1] == nums[second_end]:
                            second_end -= 1
                        second_start += 1
                        second_end -= 1
                    elif total > target:
                        second_end -= 1
                    else:
                        second_start += 1

                end -= 1

            start += 1

        return res