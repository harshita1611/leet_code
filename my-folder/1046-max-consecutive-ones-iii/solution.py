class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen=0
        l=0
        r=0
        zeros=0
        n=len(nums)
        while r<n :
            if nums[r]==0:
                zeros+=1
            while zeros > k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            r+=1
            maxlen=max(maxlen,r-l)
        return maxlen
