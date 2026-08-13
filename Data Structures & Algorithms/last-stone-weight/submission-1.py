import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)
            if stone1 == stone2:
                continue
            else:
                heapq.heappush(stones, abs(stone1-stone2)*-1)
        
        return 0 if (len(stones) == 0) else stones[0]*-1
        