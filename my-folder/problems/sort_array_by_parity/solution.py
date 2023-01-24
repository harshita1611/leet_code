class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenlist = []
        oddlist = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                evenlist.append(nums[i])
            else:
                oddlist.append(nums[i])
        
        return evenlist + oddlist