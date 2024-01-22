class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup,miss=-1,-1
        n=len(nums)
        for i in range(1,n+1):
            count=nums.count(i)
            if count==0:
                miss=i
            elif count==2:
                dup=i
        return [dup,miss]
