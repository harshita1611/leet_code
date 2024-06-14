class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        ans=0
        max
        for i in range(1,n):
            if nums[i]<=nums[i-1]:
                curr=nums[i-1]+1-nums[i]
                ans+=curr
                nums[i]=nums[i-1]+1
        return ans
