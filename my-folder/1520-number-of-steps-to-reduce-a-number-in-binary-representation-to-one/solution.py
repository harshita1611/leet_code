class Solution:
    def numSteps(self, s: str) -> int:
        count=0
        ans=int(s,2)
        while ans>1:
            if ans%2==0:
                ans=ans//2
            else:
                ans+=1
            count+=1
        return count
