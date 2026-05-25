class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)

        if n<=1:
            return s

        st = 0
        e = n-1

        while st<e:
            s[st], s[e] = s[e], s[st]
            e -=1
            st+=1
        return s
        