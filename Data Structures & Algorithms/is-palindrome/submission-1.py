class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        ans = ""
        for val in s:
            if val.isalnum():
                ans += val.lower()
            else:
                continue
        

        right = len(ans)-1

        while left <= right:
            if ans[left] == ans[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        