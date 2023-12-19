class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def getAvg(i,j,img):
            m=len(img)
            n=len(img[0])
            sum=count=0
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if x>=0 and x<m and y>=0 and y<n :
                        count+=1
                        sum+=img[x][y]

            return sum//count
        
        m=len(img)
        n=len(img[0])
        ans=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j]=getAvg(i,j,img)
        return ans