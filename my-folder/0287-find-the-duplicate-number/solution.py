class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        freq=[0]*n
        for i in nums:
            freq[i]+=1
        for i in range(n):
            if freq[i]>1:
                return i
        return -1
