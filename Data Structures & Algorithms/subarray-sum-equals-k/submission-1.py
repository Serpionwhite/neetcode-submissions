class Solution:
        def subarraySum(self, nums: List[int], k: int) -> int:
                array_length = len(nums)

                count = 0

                hash_map = {0:1}
                prefix = 0

                for number in nums:
                        prefix += number
                        count += hash_map.get(prefix-k, 0)
                        hash_map[prefix] = hash_map.get(prefix,0) + 1
                
                return count
