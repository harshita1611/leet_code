class Solution:
    def numDecodings(self, s: str) -> int:
        # def recursion(index, s):
        #     if index == len(s) :
        #         return 1
        #     if s[index] =='0':
        #         return 0
        #     ways=recursion(index+1,s)
        #     if (index+1<len(s)) and(10<= int(s[index:index+2])<=26):
        #         ways+=recursion(index+2,s)
            
        #     return ways

        # return recursion(0,s)

        # def memoisation(index,dp):
        #     if index==len(s):
        #         return 1
        #     if s[index]=='0' :
        #         return 0 


        #     if dp[index]!=-1:
        #         return dp[index]

        #     ways = memoisation(index+1,dp)
        #     if ((index+1)<len(s)) and (10<=int(s[index:index+2])<=26):
        #         ways+=memoisation(index+2,dp)
            
        #     dp[index]=ways
        #     return dp[index]
        
        # dp=[-1]*(len(s)+1)
        # return memoisation(0,dp)

        # n=len(n+1)
        
        def tabulation(n,dp):
            dp[0] = 1
            dp[1]=1
            for i in range(2,n+1):
                single=int(s[i-1])
                two=int(s[i-2:i])
            
                if single!=0:
                    dp[i]+=dp[i-1]

                if 10<=two<=26:
                    dp[i]+=dp[i-2]

            return dp[n]

        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)

        return tabulation(n,dp)