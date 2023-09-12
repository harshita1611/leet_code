class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==0 or num==1 :
            return 0 
        sum=1
        i=2
        while i*i < num :
            if num%i==0 :
                sum=sum+i+(num//i)
            i+=1
        return True if sum==num else False