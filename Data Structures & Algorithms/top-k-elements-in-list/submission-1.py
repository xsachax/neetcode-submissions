class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1

    # [1, 1, 1, 2, 2, 2, 2, 3, 3]
    # 1: 3
    # 2: 4
    # 3: 2
        
        topk = sorted(seen.items(), key=lambda x: x[1], reverse=True)[0:k]      

        return [k[0] for k in topk]



