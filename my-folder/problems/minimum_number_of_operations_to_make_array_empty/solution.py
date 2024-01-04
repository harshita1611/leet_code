class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        count=0
        for i in freq.values():
            if i==1:
                return -1
            count+=(i//3)
            if i%3==2 or i%3==1:
                count+=1
        
        return count