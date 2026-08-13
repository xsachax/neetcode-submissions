class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def formatResFromData(queens):
            combination = []
            for q in queens:
                t = "." * (q)
                t+= "Q"
                t+= "." * (n-q-1)
                combination.append(t)
            res.append(combination)

        def dfs(row, data):
            if row==n: # success case
                formatResFromData(data["queens"])
                return
            for col in range(n): # iterate over row
                ldiagMatcher = row-col+(n-1)
                rdiagMatcher = row+col
                if data["cols"][col] == 0 and data["ldiag"][ldiagMatcher] == 0 and data["rdiag"][rdiagMatcher] == 0:
                    data["cols"][col] = 1
                    data["ldiag"][ldiagMatcher] = 1
                    data["rdiag"][rdiagMatcher] = 1
                    data["queens"].append(col)
                    dfs(row+1, data)
                    data["cols"][col] = 0
                    data["ldiag"][ldiagMatcher] = 0
                    data["rdiag"][rdiagMatcher] = 0
                    data["queens"].pop()

        dfs(0, {
            "cols": [0] * n,
            "ldiag": [0] * (n*2-1),
            "rdiag": [0] * (n*2-1),
            "queens": []
        })

        return res



        



        