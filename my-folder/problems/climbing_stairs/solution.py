class Solution:
    def climbStairs(self, n: int) -> int:
        def memoisation(n,dp):
            if n == 0 or  n == 1:
                return 1
            if dp[n]!=-1:
                return dp
            
            return (memoisation(n-1,dp)+memoisation(n-2,dp))
        

        def tabulation(n,dp):
            dp[0]=1
            dp[1]=1
            for i in range(2,n+1):
                dp[i]=dp[i-1]+dp[i-2]
            return dp[n]
        dp=[-1]*(n+1)
        return tabulation(n,dp)