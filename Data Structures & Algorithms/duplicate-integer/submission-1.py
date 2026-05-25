class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hash_map = {}

        for value in nums:
            hash_map[value] = hash_map.get(value,0) + 1
            if hash_map[value] > 1:
                return True

        return False
        