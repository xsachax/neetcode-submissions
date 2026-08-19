class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []
        self.even = True

    def addNum(self, num: int) -> None:
        if self.even:
            if self.low and num <= self.low[0]:
                heapq.heappush_max(self.low, num)
            else:
                heapq.heappush(self.high, num)
            self.even = False
        else: #odd, might need to move a number over
            if not self.high or len(self.low) > len(self.high):
                if num <= self.low[0]:
                    x = heapq.heappushpop_max(self.low, num)
                    heapq.heappush(self.high, x)
                else:
                    heapq.heappush(self.high, num)
            else:
                if not self.low or num >= self.high[0]:
                    x = heapq.heappushpop(self.high, num)
                    heapq.heappush_max(self.low, x)
                else:
                    heapq.heappush_max(self.low, num)
            self.even = True

    def findMedian(self) -> float:
        if not self.low and not self.high:
            return 0
        if self.even:
            return (self.low[0] + self.high[0]) / 2
        elif not self.high or len(self.low) > len(self.high):
            return self.low[0]
        else:
            return self.high[0]
            
        
        