class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res=-1
        total=0
        for i in nums:
            if total>i:
                res=total+i
            total+=i
        return res
