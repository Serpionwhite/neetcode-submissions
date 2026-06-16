class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_map = {}

        for char in text:
            if char in "balon":
                hash_map[char] = hash_map.get(char,0) + 1

        
        
        if len(hash_map) < 5:
            return 0

        hash_map['l'] //= 2
        hash_map['o'] //= 2

        return min(hash_map.values())


        
            
        