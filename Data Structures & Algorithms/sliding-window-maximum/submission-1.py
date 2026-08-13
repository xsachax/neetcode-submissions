class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        w = collections.defaultdict(int)
        for i in range(k):
            w[str(nums[i])]+=1
        print(w)
        if k ==1:
            return nums

        l=0
        for r in range(k-1, len(nums)):
            w[str(nums[r])]+=1
            localMax = float('-inf')
            localRes = ""
            for k, v in w.items():
                if v > 0:
                    localMax = max(localMax, int(k))
                    if int(k) == localMax:
                        localRes = str(k)
            res.append(localRes)


            w[str(nums[l])]-=1
            l+=1
        return res