class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count=1
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==count:
                count+=1
        return count
