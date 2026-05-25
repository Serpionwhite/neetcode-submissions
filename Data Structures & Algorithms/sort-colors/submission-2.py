class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)

        hash_map = {}

        for index in range(length):
            if nums[index] not in hash_map:
                hash_map[nums[index]] = 1
            else:
                hash_map[nums[index]] += 1

        
        index = 0
        
        while hash_map.get(0,0) != 0:
            nums[index] = 0
            index += 1
            hash_map[0] -= 1

        while hash_map.get(1,0) != 0:
            nums[index] = 1
            index += 1
            hash_map[1] -= 1

        while hash_map.get(2,0) != 0:
            nums[index] = 2
            index += 1
            hash_map[2] -= 1


        return nums

