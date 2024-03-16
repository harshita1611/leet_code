class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=1
        suffix=1
        ans=[]
        for i in range(n):
            ans.append(prefix)
            prefix*=nums[i]
        for i in range(n-1,-1,-1):
            ans[i]*=suffix
            suffix*=nums[i]
        return ans
        
