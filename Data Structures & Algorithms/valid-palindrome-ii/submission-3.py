class Solution:

    def isPalindrome(self,s,  left, right):
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        return True
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return self.isPalindrome(s, start+1, end) or self.isPalindrome(s, start, end-1)
            start+=1
            end -= 1

        return True


        

        