class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        maxProf=0
        for i, r in enumerate(prices):
            if prices[l] < r:
                maxProf=max(maxProf, r-prices[l])
            else:
                l=i
        return maxProf




































    # def maxProfit(self, prices: List[int]) -> int:
    #     res = 0
    #     l, r = 0, 1

    #     while r < len(prices):
    #         if prices[l] < prices[r]:
    #             res = max(res, prices[r]-prices[l])
    #         else:
    #             l = r
    #         r+=1
    #     return res