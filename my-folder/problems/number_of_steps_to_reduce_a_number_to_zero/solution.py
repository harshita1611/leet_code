class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while num :
            if num%2==0:
                num= int(num/2)
                count+=1
            if num%2 !=0 :
                num-=1
                count+=1
        return count