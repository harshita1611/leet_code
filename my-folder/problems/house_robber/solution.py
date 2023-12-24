class Solution:
    def rob(self, nums: List[int]) -> int:
        # def memoisation(index,nums,dp):
        #     if index==0:
        #         return nums[0]
        #     if index<0:
        #         return 0
        #     if dp[index]!=-1:
        #         return dp[index]

        #     pick = nums[index]+memoisation(index-2,nums,dp)
        #     notpick=0+memoisation(index-1,nums,dp)

        #     dp[index]=max(pick,notpick)

        #     return dp[index]
        # dp=[-1]*(len(nums)+1)
        # return memoisation(len(nums)-1,nums,dp)

        def tabulation(n, nums, dp):
            dp[0] = nums[0]
            for i in range(1,len(nums)):
                pick = nums[i]
                if i>1:
                    pick+=dp[i-2]
                notpick = 0+dp[i-1]
                dp[i] = max(pick, notpick)

            return dp[len(nums)-1]

        dp = [-1]*(len(nums)+1)
        return tabulation(len(nums)-1, nums, dp)