class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        ans=[[0] * (n-2)  for i in range(m-2)] 


        def findmaxi(row,col):
            maxi=grid[row][col]
            for i in range(row,row+3):
                for j in range(col,col+3):
                    maxi=max(maxi,grid[i][j])
            return maxi
        
        for i in range(m-2):
            for j in range(n-2):
                ans[i][j]=findmaxi(i,j)
        
        return ans
