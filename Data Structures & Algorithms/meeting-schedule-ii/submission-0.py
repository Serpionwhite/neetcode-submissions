"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        total_length = len(intervals)
        if total_length == 0:
            return 0

        if total_length == 1:
            return 1

        
        intervals.sort(key = lambda x: x.start)
        min_heap = []

        for index in range(total_length):
            if min_heap and min_heap[0]<= intervals[index].start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, intervals[index].end)

        return len(min_heap)