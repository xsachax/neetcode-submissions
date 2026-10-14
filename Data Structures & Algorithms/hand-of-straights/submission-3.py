from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        h = [(k,v) for k,v in counter.items()]
        heapq.heapify(h)

        while h:
            tmp = []
            for j in range(groupSize):
                if not h:
                    return False
                num, count = heapq.heappop(h)
                if j!=0 and num != prev+1:
                    return False
                prev = num
                if count-1 != 0:
                    tmp.append((num, count-1))
            for t in tmp:
                heapq.heappush(h, t)
        
        return True

