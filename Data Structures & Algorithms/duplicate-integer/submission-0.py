class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums.sort()
        n = len(nums)

        if n < 2:
            return False
        elif n==2 and nums[0] == nums[-1]:
            return True

        else:
            start = 0
            end = start + 1
            while end < n:
                if nums[start] == nums[end]:
                    return True
                start += 1
                end = start + 1
            return False
         