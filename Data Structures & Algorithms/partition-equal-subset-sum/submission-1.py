class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {(0, 0)}

        for n in nums:
            new_cache = set()
            for a,b in cache:
                new_cache.add((a+n, b))
                new_cache.add((a, b+n))
            cache = new_cache
        
        return any(x==y for x,y in cache)
