class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n=len(nums)
        left = 0 
        right = n-1
        concat=0
        if n==0 :
            return nums[0]
        while left <= right :
            if left == right:
                concat += nums[left]
            else:
                concat += int(str(nums[left]) + str(nums[right]))

            left += 1
            right -= 1
        return concat