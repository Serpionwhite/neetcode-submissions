class Solution:
    def scoreOfString(self, s: str) -> int:
        string_length = len(s)

        if string_length < 2:
            return 0

        
        total_sum = 0

        for index in range(1,string_length):
            difference = abs(ord(s[index]) - ord(s[index-1]))
            total_sum += difference

        return total_sum
        