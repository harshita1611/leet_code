class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row,zero_col=set(),set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zero_row.add(i)
                    zero_col.add(j)
        for i in zero_row:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        
        for i in range(len(matrix)):
            for j in zero_col:
                matrix[i][j]=0
        
        return matrix
        
