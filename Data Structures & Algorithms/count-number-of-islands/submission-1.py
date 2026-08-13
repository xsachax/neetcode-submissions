class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        #askdjaskldmasda
        #akdnflqkdkals
        def search(r, c):
            stack = []
            directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            stack.append((r, c))
            while stack:
                row, col = stack.pop()
                if (row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row, col) not in visited):
                    visited.add((row, col))
                    for dr, dc in directions:
                        stack.append((row+dr, col+dc))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    islands+=1
                    search(r, c)
        return islands

        