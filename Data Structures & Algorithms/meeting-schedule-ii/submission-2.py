"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s = sorted([i.start for i in intervals])
        e = sorted([i.end for i in intervals])

        
        

        i = j = 0

        curr = 0
        res = 0
        while i<len(intervals):
            if s[i] < e[j]:
                curr+=1
                i+=1
            else:
                curr-=1
                j+=1
            res=max(res, curr)

        return res