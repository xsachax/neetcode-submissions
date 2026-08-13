class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [] # (startIndex, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                res = max(res, height * (i-index))
                start = index   # move the start back
            stack.append((start, h))


        # cleanup stack left in increasing order

        for i, h in stack:
            res = max(res, h*(len(heights)-i))

        return res



