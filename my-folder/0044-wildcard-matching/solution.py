class Solution:
    def f(self,i,j,pattern,string,dp):
        if i<0 and j<0:
            return True
        if i<0 and j>=0:
            return False
        if i>=0 and j<0 :
            for k in range(i+1):
                if pattern[k]!="*":
                    return False
            return True
        
        if dp[i][j] !=-1:
            return dp[i][j]

        if pattern[i]==string[j] or pattern[i]=="?":
            dp[i][j]=self.f(i-1,j-1,pattern,string,dp)
        elif pattern[i]=="*":
            dp[i][j]=self.f(i,j-1,pattern,string,dp) or self.f(i-1,j,pattern,string,dp)
        else:
            dp[i][j]=False
        return dp[i][j]

    def isMatch(self, s: str, p: str) -> bool:
        n=len(p)
        m=len(s)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        return self.f(n-1,m-1,p,s,dp)
