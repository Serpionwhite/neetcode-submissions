class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        res = [0]*n
        stack = []
        for index in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[index]:
                stack.pop()

            if stack:
                res[index] = (stack[-1] - index)
            else:
                res[index] = 0

            stack.append(index)

        return res
        