class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans=0
        minindex=-1
        maxindex=-1
        culprit=-1
        for i in range(len(nums)):
            if nums[i]<minK or nums[i]>maxK:
                culprit=i
            if nums[i]==minK:
                minindex=i
            if nums[i]==maxK:
                maxindex=i
            
            smaller=min(minindex,maxindex)
            temp=smaller-culprit
            if temp<=0:
                ans+=0
            else:
                ans+=temp
        return ans

        


        