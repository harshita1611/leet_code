class Solution:
    def countBits(self, n: int) -> List[int]:
        arr=[] 
        arr.append(0) 
      
        def deci_to_bin(x):
            binaryNum = [0]*x
            i=0 
            ques=""
            while x>0 :
                binaryNum[i]=x%2
                x=x//2
                ques+="".join(str(binaryNum[i]))
                i+=1
            return ques


        for i in range(1,n+1) : 
            arr.append(deci_to_bin(i).count('1'))
        return arr