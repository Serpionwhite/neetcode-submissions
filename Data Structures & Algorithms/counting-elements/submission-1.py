class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_map = {}
        total_number = 0

        for number in arr:
            hash_map[number] = hash_map.get(number,0) + 1

        for number in arr:
            if number + 1 in hash_map:
                total_number += 1

        return total_number