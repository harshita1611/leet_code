class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        if nums == sorted_nums:
            return 0
        
        min_num = min(nums)
        min_index = nums.index(min_num)
        
        def is_possible():
            for i in range(n):
                if nums[(min_index + i) % n] != sorted_nums[i]:
                    return False
            return True
        
        if is_possible():
            return n - min_index
        else:
            return -1
