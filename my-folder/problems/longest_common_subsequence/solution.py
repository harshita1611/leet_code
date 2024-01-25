class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(x,y,m,n,dp):
            
            if m==0 or n==0:
                return 0

            if dp[m-1][n-1]!=-1:
                return dp[m-1][n-1]

            elif x[m-1]==y[n-1]:
                dp[m-1][n-1]=1+lcs(x,y,m-1,n-1,dp)
                return dp[m-1][n-1]
            else:
                dp[m-1][n-1]=max(lcs(x,y,m-1,n,dp),lcs(x,y,m,n-1,dp))
                return dp[m-1][n-1]
        m=len(text1)
        n=len(text2)
        dp=[[-1 for i in range(1000)] for j in range(m)]
        return lcs(text1,text2,m,n,dp)
