class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if len(s)==0:
            return 0
        sign=1
        i=0
        if s[0]=="-":
            sign=-1
            i+=1
        elif s[0]=="+":
            i+=1
        

        ans=0
        while i<len(s) and s[i].isdigit():
            ans=ans*10 +int(s[i])
            i+=1
        
        return max(-2**31,min(2**31-1,ans*sign))
