class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search rows, then search within the chosen row
        n = len(matrix[0])-1

        t, b = 0, len(matrix)-1

        while t<=b:
            m = (t+b)//2
            if matrix[m][0] <= target <= matrix[m][n]: # this row
                row = m
                break
            elif target < matrix[m][0]:
                b=m-1
            else:
                t=m+1
        else:
            return False
        

        l,r = 0, n
        while l<=r:
            m=(l+r)//2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r=m-1
            else:
                l=m+1
        return False
            
