class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count=1
        n=len(nums)
        nums.sort()
        ans=set(nums)
        for i in range(n):
            if nums[i]==count:
                count+=1
        return count
