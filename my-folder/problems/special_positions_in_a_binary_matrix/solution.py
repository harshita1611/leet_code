class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count=0

        def sum_col(mat, col):
            sum=0
            for i in range(len(mat)):
                sum+=mat[i][col]
            return sum
        
        def sum_row(mat, row):
            sum=0
            for i in range(len(mat[0])):
                sum+=mat[row][i]
            return sum
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    if sum_row(mat, i)==1 and sum_col(mat, j)==1:
                        count+=1
        return count