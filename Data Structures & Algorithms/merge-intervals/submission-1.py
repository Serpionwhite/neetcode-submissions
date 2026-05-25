class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        total_intervals = len(intervals)
        if total_intervals < 2:
            return intervals

        res = []

        start_period = [0,0]

        for index in range(total_intervals):
            if intervals[index][0] <= start_period[-1]:
                if res:
                    res.pop()
                start_period[0] = min(start_period[0], intervals[index][0])
                start_period[-1] = max(start_period[-1], intervals[index][-1])
                res.append(start_period)

            else:
                res.append(intervals[index])
                start_period = intervals[index]

        return res


            

        