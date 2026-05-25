from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s1 = Counter(s)

        if len(s) != len(t):
            return False

        for value in t:
            if value in s1:
                if s1[value] > 0:
                    s1[value] -= 1
                else:
                    return False
            else:
                return False
        
        return True
        


        