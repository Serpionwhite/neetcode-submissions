class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)

        count = 0
        for index in range(len(heights)):
            if sorted_heights[index] != heights[index]:
                count+=1

        return count
        