class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
            
        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for n in nums:
            tmp = set()
            for t in dp:
                tmp.add(t+n)
                tmp.add(t)
            dp = tmp
        
        return True if target in dp else False