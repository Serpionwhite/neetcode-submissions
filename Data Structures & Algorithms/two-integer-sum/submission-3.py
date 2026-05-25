class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index in range(len(nums)):
            difference = target - nums[index]

            if difference in hash_map:
                return [hash_map[difference], index]
            
            hash_map[nums[index]] = index

        return []

        