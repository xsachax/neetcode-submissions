class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [20, 18, 16, 19, 23, 23, 21, 19, 24, 18]

        res = [0] * len(temperatures)
        s = []
        
        for i, t in enumerate(temperatures):
            while s and t > s[-1][1]: # while current temp is bigger than top of stack
                sIndex, sTemp = s.pop()     # pop and 
                res[sIndex] = i-sIndex          # update the values at those indices in res
            s.append([i, t])
        
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res = [0] * len(temperatures)
        # stack = []

        # for i, t in enumerate(temperatures):
        #     while stack and t > stack[-1][1]:
        #         stackIndex, temp = stack.pop()
        #         res[stackIndex] = i - stackIndex
        #     stack.append((i, t))
        # return res
            

            

