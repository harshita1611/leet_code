class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=1000000007
        def binpow(a,b):
            res=1
            while b :
                if b & 1 :
                    res=(res*a) %mod
                a= (a*a) %mod
                b>>=1
            return res

        odd=n//2
        even=(n-odd)
        odd_pow = binpow(4,odd)
        even_pow = binpow(5,even)

        return (odd_pow * even_pow)%mod

