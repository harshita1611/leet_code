class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2 :
            return n 
        else :
            a = 1 
            b = 2 
            for i in range(3,n+1):
                ans = a+b
                a=b
                b=ans
        return ans
