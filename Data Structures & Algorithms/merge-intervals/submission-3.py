class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        total_intervals = len(intervals)
        if total_intervals < 2:
            return intervals

        res = [intervals[0]]

        for index in range(1,total_intervals):
            if intervals[index][0] <= res[-1][-1]:
                res[-1][0] = min(res[-1][0], intervals[index][0])
                res[-1][-1] = max(res[-1][-1], intervals[index][-1])

            else:
                res.append(intervals[index])

        return res


            

        