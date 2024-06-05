class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==divisor:
            return 1
        sign=True
        if dividend>=0 and divisor<0:
            sign=False
        if dividend<0 and divisor>0:
            sign=False

        n=abs(dividend)
        d=abs(divisor)

        ans=0
        while n>=d:
            count=0
            while n>=(d<<count+1):
                count+=1
            ans+= 2**(count)
            n=n-(d*(1<<count))
        if ans>=2**31 and sign==True:
            return 2147483647
        if ans>= 2**31 and sign ==False:
            return -2147483648
        if sign:
            return ans
        else :
            return -1*ans
