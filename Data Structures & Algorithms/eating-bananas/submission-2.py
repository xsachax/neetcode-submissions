import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = len(piles)
        
        while l <=r:
            k = l+(r-l)//2
            time = 0
            for p in piles:
                time+=math.ceil(p/k)
            
            if time <= h:
                res=k
                r=k-1
            else:
                l=k+1
        return res

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # l, r = 1, max(piles)
        # res = r

        # while l<=r:
        #     k = (l+r)//2
        #     totalTime=0
        #     for pile in piles:
        #         totalTime += math.ceil(pile / k)
        #     if totalTime <= h:
        #         res=k
        #         r=k-1
        #     else:
        #         l=k+1
        # return res

        