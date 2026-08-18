class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        while i < len(intervals) and intervals[i][1] < newInterval[0]: # find start point
            i += 1

        start, end = newInterval
        j = i

        while j < len(intervals) and intervals[j][0] <= end: #merge until stop point
            start = min(start, intervals[j][0])
            end = max(end, intervals[j][1])
            j += 1

        intervals[i:j] = [[start, end]]
        return intervals