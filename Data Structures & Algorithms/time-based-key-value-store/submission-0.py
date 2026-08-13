class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        
        store = self.store[key]
        l, r = 0, len(store)-1

        res = ""
        closest_timestamp = float('inf')
        while l<=r:
            m=(l+r)//2
            prev_timestamp = store[m][0]
            if prev_timestamp <= timestamp:
                if abs(closest_timestamp - timestamp) <= abs(closest_timestamp - prev_timestamp):
                    res = store[m][1]
                    closest_timestamp = timestamp
                l=m+1
            else:
                r=m-1
        return res
