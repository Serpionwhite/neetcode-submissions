class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_length = len(s)
        t_length = len(t)

        if s_length != t_length:
            return False

        # hash_map = {}

        # for character in s:
        #     hash_map[character] = hash_map.get(character, 0) + 1

        # for character in t:
        #     if character not in hash_map:
        #         return False

        #     hash_map[character] -= 1

        #     if hash_map[character] < 0:
        #         return False

        # return True


        count = [0] * 26

        for index in range(s_length):
            count[ord(s[index]) - ord('a')] += 1
            count[ord(t[index]) - ord('a')] -= 1

        for value in count:
            if value != 0:
                return False

        return True




        
        