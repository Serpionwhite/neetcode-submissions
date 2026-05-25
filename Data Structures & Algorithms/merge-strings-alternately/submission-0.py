class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n = len(word1)
        m = len(word2)

        i = 0
        res = ""

        while i<n and i<m:
            res += word1[i]
            res += word2[i]
            i += 1

        if n>m:
            while i<n:
                res += word1[i]
                i+=1
        elif m>n:
            while i<m:
                res += word2[i]
                i+=1

        else:
            return res

        return res


        