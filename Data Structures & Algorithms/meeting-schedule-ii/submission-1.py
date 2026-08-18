"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        h = []

        for i in intervals:
            h.append((i.start, "B_start"))
            h.append((i.end, "A_end"))

        heapq.heapify(h)

        res = 0
        curr = 0
        while h:
            x, y = heapq.heappop(h)
            if y == "B_start":
                curr+=1
            else:
                curr-=1
            res=max(res, curr)
        
        return res
            





