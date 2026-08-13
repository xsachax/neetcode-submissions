class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visitedChests = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def search(r, c, d):
            if r in range(rows) and c in range(cols) and grid[r][c] > 0 and grid[r][c] > d: 
                grid[r][c] = min(grid[r][c], d)
                for dr, dc in directions:
                    search(r+dr, c+dc, d+1)
                

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r, c) not in visitedChests:
                    visitedChests.add((r, c))
                    for dr, dc in directions:
                        search(r+dr, c+dc, 1)