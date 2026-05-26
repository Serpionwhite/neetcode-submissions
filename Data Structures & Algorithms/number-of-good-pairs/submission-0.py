class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0

        hash_map = {}

        for value in nums:
            hash_map[value] = hash_map.get(value,0) + 1

        for key in hash_map:
            total += ((hash_map[key]) * (hash_map[key]-1)) // 2

        return total