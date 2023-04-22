class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x!=0 and x%10==0) :
            return False
        num = x
        reverse=0 
        while(x):
            last_digit= x%10
            reverse = reverse*10 + last_digit
            x=x//10
        if num==reverse :
            return True
        return False