class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0

        s1 = e1 = -1
        for s2, e2 in intervals:
            if s1 == -1:
                s1, e1 = s2, e2
                continue
            
            if e1 > s2: # overlap
                if e1 > e2: # remove interval 1
                    s1, e1 = s2, e2
                else: # remove interval 2
                    pass
                res+=1
            else:
                s1, e1 = s2, e2
            
        return res
                    



