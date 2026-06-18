class Solution:
    def largestGoodInteger(self, num: str) -> str:

        best = -1

        n = len(num)

        for index in range(n-2):
            if num[index] == num[index+1] == num[index+2]:
                best = max(best, int(num[index]))

        return str(best)*3 if best != -1 else ""
        