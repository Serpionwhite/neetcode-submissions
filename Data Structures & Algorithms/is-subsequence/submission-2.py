class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_length = len(s)
        t_length = len(t)

        if s_length > t_length or (s_length > 0 and t_length == 0):
            return False

        if s_length == 0 and t_length != 0:
            return True

        
        s_index = s_length - 1

        
        for index in range(t_length-1, -1, -1):
            if t[index] == s[s_index] and s_index != -1:
                s_index -= 1

        if s_index != -1:
            return False

        return True
            

        