class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        left = 0
        n = len(s)
        max_length = 0

        for right in range(n):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            max_length = max(right-left + 1, max_length)

        return max_length
        