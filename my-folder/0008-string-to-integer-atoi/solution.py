class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if len(s)== 0 :
            return 0 
        i = 0 
        sign=1
        if s[0]=='-':
            sign=-1
            i+=1
        elif s[0]=='+':
            i+=1

        res=0
        while i<len(s) and s[i].isdigit() :
            res= res*10 + int(s[i])
            i+=1
        
        return max(-2**31 ,min(sign*res,2**31-1))
