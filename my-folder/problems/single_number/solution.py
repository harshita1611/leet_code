class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        ans=0
        for i in nums :
            if i in freq :
                freq[i]+=1
            else :
                freq[i]=1
        for j in freq :
            if freq[j]==1 : 
                ans=j
        return ans