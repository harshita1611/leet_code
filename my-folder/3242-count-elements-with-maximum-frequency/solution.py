class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        res= max(freq.values())
        count=0
        for i in freq.values():
            if i==res:
                count+=res
        return count
