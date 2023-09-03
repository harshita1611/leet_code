class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        for i in range(len(nums)):
            for j in list(combinations(nums, i)):
                power_set.append(list(j))
        power_set.append(nums)
        return power_set
