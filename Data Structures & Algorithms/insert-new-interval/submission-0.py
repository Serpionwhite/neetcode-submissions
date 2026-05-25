class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        total_intervals = len(intervals)

        if total_intervals == 0:
            return [[newInterval[0], newInterval[-1]]]


        res = []

        index = 0

        while index < total_intervals and intervals[index][-1] < newInterval[0]:
            res.append(intervals[index])
            index += 1

        
        while index < total_intervals and intervals[index][0] <= newInterval[-1]:
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1

        res.append(newInterval)

        while index < total_intervals:
            res.append(intervals[index])
            index += 1

        return res


        

        

