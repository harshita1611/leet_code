class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # def recursion(nums,idx,prev):
        #     if idx==len(nums):
        #         return 0
        #     notpick=0 + recursion(nums,idx+1,prev)
        #     pick=-float("inf")
        #     if prev==-1 or nums[idx]>nums[prev]:
        #         pick=1+recursion(nums,idx+1,idx)
        #     return max(pick,notpick)
        # return recursion(nums,0,-1)

        def memoisation(nums,idx,prev,dp):
            if idx==len(nums):
                return 0
            if dp[idx][prev+1] != -1:
                return dp[idx][prev+1]
            length=0 + memoisation(nums,idx+1,prev,dp)
            if prev==-1 or nums[idx]>nums[prev]:
                length=max(length,1+memoisation(nums,idx+1,idx,dp))
            dp[idx][prev+1]= length
            return dp[idx][prev+1]
        n=len(nums)
        dp=[[-1 for j in range(n+1)] for i in range(n+1)]
        return memoisation(nums,0,-1,dp)

        # if not nums:
        #     return 0
        # n=len(nums)
        # dp=[1]*n
        # for i in range(1,n):
        #     for j in range(i):
        #         if nums[i]>nums[j]:
        #             dp[i]=max(dp[i],dp[j]+1)
        # return max(dp)