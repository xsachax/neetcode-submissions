class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            l = i
            r = i
            maxL = maxR = height[i]
            while l >= 0:
                maxL = max(maxL, height[l])
                l-=1
            while r < len(height):
                maxR = max(maxR, height[r])
                r+=1
            res += min(maxL, maxR)-height[i]
        return res
