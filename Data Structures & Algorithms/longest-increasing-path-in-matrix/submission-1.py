from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[1 for _ in range(COLS)] for _ in range(ROWS)]
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        @cache
        def dfs(r,c):
            best = 1

            for dr, dc in DIRECTIONS:
                new_r, new_c = r+dr, c+dc
                if new_r in range(ROWS) and new_c in range(COLS) and matrix[new_r][new_c] > matrix[r][c]:
                    best = max(best, 1+dfs(new_r, new_c))
            return best


        return max(dfs(r,c) for r in range(ROWS) for c in range(COLS))