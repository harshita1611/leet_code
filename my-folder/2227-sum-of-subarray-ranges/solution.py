class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            maxi=nums[i]
            mini=nums[i]
            for j in range(i,n):
                maxi=max(maxi,nums[j])
                mini=min(mini,nums[j])
                ans+=(maxi-mini)
        return ans
