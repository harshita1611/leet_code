class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        for i in s : 
            if i.isalnum() :
                x+=i.lower()
        for i in range(len(x)):
            if x[i] != x[len(x)-i-1] :
                return False
        return True