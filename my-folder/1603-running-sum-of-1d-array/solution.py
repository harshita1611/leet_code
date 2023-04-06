class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[]
        ans=0
        for i in nums:
            ans+=i
            arr.append(ans)
        return arr
