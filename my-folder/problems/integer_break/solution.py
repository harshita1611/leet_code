class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3 :
            return n-1
        if n%3==0 :
            power=n//3
            return pow(3,power)
        if n%3==1 :
            power=(n//3)-1
            return (pow(3,power))*4
        if n%3==2 :
            power=n//3
            return (pow(3,power))*2