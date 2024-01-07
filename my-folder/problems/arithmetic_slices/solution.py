class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # def recursion(nums,index):
        #     if index<2:
        #         return 0 
        #     if nums[index]-nums[index-1]==nums[index-1]-nums[index-2]:
        #         sub=1+recursion(nums,index-1)
        #         return sub
        #     else :
        #         return 0 
        
        # count=0
        # for i in range(2,len(nums)):
        #     count+=recursion(nums,i)
        
        # return count

        def memoisation(nums,index,dp):
            if index<2:
                return 0
            if dp[index]!=0:
                return dp[index]
            if nums[index]-nums[index-1]==nums[index-1]-nums[index-2]:
                dp[index]=1+memoisation(nums,index-1,dp)
                return dp[index]
            else :
                return 0
        count = 0
        n=(len(nums))
        dp=[0] * n
        for i in range(2,n):
            count+= memoisation(nums,i,dp)
        return count