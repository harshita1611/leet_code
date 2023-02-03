class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)-1):
            if nums[i] == 0 :
                nums.pop(i)
                nums.append(0)

        return nums
obj = Solution()
print(obj.moveZeroes([0,1,0,3,12]))