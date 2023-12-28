class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def memoisation(x,y,grid,dp):
            if x==0 and y==0 :
                return grid[0][0]
            if x<0 and y<0:
                return 1e9
            if dp[x][y] !=-1:
                return dp[x][y]
            
            cost_x=cost_y=float("inf")
            if x>0:
                cost_x=grid[x][y]+ memoisation(x-1,y,grid,dp)
            if y>0:
                cost_y=grid[x][y]+ memoisation(x,y-1,grid,dp)
            
            dp[x][y]=min(cost_x,cost_y)
            return dp[x][y]
        
        dp=[[-1 for j in range(len(grid[0]))] for i in range(len(grid))]
        return memoisation(len(grid)-1,len(grid[0])-1,grid,dp)