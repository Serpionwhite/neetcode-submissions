class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        array_length = len(nums)
        max_target = array_length / 2

        hash_map = {}

        for value in nums:
            hash_map[value] = hash_map.get(value,0) + 1

        for key in hash_map:
            if hash_map[key] > max_target:
                return key
        