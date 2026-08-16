"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        pe = float('-inf')

        for i in intervals:
            if i.start<pe:
                return False
            pe = i.end
    
        return True
