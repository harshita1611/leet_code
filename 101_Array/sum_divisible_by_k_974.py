class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i , len(nums)):
                sum += nums[j]
                if sum%k==0 :
                    result+=1

        return result




obj = Solution()
obj.subarraysDivByK([4,5,0,-2,-3,1] , 5)