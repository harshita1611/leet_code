class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        evenlist = []
        oddlist = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                evenlist.append(nums[i])
            else:
                oddlist.append(nums[i])
        return evenlist + oddlist



obj = Solution()
print(obj.sortArrayByParity([3,1,2,4]))