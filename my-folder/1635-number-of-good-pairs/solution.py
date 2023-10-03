class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq={}
        for i in nums :
            if i in freq : 
                freq[i]+=1
            else :
                freq[i]=1
        sum=0
        for key,values in freq.items():
            if values>1 :
                sum+=((values)*(values-1))//2
        return sum
