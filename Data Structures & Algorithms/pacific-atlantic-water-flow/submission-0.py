class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, ocean, prevHeight):
            if r in range(rows) and c in range(cols) and (r, c) not in ocean and heights[r][c] >= prevHeight:
                ocean.add((r, c))
                for dr, dc in directions:
                    dfs(r+dr, c+dc, ocean, heights[r][c])


        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res






        