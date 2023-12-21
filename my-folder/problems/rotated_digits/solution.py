class Solution:
    def rotatedDigits(self, n: int) -> int:
        def isGoodNumber(n):
            good = False
            while n:
                digit = n%10
                if digit in [2,5,6,9]:
                    good = True
                if digit in [3,4,7]:
                    return False
                n = n//10
            return good
        count = 0
        for i in range(1,n+1):
            if isGoodNumber(i):
                count+=1
        return count