class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        all_nums = [i for i in range(1,n+1)]
        return list(set(all_nums) - set(nums))