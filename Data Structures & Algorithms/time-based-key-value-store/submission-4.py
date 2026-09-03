from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.d[key])-1
        res = ""

        while l <= r:
            m=l+(r-l)//2
            ts, v = self.d[key][m]
            if ts == timestamp:
                res = v
                break
            elif ts < timestamp:
                res = v
                l=m+1
            else:
                r=m-1
        return res

