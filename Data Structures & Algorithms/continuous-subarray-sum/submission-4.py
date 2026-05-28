class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        hash_map = {0:-1}
        prefix = 0

        for index in range(len(nums)):
            prefix += nums[index]
            if prefix % k in hash_map:
                if index - hash_map[prefix % k] >= 2:
                    return True

            if prefix % k not in hash_map:
                hash_map[prefix % k] = index

        return False

        