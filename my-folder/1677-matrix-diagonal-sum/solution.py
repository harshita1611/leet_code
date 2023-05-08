class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        n=len(mat)
        for i in range(n):
            for j in range(n):
                if i==j:
                    sum+=mat[i][j]
                elif i+j==n-1:
                    sum+=mat[i][j]
        return sum
