class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        
        frequencies = sorted(seen.values(), reverse=True)[0:k]

        res = []
        for key, val in seen.items():
            if val in frequencies:
                res.append(key)

        return res



