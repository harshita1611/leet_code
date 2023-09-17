class Solution:
    def reverse(self, x: int) -> int:
        def reverse_num(x):
            reverse = 0 
            while x :
                digit = x%10
                reverse = reverse*10 + digit 
                x=x//10
            return reverse
        if x < 0:
            x = -x
            x = reverse_num(x)
            x = -x
        else:
            x = reverse_num(x)
        if x < -2**31 or x > 2**31-1:
            return 0
        return x
