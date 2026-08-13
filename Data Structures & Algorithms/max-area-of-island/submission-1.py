class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(r, c) -> int:
            if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited:
                visited.add((r, c))
                return 1 + bfs(r-1, c) + bfs(r+1, c) + bfs(r, c-1) + bfs(r, c+1)
            else:
                return 0
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, bfs(r, c))
        return res


