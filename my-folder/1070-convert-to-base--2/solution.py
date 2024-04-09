class Solution:
    def baseNeg2(self, n: int) -> str:
        if n==0:
            return "0"
        ans=""
        while n!=0:
            digit=n%(-2)
            n=n//(-2)
            if digit < 0 :
                digit +=2
                n+=1
            ans+=str(digit)
           
            
        return ans[::-1]


