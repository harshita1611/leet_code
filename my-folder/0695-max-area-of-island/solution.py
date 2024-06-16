class Solution:
    def isSafe(self,M,row,col,ROW,COL,visited):
        return row>=0 and row<ROW and col>=0 and col<COL and not visited[row][col] and M[row][col]

    def DFS(self,M,row,col,ROW,COL,visited,count):
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]

        visited[row][col]=True
        for k in range(4):
            if self.isSafe(M,row+dx[k],col+dy[k],ROW,COL,visited):
                count[0]+=1
                self.DFS(M,row+dx[k],col+dy[k],ROW,COL,visited,count)


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW=len(grid)
        COL=len(grid[0])
        visited=[[False]*COL for i in range(ROW)]
        
        ans=0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] and not visited[i][j]:
                    count=[1]
                    self.DFS(grid,i,j,ROW,COL,visited,count)
                    ans=max(ans,count[0])
        return ans

