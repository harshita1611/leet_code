class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in nums :
            result=nums.count(i)


obj = Solution()
print(obj.singleNumber([4,1,2,1,2]))