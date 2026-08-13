class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def search(r, c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c] == "0" or (r, c) in visited):
                return
            
            visited.add((r, c))
            search(r-1, c)
            search(r+1, c)
            search(r, c-1)
            search(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    islands+=1
                    search(r, c)
        return islands

        