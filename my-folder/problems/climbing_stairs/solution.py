class Solution:
    def climbStairs(self, n: int) -> int:
        prev2=1
        prev=1
        for i in range(2,n+1) :
            curi=prev2+prev
            prev2=prev
            prev=curi
        return prev