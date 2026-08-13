class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        av = set()
        pv = set()
        res = []
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        def dfs(r, c, visited, prevHeight, ocean):
            if r in range(ROWS) and c in range(COLS) and (r,c) not in visited and heights[r][c] >= prevHeight:
                visited.add((r,c))
                if ocean == "p" and (r,c) in av or ocean == "a" and (r,c) in pv:
                    res.append([r,c])
                for dr, dc in DIRECTIONS:
                    dfs(r+dr, c+dc, visited, heights[r][c], ocean)

        for r in range(ROWS):
            dfs(r, 0, pv, 0, "p")
            dfs(r, COLS-1, av, 0, "a")

        for c in range(COLS):
            dfs(0, c, pv, 0, "p")
            dfs(ROWS-1, c, av, 0, "a")


        return res


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # rows = len(heights)
        # cols = len(heights[0])
        # pac = set()
        # atl = set()
        # directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # def dfs(r, c, ocean, prevHeight):
        #     if r in range(rows) and c in range(cols) and (r, c) not in ocean and heights[r][c] >= prevHeight:
        #         ocean.add((r, c))
        #         for dr, dc in directions:
        #             dfs(r+dr, c+dc, ocean, heights[r][c])


        # for c in range(cols):
        #     dfs(0, c, pac, heights[0][c])
        #     dfs(rows-1, c, atl, heights[rows-1][c])
        
        # for r in range(rows):
        #     dfs(r, 0, pac, heights[r][0])
        #     dfs(r, cols-1, atl, heights[r][cols-1])

        # res = []
        # for r in range(rows):
        #     for c in range(cols):
        #         if (r, c) in pac and (r, c) in atl:
        #             res.append([r, c])
        
        # return res






        