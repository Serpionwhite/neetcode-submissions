class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # sorted_heights = sorted(heights)

        # count = 0
        # for index in range(len(heights)):
        #     if sorted_heights[index] != heights[index]:
        #         count+=1

        # return count

        count = [0] * 101

        for height in heights:
            count[height] += 1

        
        expected = []
        for height in range(1,101):
            student_count = count[height]

            for student in range(student_count):
                expected.append(height)


        total = 0
        for index in range(len(heights)):
            if expected[index] != heights[index]:
                total += 1

        return total
        