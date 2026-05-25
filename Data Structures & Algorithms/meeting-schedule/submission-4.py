"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        total_meetings = len(intervals)

        if total_meetings == 0:
            return True

        intervals.sort(key=lambda x: x.start)

        for index in range(1,total_meetings):
            if intervals[index-1].end > intervals[index].start:
                return False


        
        return True

