class Solution:
    def reverse(self, x: int) -> int:
        reverse=0
        if x>=0:
            reverse=int(str(x)[::-1])
        else : 
            reverse = int(f"-{int(str(abs(x))[::-1])}")
        if reverse>=(-2**31) and reverse<=(2**31):
            return reverse
        return 0
