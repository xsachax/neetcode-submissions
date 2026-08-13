class Solution:
    def rob(self, nums: List[int]) -> int:

        def robSim(nums):
            path1, path2 = 0,0
            for amount in nums:
                maxRob = max(path1+amount, path2)
                path1 = path2
                path2 = maxRob
            return path2

        
        withoutFirst = robSim(nums[1:])
        withoutLast = robSim(nums[:-1])

        # nums[0] in case the array has length 1
        return max(nums[0], withoutFirst, withoutLast)
        