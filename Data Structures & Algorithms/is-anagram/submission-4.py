class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_length = len(s)
        t_length = len(t)

        if s_length != t_length:
            return False

        hash_map = {}

        for character in s:
            hash_map[character] = hash_map.get(character, 0) + 1

        for character in t:
            if character not in hash_map:
                return False

            hash_map[character] -= 1

            if hash_map[character] < 0:
                return False

        return True


        
        