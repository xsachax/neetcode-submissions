class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        seen = set()
        seen.add(0)

        new = []
        for n in nums:
            for s in seen:
                new.append(n+s)

            for i in new:
                seen.add(i)
            if target in seen:
                return True

        return False
            


        