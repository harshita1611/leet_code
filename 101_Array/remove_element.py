class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums = [i for i in nums if i!=val]
        return nums
obj = Solution()
print(obj.removeElement([0,1,2,2,3,0,4,2],2))
