class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        maxL = maxR = 0

        while l <= r:
            if maxL <= maxR: # tallest bar is on right, calculate water for L
                maxL = max(maxL, height[l])
                res += maxL - height[l]
                l+=1
            else: # tallest bar is on left, calculate water for R
                maxR = max(maxR, height[r])
                res += maxR - height[r]
                r-=1
        return res
