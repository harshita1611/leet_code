class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            flag = 0
            if nums[i] == target or (target<nums[i] and target>nums[i-1]) :
                flag=i
        return flag

obj = Solution()
print(obj.searchInsert([1,3,5,6],5))