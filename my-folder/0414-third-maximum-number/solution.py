class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums) - 1
        while i > 0:
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            i -= 1
        ans = 0
        if len(nums) < 3:
            ans=max(nums)
        if len(nums) >= 3:
            max_1 = max(nums)
            nums.remove(max_1)
            max_2 = max(nums)
            nums.remove(max_2)
            max_3 = max(nums)
            ans=max_3
        return ans

