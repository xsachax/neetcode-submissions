class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            d = math.sqrt(x**2 + y**2)
            heapq.heappush(minHeap, [d, x, y])
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1:])
        
        return res