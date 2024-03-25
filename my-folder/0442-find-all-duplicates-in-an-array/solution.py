class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        freq=[0]*(n+1)
        for i in nums:
            freq[i]+=1
        print(freq)
        
        ans=[]
        for i in range(n+1):
            if freq[i]==2:
                ans.append(i)
        
        return ans
