class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        if (nums1 and not nums2) or (not nums1 and nums2):
            return result

        hash_map = {}

        for value in nums1:
            hash_map[value] = hash_map.get(value,0) + 1

        
        for value in nums2:
            if value in hash_map and hash_map[value] != 0:
                hash_map[value] = 0
                result.append(value)

        return result


        