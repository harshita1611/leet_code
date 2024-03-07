class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        count=0
        if k>=numOnes:
            k-=numOnes
            count+=numOnes
        else:
            count+=k
            return count 
            
        if k>=numZeros:
            k-=numZeros
        else:
            return count 

        if k>=numNegOnes :
            count-=numNegOnes
        else:
            count-=k

        return count

       
