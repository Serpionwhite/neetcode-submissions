class Solution:
    def isPalindrome(self, s: str) -> bool:
        actual_text = ""

        for value in s:
            if value.isalnum():
                actual_text += value.lower()
            else:
                continue

        string_length = len(actual_text)

        start = 0
        end = string_length - 1

        while start <= end:
            if actual_text[start] != actual_text[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
        