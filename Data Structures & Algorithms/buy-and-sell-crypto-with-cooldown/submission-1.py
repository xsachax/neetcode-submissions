class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}


        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp: # memoize
                return dp[(i, buying)]
            
            cooldown = dfs(i+1, buying) # do nothing
            
            if buying: # ready to buy
                buy = - prices[i] + dfs(i+1, False) # pay cost of stock
                dp[(i, buying)] = max(buy, cooldown)
            else: # currently holding, let's sell
                sell = prices[i] + dfs(i+2, True) # grab profit, ready to buy in 2 days
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]



        

        return dfs(0, True)
