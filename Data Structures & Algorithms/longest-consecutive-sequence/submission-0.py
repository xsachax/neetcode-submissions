class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        maxSeq = 0
        for i in set_nums:
            if (i - 1) not in set_nums: #start of sequence
                count=1
                while (i + count) in set_nums:
                    count+=1
                maxSeq = max(maxSeq, count)
        return maxSeq

